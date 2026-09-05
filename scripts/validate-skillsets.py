from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


TOKEN = "AGENTINVESTIGATE_AI_32_PROFESSIONAL_SKILLSETS_READY"

INVESTIGATION_SKILLSETS = {
    "private-investigator",
    "investigative-analyst",
    "investigative-case-manager",
    "corporate-investigator",
    "workplace-investigator",
    "background-screening-specialist",
    "loss-prevention-investigator",
}

SECURITY_SKILLSETS = {
    "security-officer",
    "mobile-patrol-officer",
    "loss-prevention-officer",
    "security-supervisor",
    "security-operations-manager",
    "physical-security-analyst",
    "security-risk-assessor",
    "incident-response-coordinator",
    "security-program-manager",
}

HYBRID_SKILLSETS = {
    "corporate-security-investigator",
    "asset-protection-specialist",
    "corporate-security-manager",
}

ALL_SKILLSETS = INVESTIGATION_SKILLSETS | SECURITY_SKILLSETS | HYBRID_SKILLSETS

REQUIRED_FIELDS = {
    "purpose",
    "included_skills",
    "routing_triggers",
    "dependencies",
    "jurisdiction_requirements",
    "authority_requirements",
    "sensitivity_limits",
    "escalation_rules",
    "expected_outputs",
    "excluded_responsibilities",
}

REQUIRED_ROUTING_STATES = {
    "PROCEED_ROUTINE",
    "CLARIFY_SCOPE",
    "REGULATED_RESEARCH_ONLY",
    "INTRUSIVE_GATE_REQUIRED",
    "CERTIFICATION_ESCALATION",
    "PROHIBITED_REDIRECT",
}

DERIVED_ROLE_TERMS = {
    "loss-prevention-officer",
    "security-operations-manager",
    "corporate-security-manager",
}


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def taxonomy_skill_paths(repo_root: Path) -> dict[str, Path]:
    index = load_json(repo_root / "docs/architecture/taxonomy-index.yaml")
    if not isinstance(index, dict):
        return {}
    skills = index.get("skills", [])
    families = {str(family.get("slug")) for family in index.get("families", []) if isinstance(family, dict)}
    paths: dict[str, Path] = {}
    for skill in skills if isinstance(skills, list) else []:
        if not isinstance(skill, dict):
            continue
        name = str(skill.get("name", ""))
        family = str(skill.get("family", ""))
        if name and family in families:
            paths[name] = repo_root / "skills" / family / name / "SKILL.md"
    return paths


def taxonomy_role_memberships(repo_root: Path) -> dict[str, set[str]]:
    index = load_json(repo_root / "docs/architecture/taxonomy-index.yaml")
    if not isinstance(index, dict):
        return {}
    memberships: dict[str, set[str]] = {}
    skills = index.get("skills", [])
    for skill in skills if isinstance(skills, list) else []:
        if not isinstance(skill, dict):
            continue
        name = str(skill.get("name", ""))
        for role in skill.get("professional_skillsets", []):
            memberships.setdefault(str(role), set()).add(name)
    return memberships


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    registry_path = repo_root / "skillsets/professional-skillsets.json"
    fixture_path = repo_root / "tests/skillsets/AI-32-professional-skillset-composition.json"
    architecture_path = repo_root / "docs/architecture/professional-skillset-composition.md"
    readme_path = repo_root / "skillsets/README.md"

    for path in (registry_path, fixture_path, architecture_path, readme_path):
        if not path.is_file():
            errors.append(f"Missing AI-32 file: {path.relative_to(repo_root)}")

    if not registry_path.is_file():
        return errors

    try:
        registry = load_json(registry_path)
    except json.JSONDecodeError as exc:
        return [f"skillsets/professional-skillsets.json: invalid JSON: {exc}"]
    if not isinstance(registry, dict):
        return ["skillsets/professional-skillsets.json: registry must be an object"]

    if registry.get("completion_token") != TOKEN:
        errors.append("skillsets/professional-skillsets.json: missing AI-32 completion token")
    if registry.get("source_of_truth") != "docs/architecture/taxonomy-index.yaml":
        errors.append("skillsets/professional-skillsets.json: wrong source_of_truth")
    if registry.get("composition_rule") != "Skillsets compose skills. They must not duplicate underlying procedures.":
        errors.append("skillsets/professional-skillsets.json: wrong composition rule")

    skillsets = registry.get("skillsets")
    if not isinstance(skillsets, list):
        return errors + ["skillsets/professional-skillsets.json: skillsets must be a list"]
    if registry.get("skillset_count") != len(ALL_SKILLSETS):
        errors.append("skillsets/professional-skillsets.json: skillset_count mismatch")

    by_slug = {str(skillset.get("slug")): skillset for skillset in skillsets if isinstance(skillset, dict)}
    if set(by_slug) != ALL_SKILLSETS:
        errors.append("skillsets/professional-skillsets.json: roadmap skillset list mismatch")

    skill_paths = taxonomy_skill_paths(repo_root)
    taxonomy_roles = taxonomy_role_memberships(repo_root)
    taxonomy_skills = set(skill_paths)
    expected_branch = {
        **{role: "Investigation" for role in INVESTIGATION_SKILLSETS},
        **{role: "Security" for role in SECURITY_SKILLSETS},
        **{role: "Hybrid" for role in HYBRID_SKILLSETS},
    }

    for slug, skillset in by_slug.items():
        missing = REQUIRED_FIELDS - set(skillset)
        for field in sorted(missing):
            errors.append(f"{slug}: missing required field {field}")
        if skillset.get("branch") != expected_branch[slug]:
            errors.append(f"{slug}: wrong branch {skillset.get('branch')}")
        if skillset.get("composition_rule") != "Skillsets compose existing atomic skills and must not duplicate underlying procedures.":
            errors.append(f"{slug}: missing per-skillset composition rule")
        included = skillset.get("included_skills", [])
        if not isinstance(included, list) or not included:
            errors.append(f"{slug}: included_skills must be a non-empty list")
            included = []
        if len(included) != len(set(included)):
            errors.append(f"{slug}: included_skills contains duplicates")
        for name in included:
            if name not in taxonomy_skills:
                errors.append(f"{slug}: included skill missing from taxonomy: {name}")
            elif not skill_paths[name].is_file():
                errors.append(f"{slug}: included skill has no SKILL.md: {name}")
        limits_text = "\n".join(str(item) for item in skillset.get("sensitivity_limits", []))
        for state in REQUIRED_ROUTING_STATES:
            if state not in limits_text:
                errors.append(f"{slug}: missing routing state {state}")
        excluded_text = "\n".join(str(item) for item in skillset.get("excluded_responsibilities", []))
        for prohibited in ("legal advice", "licensing approval", "privacy compliance certification", "law-enforcement authority"):
            if prohibited not in excluded_text:
                errors.append(f"{slug}: excluded responsibilities missing {prohibited}")

    for direct_role in sorted(ALL_SKILLSETS - DERIVED_ROLE_TERMS):
        skillset = by_slug.get(direct_role, {})
        included = set(skillset.get("included_skills", [])) if isinstance(skillset, dict) else set()
        tagged = taxonomy_roles.get(direct_role, set())
        if tagged and included != tagged:
            errors.append(f"{direct_role}: included skills do not match taxonomy professional_skillsets")
        if direct_role in {"private-investigator", "security-officer"} and len(included) < 90:
            errors.append(f"{direct_role}: direct composition unexpectedly small")
        if direct_role == "workplace-investigator" and len(included) != 10:
            errors.append("workplace-investigator: expected 10 included skills")
        if direct_role == "background-screening-specialist" and len(included) != 10:
            errors.append("background-screening-specialist: expected 10 included skills")
        if direct_role == "asset-protection-specialist" and len(included) != 8:
            errors.append("asset-protection-specialist: expected 8 included skills")

    if by_slug.get("loss-prevention-officer") and len(by_slug["loss-prevention-officer"].get("included_skills", [])) != 8:
        errors.append("loss-prevention-officer: expected derived Family 19 skills")
    if by_slug.get("security-operations-manager") and len(by_slug["security-operations-manager"].get("included_skills", [])) < 45:
        errors.append("security-operations-manager: expected supervisor and program-management derived skills")
    if by_slug.get("corporate-security-manager") and len(by_slug["corporate-security-manager"].get("included_skills", [])) < 100:
        errors.append("corporate-security-manager: expected cross-branch derived skills")

    if fixture_path.is_file():
        try:
            fixture = load_json(fixture_path)
        except json.JSONDecodeError as exc:
            errors.append(f"tests/skillsets/AI-32-professional-skillset-composition.json: invalid JSON: {exc}")
            fixture = None
        if isinstance(fixture, dict):
            if fixture.get("completion_token") != TOKEN:
                errors.append("AI-32 fixture missing completion token")
            fixture_roles = set(fixture.get("investigation_skillsets", [])) | set(fixture.get("security_skillsets", [])) | set(
                fixture.get("hybrid_skillsets", [])
            )
            if fixture_roles != ALL_SKILLSETS:
                errors.append("AI-32 fixture skillset list mismatch")
            if set(fixture.get("required_fields", [])) != REQUIRED_FIELDS:
                errors.append("AI-32 fixture required fields mismatch")
            if set(fixture.get("required_routing_states", [])) != REQUIRED_ROUTING_STATES:
                errors.append("AI-32 fixture routing states mismatch")
            if set(fixture.get("derived_membership_roles", [])) != DERIVED_ROLE_TERMS:
                errors.append("AI-32 fixture derived membership roles mismatch")
            scenarios = fixture.get("scenarios")
            if not isinstance(scenarios, list) or len(scenarios) < 4:
                errors.append("AI-32 fixture must include at least 4 scenarios")

    if architecture_path.is_file():
        text = architecture_path.read_text(encoding="utf-8-sig")
        for required in (
            TOKEN,
            "The canonical skillset registry is `skillsets/professional-skillsets.json`.",
            "Skillsets compose skills.",
            "They must not duplicate underlying procedures.",
            "AI-32 creates professional skillset definitions.",
        ):
            if required not in text:
                errors.append(f"professional-skillset-composition.md: missing required text {required}")

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
    print(f"Validated {len(ALL_SKILLSETS)} AgentInvestigate professional skillsets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
