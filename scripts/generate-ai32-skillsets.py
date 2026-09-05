from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


TOKEN = "AGENTINVESTIGATE_AI_32_PROFESSIONAL_SKILLSETS_READY"

INVESTIGATION_SKILLSETS = [
    "private-investigator",
    "investigative-analyst",
    "investigative-case-manager",
    "corporate-investigator",
    "workplace-investigator",
    "background-screening-specialist",
    "loss-prevention-investigator",
]

SECURITY_SKILLSETS = [
    "security-officer",
    "mobile-patrol-officer",
    "loss-prevention-officer",
    "security-supervisor",
    "security-operations-manager",
    "physical-security-analyst",
    "security-risk-assessor",
    "incident-response-coordinator",
    "security-program-manager",
]

HYBRID_SKILLSETS = [
    "corporate-security-investigator",
    "asset-protection-specialist",
    "corporate-security-manager",
]

ROLE_PURPOSES = {
    "private-investigator": "Compose investigative intake, authority, research, evidence, analysis, observation-governance, reporting, screening, and program-management skills for licensed or otherwise authorized private investigation support.",
    "investigative-analyst": "Compose planning, research, identity, timeline, interviewing, surveillance-governance, and analytical skills for non-field investigative analysis support.",
    "investigative-case-manager": "Compose the full investigation case lifecycle from intake and authority checks through planning, evidence, interviews, analysis, reporting, file review, and program oversight.",
    "corporate-investigator": "Compose workplace investigation and background-screening skills for authorized corporate investigative support.",
    "workplace-investigator": "Compose workplace allegation, policy, evidence, interview, finding, and report skills for authorized workplace investigations.",
    "background-screening-specialist": "Compose consent, authority, source selection, identity ambiguity, discrepancy, relevance, and due-diligence summary skills for background-screening support.",
    "loss-prevention-investigator": "Compose asset-protection, loss-event, shrink-pattern, process-control, evidence, and case-summary skills for authorized loss-prevention investigation support.",
    "security-officer": "Compose professional core, authority, compliance, evidence, reporting, post-order, patrol, access, incident, communication, and program-management skills for authorized security officer support.",
    "mobile-patrol-officer": "Compose security operations, patrol, access, alarm, occurrence, handoff, and log-review skills for authorized mobile patrol support.",
    "loss-prevention-officer": "Compose asset-protection, loss-event, shrink-pattern, process-control, evidence, and improvement skills for authorized loss-prevention officer support.",
    "security-supervisor": "Compose security operations, incident response, and de-escalation skills for supervisory review and shift support.",
    "security-operations-manager": "Compose security operations, incident response, de-escalation, and program-management skills for operational management support.",
    "physical-security-analyst": "Compose physical-security risk and security-system skills for conceptual assessment, requirements, event-analysis, and improvement support.",
    "security-risk-assessor": "Compose physical-security risk and security-system skills for threat, vulnerability, consequence, likelihood, control, and gap assessment support.",
    "incident-response-coordinator": "Compose incident response and communication skills for escalation, notification, timeline, scene-preservation, and post-incident review support.",
    "security-program-manager": "Compose professional core, authority, compliance, evidence, reporting, physical-security, security-system, and program-management skills for security program governance support.",
    "corporate-security-investigator": "Compose loss-prevention and asset-protection skills for corporate security investigations involving loss events, shrink, process controls, and evidence mapping.",
    "asset-protection-specialist": "Compose asset-protection, loss-event, shrink-pattern, process-control, evidence, case-summary, and improvement skills for authorized asset protection support.",
    "corporate-security-manager": "Compose security program, supervisory operations, corporate investigation, and asset-protection skills for corporate security management support.",
}

DERIVED_ROLE_INPUTS = {
    "loss-prevention-officer": {
        "role_tags": ["asset-protection-specialist"],
        "families": ["19-loss-prevention-asset-protection"],
    },
    "security-operations-manager": {
        "role_tags": ["security-supervisor"],
        "families": ["20-investigation-security-program-management"],
    },
    "corporate-security-manager": {
        "role_tags": [
            "security-program-manager",
            "security-supervisor",
            "corporate-investigator",
            "asset-protection-specialist",
        ],
        "families": ["20-investigation-security-program-management"],
    },
}


def load_taxonomy(repo_root: Path) -> dict[str, object]:
    return json.loads((repo_root / "docs/architecture/taxonomy-index.yaml").read_text(encoding="utf-8"))


def skills_by_taxonomy_role(skills: list[dict[str, object]]) -> dict[str, list[str]]:
    by_role: dict[str, list[str]] = defaultdict(list)
    for skill in skills:
        name = str(skill["name"])
        for role in skill["professional_skillsets"]:
            by_role[str(role)].append(name)
    return {role: sorted(set(names)) for role, names in by_role.items()}


def skills_by_family(skills: list[dict[str, object]]) -> dict[str, list[str]]:
    by_family: dict[str, list[str]] = defaultdict(list)
    for skill in skills:
        by_family[str(skill["family"])].append(str(skill["name"]))
    return {family: sorted(set(names)) for family, names in by_family.items()}


def branch_for(role: str) -> str:
    if role in INVESTIGATION_SKILLSETS:
        return "Investigation"
    if role in SECURITY_SKILLSETS:
        return "Security"
    return "Hybrid"


def included_skills(role: str, by_role: dict[str, list[str]], by_family: dict[str, list[str]]) -> list[str]:
    if role in by_role:
        return by_role[role]

    derived = DERIVED_ROLE_INPUTS[role]
    names: set[str] = set()
    for role_tag in derived["role_tags"]:
        names.update(by_role.get(role_tag, []))
    for family in derived["families"]:
        names.update(by_family.get(family, []))
    return sorted(names)


def routing_triggers(role: str, branch: str) -> list[str]:
    common = [
        "request needs role-level composition rather than a single atomic skill",
        "jurisdiction, authority, scope, privacy, or escalation must be checked before downstream work",
        "multiple included skills are needed in sequence",
    ]
    if branch == "Investigation":
        return common + [
            "investigative intake, planning, evidence, research, interview, analysis, observation, reporting, or case-management workflow",
            "background-screening, workplace, corporate, or loss-prevention investigation workflow",
        ]
    if branch == "Security":
        return common + [
            "post-order, patrol, access, incident, communication, physical-security, security-system, or program-management workflow",
            "security operations require supervisor, manager, program, or qualified-review coordination",
        ]
    return common + [
        "corporate security, asset protection, loss-prevention, investigation, or security-management workflow crosses branches",
        "private investigation and private security boundaries must both remain visible",
    ]


def dependencies(role: str, branch: str) -> list[str]:
    deps = [
        "docs/architecture/domain-contract.md",
        "docs/architecture/authority-routing.md",
        "docs/architecture/sensitivity-model.md",
        "docs/architecture/intrusive-task-gate.md",
        "docs/architecture/certification-boundaries.md",
        "docs/architecture/canadian-jurisdiction-roadmap.md",
        "docs/architecture/taxonomy-index.yaml",
        "identify-jurisdiction",
        "identify-client-role",
        "classify-request-type",
        "define-scope-boundaries",
        "identify-escalation-requirement",
    ]
    if branch in {"Investigation", "Hybrid"}:
        deps.extend(["validate-investigative-authority", "assess-lawful-purpose"])
    if branch in {"Security", "Hybrid"}:
        deps.extend(["validate-security-service-authority", "review-post-orders"])
    deps.extend(["identify-licensing-requirement", "identify-privacy-obligation", "prepare-compliance-escalation"])
    return sorted(set(deps))


def jurisdiction_requirements(branch: str) -> list[str]:
    requirements = [
        "identify country, province, territory, state, or local jurisdiction before regulated work",
        "apply Canada federal specialization when federal privacy, criminal-law, evidence, human-rights, federally regulated workplace, or labour issues may apply",
        "apply provincial or territorial specialization when local private investigation, private security, privacy, workplace, records, trespass, training, or business-licensing issues may apply",
        "label outputs as issue spotting when current jurisdiction-specific sources have not been verified",
    ]
    if branch == "Hybrid":
        requirements.append("resolve both investigation and security jurisdiction requirements before cross-branch work proceeds")
    return requirements


def authority_requirements(branch: str) -> list[str]:
    requirements = [
        "identify user role, client role, organization authority, lawful purpose, scope, and source/access authorization",
        "do not infer licence status, business authority, regulator approval, training status, or professional certification from job title",
        "route unresolved regulated authority to REGULATED_RESEARCH_ONLY or qualified review",
    ]
    if branch in {"Investigation", "Hybrid"}:
        requirements.append("validate investigative authority before investigation planning, research, interviews, surveillance governance, findings, or reports")
    if branch in {"Security", "Hybrid"}:
        requirements.append("validate security service authority, post-order authority, site authority, and supervisor path before security-operation support")
    return requirements


def sensitivity_limits() -> list[str]:
    return [
        "PROCEED_ROUTINE only for bounded documentation or analysis with enough supplied facts",
        "CLARIFY_SCOPE when material jurisdiction, role, authority, source, scope, or subject facts are missing",
        "REGULATED_RESEARCH_ONLY for licensing, privacy, records, workplace, public-sector access, training, business, or compliance questions",
        "INTRUSIVE_GATE_REQUIRED for surveillance, monitoring, identity, screening, sensitive workplace, health-information, or third-party capture questions",
        "CERTIFICATION_ESCALATION for legal, licensing, emergency, force, weapons, restraint, alarm, engineering, fire, life-safety, training, compliance, or professional approval requests",
        "PROHIBITED_REDIRECT for hacking, credential theft, unauthorized access, lock bypass, forced entry, unlawful tracking, stalking, impersonation, coercion, evasion, alarm defeat, camera defeat, weapons use, restraint techniques, fabricated evidence, or concealed records",
    ]


def escalation_rules(branch: str) -> list[str]:
    rules = [
        "escalate legal interpretation, licence eligibility, compliance certification, privacy signoff, employment action, or regulator filings to qualified reviewers",
        "escalate immediate danger, suspected active crime, medical emergency, fire, life-safety, or violent-risk facts to responsible emergency or site authority",
        "preserve unknowns, assumptions, limitations, source currentness, and reviewer questions in outputs",
    ]
    if branch in {"Investigation", "Hybrid"}:
        rules.append("escalate consequential investigative findings, surveillance decisions, interviews, or background-screening decisions to responsible human review")
    if branch in {"Security", "Hybrid"}:
        rules.append("escalate force, detention, search, removal, weapons, patrol-dog, body-armour, alarm-response, and post-order conflict questions to qualified security leadership or emergency authority")
    return rules


def expected_outputs(branch: str) -> list[str]:
    outputs = [
        "role-scoped intake questions",
        "skill sequence plan",
        "authority and jurisdiction gap list",
        "source and evidence checklist",
        "limitations and escalation notes",
    ]
    if branch == "Investigation":
        outputs.extend(["investigation plan outline", "evidence and findings workflow", "reporting workflow"])
    elif branch == "Security":
        outputs.extend(["security operations workflow", "incident and notification workflow", "program or assessment review workflow"])
    else:
        outputs.extend(["cross-branch role-boundary map", "asset-protection or corporate-security workflow", "manager review workflow"])
    return outputs


def excluded_responsibilities(branch: str) -> list[str]:
    excluded = [
        "duplicating underlying skill procedures",
        "legal advice or final legal conclusion",
        "licensing approval or regulator substitute",
        "privacy compliance certification",
        "professional certification or training approval",
        "law-enforcement authority",
        "fabricated facts, fabricated records, altered evidence, or concealed source gaps",
    ]
    if branch in {"Investigation", "Hybrid"}:
        excluded.extend(["unauthorized investigation", "unauthorized surveillance", "coercive questioning", "background-screening without authority or required consent"])
    if branch in {"Security", "Hybrid"}:
        excluded.extend(["use-of-force instruction", "weapon instruction", "restraint technique", "detention tactic", "search tactic", "access-control bypass", "lock bypass", "alarm defeat", "camera defeat"])
    return sorted(set(excluded))


def build_registry(repo_root: Path) -> dict[str, object]:
    taxonomy = load_taxonomy(repo_root)
    skills = [skill for skill in taxonomy["skills"] if isinstance(skill, dict)]
    by_role = skills_by_taxonomy_role(skills)
    by_family = skills_by_family(skills)
    roles = INVESTIGATION_SKILLSETS + SECURITY_SKILLSETS + HYBRID_SKILLSETS

    skillsets = []
    for role in roles:
        branch = branch_for(role)
        skillsets.append(
            {
                "slug": role,
                "branch": branch,
                "purpose": ROLE_PURPOSES[role],
                "included_skills": included_skills(role, by_role, by_family),
                "routing_triggers": routing_triggers(role, branch),
                "dependencies": dependencies(role, branch),
                "jurisdiction_requirements": jurisdiction_requirements(branch),
                "authority_requirements": authority_requirements(branch),
                "sensitivity_limits": sensitivity_limits(),
                "escalation_rules": escalation_rules(branch),
                "expected_outputs": expected_outputs(branch),
                "excluded_responsibilities": excluded_responsibilities(branch),
                "composition_rule": "Skillsets compose existing atomic skills and must not duplicate underlying procedures.",
            }
        )

    return {
        "schema_version": "1.0",
        "status": "READY",
        "completion_token": TOKEN,
        "source_of_truth": "docs/architecture/taxonomy-index.yaml",
        "composition_rule": "Skillsets compose skills. They must not duplicate underlying procedures.",
        "skillset_count": len(skillsets),
        "skillsets": skillsets,
    }


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    registry = build_registry(repo_root)
    output = repo_root / "skillsets/professional-skillsets.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {output.relative_to(repo_root)} with {registry['skillset_count']} skillsets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
