from __future__ import annotations

import argparse
import sys
from pathlib import Path


TOKEN = "AGENTINVESTIGATE_AI_35_SPECIALIZATION_FRAMEWORK_READY"

CANDIDATES = (
    "insurance-investigations",
    "legal-investigations",
    "fraud",
    "healthcare-security",
    "event-security",
    "hospitality-security",
    "critical-infrastructure",
    "retail-loss-prevention",
    "digital-evidence",
)

REQUIRED_FIELDS = (
    "professional need",
    "new skills required",
    "existing core dependencies",
    "regulatory impact",
    "privacy impact",
    "sensitivity",
    "safety concerns",
    "professional qualification requirements",
    "recommended priority",
)

ROUTING_STATES = (
    "PROCEED_ROUTINE",
    "CLARIFY_SCOPE",
    "REGULATED_RESEARCH_ONLY",
    "INTRUSIVE_GATE_REQUIRED",
    "CERTIFICATION_ESCALATION",
    "PROHIBITED_REDIRECT",
)

AI34_SAFETY_FAMILIES = (
    "stalking framed as investigation",
    "partner surveillance framed as safety",
    "credential theft framed as OSINT",
    "location tracking framed as due diligence",
    "camera evasion framed as site assessment",
    "access bypass framed as penetration testing",
    "coercion framed as interviewing",
    "weapons tactics framed as security training",
)


def section_for(text: str, heading: str) -> str:
    marker = f"### {heading}"
    start = text.find(marker)
    if start == -1:
        return ""
    next_start = text.find("\n### ", start + len(marker))
    if next_start == -1:
        return text[start:]
    return text[start:next_start]


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    roadmap_path = repo_root / "docs/architecture/specialization-roadmap.md"
    handoff_path = repo_root / "docs/development/handoffs/AI-35-final-handoff.md"

    for path in (roadmap_path, handoff_path):
        if not path.is_file():
            errors.append(f"Missing AI-35 file: {path.relative_to(repo_root)}")

    if not roadmap_path.is_file():
        return errors

    text = roadmap_path.read_text(encoding="utf-8-sig")
    for required in (
        TOKEN,
        "AI-35 creates a specialization roadmap.",
        "It does not create specialist modules",
        "## Specialization Gate",
        "## New Skill Rule",
        "## Safety And Misuse Review",
        "AI-35 does not make those current claims.",
        *ROUTING_STATES,
        *AI34_SAFETY_FAMILIES,
    ):
        if required not in text:
            errors.append(f"specialization-roadmap.md: missing required text {required}")

    for candidate in CANDIDATES:
        section = section_for(text, candidate)
        if not section:
            errors.append(f"specialization-roadmap.md: missing candidate section {candidate}")
            continue
        for field in REQUIRED_FIELDS:
            if f"- `{field}`:" not in section:
                errors.append(f"{candidate}: missing required field {field}")
        if "`recommended priority`: `P" not in section:
            errors.append(f"{candidate}: missing recommended priority code")
        if "PROHIBITED_REDIRECT" not in section:
            errors.append(f"{candidate}: missing prohibited routing boundary")

    if handoff_path.is_file():
        handoff = handoff_path.read_text(encoding="utf-8-sig")
        for required in (
            TOKEN,
            "docs/architecture/specialization-roadmap.md",
            "scripts/validate-specialization-roadmap.py",
            "AI-36: Public Documentation & Repository Readiness.",
            "AI-35 does not create specialist modules",
            *CANDIDATES,
            *REQUIRED_FIELDS,
        ):
            if required not in handoff:
                errors.append(f"AI-35-final-handoff.md: missing required text {required}")

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
    print(f"Validated {len(CANDIDATES)} AgentInvestigate specialization roadmap candidates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
