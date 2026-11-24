#!/usr/bin/env python3
"""Offline validation and approval-digest generation for a Jira Feature payload."""
import argparse, hashlib, json, re, sys
from pathlib import Path

REQUIRED = ("summary", "description")
ALLOWED = {
    "project_key", "issue_type", "summary", "description", "labels",
    "components", "priority", "parent_key", "assumptions", "sources",
    "expected_value", "measurement_of_value"
}

def canonical_bytes(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")

def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ["Payload root must be a JSON object."]
    unknown = sorted(set(data) - ALLOWED)
    if unknown:
        errors.append("Unsupported payload properties: " + ", ".join(unknown))
    for field in REQUIRED:
        if not isinstance(data.get(field), str) or not data[field].strip():
            errors.append(f"'{field}' must be a non-empty string.")
    if data.get("issue_type") != "Feature":
        errors.append("issue_type must be exactly 'Feature'. No fallback issue types are permitted.")
    project = data.get("project_key")
    if not isinstance(project, str) or not re.fullmatch(r"[A-Z][A-Z0-9_]+", project):
        errors.append("project_key must be a Jira project key such as AIST.")
    if isinstance(data.get("summary"), str) and len(data["summary"]) > 255:
        errors.append("summary exceeds Jira's 255-character limit.")
    for field in ("labels", "components", "assumptions", "sources"):
        if field in data and (not isinstance(data[field], list) or not all(isinstance(x, str) for x in data[field])):
            errors.append(f"'{field}' must be an array of strings.")
    if "priority" in data and data["priority"] is not None and not isinstance(data["priority"], str):
        errors.append("'priority' must be a string when supplied.")
    if "parent_key" in data and data["parent_key"] is not None:
        errors.append("Parent/child linking is not supported by Feature Writer Create.")
    return errors

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("payload", type=Path)
    args = ap.parse_args()
    try:
        data = json.loads(args.payload.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"Cannot read payload JSON: {exc}", file=sys.stderr); return 2
    errors = validate(data)
    if errors:
        print("PAYLOAD INVALID")
        for e in errors: print(f"- {e}")
        return 2
    digest = hashlib.sha256(canonical_bytes(data)).hexdigest()
    print("PAYLOAD VALID")
    print(f"Project: {data['project_key']}")
    print(f"Issue type: {data['issue_type']}")
    print(f"Summary: {data['summary']}")
    print(f"Approval SHA-256: {digest}")
    print("Review the complete payload before approving Create.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
