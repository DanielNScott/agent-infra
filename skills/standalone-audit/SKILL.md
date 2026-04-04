---
name: agent-infra-standalone-audit
description: Use when the user asks for a quality audit of recent changes, or before committing to check for LLM-specific code quality problems
argument-hint: "[description of what the changes are trying to accomplish]"
---

Run a standalone quality audit on the current diff using the `agent-standalone-quality-audit` agent.

If `$ARGUMENTS` is provided, pass it as the stated goals. If not, pass "infer" so the agent determines intent from the diff and recent commits.

Launch the agent with the Agent tool (subagent_type: general-purpose) and include the goals in the prompt. When the agent returns, display the report path and a concise summary of the findings to the user.
