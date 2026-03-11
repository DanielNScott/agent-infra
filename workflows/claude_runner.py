#!/usr/bin/env python3
"""
Claude agent runner.
Builds prompts from lifecycle and agent configs, dispatches to Docker.
"""

import subprocess, uuid, re, shutil
from datetime import datetime
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent
AGENTS_DIR = SCRIPT_DIR / "agents"
SHARED_FILE = AGENTS_DIR / "shared.md"
WORKSPACE_DIR = SCRIPT_DIR / "workspace"


# Project-scoped directories

def get_reports_dir(project):
    """Return reports directory for a project."""
    return WORKSPACE_DIR / project / "reports"


# File utilities

def find_latest_report(pattern, project):
    """Find most recent file matching glob pattern in project reports directory."""
    reports_dir = get_reports_dir(project)
    matches = list(reports_dir.glob(pattern))
    if not matches:
        return None
    return max(matches, key=lambda p: p.stat().st_mtime)


def load_text(path):
    """Load text file, return empty string if missing."""
    if path.exists():
        return path.read_text()
    return ""


def get_ids_from_report(path, prefix="Issue"):
    """Extract integer IDs from markdown headings like '## Issue 1: ...'."""
    text = path.read_text()
    return [int(m) for m in re.findall(rf'^##\s+{prefix}\s+(\d+)', text, re.MULTILINE)]


def archive_reports(project):
    """Archive existing reports for a project to a zip file."""
    reports_dir = get_reports_dir(project)
    if not reports_dir.exists():
        return

    files = list(reports_dir.iterdir())
    if not files:
        return

    archive_dir = SCRIPT_DIR / "archive"
    archive_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    archive_name = archive_dir / f"reports_{project}_{timestamp}"
    shutil.make_archive(str(archive_name), "zip", reports_dir)

    for f in files:
        f.unlink()

    print(f"Archived {len(files)} files to archive/{archive_name.name}.zip")


# Prompt assembly

def build_prompt(agent_type, task, session_uuid=None):
    """Assemble full prompt from lifecycle, agent config, and task."""

    if session_uuid is None:
        session_uuid = uuid.uuid4().hex[:8]

    # Load instruction files
    lifecycle = load_text(SHARED_FILE)
    agent_instructions = load_text(AGENTS_DIR / f"{agent_type}.md")

    # Assemble prompt
    prompt = f"""{lifecycle}

---
{agent_instructions}

---
Agent Type: {agent_type}
Session UUID: {session_uuid}

---
USER TASK:
{task}"""

    return prompt


# Execution

def run_agent(agent_type, task, project):
    """Run a Claude agent with the given task in a project workspace."""
    prompt = build_prompt(agent_type, task)

    result = subprocess.run(
        [str(SCRIPT_DIR / "docker-claude.sh"), project, prompt],
        capture_output=False
    )

    return result.returncode


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run Claude agent")
    parser.add_argument("--project", required=True, help="Project name")
    parser.add_argument("--agent", default="general", help="Agent type")
    parser.add_argument("--task", required=True, help="Task prompt")
    args = parser.parse_args()

    exit(run_agent(args.agent, args.task, args.project))
