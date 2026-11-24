#!/usr/bin/env python3
"""Validate a mapped Jira Cloud create-issue request. Read-only; no API calls."""
import argparse, json
from pathlib import Path

def validate(data, cfg):
    errors = []
    if not isinstance(data, dict):
        return ["Request body root must be an object."]
    fields = data.get("fields")
    if not isinstance(fields, dict):
        return ["Jira request must contain an object named 'fields'."]

    for key in ("project", "issuetype", "summary", "description"):
        if key not in fields:
            errors.append(f"Jira fields.{key} is required.")

    project = fields.get("project", {})
    if isinstance(project, dict):
        project_key = project.get("key")
        allowed = cfg.get("allowed_projects", [])
        if project_key and project_key not in allowed:
            errors.append(f"Project {project_key!r} is not allowed by config.")
    else:
        errors.append("fields.project must be an object with a key.")

    issue_type = fields.get("issuetype", {})
    if isinstance(issue_type, dict):
        name = issue_type.get("name")
        allowed_types = cfg.get("allowed_issue_types", [])
        if name and name not in allowed_types:
            errors.append(f"Issue type {name!r} is not allowed by config.")
    else:
        errors.append("fields.issuetype must be an object.")

    summary = fields.get("summary")
    if not isinstance(summary, str) or not summary.strip():
        errors.append("fields.summary must be a non-empty string.")

    # Jira Cloud descriptions normally use Atlassian Document Format.
    desc = fields.get("description")
    if not isinstance(desc, dict) or desc.get("type") != "doc" or not isinstance(desc.get("content"), list):
        errors.append("fields.description must be an Atlassian Document Format (ADF) document.")

    return errors

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jira_request", help="Mapped Jira REST request JSON")
    ap.add_argument("--config", default="config/jira.config.json")
    args = ap.parse_args()
    try:
        req = json.loads(Path(args.jira_request).read_text(encoding="utf-8"))
        cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
    except Exception as e:
        print(f"ERROR: Cannot read JSON: {e}")
        return 2
    errs = validate(req, cfg)
    if errs:
        print("\n".join("ERROR: " + e for e in errs))
        return 1
    print("Mapped Jira create request passed structural/config validation.")
    print("No API call was made.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
