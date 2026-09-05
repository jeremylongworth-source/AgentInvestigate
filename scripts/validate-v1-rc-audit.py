from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


TOKEN = "AGENTINVESTIGATE_AI_37_V1_RC_AUDIT_COMPLETE"
SELECTED_VERDICT = "V1_PARTIALLY_READY"

POSSIBLE_VERDICTS = {
    "V1_READY",
    "V1_PARTIALLY_READY",
    "V1_BLOCKED",
}

AUDIT_DIMENSIONS = {
    "taxonomy implementation",
    "skill completeness",
    "routing correctness",
    "authority gating",
    "privacy gating",
    "regulatory freshness",
    "source integrity",
    "jurisdiction isolation",
    "safety boundaries",
    "evidence reasoning",
    "identity-confidence behavior",
    "tests",
    "integration",
    "professional skillsets",
    "documentation",
    "repository hygiene",
    "licensing",
}

REQUIRED_CONDITIONS = {
    "maintainer approval for the v1 release",
    "independent current-source re-verification or explicit dated freshness exception for high-supersession regulatory sources",
    "live prompt regression results for representative routing, integration, evidence, privacy, jurisdiction, and adversarial safety scenarios",
    "legal, privacy, and safety reviewer sign-off or documented release-risk acceptance",
    "release notes and tag decision",
    "support and issue-response owner for post-release reports",
}

NOT_PERFORMED = {
    "external legal review",
    "external privacy review",
    "external safety review",
    "independent current-source web re-verification",
    "live prompt regression testing",
    "package publication",
    "release tagging",
    "production deployment",
    "public launch communications",
}


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    audit_path = repo_root / "docs/evaluation/v1-release-candidate-audit.md"
    fixture_path = repo_root / "tests/release/AI-37-v1-release-candidate-audit.json"
    handoff_path = repo_root / "docs/development/handoffs/AI-37-final-handoff.md"

    for path in (audit_path, fixture_path, handoff_path):
        if not path.is_file():
            errors.append(f"Missing AI-37 file: {path.relative_to(repo_root)}")

    if not fixture_path.is_file():
        return errors

    try:
        fixture = load_json(fixture_path)
    except json.JSONDecodeError as exc:
        return [f"tests/release/AI-37-v1-release-candidate-audit.json: invalid JSON: {exc}"]
    if not isinstance(fixture, dict):
        return ["tests/release/AI-37-v1-release-candidate-audit.json: fixture must be an object"]

    if fixture.get("completion_token") != TOKEN:
        errors.append("AI-37 fixture missing completion token")
    if fixture.get("audit_artifact") != "docs/evaluation/v1-release-candidate-audit.md":
        errors.append("AI-37 fixture has wrong audit artifact")
    if set(fixture.get("possible_verdicts", [])) != POSSIBLE_VERDICTS:
        errors.append("AI-37 possible verdicts mismatch")
    if fixture.get("selected_verdict") != SELECTED_VERDICT:
        errors.append(f"AI-37 selected verdict must be {SELECTED_VERDICT}")
    if fixture.get("audit_rule") != "Do not equate file existence with readiness.":
        errors.append("AI-37 fixture missing audit rule")

    dimensions = fixture.get("dimensions")
    if not isinstance(dimensions, list):
        return errors + ["AI-37 dimensions must be a list"]
    if fixture.get("dimension_count") != len(AUDIT_DIMENSIONS) or len(dimensions) != len(AUDIT_DIMENSIONS):
        errors.append("AI-37 dimension count mismatch")

    dimension_by_name = {str(dimension.get("name")): dimension for dimension in dimensions if isinstance(dimension, dict)}
    if set(dimension_by_name) != AUDIT_DIMENSIONS:
        errors.append("AI-37 audit dimension set mismatch")

    for name, dimension in dimension_by_name.items():
        result = dimension.get("result")
        if result not in {"PASS", "PARTIAL", "BLOCKED"}:
            errors.append(f"{name}: invalid audit result {result}")
        evidence = dimension.get("evidence", [])
        if not isinstance(evidence, list) or len(evidence) < 2:
            errors.append(f"{name}: must include at least two evidence entries")
        if not dimension.get("remaining_risk"):
            errors.append(f"{name}: missing remaining risk")

    if dimension_by_name.get("regulatory freshness", {}).get("result") != "PARTIAL":
        errors.append("regulatory freshness must be PARTIAL for AI-37")
    if dimension_by_name.get("tests", {}).get("result") != "PASS":
        errors.append("tests dimension must be PASS")
    if dimension_by_name.get("safety boundaries", {}).get("result") != "PASS":
        errors.append("safety boundaries dimension must be PASS")

    if set(fixture.get("conditions_for_v1_ready", [])) != REQUIRED_CONDITIONS:
        errors.append("AI-37 conditions_for_v1_ready mismatch")
    if set(fixture.get("not_performed_in_ai37", [])) != NOT_PERFORMED:
        errors.append("AI-37 not_performed_in_ai37 mismatch")

    if audit_path.is_file():
        audit = audit_path.read_text(encoding="utf-8-sig")
        for required in (
            TOKEN,
            SELECTED_VERDICT,
            "Do not equate file existence with readiness.",
            "AgentInvestigate deserves a public v1 release-candidate posture, but not an unconditional v1 readiness verdict.",
            "AI-37 did not independently re-check live official sources",
            *sorted(POSSIBLE_VERDICTS),
            *sorted(AUDIT_DIMENSIONS),
            *sorted(REQUIRED_CONDITIONS),
            *sorted(NOT_PERFORMED),
        ):
            if required not in audit:
                errors.append(f"v1-release-candidate-audit.md: missing required text {required}")

    if handoff_path.is_file():
        handoff = handoff_path.read_text(encoding="utf-8-sig")
        for required in (
            TOKEN,
            SELECTED_VERDICT,
            "docs/evaluation/v1-release-candidate-audit.md",
            "tests/release/AI-37-v1-release-candidate-audit.json",
            "scripts/validate-v1-rc-audit.py",
            "Post-v1 candidate tracks require separate review before roadmap admission.",
            *sorted(AUDIT_DIMENSIONS),
        ):
            if required not in handoff:
                errors.append(f"AI-37-final-handoff.md: missing required text {required}")

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
    print(f"Validated AgentInvestigate v1 release candidate audit: {SELECTED_VERDICT}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
