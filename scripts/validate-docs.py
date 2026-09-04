from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_FILES = (
    "README.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "LICENSE",
    "AGENTS.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    ".gitattributes",
    ".gitignore",
    "docs/development/AI-00-baseline-audit.md",
    "docs/development/handoffs/AI-00-final-handoff.md",
    "docs/architecture/domain-contract.md",
    "docs/architecture/scope-boundaries.md",
    "docs/architecture/prohibited-capabilities.md",
    "docs/development/handoffs/AI-01-final-handoff.md",
    "docs/architecture/master-taxonomy-v1.md",
    "docs/architecture/taxonomy-index.yaml",
    "docs/development/handoffs/AI-02-final-handoff.md",
    "scripts/validate-all.ps1",
    "scripts/validate-docs.py",
    "scripts/validate-taxonomy.py",
    "scripts/generate-taxonomy.py",
)

REQUIRED_TOKENS = {
    "ROADMAP.md": (
        "AgentInvestigate Development Roadmap",
        "Roadmap version: 0.1",
        "AGENTINVESTIGATE_DEVELOPMENT_ROADMAP_V0_1_READY",
    ),
    "docs/development/AI-00-baseline-audit.md": (
        "AGENTINVESTIGATE_AI_00_BASELINE_READY",
        "Source handling rule applied",
        "No skill folders, skillsets, specializations, shared assets, fixtures, or future-wave architecture files were created.",
    ),
    "docs/development/handoffs/AI-00-final-handoff.md": (
        "AGENTINVESTIGATE_AI_00_BASELINE_READY",
        "AI-01: Domain & Scope Contract.",
    ),
    "docs/architecture/domain-contract.md": (
        "AGENTINVESTIGATE_AI_01_DOMAIN_CONTRACT_READY",
        "Private Investigation",
        "Private Security",
        "Taxonomy Family Mapping",
        "Every roadmap taxonomy family maps cleanly to the domain contract.",
    ),
    "docs/architecture/scope-boundaries.md": (
        "AGENTINVESTIGATE_AI_01_DOMAIN_CONTRACT_READY",
        "In Scope",
        "Out Of Scope",
        "Required Gates",
        "Acceptance Criteria",
    ),
    "docs/architecture/prohibited-capabilities.md": (
        "AGENTINVESTIGATE_AI_01_DOMAIN_CONTRACT_READY",
        "Absolute Exclusions",
        "Response And Routing Rules",
        "Design Constraints For Future Skills",
    ),
    "docs/development/handoffs/AI-01-final-handoff.md": (
        "AGENTINVESTIGATE_AI_01_DOMAIN_CONTRACT_READY",
        "AI-02: Master Taxonomy Integration.",
    ),
    "docs/architecture/master-taxonomy-v1.md": (
        "AGENTINVESTIGATE_AI_02_MASTER_TAXONOMY_READY",
        "`docs/architecture/taxonomy-index.yaml` is the canonical taxonomy source.",
        "Exactly one canonical taxonomy source exists: docs/architecture/taxonomy-index.yaml",
    ),
    "docs/architecture/taxonomy-index.yaml": (
        "AGENTINVESTIGATE_AI_02_MASTER_TAXONOMY_READY",
        "AgentInvestigate Master Taxonomy v1.0",
        "\"skills\": 212",
    ),
    "docs/development/handoffs/AI-02-final-handoff.md": (
        "AGENTINVESTIGATE_AI_02_MASTER_TAXONOMY_READY",
        "AI-03: Sensitivity, Authority & Routing Contract.",
    ),
}

IGNORED_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


def find_empty_dirs(repo_root: Path) -> list[Path]:
    empty_dirs: list[Path] = []
    for path in sorted(p for p in repo_root.rglob("*") if p.is_dir()):
        relative_parts = path.relative_to(repo_root).parts
        if any(part in IGNORED_DIRS for part in relative_parts):
            continue
        if not any(path.iterdir()):
            empty_dirs.append(path)
    return empty_dirs


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        path = repo_root / relative
        if not path.is_file():
            errors.append(f"Missing required file: {relative}")

    for relative, tokens in REQUIRED_TOKENS.items():
        path = repo_root / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8-sig")
        for token in tokens:
            if token not in text:
                errors.append(f"{relative}: missing required text {token}")

    for path in find_empty_dirs(repo_root):
        errors.append(f"Empty directory should not be committed: {path.relative_to(repo_root)}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    errors = validate(repo_root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("Validated AgentInvestigate baseline documentation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
