#!/usr/bin/env bash
cat ~/.claude/agent-infra-claude.md
cat AGENT_INFRA_DIR/agent_docs/code-style-short.md
agent-tools --tree --depth 3 "$(pwd)"
