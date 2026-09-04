from __future__ import annotations

import argparse
import sys
from pathlib import Path


TOKEN = "AGENTINVESTIGATE_AI_03_SENSITIVITY_ROUTING_READY"

REQUIRED_FILES = (
    "docs/architecture/sensitivity-model.md",
    "docs/architecture/authority-routing.md",
    "docs/architecture/intrusive-task-gate.md",
    "docs/architecture/certification-boundaries.md",
    "docs/development/handoffs/AI-03-final-handoff.md",
)

REQUIRED_TEXT = {
    "docs/architecture/sensitivity-model.md": (
        TOKEN,
        "ROUTINE",
        "REGULATED",
        "INTRUSIVE",
        "CERTIFICATION_BOUNDARY",
        "Classification precedence",
        "PROHIBITED",
    ),
    "docs/architecture/authority-routing.md": (
        TOKEN,
        "PROCEED_ROUTINE",
        "CLARIFY_SCOPE",
        "REGULATED_RESEARCH_ONLY",
        "INTRUSIVE_GATE_REQUIRED",
        "CERTIFICATION_ESCALATION",
        "PROHIBITED_REDIRECT",
        "Representative Request Routing",
        "Representative requests from all four sensitivity classes route correctly on paper.",
    ),
    "docs/architecture/intrusive-task-gate.md": (
        TOKEN,
        "No intrusive skill routes directly from a raw user request.",
        "validate-investigative-authority or validate-security-service-authority",
        "assess-lawful-purpose",
        "identify-privacy-obligation",
        "HUMAN APPROVAL",
        "Fail-Closed Conditions",
    ),
    "docs/architecture/certification-boundaries.md": (
        TOKEN,
        "Allowed Support",
        "Prohibited Substitutes",
        "CERTIFICATION_ESCALATION",
        "PROHIBITED_REDIRECT",
    ),
    "docs/development/handoffs/AI-03-final-handoff.md": (
        TOKEN,
        "AI-04: Skill Authoring Standard.",
    ),
}


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (repo_root / relative).is_file():
            errors.append(f"Missing AI-03 artifact: {relative}")

    for relative, phrases in REQUIRED_TEXT.items():
        path = repo_root / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8-sig")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{relative}: missing required text {phrase}")

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

    print("Validated AgentInvestigate AI-03 routing contracts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
