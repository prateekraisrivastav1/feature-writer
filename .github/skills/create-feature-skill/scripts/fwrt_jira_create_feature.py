#!/usr/bin/env python3
"""
Create exactly one Jira Feature after explicit hash-bound approval.

Requires .env at repository root (or JIRA_ENV_FILE):
  JIRA_BASE_URL=https://your-domain.atlassian.net
  JIRA_EMAIL=...
  JIRA_API_TOKEN=...

No automatic retries. On ambiguous network outcomes, exits with an explicit
verification warning and does not repeat POST.
"""
import argparse, hashlib, json, os, re, sys, urllib.error, urllib.request
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    print("Missing dependency: install python-dotenv (pip install python-dotenv).", file=sys.stderr)
    raise SystemExit(2)

def locate_env_file():
    # An explicitly configured path takes precedence.
    explicit = os.getenv("JIRA_ENV_FILE")
    if explicit:
        path = Path(explicit).expanduser()
        if not path.is_absolute():
            path = Path.cwd() / path
        if path.is_file():
            return path.resolve()
        raise FileNotFoundError(f"JIRA_ENV_FILE does not exist: {path}")

    # Search from the current working directory and script directory upwards.
    search_starts = [Path.cwd(), Path(__file__).resolve().parent]

    checked = set()
    for start in search_starts:
        for directory in (start, *start.parents):
            candidate = directory / ".env"
            if candidate in checked:
                continue
            checked.add(candidate)
            if candidate.is_file():
                return candidate.resolve()

    raise FileNotFoundError(
        "Could not locate .env. Expected it in the repository root "
        "or a parent directory."
    )

ENV_FILE = locate_env_file()
load_dotenv(ENV_FILE, override=False)
print(f"Loaded Jira configuration from: {ENV_FILE}")

def canonical_bytes(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")

def fail(msg, code=2):
    print(msg, file=sys.stderr); raise SystemExit(code)

def request(method, url, email, token, body=None, timeout=25):
    import base64
    auth = base64.b64encode(f"{email}:{token}".encode()).decode()
    data = None if body is None else json.dumps(body, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Basic {auth}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Feature-Writer-Copilot/1.0"
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            raw = response.read()
            return response.status, json.loads(raw.decode("utf-8")) if raw else {}
    except urllib.error.HTTPError as exc:
        body_text = exc.read().decode("utf-8", errors="replace")
        # Jira validation details are useful, but never print request headers.
        fail(f"Jira returned HTTP {exc.code}: {body_text[:4000]}", 3)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        fail("Jira request outcome may be ambiguous. No retry was attempted. "
             "Obtain separate approval to search/verify whether the issue was created. "
             f"Transport detail: {type(exc).__name__}", 4)

def adf_from_text(text):
    # Preserve paragraphs as plain text in ADF; markdown syntax is not rendered.
    paragraphs = []
    for line in text.splitlines():
        if line.strip():
            paragraphs.append({"type":"paragraph","content":[{"type":"text","text":line}]})
    if not paragraphs:
        paragraphs = [{"type":"paragraph","content":[{"type":"text","text":" " }]}]
    return {"type":"doc","version":1,"content":paragraphs}

def build_fields(p):
    fields = {
        "project": {"key": p["project_key"]},
        "issuetype": {"name": "Feature"},
        "summary": p["summary"].strip(),
        "description": adf_from_text(p["description"].strip())
    }
    if p.get("labels"): fields["labels"] = p["labels"]
    if p.get("priority"): fields["priority"] = {"name": p["priority"]}
    if p.get("components"): fields["components"] = [{"name": x} for x in p["components"]]
    return fields

def main():
    ap = argparse.ArgumentParser(description="Create a Jira Feature with hash-bound approval.")
    ap.add_argument("--payload", required=True, type=Path)
    ap.add_argument("--approved-sha256", help="Exact digest reviewed and approved by the user.")
    ap.add_argument("--dry-run", action="store_true", help="Validate and inspect Jira metadata; never POST.")
    args = ap.parse_args()

    try: payload = json.loads(args.payload.read_text(encoding="utf-8"))
    except Exception as exc: fail(f"Cannot read payload: {exc}")
    from fwrt_validate_payload import validate
    errors = validate(payload)
    if errors: fail("Payload invalid:\n- " + "\n- ".join(errors))

    digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
    print(f"Payload SHA-256: {digest}")
    if not args.dry_run and not args.approved_sha256:
        fail("Create blocked. Review the payload, then rerun with --approved-sha256 <exact-digest>.")
    if args.approved_sha256 and args.approved_sha256.lower() != digest:
        fail("Approval digest does not match current payload. Re-review and approve the changed payload.")

    base = (os.getenv("JIRA_BASE_URL") or "").rstrip("/")
    email, token = os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN")
    if not base or not email or not token:
        fail("Missing JIRA_BASE_URL, JIRA_EMAIL, or JIRA_API_TOKEN in .env/environment.")
    if not re.fullmatch(r"https://[A-Za-z0-9.-]+\.atlassian\.net", base):
        fail("JIRA_BASE_URL must be your HTTPS Atlassian Cloud site URL.")
    project = payload["project_key"]

    # Preflight: verify the exact issue type is available for creation in this project.
    url = f"{base}/rest/api/3/issue/createmeta/{project}/issuetypes?startAt=0&maxResults=100"
    _, meta = request("GET", url, email, token)
    types = meta.get("values") or meta.get("issueTypes") or []
    feature_types = [x for x in types if (x.get("name") or "").casefold() == "feature"]
    if not feature_types:
        names = ", ".join(sorted({x.get("name","?") for x in types})) or "none returned"
        fail(f"CREATE BLOCKED: Jira does not expose a Feature issue type for project {project}. "
             f"Available create types: {names}. No substitute will be used. "
             "Ask the Jira administrator to configure Feature for this project, then rerun preflight.")
    if len(feature_types) != 1:
        fail("CREATE BLOCKED: Jira returned multiple Feature issue type entries; resolve configuration before creating.")

    issue_type_id = str(feature_types[0].get("id") or "")
    if not issue_type_id: fail("Create metadata did not include a Feature issue type ID.")
    fields_url = f"{base}/rest/api/3/issue/createmeta/{project}/issuetypes/{issue_type_id}?startAt=0&maxResults=100"
    _, field_meta = request("GET", fields_url, email, token)
    allowed_fields = {x.get("fieldId") for x in field_meta.get("values", field_meta.get("fields", []))}
    fields = build_fields(payload)
    # Check fields that Jira says are creatable. Required custom fields must be
    # configured/mapped explicitly; never guess custom field IDs or values.
    for key in fields:
        if key not in allowed_fields and key not in ("project", "issuetype"):
            fail(f"CREATE BLOCKED: field '{key}' is not present in Jira create metadata for Feature. "
                 "Review the project's create screen/field configuration.")
    if args.dry_run:
        print("DRY RUN PASSED: Feature issue type and submitted fields are available.")
        print("No Jira issue was created.")
        return 0

    # Final guard immediately before the only mutating request.
    if args.approved_sha256.lower() != hashlib.sha256(canonical_bytes(payload)).hexdigest():
        fail("Payload changed after approval. Create blocked.")
    print("Submitting one Jira Create request. No retries will be attempted.")
    status, result = request("POST", f"{base}/rest/api/3/issue", email, token, {"fields": fields})
    key = result.get("key")
    if not key:
        fail("Jira response did not include an issue key. Do not retry; obtain separate approval to verify.", 4)
    print(f"CREATED: {key}")
    print(f"URL: {base}/browse/{key}")
    print(f"HTTP status: {status}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
