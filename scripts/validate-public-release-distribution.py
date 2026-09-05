from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


TOKEN = "AGENTINVESTIGATE_AI_38_PUBLIC_DISTRIBUTION_READY"
VERDICT = "PUBLIC_RELEASE_READY"

WIKI_PAGES = (
    "docs/wiki/Home.md",
    "docs/wiki/_Sidebar.md",
    "docs/wiki/Getting-Started.md",
    "docs/wiki/Architecture-Overview.md",
    "docs/wiki/Skill-Catalog.md",
    "docs/wiki/Professional-Skillsets.md",
    "docs/wiki/Sensitivity-And-Routing.md",
    "docs/wiki/Jurisdiction-Model.md",
    "docs/wiki/Safety-Boundaries.md",
    "docs/wiki/Validation-And-Testing.md",
    "docs/wiki/Contributing-Guide.md",
    "docs/wiki/Release-Readiness.md",
)

README_REQUIRED_TEXT = (
    TOKEN,
    "GitHub Wiki: `https://github.com/jeremylongworth-source/AgentInvestigate/wiki`",
    "gh skill publish --dry-run",
    "gh skill preview jeremylongworth-source/AgentInvestigate classify-request-type",
    "gh skill install jeremylongworth-source/AgentInvestigate classify-request-type",
    "gh skill install jeremylongworth-source/AgentInvestigate classify-request-type --agent github-copilot --scope user",
    "Latest completed wave: `AI-38 Public Release Distribution`",
    "Current public distribution verdict: `PUBLIC_RELEASE_READY`",
)


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    artifact_path = repo_root / "docs/release/public-release-distribution.md"
    fixture_path = repo_root / "tests/release/AI-38-public-release-distribution.json"
    handoff_path = repo_root / "docs/development/handoffs/AI-38-final-handoff.md"
    readme_path = repo_root / "README.md"

    for path in (artifact_path, fixture_path, handoff_path):
        if not path.is_file():
            errors.append(f"Missing AI-38 file: {path.relative_to(repo_root)}")

    for relative in WIKI_PAGES:
        path = repo_root / relative
        if not path.is_file():
            errors.append(f"Missing wiki source page: {relative}")
        elif not path.read_text(encoding="utf-8-sig").strip():
            errors.append(f"Wiki source page is empty: {relative}")

    if fixture_path.is_file():
        try:
            fixture = load_json(fixture_path)
        except json.JSONDecodeError as exc:
            errors.append(f"tests/release/AI-38-public-release-distribution.json: invalid JSON: {exc}")
            fixture = None
        if isinstance(fixture, dict):
            if fixture.get("completion_token") != TOKEN:
                errors.append("AI-38 fixture missing completion token")
            if fixture.get("release_artifact") != "docs/release/public-release-distribution.md":
                errors.append("AI-38 fixture has wrong release artifact")
            if fixture.get("distribution_verdict") != VERDICT:
                errors.append(f"AI-38 fixture distribution verdict must be {VERDICT}")
            repository = fixture.get("repository", {})
            if not isinstance(repository, dict):
                errors.append("AI-38 fixture repository must be an object")
                repository = {}
            if repository.get("visibility_required") != "PUBLIC":
                errors.append("AI-38 fixture must require PUBLIC repository visibility")
            if repository.get("wiki_required") is not True:
                errors.append("AI-38 fixture must require GitHub Wiki")
            if repository.get("required_topic") != "agent-skills":
                errors.append("AI-38 fixture must require agent-skills topic")
            wiki = fixture.get("wiki", {})
            if not isinstance(wiki, dict) or set(wiki.get("source_pages", [])) != set(WIKI_PAGES):
                errors.append("AI-38 fixture wiki source pages mismatch")
            distribution = fixture.get("copilot_skill_distribution", {})
            if not isinstance(distribution, dict):
                errors.append("AI-38 fixture copilot_skill_distribution must be an object")
            else:
                for key in ("publish_dry_run_command", "preview_command", "install_command", "copilot_install_command"):
                    if key not in distribution:
                        errors.append(f"AI-38 fixture missing Copilot skill command {key}")

    if artifact_path.is_file():
        artifact = artifact_path.read_text(encoding="utf-8-sig")
        for required in (
            TOKEN,
            VERDICT,
            "visibility: `PUBLIC`",
            "wiki: `enabled`",
            "topic: `agent-skills`",
            "gh skill publish --dry-run",
            "gh skill preview jeremylongworth-source/AgentInvestigate classify-request-type",
            "gh skill install jeremylongworth-source/AgentInvestigate classify-request-type",
            "gh skill install jeremylongworth-source/AgentInvestigate classify-request-type --agent github-copilot --scope user",
            *WIKI_PAGES,
        ):
            if required not in artifact:
                errors.append(f"public-release-distribution.md: missing required text {required}")

    if readme_path.is_file():
        readme = readme_path.read_text(encoding="utf-8-sig")
        for required in README_REQUIRED_TEXT:
            if required not in readme:
                errors.append(f"README.md: missing AI-38 distribution text {required}")
    else:
        errors.append("Missing README.md")

    if handoff_path.is_file():
        handoff = handoff_path.read_text(encoding="utf-8-sig")
        for required in (
            TOKEN,
            VERDICT,
            "docs/release/public-release-distribution.md",
            "tests/release/AI-38-public-release-distribution.json",
            "scripts/validate-public-release-distribution.py",
            "GitHub repository visibility verified as PUBLIC",
            "GitHub Wiki verified as enabled",
            "gh skill publish --dry-run",
            "Post-v1 candidate tracks require separate review before roadmap admission.",
            *WIKI_PAGES,
        ):
            if required not in handoff:
                errors.append(f"AI-38-final-handoff.md: missing required text {required}")

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
    print(f"Validated AgentInvestigate public release distribution: {VERDICT}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
