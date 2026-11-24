#!/usr/bin/env python3
"""Review a Jira config for Feature Writer compatibility. Read-only."""
import argparse, json
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("config", nargs="?", default="config/jira.config.json")
    args = ap.parse_args()
    cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
    problems, notes = [], []

    if cfg.get("deployment") != "cloud":
        notes.append("Config is not marked Jira Cloud; API adapter may need deployment-specific handling.")
    if not cfg.get("base_url"):
        problems.append("base_url is missing.")
    if not cfg.get("default_project"):
        problems.append("default_project is missing.")
    if cfg.get("default_project") not in cfg.get("allowed_projects", []):
        problems.append("default_project is not included in allowed_projects.")

    allowed_types = cfg.get("allowed_issue_types", [])
    default_type = cfg.get("default_issue_type")
    if default_type and default_type not in allowed_types:
        problems.append("default_issue_type is not included in allowed_issue_types.")

    if "Feature" not in allowed_types:
        problems.append("Feature issue type is NOT allowed by this config. Do not create Features using this config as-is.")
    if default_type == "Story":
        notes.append("Current default issue type is Story. Feature Writer must override via its isolated config, not change Story Writer defaults.")
    labels = cfg.get("default_labels", [])
    if "story-writer" in labels:
        notes.append("Story Writer label is present. Feature Writer should use isolated labels/config.")
    if not cfg.get("fields"):
        notes.append("No custom field mappings are configured.")

    print("CONFIG REVIEW")
    print(f"Base URL: {'present' if cfg.get('base_url') else 'missing'}")
    print(f"Default project: {cfg.get('default_project', '(missing)')}")
    print(f"Allowed projects: {', '.join(cfg.get('allowed_projects', []))}")
    print(f"Default issue type: {default_type or '(missing)'}")
    print(f"Allowed issue types: {', '.join(allowed_types)}")
    print("\nBLOCKERS:")
    if problems:
        for p in problems: print(f"- {p}")
    else: print("- None detected by this basic check.")
    print("\nNOTES:")
    for n in notes: print(f"- {n}")
    return 1 if problems else 0

if __name__ == "__main__":
    raise SystemExit(main())
