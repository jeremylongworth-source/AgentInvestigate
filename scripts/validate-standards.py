from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


STANDARD_FILES = (
    "docs/standards/skill-authoring-standard.md",
    "docs/standards/skill-naming-standard.md",
    "docs/standards/output-contract-standard.md",
)

COMPLETION_TOKEN = "AGENTINVESTIGATE_AI_04_SKILL_STANDARD_READY"

AUTHORING_REQUIRED_TERMS = (
    "naming",
    "frontmatter",
    "description",
    "Triggers",
    "Non-Triggers",
    "Required Inputs",
    "Optional Inputs",
    "Assumptions",
    "Dependencies",
    "Core Procedure",
    "Evidence Requirements",
    "Source Requirements",
    "Jurisdiction Requirements",
    "Authority Checks",
    "Sensitivity Handling",
    "Output Contract",
    "Limitations",
    "Escalation",
    "References",
    "Testing",
)

AUTHORING_SECTION_ORDER = (
    "Overview",
    "Triggers",
    "Non-Triggers",
    "Required Inputs",
    "Optional Inputs",
    "Assumptions",
    "Dependencies",
    "Core Procedure",
    "Evidence Requirements",
    "Source Requirements",
    "Jurisdiction Requirements",
    "Authority Checks",
    "Sensitivity Handling",
    "Output Contract",
    "Limitations",
    "Escalation",
    "References",
    "Testing",
)

NAMING_REQUIRED_TERMS = (
    "<verb>-<investigative-or-security-object>",
    "docs/architecture/taxonomy-index.yaml",
    "Disallowed Patterns",
    "Naming Review",
    "prohibited capability",
)

OUTPUT_REQUIRED_TERMS = (
    "facts",
    "allegation",
    "inference",
    "unknowns",
    "limitations",
    "jurisdiction",
    "authority status",
    "human-approval status",
    "qualified-review",
    "Testing Requirements",
)

SENSITIVITY_CLASSES = (
    "ROUTINE",
    "REGULATED",
    "INTRUSIVE",
    "CERTIFICATION_BOUNDARY",
)


def read_text(repo_root: Path, relative: str) -> str:
    return (repo_root / relative).read_text(encoding="utf-8-sig")


def validate_required_files(repo_root: Path, errors: list[str]) -> None:
    for relative in STANDARD_FILES:
        path = repo_root / relative
        if not path.is_file():
            errors.append(f"Missing required AI-04 standard: {relative}")


def validate_token(repo_root: Path, errors: list[str]) -> None:
    for relative in STANDARD_FILES:
        path = repo_root / relative
        if path.is_file() and COMPLETION_TOKEN not in read_text(repo_root, relative):
            errors.append(f"{relative}: missing completion token")


def validate_terms(text: str, relative: str, terms: tuple[str, ...], errors: list[str]) -> None:
    for term in terms:
        if term not in text:
            errors.append(f"{relative}: missing required term {term}")


def validate_authoring_section_order(text: str, errors: list[str]) -> None:
    match = re.search(r"Every skill must include these `##` sections in this order:\n\n(?P<body>(?:\d+\. `[^`]+`\n?)+)", text)
    if not match:
        errors.append("docs/standards/skill-authoring-standard.md: missing required section-order list")
        return

    found = re.findall(r"\d+\. `([^`]+)`", match.group("body"))
    if tuple(found) != AUTHORING_SECTION_ORDER:
        errors.append(
            "docs/standards/skill-authoring-standard.md: required skill sections are not in the standard order"
        )


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    validate_required_files(repo_root, errors)
    validate_token(repo_root, errors)

    authoring_relative = "docs/standards/skill-authoring-standard.md"
    naming_relative = "docs/standards/skill-naming-standard.md"
    output_relative = "docs/standards/output-contract-standard.md"

    if (repo_root / authoring_relative).is_file():
        authoring = read_text(repo_root, authoring_relative)
        validate_terms(authoring, authoring_relative, AUTHORING_REQUIRED_TERMS, errors)
        validate_authoring_section_order(authoring, errors)
        for sensitivity_class in SENSITIVITY_CLASSES:
            if sensitivity_class not in authoring:
                errors.append(f"{authoring_relative}: missing sensitivity class {sensitivity_class}")

    if (repo_root / naming_relative).is_file():
        naming = read_text(repo_root, naming_relative)
        validate_terms(naming, naming_relative, NAMING_REQUIRED_TERMS, errors)

    if (repo_root / output_relative).is_file():
        output = read_text(repo_root, output_relative)
        validate_terms(output, output_relative, OUTPUT_REQUIRED_TERMS, errors)
        for sensitivity_class in SENSITIVITY_CLASSES:
            if sensitivity_class not in output:
                errors.append(f"{output_relative}: missing sensitivity class {sensitivity_class}")

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

    print("Validated AgentInvestigate AI-04 standards.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
