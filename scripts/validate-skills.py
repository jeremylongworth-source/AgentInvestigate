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

    print("Validated AgentInvestigate AI-08 reference through AI-17 reporting skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
