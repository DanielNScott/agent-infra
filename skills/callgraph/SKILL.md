---
name: agent-infra-callgraph
description: >
  Generate and display call graphs for a codebase directory. Analyzes function/method
  call relationships to visualize program flow and identify complexity hotspots.
  Trigger terms: call graph, callgraph, function dependencies, code flow,
  complexity analysis, program structure, dependency graph, who calls what.
argument-hint: "[directory]"
---

# Call Graph Analysis

Generate a call graph for the target directory using the `callgraph` MCP tool.

## Workflow

1. **Resolve directory**: Use `$ARGUMENTS` if provided. Otherwise, ask the user which directory to analyze.
2. **Validate path**: Confirm the directory exists (`ls` or `Glob`). If invalid, report the error and ask for correction.
3. **Generate graph**: Call the `callgraph` MCP tool with the resolved directory.
4. **Display results**: Present the call graph output to the user.
5. **Summarize**: Highlight high fan-out functions (many outgoing calls) and deeply nested call chains as complexity risks.

## Error Recovery

| Problem | Action |
|---------|--------|
| Directory does not exist | List parent directory contents, suggest closest match |
| `callgraph` MCP tool unavailable | Inform user the tool is not configured; suggest checking MCP setup |
| Empty output / no functions found | Confirm directory contains source files; suggest a subdirectory with code |

## Example

```
User: "Show me the call graph for src/engine"
→ Validate: ls src/engine (confirm exists)
→ Run: callgraph MCP tool with directory="src/engine"
→ Display: call graph output
→ Summarize: "processEvent has 12 outgoing calls — consider decomposing"
```
