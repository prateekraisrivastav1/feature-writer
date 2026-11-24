#!/usr/bin/env python3
"""Copilot preToolUse guard for Feature Writer Jira-create commands.

Reads hook JSON from stdin. It only guards shell commands that appear to invoke
fwrt_jira_create.py. It does not invoke Jira.
"""
import json, re, sys

def main():
    try:
        event=json.load(sys.stdin)
    except Exception:
        print(json.dumps({"permissionDecision":"deny",
                          "permissionDecisionReason":"Feature Writer hook could not parse tool input; fail closed."}))
        return 0

    tool=(event.get("toolName") or event.get("tool_name") or "").lower()
    args=event.get("toolArgs", event.get("tool_input", {}))
    if isinstance(args, str):
        try: args=json.loads(args)
        except Exception: args={"raw":args}
    command=str(args.get("command", args.get("cmd", args.get("raw","")))) if isinstance(args,dict) else str(args)

    # Only guard shell tool invocations mentioning the Feature Writer create script.
    if tool not in ("bash","powershell","basheshell","shell") or "fwrt_jira_create.py" not in command:
        return 0

    if re.search(r"(^|\s)--approved-create(\s|$)", command):
        # This flag is a secondary safety gate, not proof of conversational approval.
        return 0

    print(json.dumps({
        "permissionDecision":"deny",
        "permissionDecisionReason":"Feature Writer Jira Create script requires the explicit --approved-create gate. Confirm the exact Jira action with the user first."
    }))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
