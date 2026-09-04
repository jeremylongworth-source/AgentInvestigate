from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


TOKEN = "AGENTINVESTIGATE_AI_07_SHARED_FOUNDATIONS_READY"

REQUIRED_FILES = (
    "docs/foundations/foundation-catalog.md",
    "docs/foundations/professional-vocabulary.md",
    "docs/foundations/shared-schemas.md",
    "docs/foundations/report-structure-contracts.md",
    "docs/foundations/foundation-consumer-map.json",
    "docs/development/handoffs/AI-07-final-handoff.md",
)

FOUNDATION_CANDIDATES = (
    "professional terminology",
    "evidence terminology",
    "case status vocabulary",
    "confidence vocabulary",
    "source reliability vocabulary",
    "jurisdiction schema",
    "authority schema",
    "sensitivity schema",
    "common report structures",
)

TEMPLATE_CONTRACTS = (
    "case-intake",
    "conflict-check",
    "authority-check",
    "investigation-plan",
    "case-action-log",
    "research-source-log",
    "interview-plan",
    "evidence-log",
    "chain-of-custody",
    "evidence-matrix",
    "case-chronology",
    "incident-report",
    "shift-handoff",
    "risk-register",
    "case-closure",
)

REQUIRED_SCHEMA_TERMS = (
    "Jurisdiction Schema",
    "Authority Schema",
    "Sensitivity Schema",
    "Source Schema",
    "Evidence Item Schema",
    "Artifact Metadata Schema",
)

REQUIRED_VOCABULARY_TERMS = (
    "Professional Terminology",
    "Evidence Terminology",
    "Case Status Vocabulary",
    "Confidence Vocabulary",
    "Source Reliability Vocabulary",
)

FOUNDATION_FIELDS = {"id", "path", "type", "covers", "planned_consumers", "materialized_asset"}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(repo_root: Path, relative: str) -> str:
    return (repo_root / relative).read_text(encoding="utf-8-sig")


def taxonomy_skill_names(repo_root: Path) -> set[str]:
    index = load_json(repo_root / "docs" / "architecture" / "taxonomy-index.yaml")
    return {skill["name"] for skill in index["skills"]}


def validate_required_files(repo_root: Path, errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (repo_root / relative).is_file():
            errors.append(f"Missing AI-07 artifact: {relative}")


def validate_text_artifacts(repo_root: Path, errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        path = repo_root / relative
        if path.suffix == ".json" or not path.is_file():
            continue
        text = read_text(repo_root, relative)
        if TOKEN not in text:
            errors.append(f"{relative}: missing completion token")

    catalog_path = repo_root / "docs" / "foundations" / "foundation-catalog.md"
    if catalog_path.is_file():
        catalog = read_text(repo_root, "docs/foundations/foundation-catalog.md")
        for candidate in FOUNDATION_CANDIDATES:
            if candidate not in catalog:
                errors.append(f"foundation-catalog.md: missing candidate resource {candidate}")
        for template in TEMPLATE_CONTRACTS:
            if template not in catalog:
                errors.append(f"foundation-catalog.md: missing template contract {template}")
        if "Do not create a shared asset unless a real skill consumes it." not in catalog:
            errors.append("foundation-catalog.md: missing shared asset rule")

    vocabulary_path = repo_root / "docs" / "foundations" / "professional-vocabulary.md"
    if vocabulary_path.is_file():
        vocabulary = read_text(repo_root, "docs/foundations/professional-vocabulary.md")
        for term in REQUIRED_VOCABULARY_TERMS:
            if term not in vocabulary:
                errors.append(f"professional-vocabulary.md: missing section {term}")

    schemas_path = repo_root / "docs" / "foundations" / "shared-schemas.md"
    if schemas_path.is_file():
        schemas = read_text(repo_root, "docs/foundations/shared-schemas.md")
        for term in REQUIRED_SCHEMA_TERMS:
            if term not in schemas:
                errors.append(f"shared-schemas.md: missing section {term}")

    reports_path = repo_root / "docs" / "foundations" / "report-structure-contracts.md"
    if reports_path.is_file():
        reports = read_text(repo_root, "docs/foundations/report-structure-contracts.md")
        for template in TEMPLATE_CONTRACTS:
            if f"### {template}" not in reports:
                errors.append(f"report-structure-contracts.md: missing template contract {template}")
        if "not filled template assets" not in reports:
            errors.append("report-structure-contracts.md: missing materialization boundary")


def validate_consumer_map(repo_root: Path, errors: list[str]) -> None:
    path = repo_root / "docs" / "foundations" / "foundation-consumer-map.json"
    if not path.is_file():
        return

    try:
        data = load_json(path)
    except json.JSONDecodeError as exc:
        errors.append(f"foundation-consumer-map.json: invalid JSON: {exc}")
        return

    if data.get("completion_token") != TOKEN:
        errors.append("foundation-consumer-map.json: missing AI-07 completion token")
    if data.get("asset_rule") != "Do not create a shared asset unless a real skill consumes it.":
        errors.append("foundation-consumer-map.json: asset rule mismatch")

    foundations = data.get("foundations")
    if not isinstance(foundations, list):
        errors.append("foundation-consumer-map.json: foundations must be a list")
        return

    skill_names = taxonomy_skill_names(repo_root)
    seen_ids: set[str] = set()
    covered: set[str] = set()
    for foundation in foundations:
        if not isinstance(foundation, dict):
            errors.append("foundation-consumer-map.json: foundation must be an object")
            continue
        foundation_id = str(foundation.get("id", "<missing id>"))
        if foundation_id in seen_ids:
            errors.append(f"foundation-consumer-map.json: duplicate foundation id {foundation_id}")
        seen_ids.add(foundation_id)
        missing = FOUNDATION_FIELDS - set(foundation)
        for field in sorted(missing):
            errors.append(f"{foundation_id}: missing field {field}")
        if not (repo_root / str(foundation.get("path", ""))).is_file():
            errors.append(f"{foundation_id}: path does not exist")
        covers = foundation.get("covers")
        if not isinstance(covers, list) or not covers:
            errors.append(f"{foundation_id}: covers must be a non-empty list")
        else:
            covered.update(str(item) for item in covers)
        consumers = foundation.get("planned_consumers")
        if not isinstance(consumers, list) or not consumers:
            errors.append(f"{foundation_id}: planned_consumers must be a non-empty list")
        else:
            for consumer in consumers:
                if consumer not in skill_names:
                    errors.append(f"{foundation_id}: unknown planned consumer {consumer}")
        if foundation.get("materialized_asset") is not False:
            errors.append(f"{foundation_id}: materialized_asset must be false in AI-07")

    for candidate in FOUNDATION_CANDIDATES:
        if candidate not in covered:
            errors.append(f"foundation-consumer-map.json: missing coverage for {candidate}")
    for template in TEMPLATE_CONTRACTS:
        if template not in covered:
            errors.append(f"foundation-consumer-map.json: missing coverage for template {template}")


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    validate_required_files(repo_root, errors)
    validate_text_artifacts(repo_root, errors)
    validate_consumer_map(repo_root, errors)
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

    print("Validated AgentInvestigate AI-07 shared foundations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
