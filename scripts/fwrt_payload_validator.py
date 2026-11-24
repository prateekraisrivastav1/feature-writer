#!/usr/bin/env python3
"""Validate Feature draft payload before Jira mapping. Read-only."""
import argparse, json
from pathlib import Path

REQUIRED = ("summary", "description", "expectedValue", "measurementOfValue")

def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ["Payload root must be a JSON object."]
    missing = [k for k in REQUIRED if k not in data]
    if missing: errors.append("Missing required fields: " + ", ".join(missing))
    for k in REQUIRED:
        if k in data and (not isinstance(data[k], str) or not data[k].strip()):
            errors.append(f"{k} must be a non-empty string.")
    extras = sorted(set(data) - set(REQUIRED))
    if extras: errors.append("Unexpected fields: " + ", ".join(extras))
    return errors

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("payload", nargs="?", default="feature-payload.json")
    args = ap.parse_args()
    try:
        obj = json.loads(Path(args.payload).read_text(encoding="utf-8"))
    except Exception as e:
        print(f"ERROR: Cannot read JSON: {e}")
        return 2
    errs = validate(obj)
    if errs:
        print("\n".join("ERROR: " + e for e in errs))
        return 1
    print("Feature draft payload is structurally valid.")
    print("NOTE: This is not yet a Jira REST API payload; Jira field mapping is a separate step.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
