#!/usr/bin/env python3
"""
Feature Writer Jira Cloud Create draft.

Safety:
- No request is sent without --approved-create.
- --dry-run is read-only and prints a redacted request preview.
- This CLI flag is an additional safeguard, not a replacement for explicit
  conversational user permission.
- Does not automatically retry create requests.
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error
import base64
from pathlib import Path
from dotenv import load_dotenv

REQUIRED_PAYLOAD_FIELDS = ("summary", "description", "expectedValue", "measurementOfValue")

REPO_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = REPO_ROOT / ".env"

load_dotenv(ENV_FILE)

email = os.getenv("JIRA_EMAIL")
token = os.getenv("JIRA_API_TOKEN")

if not email or not token:
    raise RuntimeError(
        "Jira authentication is not configured. "
        "Please set JIRA_EMAIL and JIRA_API_TOKEN in .env."
    )

def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def validate_config(cfg):
    errors=[]
    if not cfg.get("base_url"): errors.append("Missing base_url.")
    if cfg.get("deployment") != "cloud":
        errors.append("This draft supports Jira Cloud only (deployment must be 'cloud').")
    project=cfg.get("default_project")
    if not project: errors.append("Missing default_project.")
    if project not in cfg.get("allowed_projects", []):
        errors.append("default_project must be in allowed_projects.")
    if cfg.get("default_issue_type") != "Feature":
        errors.append("default_issue_type must be 'Feature' for this isolated script.")
    if "Feature" not in cfg.get("allowed_issue_types", []):
        errors.append("'Feature' must be in allowed_issue_types.")
    fields=cfg.get("fields", {})
    for mapping in ("expected_value", "measurement_of_value"):
        if not fields.get(mapping) or str(fields[mapping]).startswith("TBD"):
            errors.append(f"Configure Jira field ID for fields.{mapping}.")
    return errors

def validate_payload(payload):
    errors=[]
    if not isinstance(payload, dict): return ["Payload root must be a JSON object."]
    for key in REQUIRED_PAYLOAD_FIELDS:
        value=payload.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{key} must be a non-empty string.")
    extra=set(payload)-set(REQUIRED_PAYLOAD_FIELDS)
    if extra: errors.append("Unexpected payload keys: "+", ".join(sorted(extra)))
    return errors

def text_to_adf(text):
    # Minimal ADF paragraph representation. Preserves line breaks as paragraphs.
    paragraphs=[]
    for line in text.splitlines():
        paragraphs.append({
            "type":"paragraph",
            "content":[{"type":"text","text":line}] if line else []
        })
    if not paragraphs:
        paragraphs=[{"type":"paragraph","content":[]}]
    return {"type":"doc","version":1,"content":paragraphs}

def build_request(payload, cfg):
    project=cfg["default_project"]
    issue_type=cfg["default_issue_type"]
    fields={
        "project":{"key":project},
        "issuetype":{"name":issue_type},
        "summary":payload["summary"].strip(),
        "description":text_to_adf(payload["description"]),
        "labels":cfg.get("default_labels", []),
    }
    mappings=cfg.get("fields", {})
    fields[mappings["expected_value"]]=payload["expectedValue"]
    fields[mappings["measurement_of_value"]]=payload["measurementOfValue"]
    for k,v in cfg.get("default_fields", {}).items():
        if k not in fields:
            fields[k]=v
    return {"fields":fields}

def redacted_preview(request):
    preview=json.loads(json.dumps(request))
    return preview

def jira_create(cfg, request):
    base=cfg["base_url"].rstrip("/")
    url=base+"/rest/api/3/issue"
    email=os.environ.get("JIRA_EMAIL")
    token=os.environ.get("JIRA_API_TOKEN")
    if not email or not token:
        raise RuntimeError("JIRA_EMAIL and JIRA_API_TOKEN environment variables are required.")
    auth=base64.b64encode(f"{email}:{token}".encode()).decode()
    body=json.dumps(request).encode("utf-8")
    req=urllib.request.Request(
        url, data=body, method="POST",
        headers={
            "Authorization":"Basic "+auth,
            "Accept":"application/json",
            "Content-Type":"application/json",
        }
    )
    timeout=int(cfg.get("timeout_seconds",30))
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status, response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        # Do not include auth headers or credentials in output.
        details=e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Jira returned HTTP {e.code}: {details}") from None
    except urllib.error.URLError as e:
        # Outcome can be ambiguous for POST. Caller must not blindly retry.
        raise RuntimeError(f"Network error during create; outcome may be ambiguous. Do not retry blindly. Details: {e.reason}") from None

def main():
    ap=argparse.ArgumentParser(description="Create a Jira Feature (explicit approval gate).")
    ap.add_argument("--payload", default="feature-payload.json")
    ap.add_argument("--config", default="config/fwrt_jira.config.json")
    ap.add_argument("--dry-run", action="store_true", help="Validate and preview; no API request.")
    ap.add_argument("--approved-create", action="store_true", help="Required safety flag after explicit user approval.")
    args=ap.parse_args()

    try:
        cfg=read_json(args.config)
        payload=read_json(args.payload)
    except Exception as exc:
        print(f"ERROR reading input: {exc}", file=sys.stderr)
        return 2

    errors=validate_config(cfg)+validate_payload(payload)
    if errors:
        print("\n".join("ERROR: "+e for e in errors), file=sys.stderr)
        return 2

    request=build_request(payload,cfg)
    if args.dry_run:
        print("DRY RUN — no Jira request made.")
        print(json.dumps(redacted_preview(request), indent=2, ensure_ascii=False))
        return 0

    if not args.approved_create:
        print("BLOCKED: --approved-create is required. This is not conversational approval.", file=sys.stderr)
        return 3

    try:
        status, response=jira_create(cfg,request)
        data=json.loads(response)
        key=data.get("key")
        if key:
            print(f"Created Jira issue: {key}")
            print(cfg["base_url"].rstrip("/")+"/browse/"+key)
        else:
            print(f"Jira returned HTTP {status}, but no issue key was found in response.")
            print("Treat this as potentially successful; verify with a separately approved Read.")
        return 0
    except Exception as exc:
        print(f"CREATE ERROR: {exc}", file=sys.stderr)
        print("If the request outcome is ambiguous, do not retry until a separately approved Read verifies whether the issue exists.", file=sys.stderr)
        return 1

if __name__=="__main__":
    raise SystemExit(main())
