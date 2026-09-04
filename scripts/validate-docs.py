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
    "docs/architecture/sensitivity-model.md",
    "docs/architecture/authority-routing.md",
    "docs/architecture/intrusive-task-gate.md",
    "docs/architecture/certification-boundaries.md",
    "docs/development/handoffs/AI-03-final-handoff.md",
    "docs/standards/skill-authoring-standard.md",
    "docs/standards/skill-naming-standard.md",
    "docs/standards/output-contract-standard.md",
    "docs/development/handoffs/AI-04-final-handoff.md",
    "docs/standards/research-and-evidence-standard.md",
    "docs/standards/regulatory-source-standard.md",
    "docs/standards/source-freshness-standard.md",
    "docs/development/handoffs/AI-05-final-handoff.md",
    "docs/standards/testing-standard.md",
    "docs/standards/evaluation-standard.md",
    "tests/validation-scenarios.json",
    "tests/evaluation-rubric.json",
    "docs/development/handoffs/AI-06-final-handoff.md",
    "docs/foundations/foundation-catalog.md",
    "docs/foundations/professional-vocabulary.md",
    "docs/foundations/shared-schemas.md",
    "docs/foundations/report-structure-contracts.md",
    "docs/foundations/foundation-consumer-map.json",
    "docs/development/handoffs/AI-07-final-handoff.md",
    "tests/reference-skills/AI-08-reference-scenarios.json",
    "docs/development/handoffs/AI-08-final-handoff.md",
    "tests/reference-skills/AI-09-professional-core-scenarios.json",
    "docs/development/handoffs/AI-09-final-handoff.md",
    "scripts/validate-all.ps1",
    "scripts/validate-docs.py",
    "scripts/validate-taxonomy.py",
    "scripts/generate-taxonomy.py",
    "scripts/validate-routing.py",
    "scripts/validate-standards.py",
    "scripts/validate-tests.py",
    "scripts/validate-foundations.py",
    "scripts/validate-skills.py",
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
    "docs/architecture/sensitivity-model.md": (
        "AGENTINVESTIGATE_AI_03_SENSITIVITY_ROUTING_READY",
        "ROUTINE",
        "REGULATED",
        "INTRUSIVE",
        "CERTIFICATION_BOUNDARY",
    ),
    "docs/architecture/authority-routing.md": (
        "AGENTINVESTIGATE_AI_03_SENSITIVITY_ROUTING_READY",
        "Representative Request Routing",
        "Representative requests from all four sensitivity classes route correctly on paper.",
    ),
    "docs/architecture/intrusive-task-gate.md": (
        "AGENTINVESTIGATE_AI_03_SENSITIVITY_ROUTING_READY",
        "No intrusive skill routes directly from a raw user request.",
        "Fail-Closed Conditions",
    ),
    "docs/architecture/certification-boundaries.md": (
        "AGENTINVESTIGATE_AI_03_SENSITIVITY_ROUTING_READY",
        "Allowed Support",
        "Prohibited Substitutes",
    ),
    "docs/development/handoffs/AI-03-final-handoff.md": (
        "AGENTINVESTIGATE_AI_03_SENSITIVITY_ROUTING_READY",
        "AI-04: Skill Authoring Standard.",
    ),
    "docs/standards/skill-authoring-standard.md": (
        "AGENTINVESTIGATE_AI_04_SKILL_STANDARD_READY",
        "Required Skill Sections",
        "Evidence Requirements",
        "Authority Checks",
        "Sensitivity Handling",
        "Output Contract",
    ),
    "docs/standards/skill-naming-standard.md": (
        "AGENTINVESTIGATE_AI_04_SKILL_STANDARD_READY",
        "<verb>-<investigative-or-security-object>",
        "Disallowed Patterns",
        "Naming Review",
    ),
    "docs/standards/output-contract-standard.md": (
        "AGENTINVESTIGATE_AI_04_SKILL_STANDARD_READY",
        "Universal Output Fields",
        "Evidence Output Requirements",
        "Sensitivity Output Requirements",
        "Testing Requirements",
    ),
    "docs/development/handoffs/AI-04-final-handoff.md": (
        "AGENTINVESTIGATE_AI_04_SKILL_STANDARD_READY",
        "AI-05: Legal, Regulatory & Evidence Source Standard.",
    ),
    "docs/standards/research-and-evidence-standard.md": (
        "AGENTINVESTIGATE_AI_05_SOURCE_STANDARD_READY",
        "Source Hierarchy",
        "Evidence Handling Requirements",
        "A source-backed regulated skill can be updated without rewriting repository architecture",
    ),
    "docs/standards/regulatory-source-standard.md": (
        "AGENTINVESTIGATE_AI_05_SOURCE_STANDARD_READY",
        "Regulatory Metadata",
        "source_title",
        "supersession_risk",
        "used_by",
    ),
    "docs/standards/source-freshness-standard.md": (
        "AGENTINVESTIGATE_AI_05_SOURCE_STANDARD_READY",
        "Freshness Classes",
        "Stale Source Behavior",
        "Currentness In Outputs",
    ),
    "docs/development/handoffs/AI-05-final-handoff.md": (
        "AGENTINVESTIGATE_AI_05_SOURCE_STANDARD_READY",
        "AI-06: Validation & Evaluation Framework.",
    ),
    "docs/standards/testing-standard.md": (
        "AGENTINVESTIGATE_AI_06_VALIDATION_FRAMEWORK_READY",
        "Required Test Classes",
        "correct routing",
        "output-format compliance",
    ),
    "docs/standards/evaluation-standard.md": (
        "AGENTINVESTIGATE_AI_06_VALIDATION_FRAMEWORK_READY",
        "general model",
        "general model + AgentInvestigate skill",
        "Required Dimensions",
    ),
    "docs/development/handoffs/AI-06-final-handoff.md": (
        "AGENTINVESTIGATE_AI_06_VALIDATION_FRAMEWORK_READY",
        "AI-07: Shared Professional Foundations.",
    ),
    "docs/foundations/foundation-catalog.md": (
        "AGENTINVESTIGATE_AI_07_SHARED_FOUNDATIONS_READY",
        "professional terminology",
        "common report structures",
        "Do not create a shared asset unless a real skill consumes it.",
    ),
    "docs/foundations/professional-vocabulary.md": (
        "AGENTINVESTIGATE_AI_07_SHARED_FOUNDATIONS_READY",
        "Professional Terminology",
        "Evidence Terminology",
        "Source Reliability Vocabulary",
    ),
    "docs/foundations/shared-schemas.md": (
        "AGENTINVESTIGATE_AI_07_SHARED_FOUNDATIONS_READY",
        "Jurisdiction Schema",
        "Authority Schema",
        "Sensitivity Schema",
    ),
    "docs/foundations/report-structure-contracts.md": (
        "AGENTINVESTIGATE_AI_07_SHARED_FOUNDATIONS_READY",
        "case-intake",
        "evidence-matrix",
        "not filled template assets",
    ),
    "docs/development/handoffs/AI-07-final-handoff.md": (
        "AGENTINVESTIGATE_AI_07_SHARED_FOUNDATIONS_READY",
        "AI-08: Four-Class Reference Implementation.",
    ),
    "docs/development/handoffs/AI-08-final-handoff.md": (
        "AGENTINVESTIGATE_AI_08_REFERENCE_SKILLS_READY",
        "build-evidence-matrix",
        "identify-licensing-requirement",
        "assess-observation-proportionality",
        "determine-emergency-escalation",
        "AI-09: Professional Core & Ethics.",
    ),
    "tests/reference-skills/AI-09-professional-core-scenarios.json": (
        "AGENTINVESTIGATE_AI_09_PROFESSIONAL_CORE_READY",
        "define-professional-role-boundaries",
        "assess-conflict-of-interest",
        "document-professional-decision",
    ),
    "docs/development/handoffs/AI-09-final-handoff.md": (
        "AGENTINVESTIGATE_AI_09_PROFESSIONAL_CORE_READY",
        "define-professional-role-boundaries",
        "assess-conflict-of-interest",
        "apply-ethical-decision-framework",
        "identify-investigative-bias",
        "separate-fact-from-inference",
        "assess-duty-of-care",
        "protect-confidential-information",
        "identify-escalation-requirement",
        "document-professional-decision",
        "AI-10: Intake, Authority, Law & Privacy.",
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
