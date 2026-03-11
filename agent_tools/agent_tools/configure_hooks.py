"""
Patch ~/.claude/settings.json to register the SessionStart hook.
Adds the hook entry if absent; leaves existing settings untouched.
"""

import json
import os
import sys


SETTINGS_PATH = os.path.expanduser("~/.claude/settings.json")
STARTUP_SCRIPT = os.path.expanduser("~/.claude/agent-infra-startup.sh")
HOOK_COMMAND = f"bash {STARTUP_SCRIPT}"


def configure():
    """Add SessionStart hook entry to Claude settings."""

    if os.path.exists(SETTINGS_PATH):
        with open(SETTINGS_PATH) as f:
            settings = json.load(f)
    else:
        settings = {}

    hooks = settings.setdefault("hooks", {})
    session_hooks = hooks.setdefault("SessionStart", [])

    # Check if our hook is already registered
    for group in session_hooks:
        for hook in group.get("hooks", []):
            if hook.get("command") == HOOK_COMMAND:
                print(f"SessionStart hook already registered in {SETTINGS_PATH}")
                return

    session_hooks.append({"hooks": [{"type": "command", "command": HOOK_COMMAND}]})

    with open(SETTINGS_PATH, "w") as f:
        json.dump(settings, f, indent=2)
        f.write("\n")

    print(f"Registered SessionStart hook in {SETTINGS_PATH}")


def deconfigure():
    """Remove SessionStart hook entry from Claude settings."""

    if not os.path.exists(SETTINGS_PATH):
        return

    with open(SETTINGS_PATH) as f:
        settings = json.load(f)

    session_hooks = settings.get("hooks", {}).get("SessionStart", [])
    filtered = [
        group for group in session_hooks
        if not any(h.get("command") == HOOK_COMMAND for h in group.get("hooks", []))
    ]

    if len(filtered) == len(session_hooks):
        return

    settings["hooks"]["SessionStart"] = filtered

    with open(SETTINGS_PATH, "w") as f:
        json.dump(settings, f, indent=2)
        f.write("\n")

    print(f"Removed SessionStart hook from {SETTINGS_PATH}")


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("install", "uninstall"):
        print("Usage: configure_hooks.py install|uninstall")
        sys.exit(1)

    if sys.argv[1] == "install":
        configure()
    else:
        deconfigure()


if __name__ == "__main__":
    main()
