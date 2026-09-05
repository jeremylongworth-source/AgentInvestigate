from __future__ import annotations

import argparse
import sys
from pathlib import Path


TOKEN = "AGENTINVESTIGATE_AI_36_PUBLIC_READINESS_READY"

PUBLIC_FILES = (
    "README.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "LICENSE",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
)

README_TOPICS = (
    "what AgentInvestigate is",
    "who it is for",
    "supported domains",
    "skill examples",
    "sensitivity model",
    "jurisdiction model",
    "installation/use",
    "validation",
    "limitations",
    "prohibited capabilities",
    "contribution process",
)

README_REQUIRED_TEXT = (
    TOKEN,
    "AgentInvestigate is an open-source AI skill repository",
    "## Who It Is For",
    "## Supported Domains",
    "## Skill Examples",
    "## Sensitivity Model",
    "## Jurisdiction Model",
    "## Installation And Use",
    "## Validation",
    "## Limitations",
    "## Prohibited Capabilities",
    "## Contributing",
    "## Public Files",
    ".\\scripts\\validate-all.ps1",
    "skills/<family>/<skill>/SKILL.md",
    "skillsets/professional-skillsets.json",
    "docs/architecture/authority-routing.md",
    "docs/architecture/prohibited-capabilities.md",
    "docs/architecture/canadian-jurisdiction-roadmap.md",
    "docs/architecture/specialization-roadmap.md",
    "Latest completed wave: `AI-36 Public Documentation & Repository Readiness`",
    "Recommended next wave: `AI-37 v1 Release Candidate Audit`",
)

ROUTING_STATES = (
    "PROCEED_ROUTINE",
    "CLARIFY_SCOPE",
    "REGULATED_RESEARCH_ONLY",
    "INTRUSIVE_GATE_REQUIRED",
    "CERTIFICATION_ESCALATION",
    "PROHIBITED_REDIRECT",
)

PUBLIC_BOUNDARIES = (
    "does not confer investigator licensing",
    "not a substitute for counsel",
    "Current-source verification is required",
    "must not provide procedural assistance",
)


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    readme_path = repo_root / "README.md"
    handoff_path = repo_root / "docs/development/handoffs/AI-36-final-handoff.md"

    for relative in PUBLIC_FILES:
        if not (repo_root / relative).is_file():
            errors.append(f"Missing public file: {relative}")

    if not readme_path.is_file():
        return errors

    readme = readme_path.read_text(encoding="utf-8-sig")
    for required in (*README_REQUIRED_TEXT, *ROUTING_STATES, *PUBLIC_BOUNDARIES):
        if required not in readme:
            errors.append(f"README.md: missing required public-readiness text {required}")

    for public_file in PUBLIC_FILES:
        if f"- `{public_file}`" not in readme:
            errors.append(f"README.md: missing public file listing {public_file}")

    for heading in (
        "# AgentInvestigate",
        "## Who It Is For",
        "## Supported Domains",
        "## Skill Examples",
        "## Sensitivity Model",
        "## Jurisdiction Model",
        "## Installation And Use",
        "## Validation",
        "## Limitations",
        "## Prohibited Capabilities",
        "## Contributing",
        "## License",
    ):
        if heading not in readme:
            errors.append(f"README.md: missing heading {heading}")

    if handoff_path.is_file():
        handoff = handoff_path.read_text(encoding="utf-8-sig")
        for required in (
            TOKEN,
            "README.md",
            "CONTRIBUTING.md",
            "CHANGELOG.md",
            "LICENSE",
            "SECURITY.md",
            "CODE_OF_CONDUCT.md",
            "scripts/validate-public-readiness.py",
            "AI-37: v1 Release Candidate Audit.",
            *README_TOPICS,
        ):
            if required not in handoff:
                errors.append(f"AI-36-final-handoff.md: missing required text {required}")
    else:
        errors.append("Missing AI-36 file: docs/development/handoffs/AI-36-final-handoff.md")

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
    print("Validated AgentInvestigate public documentation readiness.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
