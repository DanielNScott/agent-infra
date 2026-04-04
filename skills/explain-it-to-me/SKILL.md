---
name: agent-infra-explain-it-to-me
description: Use when the user asks for a structured explanation of a system, module, or concept in the codebase
argument-hint: "<topic to explain>"
---

Provide a structured explanation of the topic the user asked about, following the template in `agent_docs/template-explanation.md`.

If `$ARGUMENTS` is provided, use it as the topic. Otherwise ask the user what they would like explained.

Launch an agent (subagent_type: Explore) with a prompt that:
1. Reads `agent_docs/template-explanation.md` to load the explanation template.
2. Explores the codebase to gather the information needed to explain the requested topic.
3. Produces an explanation that strictly follows the template structure: system context, step-by-step walkthrough, links, mechanistic clarifications (if needed), and a resource tree / call-tree diagram.

Display the completed explanation to the user.
