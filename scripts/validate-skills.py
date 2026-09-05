from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


TOKENS = {
    "AI-08": "AGENTINVESTIGATE_AI_08_REFERENCE_SKILLS_READY",
    "AI-09": "AGENTINVESTIGATE_AI_09_PROFESSIONAL_CORE_READY",
    "AI-10": "AGENTINVESTIGATE_AI_10_AUTHORITY_COMPLIANCE_READY",
    "AI-11": "AGENTINVESTIGATE_AI_11_CASE_MANAGEMENT_READY",
    "AI-12": "AGENTINVESTIGATE_AI_12_RESEARCH_OSINT_READY",
    "AI-13": "AGENTINVESTIGATE_AI_13_ENTITY_ANALYSIS_READY",
    "AI-14": "AGENTINVESTIGATE_AI_14_INTERVIEWING_READY",
    "AI-15": "AGENTINVESTIGATE_AI_15_EVIDENCE_READY",
    "AI-16": "AGENTINVESTIGATE_AI_16_INVESTIGATIVE_ANALYSIS_READY",
    "AI-17": "AGENTINVESTIGATE_AI_17_REPORTING_READY",
    "AI-18": "AGENTINVESTIGATE_AI_18_OBSERVATION_GOVERNANCE_READY",
    "AI-19": "AGENTINVESTIGATE_AI_19_WORKPLACE_INVESTIGATIONS_READY",
    "AI-20": "AGENTINVESTIGATE_AI_20_SCREENING_DUE_DILIGENCE_READY",
    "AI-21": "AGENTINVESTIGATE_AI_21_SECURITY_OPERATIONS_READY",
    "AI-22": "AGENTINVESTIGATE_AI_22_INCIDENT_COMMUNICATION_READY",
    "AI-23": "AGENTINVESTIGATE_AI_23_PHYSICAL_SECURITY_READY",
    "AI-24": "AGENTINVESTIGATE_AI_24_SECURITY_SYSTEMS_READY",
}

AI10_FAMILIES = {
    "02-case-intake-scope-authority",
    "03-law-licensing-privacy-compliance",
}

AI10_REFERENCE_OVERRIDES = {
    "identify-licensing-requirement": "references/licensing-source-checklist.md",
}

AI10_CRITICAL_INTEGRATION_TESTS = {
    "ordinary research",
    "workplace investigation",
    "surveillance",
    "personal background screening",
    "unknown jurisdiction",
    "prohibited request",
    "conflicting client authority",
}

AI11_FAMILY = "04-investigation-planning-case-management"

AI11_SCENARIO_TOPICS = {
    "investigation plan",
    "investigative questions",
    "timeline",
    "leads",
    "resources",
    "milestones",
    "case log",
    "notes",
    "status",
    "retention",
    "review",
    "gaps",
    "closure",
}

AI12_FAMILY = "05-research-osint-public-records"

AI12_RESEARCH_TOPICS = {
    "research planning",
    "public records",
    "open sources",
    "corporate records",
    "court records",
    "regulatory records",
    "source reliability",
    "provenance",
    "corroboration",
    "source conflict",
    "organization research",
    "property context",
    "litigation research",
    "research summaries",
}

AI12_HARD_BOUNDARY_TESTS = {
    "unauthorized database access",
    "credential acquisition",
    "private-account compromise",
    "protected-record acquisition through deception",
}

AI13_FAMILY = "06-identity-entity-timeline-analysis"

AI13_REQUIRED_CAPABILITIES = {
    "identity ambiguity",
    "same-name differentiation",
    "identifier normalization",
    "subject timelines",
    "relationship mapping",
    "association evidence",
    "timeline gaps",
    "entity contradictions",
}

AI13_CONFIDENCE_MODEL = {
    "POSSIBLE",
    "PROBABLE",
    "CORROBORATED",
    "CONFIRMED",
    "UNRESOLVED",
}

AI14_FAMILY = "07-interviewing-witnesses-statements"

AI14_REQUIRED_EMPHASIS = {
    "neutral questioning",
    "objectives",
    "sequencing",
    "information gaps",
    "statements",
    "notes",
    "consistency",
    "corroboration",
    "follow-up",
    "bias",
}

AI14_PROHIBITED_INFERENCE = {
    "body language",
    "eye contact",
    "nervousness",
    "personality",
    "unsupported behavioral stereotypes",
}

AI15_FAMILY = "08-evidence-chain-of-custody"

AI15_REQUIRED_EMPHASIS = {
    "evidence log",
    "evidence type",
    "source",
    "relevance",
    "chain of custody",
    "continuity gap",
    "transfer",
    "original and copy",
    "timestamp",
    "allegation mapping",
    "continuity issue",
    "handling escalation",
}

AI15_CONTINUITY_ELEMENTS = {
    "original evidence item",
    "transfer",
    "missing signature",
    "duplicate copy",
    "disputed timestamp",
    "partial continuity record",
}

AI15_GATE = "Continuity issues must be identified without claiming admissibility as a legal conclusion."

AI16_FAMILY = "09-investigative-analysis"

AI16_REASONING_RULE = "FACT ≠ INFERENCE ≠ ALLEGATION ≠ FINDING"

AI16_REASONING_CATEGORIES = {
    "FACT",
    "INFERENCE",
    "ALLEGATION",
    "FINDING",
}

AI16_REQUIRED_CAPABILITIES = {
    "evidence matrix",
    "hypothesis generation",
    "hypothesis testing",
    "alternative explanations",
    "evidence contradiction",
    "event chronology",
    "pattern analysis",
    "source weight",
    "finding confidence",
    "unresolved question",
    "investigative finding",
}

AI16_GATE = "Integration tests must include plausible but incorrect hypotheses and disconfirming evidence."

AI17_FAMILY = "11-reporting-findings-case-presentation"

AI17_REQUIRED_OUTPUTS = {
    "investigative reports",
    "incident reports",
    "chronology",
    "evidence summaries",
    "findings matrices",
    "executive summaries",
    "report QA",
    "case presentations",
    "testimony-support outlines",
    "report limitations",
}

AI17_REQUIRED_REPORT_FIELDS = {
    "facts",
    "sources",
    "evidence",
    "inference",
    "limitations",
    "unresolved questions",
    "confidence",
}

AI17_GATE = "Reports must identify facts, sources, evidence, inference, limitations, unresolved questions, and confidence."

AI18_FAMILY = "10-observation-surveillance-governance"

AI18_IMPLEMENTED_SKILLS = {
    "assess-observation-authorization",
    "assess-observation-necessity",
    "assess-observation-proportionality",
    "define-observation-purpose",
    "plan-lawful-observation-assignment",
    "record-field-observation",
    "minimize-third-party-information",
    "review-observation-record-for-compliance",
}

AI18_MANDATORY_PROPERTIES = {
    "sensitivity": "INTRUSIVE",
    "jurisdiction_required": True,
    "human_review_required": True,
}

AI18_PROHIBITED_OPERATIONAL_SKILLS = {
    "avoiding detection",
    "following targets covertly",
    "counter-surveillance defeat",
    "tracking-device installation",
    "security evasion",
}

AI18_GATE = "Observation governance skills must be intrusive, jurisdiction-gated, and human-review-gated without operational surveillance tactics."

AI19_FAMILY = "12-corporate-workplace-investigations"

AI19_WORKFLOW_STEPS = {
    "allegation",
    "scope",
    "allegations matrix",
    "policy mapping",
    "interview planning",
    "evidence analysis",
    "statement comparison",
    "evidentiary support",
    "findings",
    "report",
}

AI19_PROHIBITED_DECISIONS = {
    "discipline",
    "termination",
    "legal liability",
    "criminal guilt",
}

AI19_GATE = "End-to-end workplace investigation flow must not decide discipline, termination, legal liability, or criminal guilt."

AI20_FAMILY = "13-background-screening-due-diligence"

AI20_REQUIRED_SPLIT = {
    "PERSON SCREENING",
    "ENTITY DUE DILIGENCE",
}

AI20_INTEGRATION_REQUIREMENTS = {
    "consent",
    "relevance",
    "public records",
    "conflicting identities",
    "adverse information",
    "unresolved records",
    "bias risk",
}

AI20_GATE = "Personal screening requires stronger privacy and authority controls than entity due diligence."

AI21_FAMILY = "14-security-operations-access-patrol"

AI21_LIFECYCLE_STEPS = {
    "post orders",
    "shift plan",
    "patrol",
    "observation",
    "access event",
    "alarm",
    "occurrence",
    "handoff",
    "log review",
}

AI21_COMPOSITION_TARGETS = {
    "security-officer",
    "mobile-patrol-officer",
}

AI21_PROHIBITED_OPERATIONAL_CONTENT = {
    "physical intervention",
    "use of force",
    "restraint techniques",
    "weapons use",
    "access-control bypass",
    "lock bypass",
    "alarm defeat",
    "law-enforcement impersonation",
}

AI21_GATE = "Security operations skills must support post orders through log review without physical intervention, use of force, access-control bypass, alarm defeat, or law-enforcement impersonation."

AI22_FAMILIES = {
    "15-incident-response",
    "16-communication-deescalation",
}

AI22_REFERENCE_OVERRIDES = {
    "determine-emergency-escalation": "references/emergency-escalation-checklist.md",
}

AI22_INCIDENT_CAPABILITIES = {
    "recognition",
    "escalation",
    "notification",
    "scene preservation",
    "emergency-service support",
    "documentation",
    "post-incident review",
}

AI22_COMMUNICATION_CAPABILITIES = {
    "conflict avoidance",
    "de-escalation",
    "radio communication",
    "incident notification",
    "audience adaptation",
    "bias review",
}

AI22_PROHIBITED_PHYSICAL_INTERVENTION = {
    "physical intervention instruction",
    "use of force",
    "restraint techniques",
    "weapons use",
    "tactical confrontation",
    "pursuit",
    "detention",
    "search",
}

AI22_CERTIFICATION_BOUNDARY = "No physical intervention instruction."

AI22_GATE = "Incident response and communication skills must not provide physical intervention instruction."

AI23_FAMILY = "17-physical-security-risk-assessment"

AI23_REASONING_CHAIN = {
    "assets",
    "threats",
    "vulnerabilities",
    "consequences",
    "likelihood",
    "risk",
    "controls",
    "gaps",
    "options",
    "prioritized improvements",
}

AI23_BOUNDARY_TERMS = {
    "structural engineering",
    "electrical approval",
    "fire-code approval",
    "life-safety certification",
}

AI23_COMPOSITION_TARGETS = {
    "physical-security-analyst",
    "security-risk-assessor",
}

AI23_PROHIBITED_SECURITY_DETAIL = {
    "attack instructions",
    "bypass instructions",
    "forced entry",
    "alarm defeat",
    "camera evasion",
    "access-control circumvention",
}

AI23_GATE = "Conceptual security analysis must not be presented as structural engineering, electrical approval, fire-code approval, or life-safety certification."

AI24_FAMILY = "18-security-systems-technology"

AI24_SYSTEM_ANALYSIS_CAPABILITIES = {
    "access control",
    "video surveillance",
    "intrusion detection",
    "alarm monitoring",
    "event analysis",
    "coverage",
    "failures",
    "requirements",
}

AI24_EXPLICIT_PROHIBITIONS = {
    "alarm bypass",
    "camera defeat",
    "credential cloning",
    "access-control circumvention",
    "monitoring evasion",
}

AI24_QUALIFIED_BOUNDARIES = {
    "licensed technician review",
    "privacy review",
    "life-safety review",
    "security authority review",
}

AI24_GATE = "Security systems and technology skills must not provide alarm bypass, camera defeat, credential cloning, access-control circumvention, or monitoring evasion."

REFERENCE_SKILLS = {
    "build-evidence-matrix": {
        "family": "09-investigative-analysis",
        "sensitivity": "ROUTINE",
        "reference": "references/evidence-matrix-reference.md",
    },
    "identify-licensing-requirement": {
        "family": "03-law-licensing-privacy-compliance",
        "sensitivity": "REGULATED",
        "reference": "references/licensing-source-checklist.md",
    },
    "assess-observation-proportionality": {
        "family": "10-observation-surveillance-governance",
        "sensitivity": "INTRUSIVE",
        "reference": "references/observation-proportionality-checklist.md",
    },
    "determine-emergency-escalation": {
        "family": "15-incident-response",
        "sensitivity": "CERTIFICATION_BOUNDARY",
        "reference": "references/emergency-escalation-checklist.md",
    },
}

PROFESSIONAL_CORE_SKILLS = {
    "define-professional-role-boundaries": {
        "family": "01-professional-core-ethics",
        "sensitivity": "ROUTINE",
        "reference": "references/role-boundary-checklist.md",
    },
    "assess-conflict-of-interest": {
        "family": "01-professional-core-ethics",
        "sensitivity": "ROUTINE",
        "reference": "references/conflict-check-reference.md",
    },
    "apply-ethical-decision-framework": {
        "family": "01-professional-core-ethics",
        "sensitivity": "ROUTINE",
        "reference": "references/ethical-decision-reference.md",
    },
    "identify-investigative-bias": {
        "family": "01-professional-core-ethics",
        "sensitivity": "ROUTINE",
        "reference": "references/bias-review-reference.md",
    },
    "separate-fact-from-inference": {
        "family": "01-professional-core-ethics",
        "sensitivity": "ROUTINE",
        "reference": "references/fact-inference-reference.md",
    },
    "assess-duty-of-care": {
        "family": "01-professional-core-ethics",
        "sensitivity": "ROUTINE",
        "reference": "references/duty-of-care-reference.md",
    },
    "protect-confidential-information": {
        "family": "01-professional-core-ethics",
        "sensitivity": "ROUTINE",
        "reference": "references/confidentiality-handling-reference.md",
    },
    "identify-escalation-requirement": {
        "family": "01-professional-core-ethics",
        "sensitivity": "ROUTINE",
        "reference": "references/escalation-routing-reference.md",
    },
    "document-professional-decision": {
        "family": "01-professional-core-ethics",
        "sensitivity": "ROUTINE",
        "reference": "references/professional-decision-record-reference.md",
    },
}

REQUIRED_SECTIONS = (
    "Overview",
    "Triggers",
    "Non-Triggers",
    "Required Inputs",
    "Optional Inputs",
    "Assumptions",
    "Dependencies",
    "Core Procedure",
    "Evidence Requirements",
    "Source Requirements",
    "Jurisdiction Requirements",
    "Authority Checks",
    "Sensitivity Handling",
    "Output Contract",
    "Limitations",
    "Escalation",
    "References",
    "Testing",
)

SKILL_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"^---\n(?P<body>.*?)\n---\n", re.DOTALL)
HEADING_RE = re.compile(r"^## (?P<section>.+)$", re.MULTILINE)

SCENARIO_FIELDS = {
    "id",
    "skill_under_test",
    "test_type",
    "test_classes",
    "prompt",
    "expected_routing_state",
    "required_checks",
    "blocked_outputs",
}

VALID_TEST_TYPES = {"positive", "negative-routing"}
VALID_ROUTING_STATES = {
    "PROCEED_ROUTINE",
    "CLARIFY_SCOPE",
    "REGULATED_RESEARCH_ONLY",
    "INTRUSIVE_GATE_REQUIRED",
    "CERTIFICATION_ESCALATION",
    "PROHIBITED_REDIRECT",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.search(text)
    if not match:
        return {}

    fields: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def taxonomy(repo_root: Path) -> dict[str, dict[str, Any]]:
    index = load_json(repo_root / "docs" / "architecture" / "taxonomy-index.yaml")
    return {skill["name"]: skill for skill in index["skills"]}


def authority_compliance_skills(taxonomy_by_name: dict[str, dict[str, Any]]) -> dict[str, dict[str, str]]:
    skills: dict[str, dict[str, str]] = {}
    for name, row in taxonomy_by_name.items():
        family = row.get("family")
        if family not in AI10_FAMILIES:
            continue
        skills[name] = {
            "family": str(family),
            "sensitivity": str(row.get("sensitivity")),
            "reference": AI10_REFERENCE_OVERRIDES.get(name, f"references/{name}-reference.md"),
        }
    return skills


def case_management_skills(taxonomy_by_name: dict[str, dict[str, Any]]) -> dict[str, dict[str, str]]:
    skills: dict[str, dict[str, str]] = {}
    for name, row in taxonomy_by_name.items():
        family = row.get("family")
        if family != AI11_FAMILY:
            continue
        skills[name] = {
            "family": str(family),
            "sensitivity": str(row.get("sensitivity")),
            "reference": f"references/{name}-reference.md",
        }
    return skills


def research_osint_skills(taxonomy_by_name: dict[str, dict[str, Any]]) -> dict[str, dict[str, str]]:
    skills: dict[str, dict[str, str]] = {}
    for name, row in taxonomy_by_name.items():
        family = row.get("family")
        if family != AI12_FAMILY:
            continue
        skills[name] = {
            "family": str(family),
            "sensitivity": str(row.get("sensitivity")),
            "reference": f"references/{name}-reference.md",
        }
    return skills


def entity_analysis_skills(taxonomy_by_name: dict[str, dict[str, Any]]) -> dict[str, dict[str, str]]:
    skills: dict[str, dict[str, str]] = {}
    for name, row in taxonomy_by_name.items():
        family = row.get("family")
        if family != AI13_FAMILY:
            continue
        skills[name] = {
            "family": str(family),
            "sensitivity": str(row.get("sensitivity")),
            "reference": f"references/{name}-reference.md",
        }
    return skills


def interviewing_skills(taxonomy_by_name: dict[str, dict[str, Any]]) -> dict[str, dict[str, str]]:
    skills: dict[str, dict[str, str]] = {}
    for name, row in taxonomy_by_name.items():
        family = row.get("family")
        if family != AI14_FAMILY:
            continue
        skills[name] = {
            "family": str(family),
            "sensitivity": str(row.get("sensitivity")),
            "reference": f"references/{name}-reference.md",
        }
    return skills


def evidence_skills(taxonomy_by_name: dict[str, dict[str, Any]]) -> dict[str, dict[str, str]]:
    skills: dict[str, dict[str, str]] = {}
    for name, row in taxonomy_by_name.items():
        family = row.get("family")
        if family != AI15_FAMILY:
            continue
        skills[name] = {
            "family": str(family),
            "sensitivity": str(row.get("sensitivity")),
            "reference": f"references/{name}-reference.md",
        }
    return skills


def investigative_analysis_skills(taxonomy_by_name: dict[str, dict[str, Any]]) -> dict[str, dict[str, str]]:
    skills: dict[str, dict[str, str]] = {}
    for name, row in taxonomy_by_name.items():
        family = row.get("family")
        if family != AI16_FAMILY:
            continue
        reference = "references/evidence-matrix-reference.md" if name == "build-evidence-matrix" else f"references/{name}-reference.md"
        skills[name] = {
            "family": str(family),
            "sensitivity": str(row.get("sensitivity")),
            "reference": reference,
        }
    return skills


def reporting_skills(taxonomy_by_name: dict[str, dict[str, Any]]) -> dict[str, dict[str, str]]:
    skills: dict[str, dict[str, str]] = {}
    for name, row in taxonomy_by_name.items():
        family = row.get("family")
        if family != AI17_FAMILY:
            continue
        skills[name] = {
            "family": str(family),
            "sensitivity": str(row.get("sensitivity")),
            "reference": f"references/{name}-reference.md",
        }
    return skills


def observation_governance_skills(taxonomy_by_name: dict[str, dict[str, Any]]) -> dict[str, dict[str, str]]:
    skills: dict[str, dict[str, str]] = {}
    for name, row in taxonomy_by_name.items():
        family = row.get("family")
        if family != AI18_FAMILY or name not in AI18_IMPLEMENTED_SKILLS:
            continue
        reference = (
            "references/observation-proportionality-checklist.md"
            if name == "assess-observation-proportionality"
            else f"references/{name}-reference.md"
        )
        skills[name] = {
            "family": str(family),
            "sensitivity": str(row.get("sensitivity")),
            "reference": reference,
        }
    return skills


def workplace_investigation_skills(taxonomy_by_name: dict[str, dict[str, Any]]) -> dict[str, dict[str, str]]:
    skills: dict[str, dict[str, str]] = {}
    for name, row in taxonomy_by_name.items():
        family = row.get("family")
        if family != AI19_FAMILY:
            continue
        skills[name] = {
            "family": str(family),
            "sensitivity": str(row.get("sensitivity")),
            "reference": f"references/{name}-reference.md",
        }
    return skills


def screening_due_diligence_skills(taxonomy_by_name: dict[str, dict[str, Any]]) -> dict[str, dict[str, str]]:
    skills: dict[str, dict[str, str]] = {}
    for name, row in taxonomy_by_name.items():
        family = row.get("family")
        if family != AI20_FAMILY:
            continue
        skills[name] = {
            "family": str(family),
            "sensitivity": str(row.get("sensitivity")),
            "reference": f"references/{name}-reference.md",
        }
    return skills


def security_operations_skills(taxonomy_by_name: dict[str, dict[str, Any]]) -> dict[str, dict[str, str]]:
    skills: dict[str, dict[str, str]] = {}
    for name, row in taxonomy_by_name.items():
        family = row.get("family")
        if family != AI21_FAMILY:
            continue
        skills[name] = {
            "family": str(family),
            "sensitivity": str(row.get("sensitivity")),
            "reference": f"references/{name}-reference.md",
        }
    return skills


def incident_communication_skills(taxonomy_by_name: dict[str, dict[str, Any]]) -> dict[str, dict[str, str]]:
    skills: dict[str, dict[str, str]] = {}
    for name, row in taxonomy_by_name.items():
        family = row.get("family")
        if family not in AI22_FAMILIES:
            continue
        skills[name] = {
            "family": str(family),
            "sensitivity": str(row.get("sensitivity")),
            "reference": AI22_REFERENCE_OVERRIDES.get(name, f"references/{name}-reference.md"),
        }
    return skills


def physical_security_skills(taxonomy_by_name: dict[str, dict[str, Any]]) -> dict[str, dict[str, str]]:
    skills: dict[str, dict[str, str]] = {}
    for name, row in taxonomy_by_name.items():
        family = row.get("family")
        if family != AI23_FAMILY:
            continue
        skills[name] = {
            "family": str(family),
            "sensitivity": str(row.get("sensitivity")),
            "reference": f"references/{name}-reference.md",
        }
    return skills


def security_systems_skills(taxonomy_by_name: dict[str, dict[str, Any]]) -> dict[str, dict[str, str]]:
    skills: dict[str, dict[str, str]] = {}
    for name, row in taxonomy_by_name.items():
        family = row.get("family")
        if family != AI24_FAMILY:
            continue
        skills[name] = {
            "family": str(family),
            "sensitivity": str(row.get("sensitivity")),
            "reference": f"references/{name}-reference.md",
        }
    return skills


def required_skills(taxonomy_by_name: dict[str, dict[str, Any]]) -> dict[str, dict[str, str]]:
    return {
        **REFERENCE_SKILLS,
        **PROFESSIONAL_CORE_SKILLS,
        **authority_compliance_skills(taxonomy_by_name),
        **case_management_skills(taxonomy_by_name),
        **research_osint_skills(taxonomy_by_name),
        **entity_analysis_skills(taxonomy_by_name),
        **interviewing_skills(taxonomy_by_name),
        **evidence_skills(taxonomy_by_name),
        **investigative_analysis_skills(taxonomy_by_name),
        **reporting_skills(taxonomy_by_name),
        **observation_governance_skills(taxonomy_by_name),
        **workplace_investigation_skills(taxonomy_by_name),
        **screening_due_diligence_skills(taxonomy_by_name),
        **security_operations_skills(taxonomy_by_name),
        **incident_communication_skills(taxonomy_by_name),
        **physical_security_skills(taxonomy_by_name),
        **security_systems_skills(taxonomy_by_name),
    }


def scenario_suites(
    ai10_skills: dict[str, dict[str, str]],
    ai11_skills: dict[str, dict[str, str]],
    ai12_skills: dict[str, dict[str, str]],
    ai13_skills: dict[str, dict[str, str]],
    ai14_skills: dict[str, dict[str, str]],
    ai15_skills: dict[str, dict[str, str]],
    ai16_skills: dict[str, dict[str, str]],
    ai17_skills: dict[str, dict[str, str]],
    ai18_skills: dict[str, dict[str, str]],
    ai19_skills: dict[str, dict[str, str]],
    ai20_skills: dict[str, dict[str, str]],
    ai21_skills: dict[str, dict[str, str]],
    ai22_skills: dict[str, dict[str, str]],
    ai23_skills: dict[str, dict[str, str]],
    ai24_skills: dict[str, dict[str, str]],
) -> tuple[dict[str, Any], ...]:
    return (
        {
            "label": "AI-08-reference-scenarios.json",
            "relative_path": "tests/reference-skills/AI-08-reference-scenarios.json",
            "token": TOKENS["AI-08"],
            "skills": REFERENCE_SKILLS,
            "skill_list_key": "reference_skills",
        },
        {
            "label": "AI-09-professional-core-scenarios.json",
            "relative_path": "tests/reference-skills/AI-09-professional-core-scenarios.json",
            "token": TOKENS["AI-09"],
            "skills": PROFESSIONAL_CORE_SKILLS,
            "skill_list_key": "skills",
        },
        {
            "label": "AI-10-authority-compliance-scenarios.json",
            "relative_path": "tests/reference-skills/AI-10-authority-compliance-scenarios.json",
            "token": TOKENS["AI-10"],
            "skills": ai10_skills,
            "skill_list_key": "skills",
            "critical_integration_tests": AI10_CRITICAL_INTEGRATION_TESTS,
        },
        {
            "label": "AI-11-case-management-scenarios.json",
            "relative_path": "tests/reference-skills/AI-11-case-management-scenarios.json",
            "token": TOKENS["AI-11"],
            "skills": ai11_skills,
            "skill_list_key": "skills",
            "scenario_topics": AI11_SCENARIO_TOPICS,
        },
        {
            "label": "AI-12-research-osint-scenarios.json",
            "relative_path": "tests/reference-skills/AI-12-research-osint-scenarios.json",
            "token": TOKENS["AI-12"],
            "skills": ai12_skills,
            "skill_list_key": "skills",
            "research_topics": AI12_RESEARCH_TOPICS,
            "hard_boundary_tests": AI12_HARD_BOUNDARY_TESTS,
        },
        {
            "label": "AI-13-entity-analysis-scenarios.json",
            "relative_path": "tests/reference-skills/AI-13-entity-analysis-scenarios.json",
            "token": TOKENS["AI-13"],
            "skills": ai13_skills,
            "skill_list_key": "skills",
            "required_capabilities": AI13_REQUIRED_CAPABILITIES,
            "confidence_model": AI13_CONFIDENCE_MODEL,
            "gate": "Tests must detect and penalize identity overclaiming.",
        },
        {
            "label": "AI-14-interviewing-scenarios.json",
            "relative_path": "tests/reference-skills/AI-14-interviewing-scenarios.json",
            "token": TOKENS["AI-14"],
            "skills": ai14_skills,
            "skill_list_key": "skills",
            "required_emphasis": AI14_REQUIRED_EMPHASIS,
            "prohibited_inference": AI14_PROHIBITED_INFERENCE,
        },
        {
            "label": "AI-15-evidence-scenarios.json",
            "relative_path": "tests/reference-skills/AI-15-evidence-scenarios.json",
            "token": TOKENS["AI-15"],
            "skills": ai15_skills,
            "skill_list_key": "skills",
            "required_emphasis": AI15_REQUIRED_EMPHASIS,
            "continuity_elements": AI15_CONTINUITY_ELEMENTS,
            "gate": AI15_GATE,
        },
        {
            "label": "AI-16-investigative-analysis-scenarios.json",
            "relative_path": "tests/reference-skills/AI-16-investigative-analysis-scenarios.json",
            "token": TOKENS["AI-16"],
            "skills": ai16_skills,
            "skill_list_key": "skills",
            "required_capabilities": AI16_REQUIRED_CAPABILITIES,
            "reasoning_rule": AI16_REASONING_RULE,
            "reasoning_categories": AI16_REASONING_CATEGORIES,
            "gate": AI16_GATE,
        },
        {
            "label": "AI-17-reporting-scenarios.json",
            "relative_path": "tests/reference-skills/AI-17-reporting-scenarios.json",
            "token": TOKENS["AI-17"],
            "skills": ai17_skills,
            "skill_list_key": "skills",
            "required_outputs": AI17_REQUIRED_OUTPUTS,
            "required_report_fields": AI17_REQUIRED_REPORT_FIELDS,
            "gate": AI17_GATE,
        },
        {
            "label": "AI-18-observation-governance-scenarios.json",
            "relative_path": "tests/reference-skills/AI-18-observation-governance-scenarios.json",
            "token": TOKENS["AI-18"],
            "skills": ai18_skills,
            "skill_list_key": "skills",
            "mandatory_properties": AI18_MANDATORY_PROPERTIES,
            "prohibited_operational_skills": AI18_PROHIBITED_OPERATIONAL_SKILLS,
            "gate": AI18_GATE,
        },
        {
            "label": "AI-19-workplace-investigations-scenarios.json",
            "relative_path": "tests/reference-skills/AI-19-workplace-investigations-scenarios.json",
            "token": TOKENS["AI-19"],
            "skills": ai19_skills,
            "skill_list_key": "skills",
            "workflow_steps": AI19_WORKFLOW_STEPS,
            "prohibited_decisions": AI19_PROHIBITED_DECISIONS,
            "gate": AI19_GATE,
        },
        {
            "label": "AI-20-screening-due-diligence-scenarios.json",
            "relative_path": "tests/reference-skills/AI-20-screening-due-diligence-scenarios.json",
            "token": TOKENS["AI-20"],
            "skills": ai20_skills,
            "skill_list_key": "skills",
            "required_split": AI20_REQUIRED_SPLIT,
            "integration_requirements": AI20_INTEGRATION_REQUIREMENTS,
            "gate": AI20_GATE,
        },
        {
            "label": "AI-21-security-operations-scenarios.json",
            "relative_path": "tests/reference-skills/AI-21-security-operations-scenarios.json",
            "token": TOKENS["AI-21"],
            "skills": ai21_skills,
            "skill_list_key": "skills",
            "lifecycle_steps": AI21_LIFECYCLE_STEPS,
            "composition_targets": AI21_COMPOSITION_TARGETS,
            "prohibited_operational_content": AI21_PROHIBITED_OPERATIONAL_CONTENT,
            "gate": AI21_GATE,
        },
        {
            "label": "AI-22-incident-communication-scenarios.json",
            "relative_path": "tests/reference-skills/AI-22-incident-communication-scenarios.json",
            "token": TOKENS["AI-22"],
            "skills": ai22_skills,
            "skill_list_key": "skills",
            "families": AI22_FAMILIES,
            "incident_capabilities": AI22_INCIDENT_CAPABILITIES,
            "communication_capabilities": AI22_COMMUNICATION_CAPABILITIES,
            "certification_boundary": AI22_CERTIFICATION_BOUNDARY,
            "prohibited_physical_intervention": AI22_PROHIBITED_PHYSICAL_INTERVENTION,
            "gate": AI22_GATE,
        },
        {
            "label": "AI-23-physical-security-scenarios.json",
            "relative_path": "tests/reference-skills/AI-23-physical-security-scenarios.json",
            "token": TOKENS["AI-23"],
            "skills": ai23_skills,
            "skill_list_key": "skills",
            "reasoning_chain": AI23_REASONING_CHAIN,
            "composition_targets": AI23_COMPOSITION_TARGETS,
            "boundary_terms": AI23_BOUNDARY_TERMS,
            "prohibited_security_detail": AI23_PROHIBITED_SECURITY_DETAIL,
            "gate": AI23_GATE,
        },
        {
            "label": "AI-24-security-systems-scenarios.json",
            "relative_path": "tests/reference-skills/AI-24-security-systems-scenarios.json",
            "token": TOKENS["AI-24"],
            "skills": ai24_skills,
            "skill_list_key": "skills",
            "system_analysis_capabilities": AI24_SYSTEM_ANALYSIS_CAPABILITIES,
            "explicit_prohibitions": AI24_EXPLICIT_PROHIBITIONS,
            "qualified_boundaries": AI24_QUALIFIED_BOUNDARIES,
            "gate": AI24_GATE,
        },
    )


def skill_path(repo_root: Path, name: str, expected_skills: dict[str, dict[str, str]]) -> Path:
    family = expected_skills[name]["family"]
    return repo_root / "skills" / family / name


def validate_skill_package(
    repo_root: Path,
    name: str,
    expected_skills: dict[str, dict[str, str]],
    taxonomy_by_name: dict[str, dict[str, Any]],
    errors: list[str],
) -> None:
    expected_package = expected_skills[name]
    base = skill_path(repo_root, name, expected_skills)
    skill_md = base / "SKILL.md"
    agents_yaml = base / "agents" / "openai.yaml"
    reference_path = base / expected_package["reference"]

    for path in (skill_md, agents_yaml, reference_path):
        if not path.is_file():
            errors.append(f"{name}: missing required file {path.relative_to(repo_root)}")

    if name not in taxonomy_by_name:
        errors.append(f"{name}: missing from taxonomy")
        return

    taxonomy_row = taxonomy_by_name[name]
    if taxonomy_row.get("family") != expected_package["family"]:
        errors.append(f"{name}: family does not match taxonomy")
    if taxonomy_row.get("sensitivity") != expected_package["sensitivity"]:
        errors.append(f"{name}: sensitivity does not match taxonomy")

    if not skill_md.is_file():
        return

    text = skill_md.read_text(encoding="utf-8-sig")
    fields = parse_frontmatter(text)
    if fields.get("name") != name:
        errors.append(f"{name}: frontmatter name mismatch")
    if fields.get("license") != "MIT":
        errors.append(f"{name}: frontmatter license must be MIT")
    description = fields.get("description", "")
    if not description:
        errors.append(f"{name}: missing frontmatter description")
    if not SKILL_RE.match(name):
        errors.append(f"{name}: invalid skill name")

    sections = tuple(match.group("section") for match in HEADING_RE.finditer(text))
    if sections != REQUIRED_SECTIONS:
        errors.append(f"{name}: required sections are not in AI-04 order")

    if expected_package["sensitivity"] not in text:
        errors.append(f"{name}: missing sensitivity class in SKILL.md")
    if expected_package["family"] == AI13_FAMILY:
        for label in AI13_CONFIDENCE_MODEL:
            if label not in text:
                errors.append(f"{name}: missing AI-13 confidence label {label}")
    if expected_package["family"] == AI14_FAMILY:
        for term in AI14_PROHIBITED_INFERENCE:
            if term not in text:
                errors.append(f"{name}: missing AI-14 prohibited inference term {term}")
    if expected_package["family"] == AI15_FAMILY:
        for term in AI15_CONTINUITY_ELEMENTS:
            if term not in text:
                errors.append(f"{name}: missing AI-15 continuity element {term}")
        if "admissibility as a legal conclusion" not in text:
            errors.append(f"{name}: missing AI-15 admissibility legal conclusion boundary")
    if expected_package["family"] == AI16_FAMILY:
        if AI16_REASONING_RULE not in text:
            errors.append(f"{name}: missing AI-16 hard reasoning rule")
        if "disconfirming evidence" not in text:
            errors.append(f"{name}: missing AI-16 disconfirming evidence gate")
        if "plausible but incorrect hypotheses" not in text:
            errors.append(f"{name}: missing AI-16 plausible incorrect hypothesis gate")
    if expected_package["family"] == AI17_FAMILY:
        lower_text = text.lower()
        for field in AI17_REQUIRED_REPORT_FIELDS:
            if field not in lower_text:
                errors.append(f"{name}: missing AI-17 report field {field}")
        if "coach testimony" not in lower_text:
            errors.append(f"{name}: missing AI-17 testimony coaching boundary")
    if expected_package["family"] == AI18_FAMILY:
        lower_text = text.lower()
        for term in ("sensitivity: intrusive", "jurisdiction_required: true", "human_review_required: true"):
            if term not in lower_text:
                errors.append(f"{name}: missing AI-18 mandatory property {term}")
        for term in AI18_PROHIBITED_OPERATIONAL_SKILLS:
            if term not in lower_text:
                errors.append(f"{name}: missing AI-18 prohibited operational term {term}")
        if "operational surveillance tactics" not in lower_text:
            errors.append(f"{name}: missing AI-18 operational surveillance tactics boundary")
    if expected_package["family"] == AI19_FAMILY:
        lower_text = text.lower()
        for step in AI19_WORKFLOW_STEPS:
            if step not in lower_text:
                errors.append(f"{name}: missing AI-19 workflow step {step}")
        for decision in AI19_PROHIBITED_DECISIONS:
            if decision not in lower_text:
                errors.append(f"{name}: missing AI-19 prohibited decision {decision}")
        if "qualified human review" not in lower_text and "qualified review" not in lower_text:
            errors.append(f"{name}: missing AI-19 qualified review boundary")
    if expected_package["family"] == AI20_FAMILY:
        lower_text = text.lower()
        for split in AI20_REQUIRED_SPLIT:
            if split not in text:
                errors.append(f"{name}: missing AI-20 required split {split}")
        for term in AI20_INTEGRATION_REQUIREMENTS:
            if term not in lower_text:
                errors.append(f"{name}: missing AI-20 integration requirement {term}")
        if "stronger privacy and authority controls" not in lower_text:
            errors.append(f"{name}: missing AI-20 stronger privacy and authority controls gate")
        for term in ("eligibility", "adverse action", "criminal guilt", "legal liability"):
            if term not in lower_text:
                errors.append(f"{name}: missing AI-20 prohibited outcome term {term}")
    if expected_package["family"] == AI21_FAMILY:
        lower_text = text.lower()
        for step in AI21_LIFECYCLE_STEPS:
            if step not in lower_text:
                errors.append(f"{name}: missing AI-21 lifecycle step {step}")
        for target in AI21_COMPOSITION_TARGETS:
            if target not in lower_text:
                errors.append(f"{name}: missing AI-21 composition target {target}")
        for term in AI21_PROHIBITED_OPERATIONAL_CONTENT:
            if term not in lower_text:
                errors.append(f"{name}: missing AI-21 prohibited operational content {term}")
        if "supervisor" not in lower_text:
            errors.append(f"{name}: missing AI-21 supervisor escalation boundary")
    if expected_package["family"] in AI22_FAMILIES:
        lower_text = text.lower()
        for term in AI22_INCIDENT_CAPABILITIES:
            if term not in lower_text:
                errors.append(f"{name}: missing AI-22 incident capability {term}")
        for term in AI22_COMMUNICATION_CAPABILITIES:
            if term not in lower_text:
                errors.append(f"{name}: missing AI-22 communication capability {term}")
        for term in AI22_PROHIBITED_PHYSICAL_INTERVENTION:
            if term not in lower_text:
                errors.append(f"{name}: missing AI-22 physical intervention boundary term {term}")
        if AI22_CERTIFICATION_BOUNDARY.lower() not in lower_text:
            errors.append(f"{name}: missing AI-22 certification boundary")
    if expected_package["family"] == AI23_FAMILY:
        lower_text = text.lower()
        for term in AI23_REASONING_CHAIN:
            if term not in lower_text:
                errors.append(f"{name}: missing AI-23 reasoning-chain term {term}")
        for term in AI23_COMPOSITION_TARGETS:
            if term not in lower_text:
                errors.append(f"{name}: missing AI-23 composition target {term}")
        for term in AI23_BOUNDARY_TERMS:
            if term not in lower_text:
                errors.append(f"{name}: missing AI-23 boundary term {term}")
        for term in AI23_PROHIBITED_SECURITY_DETAIL:
            if term not in lower_text:
                errors.append(f"{name}: missing AI-23 prohibited security detail {term}")
    if expected_package["family"] == AI24_FAMILY:
        lower_text = text.lower()
        for term in AI24_SYSTEM_ANALYSIS_CAPABILITIES:
            if term not in lower_text:
                errors.append(f"{name}: missing AI-24 system-analysis capability {term}")
        for term in AI24_EXPLICIT_PROHIBITIONS:
            if term not in lower_text:
                errors.append(f"{name}: missing AI-24 explicit prohibition {term}")
        for term in AI24_QUALIFIED_BOUNDARIES:
            if term not in lower_text:
                errors.append(f"{name}: missing AI-24 qualified boundary {term}")
        if expected_package["sensitivity"] == "INTRUSIVE" and "INTRUSIVE_GATE_REQUIRED" not in text:
            errors.append(f"{name}: missing AI-24 intrusive routing gate")
        if expected_package["sensitivity"] == "CERTIFICATION_BOUNDARY":
            if "CERTIFICATION_ESCALATION" not in text:
                errors.append(f"{name}: missing AI-24 certification escalation routing gate")
            if "qualified review" not in lower_text:
                errors.append(f"{name}: missing AI-24 qualified review boundary")
    if "Output Contract" not in text:
        errors.append(f"{name}: missing output contract")
    if "PROHIBITED_REDIRECT" not in text and "prohibited" not in text.lower():
        errors.append(f"{name}: missing prohibited routing boundary")

    for dependency in taxonomy_row.get("dependencies", []):
        expected = f"Canonical taxonomy dependency: `{dependency}`"
        if expected not in text:
            errors.append(f"{name}: missing dependency check for {dependency}")

    if agents_yaml.is_file():
        metadata = agents_yaml.read_text(encoding="utf-8-sig")
        for phrase in ("display_name:", "short_description:", "default_prompt:", "allow_implicit_invocation: true"):
            if phrase not in metadata:
                errors.append(f"{name}: agents/openai.yaml missing {phrase}")
        if f"${name}" not in metadata:
            errors.append(f"{name}: default_prompt must mention ${name}")

    if reference_path.is_file():
        reference = reference_path.read_text(encoding="utf-8-sig")
        if "When To Read" not in reference:
            errors.append(f"{name}: reference file must include When To Read")


def validate_scenario_suite(
    repo_root: Path,
    suite: dict[str, Any],
    errors: list[str],
) -> None:
    relative_path = suite["relative_path"]
    path = repo_root / relative_path
    label = suite["label"]
    expected_skills = suite["skills"]
    skill_list_key = suite["skill_list_key"]

    if not path.is_file():
        errors.append(f"Missing scenario fixture: {relative_path}")
        return

    try:
        data = load_json(path)
    except json.JSONDecodeError as exc:
        errors.append(f"{label}: invalid JSON: {exc}")
        return

    if data.get("completion_token") != suite["token"]:
        errors.append(f"{label}: missing completion token")
    if set(data.get(skill_list_key, [])) != set(expected_skills):
        errors.append(f"{label}: {skill_list_key} mismatch")
    expected_critical_tests = suite.get("critical_integration_tests")
    if expected_critical_tests is not None:
        if set(data.get("critical_integration_tests", [])) != set(expected_critical_tests):
            errors.append(f"{label}: critical_integration_tests mismatch")
    expected_scenario_topics = suite.get("scenario_topics")
    if expected_scenario_topics is not None:
        if set(data.get("scenario_topics", [])) != set(expected_scenario_topics):
            errors.append(f"{label}: scenario_topics mismatch")
    expected_research_topics = suite.get("research_topics")
    if expected_research_topics is not None:
        if set(data.get("research_topics", [])) != set(expected_research_topics):
            errors.append(f"{label}: research_topics mismatch")
    expected_hard_boundary_tests = suite.get("hard_boundary_tests")
    if expected_hard_boundary_tests is not None:
        if set(data.get("hard_boundary_tests", [])) != set(expected_hard_boundary_tests):
            errors.append(f"{label}: hard_boundary_tests mismatch")
    expected_required_capabilities = suite.get("required_capabilities")
    if expected_required_capabilities is not None:
        if set(data.get("required_capabilities", [])) != set(expected_required_capabilities):
            errors.append(f"{label}: required_capabilities mismatch")
    expected_confidence_model = suite.get("confidence_model")
    if expected_confidence_model is not None:
        if set(data.get("confidence_model", [])) != set(expected_confidence_model):
            errors.append(f"{label}: confidence_model mismatch")
    expected_required_emphasis = suite.get("required_emphasis")
    if expected_required_emphasis is not None:
        if set(data.get("required_emphasis", [])) != set(expected_required_emphasis):
            errors.append(f"{label}: required_emphasis mismatch")
    expected_prohibited_inference = suite.get("prohibited_inference")
    if expected_prohibited_inference is not None:
        if set(data.get("prohibited_inference", [])) != set(expected_prohibited_inference):
            errors.append(f"{label}: prohibited_inference mismatch")
    expected_continuity_elements = suite.get("continuity_elements")
    if expected_continuity_elements is not None:
        if set(data.get("continuity_elements", [])) != set(expected_continuity_elements):
            errors.append(f"{label}: continuity_elements mismatch")
    expected_reasoning_rule = suite.get("reasoning_rule")
    if expected_reasoning_rule is not None and data.get("reasoning_rule") != expected_reasoning_rule:
        errors.append(f"{label}: reasoning_rule mismatch")
    expected_reasoning_categories = suite.get("reasoning_categories")
    if expected_reasoning_categories is not None:
        if set(data.get("reasoning_categories", [])) != set(expected_reasoning_categories):
            errors.append(f"{label}: reasoning_categories mismatch")
    expected_required_outputs = suite.get("required_outputs")
    if expected_required_outputs is not None:
        if set(data.get("required_outputs", [])) != set(expected_required_outputs):
            errors.append(f"{label}: required_outputs mismatch")
    expected_required_report_fields = suite.get("required_report_fields")
    if expected_required_report_fields is not None:
        if set(data.get("required_report_fields", [])) != set(expected_required_report_fields):
            errors.append(f"{label}: required_report_fields mismatch")
    expected_mandatory_properties = suite.get("mandatory_properties")
    if expected_mandatory_properties is not None:
        if data.get("mandatory_properties") != expected_mandatory_properties:
            errors.append(f"{label}: mandatory_properties mismatch")
    expected_prohibited_operational_skills = suite.get("prohibited_operational_skills")
    if expected_prohibited_operational_skills is not None:
        if set(data.get("prohibited_operational_skills", [])) != set(expected_prohibited_operational_skills):
            errors.append(f"{label}: prohibited_operational_skills mismatch")
    expected_workflow_steps = suite.get("workflow_steps")
    if expected_workflow_steps is not None:
        if set(data.get("workflow_steps", [])) != set(expected_workflow_steps):
            errors.append(f"{label}: workflow_steps mismatch")
    expected_prohibited_decisions = suite.get("prohibited_decisions")
    if expected_prohibited_decisions is not None:
        if set(data.get("prohibited_decisions", [])) != set(expected_prohibited_decisions):
            errors.append(f"{label}: prohibited_decisions mismatch")
    expected_required_split = suite.get("required_split")
    if expected_required_split is not None:
        if set(data.get("required_split", [])) != set(expected_required_split):
            errors.append(f"{label}: required_split mismatch")
    expected_integration_requirements = suite.get("integration_requirements")
    if expected_integration_requirements is not None:
        if set(data.get("integration_requirements", [])) != set(expected_integration_requirements):
            errors.append(f"{label}: integration_requirements mismatch")
    expected_lifecycle_steps = suite.get("lifecycle_steps")
    if expected_lifecycle_steps is not None:
        if set(data.get("lifecycle_steps", [])) != set(expected_lifecycle_steps):
            errors.append(f"{label}: lifecycle_steps mismatch")
    expected_composition_targets = suite.get("composition_targets")
    if expected_composition_targets is not None:
        if set(data.get("composition_targets", [])) != set(expected_composition_targets):
            errors.append(f"{label}: composition_targets mismatch")
    expected_prohibited_operational_content = suite.get("prohibited_operational_content")
    if expected_prohibited_operational_content is not None:
        if set(data.get("prohibited_operational_content", [])) != set(expected_prohibited_operational_content):
            errors.append(f"{label}: prohibited_operational_content mismatch")
    expected_families = suite.get("families")
    if expected_families is not None:
        if set(data.get("families", [])) != set(expected_families):
            errors.append(f"{label}: families mismatch")
    expected_incident_capabilities = suite.get("incident_capabilities")
    if expected_incident_capabilities is not None:
        if set(data.get("incident_capabilities", [])) != set(expected_incident_capabilities):
            errors.append(f"{label}: incident_capabilities mismatch")
    expected_communication_capabilities = suite.get("communication_capabilities")
    if expected_communication_capabilities is not None:
        if set(data.get("communication_capabilities", [])) != set(expected_communication_capabilities):
            errors.append(f"{label}: communication_capabilities mismatch")
    expected_certification_boundary = suite.get("certification_boundary")
    if expected_certification_boundary is not None:
        if data.get("certification_boundary") != expected_certification_boundary:
            errors.append(f"{label}: certification_boundary mismatch")
    expected_prohibited_physical_intervention = suite.get("prohibited_physical_intervention")
    if expected_prohibited_physical_intervention is not None:
        if set(data.get("prohibited_physical_intervention", [])) != set(expected_prohibited_physical_intervention):
            errors.append(f"{label}: prohibited_physical_intervention mismatch")
    expected_reasoning_chain = suite.get("reasoning_chain")
    if expected_reasoning_chain is not None:
        if set(data.get("reasoning_chain", [])) != set(expected_reasoning_chain):
            errors.append(f"{label}: reasoning_chain mismatch")
    expected_boundary_terms = suite.get("boundary_terms")
    if expected_boundary_terms is not None:
        if set(data.get("boundary_terms", [])) != set(expected_boundary_terms):
            errors.append(f"{label}: boundary_terms mismatch")
    expected_prohibited_security_detail = suite.get("prohibited_security_detail")
    if expected_prohibited_security_detail is not None:
        if set(data.get("prohibited_security_detail", [])) != set(expected_prohibited_security_detail):
            errors.append(f"{label}: prohibited_security_detail mismatch")
    expected_system_analysis_capabilities = suite.get("system_analysis_capabilities")
    if expected_system_analysis_capabilities is not None:
        if set(data.get("system_analysis_capabilities", [])) != set(expected_system_analysis_capabilities):
            errors.append(f"{label}: system_analysis_capabilities mismatch")
    expected_explicit_prohibitions = suite.get("explicit_prohibitions")
    if expected_explicit_prohibitions is not None:
        if set(data.get("explicit_prohibitions", [])) != set(expected_explicit_prohibitions):
            errors.append(f"{label}: explicit_prohibitions mismatch")
    expected_qualified_boundaries = suite.get("qualified_boundaries")
    if expected_qualified_boundaries is not None:
        if set(data.get("qualified_boundaries", [])) != set(expected_qualified_boundaries):
            errors.append(f"{label}: qualified_boundaries mismatch")
    expected_gate = suite.get("gate")
    if expected_gate is not None and data.get("gate") != expected_gate:
        errors.append(f"{label}: gate mismatch")

    scenarios = data.get("scenarios")
    if not isinstance(scenarios, list):
        errors.append(f"{label}: scenarios must be a list")
        return

    coverage: dict[str, set[str]] = defaultdict(set)
    scenario_ids: set[str] = set()
    has_identity_overclaiming = False
    has_prohibited_inference = False
    has_representative_continuity = False
    has_plausible_incorrect_hypothesis = False
    has_disconfirming_evidence = False
    has_report_field_coverage = False
    has_testimony_boundary = False
    has_mandatory_properties = False
    observed_prohibited_operational_skills: set[str] = set()
    has_workplace_flow = False
    has_prohibited_workplace_decision = False
    has_person_screening_split = False
    has_entity_due_diligence_split = False
    has_stronger_privacy_authority_controls = False
    observed_ai20_integration_requirements: set[str] = set()
    has_security_operations_lifecycle = False
    observed_ai21_lifecycle_steps: set[str] = set()
    has_composition_target = False
    observed_ai21_composition_targets: set[str] = set()
    observed_ai21_prohibited_operational_content: set[str] = set()
    has_incident_capabilities = False
    observed_ai22_incident_capabilities: set[str] = set()
    has_communication_capabilities = False
    observed_ai22_communication_capabilities: set[str] = set()
    observed_ai22_prohibited_physical_intervention: set[str] = set()
    has_ai23_reasoning_chain = False
    observed_ai23_reasoning_chain: set[str] = set()
    has_ai23_composition_target = False
    observed_ai23_composition_targets: set[str] = set()
    observed_ai23_boundary_terms: set[str] = set()
    observed_ai23_prohibited_security_detail: set[str] = set()
    has_ai24_system_analysis_capabilities = False
    observed_ai24_system_analysis_capabilities: set[str] = set()
    has_ai24_explicit_prohibition = False
    observed_ai24_explicit_prohibitions: set[str] = set()
    for scenario in scenarios:
        if not isinstance(scenario, dict):
            errors.append(f"{label}: scenario must be an object")
            continue
        scenario_id = str(scenario.get("id", "<missing id>"))
        if scenario_id in scenario_ids:
            errors.append(f"{label}: duplicate scenario id {scenario_id}")
        scenario_ids.add(scenario_id)
        missing = SCENARIO_FIELDS - set(scenario)
        for field in sorted(missing):
            errors.append(f"{scenario_id}: missing field {field}")
        skill = scenario.get("skill_under_test")
        if skill not in expected_skills:
            errors.append(f"{scenario_id}: unknown skill_under_test {skill}")
        test_type = scenario.get("test_type")
        if test_type not in VALID_TEST_TYPES:
            errors.append(f"{scenario_id}: invalid test_type {test_type}")
        if scenario.get("expected_routing_state") not in VALID_ROUTING_STATES:
            errors.append(f"{scenario_id}: invalid expected_routing_state {scenario.get('expected_routing_state')}")
        for field in ("test_classes", "required_checks", "blocked_outputs"):
            if not isinstance(scenario.get(field), list) or not scenario.get(field):
                errors.append(f"{scenario_id}: {field} must be a non-empty list")
        if "identity overclaiming" in scenario.get("test_classes", []):
            has_identity_overclaiming = True
        if "prohibited inference" in scenario.get("test_classes", []):
            has_prohibited_inference = True
        if "representative continuity test" in scenario.get("test_classes", []):
            has_representative_continuity = True
            scenario_text = " ".join(
                str(scenario.get(field, ""))
                for field in ("prompt", "required_checks", "blocked_outputs")
            )
            for element in AI15_CONTINUITY_ELEMENTS:
                if element not in scenario_text:
                    errors.append(f"{scenario_id}: missing representative continuity element {element}")
            if "admissibility" not in scenario_text:
                errors.append(f"{scenario_id}: missing admissibility boundary")
        if "plausible incorrect hypothesis" in scenario.get("test_classes", []):
            has_plausible_incorrect_hypothesis = True
            scenario_text = " ".join(
                str(scenario.get(field, ""))
                for field in ("prompt", "required_checks", "blocked_outputs")
            )
            if "disconfirming evidence" not in scenario_text:
                errors.append(f"{scenario_id}: missing disconfirming evidence")
            for category in AI16_REASONING_CATEGORIES:
                if category.lower() not in scenario_text.lower():
                    errors.append(f"{scenario_id}: missing reasoning category {category}")
        if "disconfirming evidence" in scenario.get("test_classes", []):
            has_disconfirming_evidence = True
        if "report field coverage" in scenario.get("test_classes", []):
            has_report_field_coverage = True
            scenario_text = " ".join(
                str(scenario.get(field, ""))
                for field in ("prompt", "required_checks", "blocked_outputs")
            ).lower()
            for report_field in AI17_REQUIRED_REPORT_FIELDS:
                if report_field not in scenario_text:
                    errors.append(f"{scenario_id}: missing report field {report_field}")
        if "testimony boundary" in scenario.get("test_classes", []):
            has_testimony_boundary = True
        if "mandatory properties" in scenario.get("test_classes", []):
            has_mandatory_properties = True
            scenario_text = " ".join(
                str(scenario.get(field, ""))
                for field in ("prompt", "required_checks", "blocked_outputs")
            ).lower()
            for term in ("sensitivity: intrusive", "jurisdiction_required: true", "human_review_required: true"):
                if term not in scenario_text:
                    errors.append(f"{scenario_id}: missing mandatory property {term}")
        if "prohibited operational skill" in scenario.get("test_classes", []):
            for term in AI18_PROHIBITED_OPERATIONAL_SKILLS:
                if term in scenario.get("test_classes", []):
                    observed_prohibited_operational_skills.add(term)
        if "end-to-end workplace flow" in scenario.get("test_classes", []):
            has_workplace_flow = True
            scenario_text = " ".join(
                str(scenario.get(field, ""))
                for field in ("prompt", "required_checks", "blocked_outputs")
            ).lower()
            for step in AI19_WORKFLOW_STEPS:
                if step not in scenario_text:
                    errors.append(f"{scenario_id}: missing workplace workflow step {step}")
            for decision in AI19_PROHIBITED_DECISIONS:
                if decision not in scenario_text:
                    errors.append(f"{scenario_id}: missing prohibited workplace decision {decision}")
        if "prohibited decision" in scenario.get("test_classes", []):
            has_prohibited_workplace_decision = True
        if "person screening split" in scenario.get("test_classes", []):
            has_person_screening_split = True
        if "entity due diligence split" in scenario.get("test_classes", []):
            has_entity_due_diligence_split = True
        if "stronger privacy authority controls" in scenario.get("test_classes", []):
            has_stronger_privacy_authority_controls = True
        for term in AI20_INTEGRATION_REQUIREMENTS:
            if term in scenario.get("test_classes", []):
                observed_ai20_integration_requirements.add(term)
        if "security operations lifecycle" in scenario.get("test_classes", []):
            has_security_operations_lifecycle = True
            scenario_text = " ".join(
                str(scenario.get(field, ""))
                for field in ("prompt", "required_checks", "blocked_outputs")
            ).lower()
            for step in AI21_LIFECYCLE_STEPS:
                if step not in scenario_text:
                    errors.append(f"{scenario_id}: missing AI-21 lifecycle step {step}")
        for step in AI21_LIFECYCLE_STEPS:
            if step in scenario.get("test_classes", []):
                observed_ai21_lifecycle_steps.add(step)
        if "composition target" in scenario.get("test_classes", []):
            has_composition_target = True
        for target in AI21_COMPOSITION_TARGETS:
            if target in scenario.get("test_classes", []):
                observed_ai21_composition_targets.add(target)
        for term in AI21_PROHIBITED_OPERATIONAL_CONTENT:
            if term in scenario.get("test_classes", []):
                observed_ai21_prohibited_operational_content.add(term)
        if "incident capabilities" in scenario.get("test_classes", []):
            has_incident_capabilities = True
        for term in AI22_INCIDENT_CAPABILITIES:
            if term in scenario.get("test_classes", []):
                observed_ai22_incident_capabilities.add(term)
        if "communication capabilities" in scenario.get("test_classes", []):
            has_communication_capabilities = True
        for term in AI22_COMMUNICATION_CAPABILITIES:
            if term in scenario.get("test_classes", []):
                observed_ai22_communication_capabilities.add(term)
        for term in AI22_PROHIBITED_PHYSICAL_INTERVENTION:
            if term in scenario.get("test_classes", []):
                observed_ai22_prohibited_physical_intervention.add(term)
        if "required reasoning chain" in scenario.get("test_classes", []):
            has_ai23_reasoning_chain = True
            scenario_text = " ".join(
                str(scenario.get(field, ""))
                for field in ("prompt", "required_checks", "blocked_outputs")
            ).lower()
            for term in AI23_REASONING_CHAIN:
                if term not in scenario_text:
                    errors.append(f"{scenario_id}: missing AI-23 reasoning-chain term {term}")
        for term in AI23_REASONING_CHAIN:
            if term in scenario.get("test_classes", []):
                observed_ai23_reasoning_chain.add(term)
        if "composition target" in scenario.get("test_classes", []):
            has_ai23_composition_target = True
        for term in AI23_COMPOSITION_TARGETS:
            if term in scenario.get("test_classes", []):
                observed_ai23_composition_targets.add(term)
        for term in AI23_BOUNDARY_TERMS:
            if term in scenario.get("test_classes", []):
                observed_ai23_boundary_terms.add(term)
        for term in AI23_PROHIBITED_SECURITY_DETAIL:
            if term in scenario.get("test_classes", []):
                observed_ai23_prohibited_security_detail.add(term)
        if "system analysis capabilities" in scenario.get("test_classes", []):
            has_ai24_system_analysis_capabilities = True
            scenario_text = " ".join(
                str(scenario.get(field, ""))
                for field in ("prompt", "required_checks", "blocked_outputs")
            ).lower()
            for term in AI24_SYSTEM_ANALYSIS_CAPABILITIES:
                if term not in scenario_text:
                    errors.append(f"{scenario_id}: missing AI-24 system-analysis capability {term}")
        for term in AI24_SYSTEM_ANALYSIS_CAPABILITIES:
            if term in scenario.get("test_classes", []):
                observed_ai24_system_analysis_capabilities.add(term)
        if "explicit prohibition" in scenario.get("test_classes", []):
            has_ai24_explicit_prohibition = True
        for term in AI24_EXPLICIT_PROHIBITIONS:
            if term in scenario.get("test_classes", []):
                observed_ai24_explicit_prohibitions.add(term)
        if skill in expected_skills and test_type in VALID_TEST_TYPES:
            coverage[str(skill)].add(str(test_type))

    for skill in expected_skills:
        if coverage[skill] != VALID_TEST_TYPES:
            errors.append(f"{skill}: must have positive and negative-routing scenarios in {label}")
    if suite.get("gate") == "Tests must detect and penalize identity overclaiming." and not has_identity_overclaiming:
        errors.append(f"{label}: missing identity overclaiming scenario coverage")
    if suite.get("prohibited_inference") is not None and not has_prohibited_inference:
        errors.append(f"{label}: missing prohibited inference scenario coverage")
    if suite.get("gate") == AI15_GATE and not has_representative_continuity:
        errors.append(f"{label}: missing representative continuity scenario coverage")
    if suite.get("gate") == AI16_GATE:
        if not has_plausible_incorrect_hypothesis:
            errors.append(f"{label}: missing plausible incorrect hypothesis scenario coverage")
        if not has_disconfirming_evidence:
            errors.append(f"{label}: missing disconfirming evidence scenario coverage")
    if suite.get("gate") == AI17_GATE:
        if not has_report_field_coverage:
            errors.append(f"{label}: missing report field coverage scenario")
        if not has_testimony_boundary:
            errors.append(f"{label}: missing testimony boundary scenario")
    if suite.get("gate") == AI18_GATE:
        if not has_mandatory_properties:
            errors.append(f"{label}: missing mandatory properties scenario")
        if observed_prohibited_operational_skills != AI18_PROHIBITED_OPERATIONAL_SKILLS:
            errors.append(f"{label}: prohibited operational skill coverage mismatch")
    if suite.get("gate") == AI19_GATE:
        if not has_workplace_flow:
            errors.append(f"{label}: missing end-to-end workplace flow scenario")
        if not has_prohibited_workplace_decision:
            errors.append(f"{label}: missing prohibited workplace decision scenario coverage")
    if suite.get("gate") == AI20_GATE:
        if not has_person_screening_split:
            errors.append(f"{label}: missing PERSON SCREENING split scenario")
        if not has_entity_due_diligence_split:
            errors.append(f"{label}: missing ENTITY DUE DILIGENCE split scenario")
        if not has_stronger_privacy_authority_controls:
            errors.append(f"{label}: missing stronger privacy and authority controls scenario")
        if observed_ai20_integration_requirements != AI20_INTEGRATION_REQUIREMENTS:
            errors.append(f"{label}: AI-20 integration requirement coverage mismatch")
    if suite.get("gate") == AI21_GATE:
        if not has_security_operations_lifecycle:
            errors.append(f"{label}: missing security operations lifecycle scenario")
        if observed_ai21_lifecycle_steps != AI21_LIFECYCLE_STEPS:
            errors.append(f"{label}: AI-21 lifecycle coverage mismatch")
        if not has_composition_target:
            errors.append(f"{label}: missing composition target scenario")
        if observed_ai21_composition_targets != AI21_COMPOSITION_TARGETS:
            errors.append(f"{label}: AI-21 composition target coverage mismatch")
        if observed_ai21_prohibited_operational_content != AI21_PROHIBITED_OPERATIONAL_CONTENT:
            errors.append(f"{label}: AI-21 prohibited operational content coverage mismatch")
    if suite.get("gate") == AI22_GATE:
        if not has_incident_capabilities:
            errors.append(f"{label}: missing incident capabilities scenario")
        if observed_ai22_incident_capabilities != AI22_INCIDENT_CAPABILITIES:
            errors.append(f"{label}: AI-22 incident capability coverage mismatch")
        if not has_communication_capabilities:
            errors.append(f"{label}: missing communication capabilities scenario")
        if observed_ai22_communication_capabilities != AI22_COMMUNICATION_CAPABILITIES:
            errors.append(f"{label}: AI-22 communication capability coverage mismatch")
        if observed_ai22_prohibited_physical_intervention != AI22_PROHIBITED_PHYSICAL_INTERVENTION:
            errors.append(f"{label}: AI-22 physical intervention boundary coverage mismatch")
    if suite.get("gate") == AI23_GATE:
        if not has_ai23_reasoning_chain:
            errors.append(f"{label}: missing required reasoning chain scenario")
        if observed_ai23_reasoning_chain != AI23_REASONING_CHAIN:
            errors.append(f"{label}: AI-23 reasoning-chain coverage mismatch")
        if not has_ai23_composition_target:
            errors.append(f"{label}: missing composition target scenario")
        if observed_ai23_composition_targets != AI23_COMPOSITION_TARGETS:
            errors.append(f"{label}: AI-23 composition target coverage mismatch")
        if observed_ai23_boundary_terms != AI23_BOUNDARY_TERMS:
            errors.append(f"{label}: AI-23 boundary term coverage mismatch")
        if observed_ai23_prohibited_security_detail != AI23_PROHIBITED_SECURITY_DETAIL:
            errors.append(f"{label}: AI-23 prohibited security detail coverage mismatch")
    if suite.get("gate") == AI24_GATE:
        if not has_ai24_system_analysis_capabilities:
            errors.append(f"{label}: missing system analysis capabilities scenario")
        if observed_ai24_system_analysis_capabilities != AI24_SYSTEM_ANALYSIS_CAPABILITIES:
            errors.append(f"{label}: AI-24 system-analysis capability coverage mismatch")
        if not has_ai24_explicit_prohibition:
            errors.append(f"{label}: missing explicit prohibition scenario")
        if observed_ai24_explicit_prohibitions != AI24_EXPLICIT_PROHIBITIONS:
            errors.append(f"{label}: AI-24 explicit prohibition coverage mismatch")


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    taxonomy_by_name = taxonomy(repo_root)
    ai10_skills = authority_compliance_skills(taxonomy_by_name)
    ai11_skills = case_management_skills(taxonomy_by_name)
    ai12_skills = research_osint_skills(taxonomy_by_name)
    ai13_skills = entity_analysis_skills(taxonomy_by_name)
    ai14_skills = interviewing_skills(taxonomy_by_name)
    ai15_skills = evidence_skills(taxonomy_by_name)
    ai16_skills = investigative_analysis_skills(taxonomy_by_name)
    ai17_skills = reporting_skills(taxonomy_by_name)
    ai18_skills = observation_governance_skills(taxonomy_by_name)
    ai19_skills = workplace_investigation_skills(taxonomy_by_name)
    ai20_skills = screening_due_diligence_skills(taxonomy_by_name)
    ai21_skills = security_operations_skills(taxonomy_by_name)
    ai22_skills = incident_communication_skills(taxonomy_by_name)
    ai23_skills = physical_security_skills(taxonomy_by_name)
    ai24_skills = security_systems_skills(taxonomy_by_name)
    expected_skills = required_skills(taxonomy_by_name)
    for name in expected_skills:
        validate_skill_package(repo_root, name, expected_skills, taxonomy_by_name, errors)
    for suite in scenario_suites(
        ai10_skills,
        ai11_skills,
        ai12_skills,
        ai13_skills,
        ai14_skills,
        ai15_skills,
        ai16_skills,
        ai17_skills,
        ai18_skills,
        ai19_skills,
        ai20_skills,
        ai21_skills,
        ai22_skills,
        ai23_skills,
        ai24_skills,
    ):
        validate_scenario_suite(repo_root, suite, errors)
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

    print("Validated AgentInvestigate AI-08 reference through AI-24 security systems skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
