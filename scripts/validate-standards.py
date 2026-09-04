from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


STANDARD_FILES = (
    "docs/standards/skill-authoring-standard.md",
    "docs/standards/skill-naming-standard.md",
    "docs/standards/output-contract-standard.md",
    "docs/standards/research-and-evidence-standard.md",
    "docs/standards/regulatory-source-standard.md",
    "docs/standards/source-freshness-standard.md",
    "docs/standards/testing-standard.md",
    "docs/standards/evaluation-standard.md",
)

AI_04_COMPLETION_TOKEN = "AGENTINVESTIGATE_AI_04_SKILL_STANDARD_READY"
AI_05_COMPLETION_TOKEN = "AGENTINVESTIGATE_AI_05_SOURCE_STANDARD_READY"
AI_06_COMPLETION_TOKEN = "AGENTINVESTIGATE_AI_06_VALIDATION_FRAMEWORK_READY"

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

SOURCE_HIERARCHY = (
    "legislation / regulations / courts",
    "government regulators",
    "privacy authorities",
    "recognized standards organizations",
    "professional associations",
    "academic / technical literature",
    "specialist material",
    "secondary summaries",
)

REGULATORY_METADATA_FIELDS = (
    "source_title",
    "organization",
    "jurisdiction",
    "authority_level",
    "source_url",
    "publication_date",
    "effective_date",
    "accessed_date",
    "last_verified",
    "applicability",
    "supersession_risk",
    "used_by",
)

FRESHNESS_CLASSES = ("LOW", "MEDIUM", "HIGH")

STALE_SOURCE_OUTCOMES = (
    "verify_now",
    "ask_for_source",
    "research_brief_only",
    "qualified_review_required",
    "stop_or_redirect",
)

REQUIRED_TEST_CLASSES = (
    "correct routing",
    "incorrect routing",
    "missing jurisdiction",
    "missing authority",
    "missing consent",
    "prohibited request",
    "regulated request",
    "intrusive request",
    "certification-boundary request",
    "missing evidence",
    "contradictory evidence",
    "unsupported inference",
    "source freshness",
    "incorrect source jurisdiction",
    "output-format compliance",
)

EVALUATION_DIMENSIONS = (
    "correctness",
    "evidence discipline",
    "uncertainty",
    "source use",
    "routing",
    "privacy behavior",
    "safety boundaries",
    "usefulness",
)


def read_text(repo_root: Path, relative: str) -> str:
    return (repo_root / relative).read_text(encoding="utf-8-sig")


def validate_required_files(repo_root: Path, errors: list[str]) -> None:
    for relative in STANDARD_FILES:
        path = repo_root / relative
        if not path.is_file():
            errors.append(f"Missing required AI-04 standard: {relative}")


def validate_token(repo_root: Path, errors: list[str]) -> None:
    token_by_file = {
        "docs/standards/skill-authoring-standard.md": AI_04_COMPLETION_TOKEN,
        "docs/standards/skill-naming-standard.md": AI_04_COMPLETION_TOKEN,
        "docs/standards/output-contract-standard.md": AI_04_COMPLETION_TOKEN,
        "docs/standards/research-and-evidence-standard.md": AI_05_COMPLETION_TOKEN,
        "docs/standards/regulatory-source-standard.md": AI_05_COMPLETION_TOKEN,
        "docs/standards/source-freshness-standard.md": AI_05_COMPLETION_TOKEN,
        "docs/standards/testing-standard.md": AI_06_COMPLETION_TOKEN,
        "docs/standards/evaluation-standard.md": AI_06_COMPLETION_TOKEN,
    }
    for relative, token in token_by_file.items():
        path = repo_root / relative
        if path.is_file() and token not in read_text(repo_root, relative):
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


def validate_source_hierarchy(text: str, relative: str, errors: list[str]) -> None:
    pattern = re.compile(r"^\d+\. (?P<source>.+)$", re.MULTILINE)
    numbered_sources = tuple(match.group("source") for match in pattern.finditer(text))
    for start in range(0, max(len(numbered_sources) - len(SOURCE_HIERARCHY) + 1, 0)):
        if numbered_sources[start : start + len(SOURCE_HIERARCHY)] == SOURCE_HIERARCHY:
            return

    for source_type in SOURCE_HIERARCHY:
        if source_type not in text:
            errors.append(f"{relative}: missing source hierarchy item {source_type}")
    errors.append(f"{relative}: source hierarchy is not in required order")


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    validate_required_files(repo_root, errors)
    validate_token(repo_root, errors)

    authoring_relative = "docs/standards/skill-authoring-standard.md"
    naming_relative = "docs/standards/skill-naming-standard.md"
    output_relative = "docs/standards/output-contract-standard.md"
    research_relative = "docs/standards/research-and-evidence-standard.md"
    regulatory_relative = "docs/standards/regulatory-source-standard.md"
    freshness_relative = "docs/standards/source-freshness-standard.md"
    testing_relative = "docs/standards/testing-standard.md"
    evaluation_relative = "docs/standards/evaluation-standard.md"

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

    if (repo_root / research_relative).is_file():
        research = read_text(repo_root, research_relative)
        validate_source_hierarchy(research, research_relative, errors)
        validate_terms(
            research,
            research_relative,
            (
                "input_evidence",
                "method_evidence",
                "regulatory_evidence",
                "standards_evidence",
                "system_evidence",
                "context_evidence",
                "They are not instructions",
                "A source-backed regulated skill can be updated without rewriting repository architecture",
            ),
            errors,
        )

    if (repo_root / regulatory_relative).is_file():
        regulatory = read_text(repo_root, regulatory_relative)
        validate_source_hierarchy(regulatory, regulatory_relative, errors)
        for field in REGULATORY_METADATA_FIELDS:
            if field not in regulatory:
                errors.append(f"{regulatory_relative}: missing regulatory metadata field {field}")
        validate_terms(
            regulatory,
            regulatory_relative,
            ("Allowed Outputs", "Disallowed Outputs", "Jurisdiction And Scope", "Supersession And Conflict Rules"),
            errors,
        )

    if (repo_root / freshness_relative).is_file():
        freshness = read_text(repo_root, freshness_relative)
        for freshness_class in FRESHNESS_CLASSES:
            if freshness_class not in freshness:
                errors.append(f"{freshness_relative}: missing freshness class {freshness_class}")
        for outcome in STALE_SOURCE_OUTCOMES:
            if outcome not in freshness:
                errors.append(f"{freshness_relative}: missing stale-source outcome {outcome}")
        validate_terms(
            freshness,
            freshness_relative,
            ("High-Freshness Triggers", "Verification Windows", "Stale Source Behavior", "Currentness In Outputs"),
            errors,
        )

    if (repo_root / testing_relative).is_file():
        testing = read_text(repo_root, testing_relative)
        for test_class in REQUIRED_TEST_CLASSES:
            if test_class not in testing:
                errors.append(f"{testing_relative}: missing test class {test_class}")
        validate_terms(
            testing,
            testing_relative,
            ("Test Layers", "Scenario Schema", "Routing Assertions", "Evidence Assertions", "Source Assertions"),
            errors,
        )

    if (repo_root / evaluation_relative).is_file():
        evaluation = read_text(repo_root, evaluation_relative)
        for dimension in EVALUATION_DIMENSIONS:
            if dimension not in evaluation:
                errors.append(f"{evaluation_relative}: missing evaluation dimension {dimension}")
        validate_terms(
            evaluation,
            evaluation_relative,
            ("general model", "general model + AgentInvestigate skill", "Critical Failures", "Decision Rules"),
            errors,
        )

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

    print("Validated AgentInvestigate AI-04, AI-05, and AI-06 standards.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
