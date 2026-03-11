# Claude Code Automation

Orchestration layer for running Claude Code agents in Docker containers. Agents perform code analysis, planning, implementation, and review tasks on projects mounted into a sandboxed workspace.

## Pipelines

Three pipelines built on a shared runner that assembles agent prompts and dispatches them to Docker.

### Iterative Pipeline

Single-session iterative development. Runs one Docker invocation.

- Agent decomposes task, implements simplest necessary items, reviews for drift and excess
- Cycles decompose-implement-reduce until complete

### Managed Pipeline

Multi-session managed development with manager oversight.

- Manager agent scopes task into ordered work units
- Iterative agent implements each unit in its own session
- Manager reviews each result, decides proceed/adjust/done
- On adjust, manager rewrites remaining units before continuing

### Comprehensive Pipeline

Multi-stage development from architecture through implementation. Each stage is a separate agent invocation producing planning artifacts consumed by the next.

- Architecture agent drafts resource tree and pipeline sketch
- Specification agent makes structural then detail passes
- Implementation agent writes code per module from specs
- Planning artifacts accumulate in /workspace/planning/

## Module Structure

- claude_runner.py -- prompt assembly and agent dispatch
- pipeline_iterative.py -- iterative pipeline orchestration
- pipeline_managed.py -- managed pipeline orchestration
- pipeline_comprehensive.py -- comprehensive pipeline orchestration
- docker-claude.sh -- Docker wrapper for auth and volume mounts
- Dockerfile -- container image definition

## Agent Definitions

Agent instructions live in agents/. Each agent gets shared lifecycle instructions (shared.md) prepended to its role definition. The runner assembles the full prompt automatically.

Iterative and managed pipeline agents:
- iterative.md -- decompose-implement-reduce loop
- agent-manager.md -- task scoping and inter-session review

Comprehensive pipeline agents:
- agent-architecture.md -- resource tree and pipeline sketch
- agent-specification.md -- dependency analysis and function specs
- agent-implementation.md -- code implementation from specs

## Configuration

docker-claude.sh sources a `.env` file from the project root for host-specific paths. Copy `.env.example` or create `.env` with the following variables:

```
AGENT_DOCS="/path/to/agent-docs"
CODE_ANALYSIS="/path/to/code-analysis-tools"
REF_SIMPLIFIED_LEIA="/path/to/simplified-leia"
REF_HELICOPTER_PSYCHOMETRICS="/path/to/helicopter-psychometrics"
REF_COGNEE_INDUSTRY_BAYER="/path/to/cognee-industry-bayer/bayer"
REF_CUSTOM_SRE="/path/to/custom-sre"
```

AGENT_DOCS and CODE_ANALYSIS are mounted at /data/agent-docs/ and /data/code-analysis-tools/ respectively. Any variable prefixed with REF_ that points to an existing directory is mounted read-only at /data/reference/<dirname>. The .env file is gitignored.

## Directories

- workspace/ -- project subdirectories, each mounted into containers
- workspace/project/reports/ -- agent spin-down reports
- agents/ -- current agent definitions
- archive/ -- archived report bundles

## Project Isolation

Each pipeline run targets a named project subdirectory under workspace/. The Docker container mounts only that project's directory as /workspace, so agents from different pipeline runs cannot interfere with each other. Reports, planning artifacts, and code all live within the project directory.

## Usage

All pipelines require --project to specify the workspace subdirectory.

```bash
# Iterative pipeline -- single-session loop
python3 pipeline_iterative.py --project myproj --task "Build module bridge"
python3 pipeline_iterative.py --project myproj --task "Task" --restart

# Managed pipeline -- scoped iteration with manager oversight
python3 pipeline_managed.py --project myproj --task "Build feature X"
python3 pipeline_managed.py --project myproj --task "Build feature X" --only-scope
python3 pipeline_managed.py --project myproj --task "Build feature X" --restart

# Comprehensive pipeline -- architecture, specification, implementation
python3 pipeline_comprehensive.py --project myproj --task "Add feature X"
python3 pipeline_comprehensive.py --project myproj --only-architecture --task "task"
python3 pipeline_comprehensive.py --project myproj --only-spec-structural
python3 pipeline_comprehensive.py --project myproj --only-implement --modules mod_a
```

## Authentication

The Docker wrapper supports three auth methods in precedence order:

1. ANTHROPIC_API_KEY env var (API billing)
2. CLAUDE_CODE_OAUTH_TOKEN env var (Max subscription)
3. Auto-extract from ~/.claude/.credentials.json (Max subscription, default)

OAuth tokens expire in 8-12 hours; run `claude login` to refresh.

## Reference Projects

Agents consult reference projects at /data/reference/ for structure, naming, and figure style guidance. See Configuration above for mount setup.

## Code Analysis Tools

Code analysis utilities are mounted read-only at /data/code-analysis-tools/ inside containers:

- run.py -- generate resource trees
