"""
Patch ~/.claude/settings.json to register the agent-tools MCP server.
Adds the mcpServers entry if absent; leaves existing settings untouched.
"""

import json
import os
import shutil
import sys


SETTINGS_PATH = os.path.expanduser("~/.claude/settings.json")
SERVER_NAME = "agent-tools"


def configure(mcp_command):
    """Add agent-tools MCP server entry to Claude settings."""

    # Load existing settings or start fresh
    if os.path.exists(SETTINGS_PATH):
        with open(SETTINGS_PATH) as f:
            settings = json.load(f)
    else:
        settings = {}

    # Add mcpServers block if absent
    if "mcpServers" not in settings:
        settings["mcpServers"] = {}

    settings["mcpServers"][SERVER_NAME] = {"command": mcp_command, "args": []}

    # Write back with indentation
    with open(SETTINGS_PATH, "w") as f:
        json.dump(settings, f, indent=2)
        f.write("\n")

    print(f"Registered MCP server '{SERVER_NAME}' in {SETTINGS_PATH}")


def deconfigure():
    """Remove agent-tools MCP server entry from Claude settings."""

    if not os.path.exists(SETTINGS_PATH):
        return

    with open(SETTINGS_PATH) as f:
        settings = json.load(f)

    removed = settings.get("mcpServers", {}).pop(SERVER_NAME, None)

    if removed is not None:
        with open(SETTINGS_PATH, "w") as f:
            json.dump(settings, f, indent=2)
            f.write("\n")
        print(f"Removed MCP server '{SERVER_NAME}' from {SETTINGS_PATH}")


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("install", "uninstall"):
        print("Usage: configure_mcp.py install|uninstall [mcp_command]")
        sys.exit(1)

    if sys.argv[1] == "install":
        mcp_command = sys.argv[2] if len(sys.argv) > 2 else shutil.which("agent-tools-mcp")
        if not mcp_command:
            print("Error: agent-tools-mcp not found on PATH")
            sys.exit(1)
        configure(mcp_command)
    else:
        deconfigure()


if __name__ == "__main__":
    main()
