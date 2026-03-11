CLAUDE_DIR := $(HOME)/.claude
AGENTS_DIR := $(CLAUDE_DIR)/agents
SKILLS_DIR := $(CLAUDE_DIR)/skills
REPO_DIR := $(shell pwd)

.PHONY: install uninstall update

install:
	uv tool install --editable $(REPO_DIR)/agent_tools
	mkdir -p $(AGENTS_DIR) $(SKILLS_DIR)
	ln -sfn $(REPO_DIR)/agents/subagents $(AGENTS_DIR)/agent-infra
	ln -sfn $(REPO_DIR)/skills $(SKILLS_DIR)/agent-infra
	sed 's|AGENT_INFRA_DIR|$(REPO_DIR)|g' $(REPO_DIR)/agent_docs/claude.md > $(CLAUDE_DIR)/agent-infra-claude.md
	python3 $(REPO_DIR)/agent_tools/agent_tools/configure_mcp.py install

uninstall:
	python3 $(REPO_DIR)/agent_tools/agent_tools/configure_mcp.py uninstall
	uv tool uninstall agent-tools
	rm -f $(AGENTS_DIR)/agent-infra
	rm -f $(SKILLS_DIR)/agent-infra
	rm -f $(CLAUDE_DIR)/agent-infra-claude.md

update:
	uv tool install --editable $(REPO_DIR)/agent_tools
