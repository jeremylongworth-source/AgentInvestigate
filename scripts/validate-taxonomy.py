from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


TOKEN = "AGENTINVESTIGATE_AI_02_MASTER_TAXONOMY_READY"
SKILL_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VALID_TIERS = {"FOUNDATION", "CORE", "ADVANCED"}
VALID_SENSITIVITY = {"ROUTINE", "REGULATED", "INTRUSIVE", "CERTIFICATION_BOUNDARY"}
VALID_FRESHNESS = {"LOW", "MEDIUM", "HIGH"}
VALID_PRIORITIES = {"P0", "P1", "P2", "P3"}
REQUIRED_SKILL_FIELDS = {
    "name",
    "family",
    "tier",
    "sensitivity",
    "jurisdiction_requirement",
    "authority_requirement",
    "freshness_requirement",
    "priority",
    "dependencies",
    "professional_skillsets",
}
REQUIRED_ROADMAP_SKILLS = {
    "build-evidence-matrix",
    "validate-investigative-authority",
    "write-investigative-report",
    "triage-security-incident",
    "assess-physical-vulnerabilities",
    "identify-licensing-requirement",
    "assess-observation-proportionality",
    "determine-emergency-escalation",
}


def load_index(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    index_path = repo_root / "docs" / "architecture" / "taxonomy-index.yaml"
    markdown_path = repo_root / "docs" / "architecture" / "master-taxonomy-v1.md"

    if not index_path.is_file():
        return ["Missing AI-02 artifact: docs/architecture/taxonomy-index.yaml"]
    if not markdown_path.is_file():
        errors.append("Missing AI-02 artifact: docs/architecture/master-taxonomy-v1.md")

    try:
        index = load_index(index_path)
    except json.JSONDecodeError as exc:
        return [f"taxonomy-index.yaml: invalid JSON-compatible YAML: {exc}"]

    if index.get("completion_token") != TOKEN:
        errors.append("taxonomy-index.yaml: missing AI-02 completion token")
    if index.get("canonical") is not True:
        errors.append("taxonomy-index.yaml: canonical must be true")
    if index.get("taxonomy_name") != "AgentInvestigate Master Taxonomy v1.0":
        errors.append("taxonomy-index.yaml: unexpected taxonomy_name")

    families = index.get("families", [])
    skills = index.get("skills", [])
    if not isinstance(families, list):
        errors.append("taxonomy-index.yaml: families must be a list")
        families = []
    if not isinstance(skills, list):
        errors.append("taxonomy-index.yaml: skills must be a list")
        skills = []

    family_slugs = {family.get("slug") for family in families if isinstance(family, dict)}
    if len(family_slugs) != 20:
        errors.append(f"taxonomy-index.yaml: expected 20 families, found {len(family_slugs)}")
    if len(skills) != 212:
        errors.append(f"taxonomy-index.yaml: expected exactly 212 skills, found {len(skills)}")

    names: list[str] = []
    for i, skill in enumerate(skills):
        if not isinstance(skill, dict):
            errors.append(f"taxonomy-index.yaml: skill #{i + 1} is not an object")
            continue
        missing = REQUIRED_SKILL_FIELDS - set(skill)
        for field in sorted(missing):
            errors.append(f"{skill.get('name', f'skill #{i + 1}')}: missing field {field}")
        name = str(skill.get("name", ""))
        names.append(name)
        if not SKILL_RE.match(name):
            errors.append(f"{name}: invalid skill name")
        if skill.get("family") not in family_slugs:
            errors.append(f"{name}: unknown family {skill.get('family')}")
        if skill.get("tier") not in VALID_TIERS:
            errors.append(f"{name}: invalid tier {skill.get('tier')}")
        if skill.get("sensitivity") not in VALID_SENSITIVITY:
            errors.append(f"{name}: invalid sensitivity {skill.get('sensitivity')}")
        if skill.get("freshness_requirement") not in VALID_FRESHNESS:
            errors.append(f"{name}: invalid freshness {skill.get('freshness_requirement')}")
        if skill.get("priority") not in VALID_PRIORITIES:
            errors.append(f"{name}: invalid priority {skill.get('priority')}")
        if not isinstance(skill.get("dependencies"), list):
            errors.append(f"{name}: dependencies must be a list")
        if not isinstance(skill.get("professional_skillsets"), list):
            errors.append(f"{name}: professional_skillsets must be a list")

    duplicates = sorted(name for name, count in Counter(names).items() if count > 1)
    for name in duplicates:
        errors.append(f"taxonomy-index.yaml: duplicate skill name {name}")

    missing_roadmap = sorted(REQUIRED_ROADMAP_SKILLS - set(names))
    for name in missing_roadmap:
        errors.append(f"taxonomy-index.yaml: missing roadmap-named skill {name}")

    name_set = set(names)
    for skill in skills:
        if not isinstance(skill, dict):
            continue
        for dependency in skill.get("dependencies", []):
            if dependency not in name_set:
                errors.append(f"{skill.get('name')}: unknown dependency {dependency}")

    family_count_by_skill = Counter(skill.get("family") for skill in skills if isinstance(skill, dict))
    for family in families:
        if not isinstance(family, dict):
            continue
        slug = family.get("slug")
        if family.get("skill_count") != family_count_by_skill[slug]:
            errors.append(
                f"{slug}: family skill_count {family.get('skill_count')} does not match "
                f"{family_count_by_skill[slug]}"
            )

    if markdown_path.is_file():
        markdown = markdown_path.read_text(encoding="utf-8")
        for required in (
            TOKEN,
            "`docs/architecture/taxonomy-index.yaml` is the canonical taxonomy source.",
            "Exactly one canonical taxonomy source exists: docs/architecture/taxonomy-index.yaml",
        ):
            if required not in markdown:
                errors.append(f"master-taxonomy-v1.md: missing required text {required}")

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

    index = load_index(repo_root / "docs" / "architecture" / "taxonomy-index.yaml")
    print(f"Validated {len(index['skills'])} AgentInvestigate taxonomy skill candidates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
