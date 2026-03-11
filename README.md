# Agent-infra

Agent infrastructure for Claude Code: installable tools, agent definitions, skills, and workflow pipelines.

## Motivation

This repository centralizes Claude Code instructions, coding guidelines, document templates, installable CLI tools, an MCP server, agent definitions, skills, and Docker-based workflow pipelines.

## Project Structure

- `agent_tools/` installable Python package exposing CLI and MCP server
- `agent_docs/` Claude Code instructions, coding guidelines, and document templates
- `agents/` agent definitions (pipeline prompt files and Claude Code subagents)
- `skills/` slash command definitions
- `workflows/` Docker-based pipeline orchestration
- `docs/` project documentation and ADRs

## Setup

Install everything with:

```bash
git clone <repo> /home/dan/code/agent-infra
cd /home/dan/code/agent-infra
make install
```

Then add the startup hook to `~/.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "type": "command",
        "command": "cat /home/dan/code/agent-infra/agent_docs/claude.md"
      }
    ]
  }
}
```
