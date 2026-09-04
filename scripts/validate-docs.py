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
    "scripts/validate-all.ps1",
    "scripts/validate-docs.py",
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
