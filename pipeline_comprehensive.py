#!/usr/bin/env python3
"""
Development pipeline.
Runs architecture, specification, and implementation agents in sequence.
"""

import argparse
import re
from claude_runner import run_agent, find_latest_report, archive_reports


def parse_module_spec(spec):
    """Parse module specification: single name or comma-separated list."""
    if spec is None:
        return None
    return [s.strip() for s in spec.split(",")]


def get_module_ids(report_path):
    """Extract module names from specification report headings like '## Module name'."""
    text = report_path.read_text()
    return re.findall(r'^##\s+Module\s+(\S+)', text, re.MULTILINE)


# Pipeline stages

def run_architecture(project, task):
    """Run architecture agent to produce resource tree and pipeline sketch."""
    print("=== Running Architecture Planning ===")
    return run_agent("agent-architecture", f"mode=plan, task={task}", project)


def run_spec_structural(project):
    """Run specification agent structural pass (call graph, contracts, deps, def-use)."""
    print("=== Running Specification: Structural Pass ===")
    return run_agent("agent-specification", "mode=structural", project)


def run_spec_detail(project):
    """Run specification agent detail pass (function specifications)."""
    print("=== Running Specification: Detail Pass ===")
    return run_agent("agent-specification", "mode=detail", project)


def run_revise(project, agent_type, report_path):
    """Run an agent in revision mode with a report."""
    print(f"=== Running Revision: {agent_type} ===")
    task = f"mode=revise, report=/workspace/reports/{report_path.name}"
    return run_agent(agent_type, task, project)


def run_implement(project, module_name):
    """Implement a specific module."""
    print(f"=== Implementing Module: {module_name} ===")
    return run_agent("agent-implementation", f"module={module_name}", project)


# Pipeline execution

def run_pipeline(project, task=None, modules=None, only_architecture=False,
                 only_spec_structural=False, only_spec_detail=False, only_implement=False):
    """Execute pipeline stages based on options."""

    # Single stage modes
    if only_architecture:
        if not task:
            print("Error: --only-architecture requires --task")
            return 1
        return run_architecture(project, task)

    if only_spec_structural:
        return run_spec_structural(project)

    if only_spec_detail:
        return run_spec_detail(project)

    if only_implement:
        if not modules:
            print("Error: --only-implement requires --modules")
            return 1
        for mod in modules:
            ret = run_implement(project, mod)
            if ret != 0:
                return ret
        return 0

    # Full pipeline
    if not task:
        print("Error: Full pipeline requires --task")
        return 1

    # Step 1: Architecture
    ret = run_architecture(project, task)
    if ret != 0:
        return ret

    # Step 2: Specification structural pass
    ret = run_spec_structural(project)
    if ret != 0:
        return ret

    # Step 3: Specification detail pass
    ret = run_spec_detail(project)
    if ret != 0:
        return ret

    # Step 4: Implement modules
    if modules is None:
        spec_report = find_latest_report("*_agent-specification_*.md", project)
        if not spec_report:
            print("Error: Specification did not produce a report")
            return 1
        modules = get_module_ids(spec_report)

    if not modules:
        print("No modules found to implement")
        return 1

    print(f"\nFound {len(modules)} modules to implement")

    total_implemented = 0
    for mod in modules:
        print(f"\n--- Module: {mod} ---")

        ret = run_implement(project, mod)
        if ret != 0:
            print(f"Warning: Implementation failed for module {mod}")
            continue

        total_implemented += 1

    print(f"\n=== Pipeline complete: {total_implemented} modules implemented ===")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Development pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ./pipeline_comprehensive.py --project myproj --task "Build feature X"
  ./pipeline_comprehensive.py --project myproj --task "Build feature X" --modules mod_a,mod_b
  ./pipeline_comprehensive.py --project myproj --only-architecture --task "task"
  ./pipeline_comprehensive.py --project myproj --only-spec-structural
  ./pipeline_comprehensive.py --project myproj --only-spec-detail
  ./pipeline_comprehensive.py --project myproj --only-implement --modules mod
  ./pipeline_comprehensive.py --project myproj --task "task" --restart

Pipeline stages:
  1. Architecture: resource tree and pipeline sketch
  2. Specification (structural): call graph, contracts, reverse deps, def-use
  3. Specification (detail): function specifications per module
  4. Implementation: code from specifications, per module
"""
    )

    parser.add_argument("--project", required=True, help="Project name (workspace subdirectory)")
    parser.add_argument("--task", help="Development task description")
    parser.add_argument("--modules", help="Module name(s), comma-separated")
    parser.add_argument("--only-architecture", action="store_true", help="Run only architecture planning")
    parser.add_argument("--only-spec-structural", action="store_true", help="Run only structural specification")
    parser.add_argument("--only-spec-detail", action="store_true", help="Run only detail specification")
    parser.add_argument("--only-implement", action="store_true", help="Run only implementation")
    parser.add_argument("--restart", action="store_true", help="Archive old reports before starting")

    args = parser.parse_args()

    if args.restart:
        archive_reports(args.project)

    modules = parse_module_spec(args.modules)

    exit(run_pipeline(
        project=args.project,
        task=args.task,
        modules=modules,
        only_architecture=args.only_architecture,
        only_spec_structural=args.only_spec_structural,
        only_spec_detail=args.only_spec_detail,
        only_implement=args.only_implement
    ))
