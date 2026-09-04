from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


TOKEN = "AGENTINVESTIGATE_AI_06_VALIDATION_FRAMEWORK_READY"

REQUIRED_FILES = (
    "docs/standards/testing-standard.md",
    "docs/standards/evaluation-standard.md",
    "tests/validation-scenarios.json",
    "tests/evaluation-rubric.json",
    "docs/development/handoffs/AI-06-final-handoff.md",
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

REQUIRED_DIMENSIONS = (
    "correctness",
    "evidence discipline",
    "uncertainty",
    "source use",
    "routing",
    "privacy behavior",
    "safety boundaries",
    "usefulness",
)

VALID_ROUTING_STATES = {
    "PROCEED_ROUTINE",
    "CLARIFY_SCOPE",
    "REGULATED_RESEARCH_ONLY",
    "INTRUSIVE_GATE_REQUIRED",
    "CERTIFICATION_ESCALATION",
    "PROHIBITED_REDIRECT",
}

VALID_SENSITIVITY = {"ROUTINE", "REGULATED", "INTRUSIVE", "CERTIFICATION_BOUNDARY", "PROHIBITED"}

SCENARIO_FIELDS = {
    "id",
    "test_class",
    "prompt",
    "sensitivity",
    "expected_routing_state",
    "expected_behavior",
    "required_checks",
    "blocked_outputs",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_required_files(repo_root: Path, errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (repo_root / relative).is_file():
            errors.append(f"Missing AI-06 artifact: {relative}")


def validate_text_artifacts(repo_root: Path, errors: list[str]) -> None:
    for relative in (
        "docs/standards/testing-standard.md",
        "docs/standards/evaluation-standard.md",
        "docs/development/handoffs/AI-06-final-handoff.md",
    ):
        path = repo_root / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8-sig")
        if TOKEN not in text:
            errors.append(f"{relative}: missing completion token")

    testing_path = repo_root / "docs/standards/testing-standard.md"
    if testing_path.is_file():
        testing = testing_path.read_text(encoding="utf-8-sig")
        for test_class in REQUIRED_TEST_CLASSES:
            if test_class not in testing:
                errors.append(f"testing-standard.md: missing test class {test_class}")

    evaluation_path = repo_root / "docs/standards/evaluation-standard.md"
    if evaluation_path.is_file():
        evaluation = evaluation_path.read_text(encoding="utf-8-sig")
        for dimension in REQUIRED_DIMENSIONS:
            if dimension not in evaluation:
                errors.append(f"evaluation-standard.md: missing dimension {dimension}")
        for phrase in ("general model", "general model + AgentInvestigate skill"):
            if phrase not in evaluation:
                errors.append(f"evaluation-standard.md: missing comparison phrase {phrase}")


def validate_scenarios(repo_root: Path, errors: list[str]) -> None:
    path = repo_root / "tests" / "validation-scenarios.json"
    if not path.is_file():
        return

    try:
        data = load_json(path)
    except json.JSONDecodeError as exc:
        errors.append(f"validation-scenarios.json: invalid JSON: {exc}")
        return

    if data.get("completion_token") != TOKEN:
        errors.append("validation-scenarios.json: missing AI-06 completion token")

    classes = data.get("required_test_classes")
    if classes != list(REQUIRED_TEST_CLASSES):
        errors.append("validation-scenarios.json: required_test_classes do not match AI-06 contract")

    scenarios = data.get("scenarios")
    if not isinstance(scenarios, list):
        errors.append("validation-scenarios.json: scenarios must be a list")
        return

    seen_classes = {scenario.get("test_class") for scenario in scenarios if isinstance(scenario, dict)}
    for test_class in REQUIRED_TEST_CLASSES:
        if test_class not in seen_classes:
            errors.append(f"validation-scenarios.json: missing scenario for {test_class}")

    seen_ids: set[str] = set()
    for scenario in scenarios:
        if not isinstance(scenario, dict):
            errors.append("validation-scenarios.json: scenario must be an object")
            continue
        missing = SCENARIO_FIELDS - set(scenario)
        scenario_id = str(scenario.get("id", "<missing id>"))
        if scenario_id in seen_ids:
            errors.append(f"validation-scenarios.json: duplicate scenario id {scenario_id}")
        seen_ids.add(scenario_id)
        for field in sorted(missing):
            errors.append(f"{scenario_id}: missing field {field}")
        if scenario.get("test_class") not in REQUIRED_TEST_CLASSES:
            errors.append(f"{scenario_id}: unknown test_class {scenario.get('test_class')}")
        if scenario.get("sensitivity") not in VALID_SENSITIVITY:
            errors.append(f"{scenario_id}: invalid sensitivity {scenario.get('sensitivity')}")
        if scenario.get("expected_routing_state") not in VALID_ROUTING_STATES:
            errors.append(f"{scenario_id}: invalid expected_routing_state {scenario.get('expected_routing_state')}")
        for field in ("required_checks", "blocked_outputs"):
            if not isinstance(scenario.get(field), list) or not scenario.get(field):
                errors.append(f"{scenario_id}: {field} must be a non-empty list")


def validate_rubric(repo_root: Path, errors: list[str]) -> None:
    path = repo_root / "tests" / "evaluation-rubric.json"
    if not path.is_file():
        return

    try:
        data = load_json(path)
    except json.JSONDecodeError as exc:
        errors.append(f"evaluation-rubric.json: invalid JSON: {exc}")
        return

    if data.get("completion_token") != TOKEN:
        errors.append("evaluation-rubric.json: missing AI-06 completion token")

    comparison = data.get("comparison_model", {})
    if comparison.get("baseline") != "general model":
        errors.append("evaluation-rubric.json: baseline comparison model mismatch")
    if comparison.get("skill_enabled") != "general model + AgentInvestigate skill":
        errors.append("evaluation-rubric.json: skill-enabled comparison model mismatch")

    if data.get("required_dimensions") != list(REQUIRED_DIMENSIONS):
        errors.append("evaluation-rubric.json: required_dimensions do not match AI-06 contract")

    dimensions = data.get("dimensions")
    if not isinstance(dimensions, list):
        errors.append("evaluation-rubric.json: dimensions must be a list")
        return

    dimension_names = {dimension.get("name") for dimension in dimensions if isinstance(dimension, dict)}
    for dimension in REQUIRED_DIMENSIONS:
        if dimension not in dimension_names:
            errors.append(f"evaluation-rubric.json: missing dimension detail for {dimension}")

    for score in ("0", "1", "2", "3"):
        if score not in data.get("score_scale", {}):
            errors.append(f"evaluation-rubric.json: missing score scale {score}")


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    validate_required_files(repo_root, errors)
    validate_text_artifacts(repo_root, errors)
    validate_scenarios(repo_root, errors)
    validate_rubric(repo_root, errors)
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

    print("Validated AgentInvestigate AI-06 test and evaluation framework.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
