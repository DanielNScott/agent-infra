#!/usr/bin/env python3
"""
Iterative development pipeline.
Invokes a single iterative agent session that loops internally.
"""

import argparse
from claude_runner import run_agent, archive_reports


def run_pipeline(project, task):
    """Run iterative development agent on the given task."""
    print("=== Running Iterative Development ===")
    return run_agent("iterative", task, project)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Iterative development pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ./pipeline_iterative.py --project myproj --task "Implement X"
  ./pipeline_iterative.py --project myproj --task "Implement X" --restart

Notes:
  - Runs a single agent session that iterates internally
  - Agent cycles: decompose -> implement -> review/reduce
  - Agent stops when task is complete and codebase is minimal
"""
    )

    parser.add_argument("--project", required=True, help="Project name (workspace subdirectory)")
    parser.add_argument("--task", required=True, help="Development task description")
    parser.add_argument("--restart", action="store_true",
                        help="Archive old reports before starting")

    args = parser.parse_args()

    if args.restart:
        archive_reports(args.project)

    exit(run_pipeline(args.project, args.task))
