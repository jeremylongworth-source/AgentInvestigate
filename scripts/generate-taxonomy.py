from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


TOKEN = "AGENTINVESTIGATE_AI_02_MASTER_TAXONOMY_READY"

FAMILIES = [
    ("01-professional-core-ethics", "Professional Core & Ethics", "Shared"),
    ("02-case-intake-scope-authority", "Case Intake, Scope & Authority", "Shared"),
    ("03-law-licensing-privacy-compliance", "Law, Licensing, Privacy & Compliance", "Shared"),
    ("04-investigation-planning-case-management", "Investigation Planning & Case Management", "Private Investigation"),
    ("05-research-osint-public-records", "Research, OSINT & Public Records", "Private Investigation"),
    ("06-identity-entity-timeline-analysis", "Identity, Entity & Timeline Analysis", "Private Investigation"),
    ("07-interviewing-witnesses-statements", "Interviewing, Witnesses & Statements", "Private Investigation"),
    ("08-evidence-chain-of-custody", "Evidence & Chain of Custody", "Shared"),
    ("09-investigative-analysis", "Investigative Analysis", "Private Investigation"),
    ("10-observation-surveillance-governance", "Observation & Surveillance Governance", "Private Investigation"),
    ("11-reporting-findings-case-presentation", "Reporting, Findings & Case Presentation", "Shared"),
    ("12-corporate-workplace-investigations", "Corporate & Workplace Investigations", "Private Investigation"),
    ("13-background-screening-due-diligence", "Background Screening & Due Diligence", "Private Investigation"),
    ("14-security-operations-access-patrol", "Security Operations, Access & Patrol", "Private Security"),
    ("15-incident-response", "Incident Response", "Private Security"),
    ("16-communication-deescalation", "Communication & De-escalation", "Private Security"),
    ("17-physical-security-risk-assessment", "Physical Security & Risk Assessment", "Private Security"),
    ("18-security-systems-technology", "Security Systems & Technology", "Private Security"),
    ("19-loss-prevention-asset-protection", "Loss Prevention & Asset Protection", "Hybrid"),
    ("20-investigation-security-program-management", "Investigation & Security Program Management", "Shared"),
]

FAMILY_LOOKUP = {slug: {"name": name, "branch": branch} for slug, name, branch in FAMILIES}

SKILLSET_DEFAULTS = {
    "Shared": ["private-investigator", "security-officer", "investigative-case-manager", "security-program-manager"],
    "Private Investigation": ["private-investigator", "investigative-analyst", "investigative-case-manager"],
    "Private Security": ["security-officer", "security-supervisor", "security-program-manager"],
    "Hybrid": ["loss-prevention-investigator", "asset-protection-specialist", "corporate-security-investigator"],
}


def entry(
    name: str,
    family: str,
    tier: str,
    sensitivity: str,
    priority: str,
    dependencies: list[str] | None = None,
    jurisdiction: str | None = None,
    authority: str | None = None,
    freshness: str | None = None,
    skillsets: list[str] | None = None,
) -> dict[str, object]:
    branch = FAMILY_LOOKUP[family]["branch"]
    if jurisdiction is None:
        jurisdiction = {
            "ROUTINE": "contextual",
            "REGULATED": "required",
            "INTRUSIVE": "required",
            "CERTIFICATION_BOUNDARY": "required_when_operational_or_emergency_adjacent",
        }[sensitivity]
    if authority is None:
        authority = {
            "ROUTINE": "scope_required",
            "REGULATED": "authority_required",
            "INTRUSIVE": "human_approval_required",
            "CERTIFICATION_BOUNDARY": "qualified_review_or_escalation_required",
        }[sensitivity]
    if freshness is None:
        freshness = {
            "ROUTINE": "LOW",
            "REGULATED": "HIGH",
            "INTRUSIVE": "HIGH",
            "CERTIFICATION_BOUNDARY": "HIGH",
        }[sensitivity]
    return {
        "name": name,
        "family": family,
        "family_name": FAMILY_LOOKUP[family]["name"],
        "branch": branch,
        "tier": tier,
        "sensitivity": sensitivity,
        "jurisdiction_requirement": jurisdiction,
        "authority_requirement": authority,
        "freshness_requirement": freshness,
        "priority": priority,
        "dependencies": dependencies or [],
        "professional_skillsets": skillsets or SKILLSET_DEFAULTS[branch],
    }


def build_skills() -> list[dict[str, object]]:
    skills: list[dict[str, object]] = []
    add = skills.append

    f = "01-professional-core-ethics"
    for name, deps in [
        ("define-professional-role-boundaries", []),
        ("assess-conflict-of-interest", ["define-professional-role-boundaries"]),
        ("apply-ethical-decision-framework", ["define-professional-role-boundaries"]),
        ("identify-investigative-bias", ["apply-ethical-decision-framework"]),
        ("separate-fact-from-inference", []),
        ("assess-duty-of-care", ["define-professional-role-boundaries"]),
        ("protect-confidential-information", ["define-professional-role-boundaries"]),
        ("identify-escalation-requirement", ["assess-duty-of-care"]),
        ("document-professional-decision", ["separate-fact-from-inference"]),
    ]:
        add(entry(name, f, "FOUNDATION", "ROUTINE", "P0", deps))

    f = "02-case-intake-scope-authority"
    for name, deps, sens in [
        ("classify-request-type", [], "ROUTINE"),
        ("identify-client-role", ["classify-request-type"], "ROUTINE"),
        ("identify-jurisdiction", ["classify-request-type"], "REGULATED"),
        ("validate-investigative-authority", ["identify-client-role", "identify-jurisdiction"], "REGULATED"),
        ("validate-security-service-authority", ["identify-client-role", "identify-jurisdiction"], "REGULATED"),
        ("assess-lawful-purpose", ["identify-jurisdiction"], "REGULATED"),
        ("define-case-scope", ["assess-lawful-purpose"], "ROUTINE"),
        ("define-scope-boundaries", ["define-case-scope"], "ROUTINE"),
        ("identify-stakeholders-and-subjects", ["define-case-scope"], "ROUTINE"),
        ("assess-consent-requirement", ["identify-jurisdiction", "identify-stakeholders-and-subjects"], "REGULATED"),
        ("prepare-authority-check", ["validate-investigative-authority", "validate-security-service-authority"], "REGULATED"),
    ]:
        add(entry(name, f, "FOUNDATION", sens, "P0", deps))

    f = "03-law-licensing-privacy-compliance"
    for name, deps in [
        ("identify-licensing-requirement", ["identify-jurisdiction"]),
        ("identify-regulated-activity", ["classify-request-type", "identify-jurisdiction"]),
        ("identify-privacy-obligation", ["identify-jurisdiction", "identify-stakeholders-and-subjects"]),
        ("identify-recording-law-issue", ["identify-jurisdiction", "identify-privacy-obligation"]),
        ("assess-information-collection-basis", ["identify-privacy-obligation", "assess-lawful-purpose"]),
        ("assess-record-access-authority", ["identify-jurisdiction", "validate-investigative-authority"]),
        ("assess-data-minimization-requirement", ["identify-privacy-obligation"]),
        ("review-retention-obligation", ["identify-jurisdiction", "identify-privacy-obligation"]),
        ("identify-reporting-obligation", ["identify-jurisdiction", "identify-regulated-activity"]),
        ("review-training-requirements", ["identify-licensing-requirement"]),
        ("prepare-compliance-escalation", ["identify-regulated-activity"]),
    ]:
        add(entry(name, f, "FOUNDATION", "REGULATED", "P0", deps))

    f = "04-investigation-planning-case-management"
    for name, deps in [
        ("build-investigation-plan", ["define-case-scope", "prepare-authority-check"]),
        ("define-investigative-question", ["define-case-scope"]),
        ("create-case-timeline", ["build-investigation-plan"]),
        ("prioritize-investigative-leads", ["define-investigative-question"]),
        ("estimate-investigative-resources", ["build-investigation-plan"]),
        ("define-case-milestones", ["build-investigation-plan"]),
        ("maintain-case-action-log", ["build-investigation-plan"]),
        ("write-case-notes", ["maintain-case-action-log"]),
        ("prepare-case-status-update", ["maintain-case-action-log"]),
        ("review-case-retention-needs", ["review-retention-obligation"]),
        ("conduct-case-file-review", ["maintain-case-action-log"]),
        ("identify-case-gaps", ["conduct-case-file-review"]),
        ("prepare-case-closure-summary", ["identify-case-gaps"]),
    ]:
        add(entry(name, f, "CORE", "ROUTINE", "P1", deps))

    f = "05-research-osint-public-records"
    for name, deps, sens in [
        ("build-research-plan", ["define-investigative-question"], "ROUTINE"),
        ("identify-public-record-sources", ["identify-jurisdiction", "build-research-plan"], "REGULATED"),
        ("plan-open-source-research", ["build-research-plan"], "ROUTINE"),
        ("research-corporate-records", ["identify-public-record-sources"], "REGULATED"),
        ("research-court-records", ["identify-public-record-sources"], "REGULATED"),
        ("research-regulatory-records", ["identify-public-record-sources"], "REGULATED"),
        ("assess-source-reliability", ["build-research-plan"], "ROUTINE"),
        ("record-source-provenance", ["assess-source-reliability"], "ROUTINE"),
        ("corroborate-open-source-information", ["record-source-provenance"], "ROUTINE"),
        ("resolve-source-conflict", ["corroborate-open-source-information"], "ROUTINE"),
        ("research-organization-profile", ["plan-open-source-research"], "ROUTINE"),
        ("research-property-context", ["identify-public-record-sources"], "REGULATED"),
        ("research-litigation-history", ["research-court-records"], "REGULATED"),
        ("write-research-summary", ["resolve-source-conflict"], "ROUTINE"),
    ]:
        add(entry(name, f, "CORE", sens, "P1", deps))

    f = "06-identity-entity-timeline-analysis"
    for name, deps, sens in [
        ("assess-identity-ambiguity", ["record-source-provenance"], "INTRUSIVE"),
        ("differentiate-same-name-individuals", ["assess-identity-ambiguity"], "INTRUSIVE"),
        ("normalize-person-identifiers", ["assess-information-collection-basis"], "INTRUSIVE"),
        ("normalize-organization-identifiers", ["record-source-provenance"], "ROUTINE"),
        ("construct-subject-timeline", ["assess-identity-ambiguity"], "INTRUSIVE"),
        ("map-relationship-evidence", ["record-source-provenance"], "INTRUSIVE"),
        ("assess-association-strength", ["map-relationship-evidence"], "INTRUSIVE"),
        ("identify-timeline-gap", ["construct-subject-timeline"], "ROUTINE"),
        ("resolve-entity-contradiction", ["differentiate-same-name-individuals"], "INTRUSIVE"),
        ("state-identity-confidence", ["resolve-entity-contradiction"], "ROUTINE"),
    ]:
        add(entry(name, f, "CORE", sens, "P1", deps))

    f = "07-interviewing-witnesses-statements"
    for name, deps in [
        ("define-interview-objectives", ["define-investigative-question"]),
        ("prepare-neutral-question-set", ["define-interview-objectives"]),
        ("sequence-interview-topics", ["prepare-neutral-question-set"]),
        ("identify-interview-information-gaps", ["define-investigative-question"]),
        ("prepare-witness-interview-plan", ["sequence-interview-topics"]),
        ("summarize-witness-statement", ["write-case-notes"]),
        ("compare-statement-consistency", ["summarize-witness-statement"]),
        ("identify-corroboration-needs", ["compare-statement-consistency"]),
        ("prepare-follow-up-questions", ["identify-corroboration-needs"]),
        ("review-interview-bias-risk", ["identify-investigative-bias"]),
    ]:
        add(entry(name, f, "CORE", "ROUTINE", "P1", deps))

    f = "08-evidence-chain-of-custody"
    for name, deps, sens in [
        ("create-evidence-log", ["define-case-scope"], "ROUTINE"),
        ("classify-evidence-type", ["create-evidence-log"], "ROUTINE"),
        ("record-evidence-source", ["create-evidence-log"], "ROUTINE"),
        ("assess-evidence-relevance", ["classify-evidence-type"], "ROUTINE"),
        ("build-chain-of-custody-summary", ["create-evidence-log"], "ROUTINE"),
        ("identify-chain-of-custody-gap", ["build-chain-of-custody-summary"], "ROUTINE"),
        ("track-evidence-transfer", ["build-chain-of-custody-summary"], "ROUTINE"),
        ("compare-original-and-copy", ["classify-evidence-type"], "ROUTINE"),
        ("verify-evidence-timestamp", ["record-evidence-source"], "ROUTINE"),
        ("map-evidence-to-allegation", ["assess-evidence-relevance"], "ROUTINE"),
        ("identify-evidence-continuity-issue", ["identify-chain-of-custody-gap"], "ROUTINE"),
        ("prepare-evidence-handling-escalation", ["identify-evidence-continuity-issue"], "REGULATED"),
    ]:
        add(entry(name, f, "CORE", sens, "P1", deps))

    f = "09-investigative-analysis"
    for name, deps in [
        ("build-evidence-matrix", ["map-evidence-to-allegation"]),
        ("generate-investigative-hypotheses", ["build-evidence-matrix"]),
        ("test-investigative-hypothesis", ["generate-investigative-hypotheses"]),
        ("compare-alternative-explanations", ["test-investigative-hypothesis"]),
        ("identify-evidence-contradiction", ["build-evidence-matrix"]),
        ("construct-event-chronology", ["create-case-timeline"]),
        ("analyze-pattern-of-events", ["construct-event-chronology"]),
        ("assess-source-weight", ["assess-source-reliability"]),
        ("assess-finding-confidence", ["compare-alternative-explanations"]),
        ("identify-unresolved-question", ["assess-finding-confidence"]),
        ("draft-investigative-finding", ["assess-finding-confidence"]),
    ]:
        add(entry(name, f, "CORE", "ROUTINE", "P1", deps))

    f = "10-observation-surveillance-governance"
    for name, deps in [
        ("assess-observation-authorization", ["validate-investigative-authority", "identify-jurisdiction"]),
        ("assess-observation-necessity", ["assess-observation-authorization"]),
        ("assess-observation-proportionality", ["assess-observation-necessity"]),
        ("define-observation-purpose", ["assess-observation-proportionality"]),
        ("plan-lawful-observation-assignment", ["define-observation-purpose"]),
        ("record-field-observation", ["plan-lawful-observation-assignment"]),
        ("minimize-third-party-information", ["record-field-observation"]),
        ("review-observation-record-for-compliance", ["minimize-third-party-information"]),
    ]:
        add(entry(name, f, "ADVANCED", "INTRUSIVE", "P2", deps))

    f = "11-reporting-findings-case-presentation"
    for name, deps, sens in [
        ("write-investigative-report", ["draft-investigative-finding"], "ROUTINE"),
        ("write-incident-report", ["document-incident-timeline"], "ROUTINE"),
        ("prepare-case-chronology", ["construct-event-chronology"], "ROUTINE"),
        ("summarize-evidence", ["build-evidence-matrix"], "ROUTINE"),
        ("prepare-findings-matrix", ["draft-investigative-finding"], "ROUTINE"),
        ("write-executive-summary", ["prepare-findings-matrix"], "ROUTINE"),
        ("review-report-quality", ["write-investigative-report"], "ROUTINE"),
        ("prepare-case-presentation", ["review-report-quality"], "ROUTINE"),
        ("prepare-testimony-support-outline", ["prepare-case-presentation"], "REGULATED"),
        ("identify-report-limitations", ["review-report-quality"], "ROUTINE"),
    ]:
        add(entry(name, f, "CORE", sens, "P1", deps))

    f = "12-corporate-workplace-investigations"
    for name, deps, sens in [
        ("classify-workplace-allegation", ["classify-request-type"], "REGULATED"),
        ("map-allegation-to-policy", ["classify-workplace-allegation"], "ROUTINE"),
        ("build-allegations-matrix", ["map-allegation-to-policy"], "ROUTINE"),
        ("plan-workplace-investigation", ["build-allegations-matrix", "prepare-authority-check"], "REGULATED"),
        ("identify-workplace-evidence-sources", ["plan-workplace-investigation"], "INTRUSIVE"),
        ("prepare-workplace-interview-plan", ["prepare-witness-interview-plan"], "ROUTINE"),
        ("compare-workplace-statements", ["compare-statement-consistency"], "ROUTINE"),
        ("assess-evidentiary-support", ["build-evidence-matrix"], "ROUTINE"),
        ("draft-workplace-finding", ["assess-evidentiary-support"], "ROUTINE"),
        ("prepare-workplace-investigation-report", ["draft-workplace-finding"], "ROUTINE"),
    ]:
        add(entry(name, f, "ADVANCED", sens, "P2", deps, skillsets=["workplace-investigator", "corporate-investigator", "investigative-case-manager"]))

    f = "13-background-screening-due-diligence"
    for name, deps in [
        ("define-screening-purpose", ["classify-request-type"]),
        ("assess-background-screening-authority", ["define-screening-purpose", "identify-jurisdiction"]),
        ("verify-screening-consent", ["assess-background-screening-authority"]),
        ("select-screening-source-type", ["verify-screening-consent"]),
        ("assess-screening-source-reliability", ["select-screening-source-type"]),
        ("evaluate-record-relevance", ["assess-screening-source-reliability"]),
        ("identify-screening-identity-ambiguity", ["assess-identity-ambiguity"]),
        ("resolve-screening-discrepancy", ["identify-screening-identity-ambiguity"]),
        ("prepare-due-diligence-summary", ["resolve-screening-discrepancy"]),
        ("identify-adverse-information-review-need", ["evaluate-record-relevance"]),
    ]:
        add(entry(name, f, "ADVANCED", "INTRUSIVE", "P2", deps, skillsets=["background-screening-specialist", "private-investigator", "corporate-investigator"]))

    f = "14-security-operations-access-patrol"
    for name, deps, sens in [
        ("review-post-orders", ["validate-security-service-authority"], "REGULATED"),
        ("build-shift-plan", ["review-post-orders"], "ROUTINE"),
        ("plan-patrol-route", ["build-shift-plan"], "ROUTINE"),
        ("document-patrol-observation", ["plan-patrol-route"], "ROUTINE"),
        ("log-security-occurrence", ["document-patrol-observation"], "ROUTINE"),
        ("verify-access-event", ["review-post-orders"], "ROUTINE"),
        ("triage-access-control-event", ["verify-access-event"], "ROUTINE"),
        ("document-visitor-management-issue", ["verify-access-event"], "ROUTINE"),
        ("record-key-control-event", ["verify-access-event"], "REGULATED"),
        ("document-alarm-response", ["review-post-orders"], "CERTIFICATION_BOUNDARY"),
        ("prepare-shift-handoff", ["log-security-occurrence"], "ROUTINE"),
        ("review-security-log", ["prepare-shift-handoff"], "ROUTINE"),
        ("identify-post-order-gap", ["review-security-log"], "ROUTINE"),
        ("prepare-security-operations-brief", ["identify-post-order-gap"], "ROUTINE"),
        ("identify-supervisor-notification-need", ["triage-access-control-event"], "ROUTINE"),
    ]:
        add(entry(name, f, "CORE", sens, "P1", deps, skillsets=["security-officer", "mobile-patrol-officer", "security-supervisor"]))

    f = "15-incident-response"
    for name, deps, sens in [
        ("triage-security-incident", ["log-security-occurrence"], "CERTIFICATION_BOUNDARY"),
        ("determine-emergency-escalation", ["triage-security-incident"], "CERTIFICATION_BOUNDARY"),
        ("support-emergency-service-access", ["determine-emergency-escalation"], "CERTIFICATION_BOUNDARY"),
        ("preserve-incident-scene", ["triage-security-incident"], "CERTIFICATION_BOUNDARY"),
        ("identify-incident-notification-requirement", ["triage-security-incident"], "REGULATED"),
        ("document-incident-timeline", ["triage-security-incident"], "ROUTINE"),
        ("collect-incident-account", ["document-incident-timeline"], "ROUTINE"),
        ("prepare-post-incident-review", ["document-incident-timeline"], "ROUTINE"),
        ("identify-corrective-action", ["prepare-post-incident-review"], "ROUTINE"),
    ]:
        add(entry(name, f, "CORE", sens, "P1", deps, skillsets=["security-officer", "incident-response-coordinator", "security-supervisor"]))

    f = "16-communication-deescalation"
    for name, deps, sens in [
        ("assess-conflict-risk", ["log-security-occurrence"], "CERTIFICATION_BOUNDARY"),
        ("prepare-deescalation-communication-plan", ["assess-conflict-risk"], "CERTIFICATION_BOUNDARY"),
        ("draft-radio-communication", ["triage-security-incident"], "ROUTINE"),
        ("prepare-incident-notification", ["identify-incident-notification-requirement"], "ROUTINE"),
        ("adapt-message-to-audience", ["prepare-incident-notification"], "ROUTINE"),
        ("review-communication-bias", ["identify-investigative-bias"], "ROUTINE"),
        ("document-deescalation-attempt", ["prepare-deescalation-communication-plan"], "ROUTINE"),
        ("identify-communication-escalation-need", ["assess-conflict-risk"], "CERTIFICATION_BOUNDARY"),
    ]:
        add(entry(name, f, "CORE", sens, "P1", deps, skillsets=["security-officer", "incident-response-coordinator", "security-supervisor"]))

    f = "17-physical-security-risk-assessment"
    for name, deps, sens in [
        ("define-protected-assets", ["validate-security-service-authority"], "ROUTINE"),
        ("identify-security-threats", ["define-protected-assets"], "ROUTINE"),
        ("assess-physical-vulnerabilities", ["identify-security-threats"], "ROUTINE"),
        ("assess-security-consequences", ["assess-physical-vulnerabilities"], "ROUTINE"),
        ("assess-risk-likelihood", ["identify-security-threats"], "ROUTINE"),
        ("build-security-risk-register", ["assess-risk-likelihood", "assess-security-consequences"], "ROUTINE"),
        ("map-existing-controls", ["define-protected-assets"], "ROUTINE"),
        ("identify-control-gaps", ["map-existing-controls"], "ROUTINE"),
        ("compare-security-improvement-options", ["identify-control-gaps"], "ROUTINE"),
        ("prioritize-security-improvements", ["compare-security-improvement-options"], "ROUTINE"),
        ("prepare-physical-security-assessment-summary", ["prioritize-security-improvements"], "REGULATED"),
    ]:
        add(entry(name, f, "ADVANCED", sens, "P2", deps, skillsets=["physical-security-analyst", "security-risk-assessor", "security-program-manager"]))

    f = "18-security-systems-technology"
    for name, deps, sens in [
        ("define-access-control-requirements", ["identify-control-gaps"], "REGULATED"),
        ("analyze-access-control-event", ["triage-access-control-event"], "ROUTINE"),
        ("define-video-surveillance-requirements", ["identify-privacy-obligation"], "REGULATED"),
        ("assess-camera-coverage-gap", ["define-video-surveillance-requirements"], "REGULATED"),
        ("analyze-video-event-log", ["define-video-surveillance-requirements"], "INTRUSIVE"),
        ("define-intrusion-detection-requirements", ["identify-control-gaps"], "REGULATED"),
        ("analyze-alarm-event", ["document-alarm-response"], "CERTIFICATION_BOUNDARY"),
        ("identify-security-system-failure", ["analyze-alarm-event"], "CERTIFICATION_BOUNDARY"),
        ("prepare-security-system-requirements-summary", ["define-access-control-requirements", "define-intrusion-detection-requirements"], "REGULATED"),
    ]:
        add(entry(name, f, "ADVANCED", sens, "P2", deps, skillsets=["physical-security-analyst", "security-risk-assessor", "security-program-manager"]))

    f = "19-loss-prevention-asset-protection"
    for name, deps, sens in [
        ("assess-asset-protection-risk", ["define-protected-assets"], "ROUTINE"),
        ("analyze-loss-event", ["triage-security-incident"], "ROUTINE"),
        ("analyze-shrink-pattern", ["analyze-loss-event"], "ROUTINE"),
        ("triage-loss-prevention-incident", ["analyze-loss-event"], "REGULATED"),
        ("map-loss-event-evidence", ["create-evidence-log"], "ROUTINE"),
        ("identify-process-control-weakness", ["map-loss-event-evidence"], "ROUTINE"),
        ("prepare-loss-prevention-case-summary", ["identify-process-control-weakness"], "ROUTINE"),
        ("build-asset-protection-improvement-plan", ["prepare-loss-prevention-case-summary"], "ROUTINE"),
    ]:
        add(entry(name, f, "ADVANCED", sens, "P2", deps))

    f = "20-investigation-security-program-management"
    for name, deps, sens in [
        ("draft-investigative-policy", ["define-professional-role-boundaries"], "REGULATED"),
        ("draft-security-post-orders", ["review-post-orders"], "REGULATED"),
        ("review-investigative-procedure", ["draft-investigative-policy"], "REGULATED"),
        ("review-security-procedure", ["draft-security-post-orders"], "REGULATED"),
        ("audit-case-file", ["conduct-case-file-review"], "ROUTINE"),
        ("audit-security-program", ["review-security-procedure"], "REGULATED"),
        ("select-investigation-kpis", ["define-case-milestones"], "ROUTINE"),
        ("select-security-kpis", ["audit-security-program"], "ROUTINE"),
        ("review-training-requirement", ["review-training-requirements"], "REGULATED"),
        ("track-corrective-action", ["identify-corrective-action"], "ROUTINE"),
        ("measure-improvement-result", ["track-corrective-action"], "ROUTINE"),
        ("prepare-program-status-report", ["select-security-kpis", "select-investigation-kpis"], "ROUTINE"),
        ("identify-program-governance-gap", ["audit-security-program"], "REGULATED"),
    ]:
        add(entry(name, f, "ADVANCED", sens, "P2", deps))

    return skills


def build_index(skills: list[dict[str, object]]) -> dict[str, object]:
    family_counts = Counter(skill["family"] for skill in skills)
    sensitivity_counts = Counter(skill["sensitivity"] for skill in skills)
    priority_counts = Counter(skill["priority"] for skill in skills)
    tier_counts = Counter(skill["tier"] for skill in skills)

    return {
        "schema_version": "1.0",
        "taxonomy_name": "AgentInvestigate Master Taxonomy v1.0",
        "status": "READY",
        "canonical": True,
        "completion_token": TOKEN,
        "source_provenance": [
            "ROADMAP.md",
            "docs/architecture/domain-contract.md",
            "docs/architecture/scope-boundaries.md",
            "docs/architecture/prohibited-capabilities.md",
            "docs/development/handoffs/AI-01-final-handoff.md",
        ],
        "source_limitation": (
            "No standalone approved 212-skill taxonomy file was found during AI-02. "
            "This canonical in-repository taxonomy is reconstructed from the roadmap's "
            "family structure, explicitly named roadmap skills, AI-01 domain mapping, "
            "and stated 212-skill target."
        ),
        "field_contract": {
            "name": "Unique kebab-case atomic skill slug.",
            "family": "Canonical family slug.",
            "family_name": "Human-readable family name.",
            "branch": "Shared, Private Investigation, Private Security, or Hybrid.",
            "tier": "FOUNDATION, CORE, or ADVANCED.",
            "sensitivity": "ROUTINE, REGULATED, INTRUSIVE, or CERTIFICATION_BOUNDARY.",
            "jurisdiction_requirement": "Jurisdiction gate expectation.",
            "authority_requirement": "Authority or review gate expectation.",
            "freshness_requirement": "LOW, MEDIUM, or HIGH source freshness expectation.",
            "priority": "P0, P1, P2, or P3.",
            "dependencies": "Other skill slugs expected before this skill is used or authored.",
            "professional_skillsets": "Future role-level skillsets likely to compose the skill.",
        },
        "families": [
            {
                "slug": slug,
                "name": name,
                "branch": branch,
                "skill_count": family_counts[slug],
            }
            for slug, name, branch in FAMILIES
        ],
        "summary_counts": {
            "skills": len(skills),
            "families": len(FAMILIES),
            "sensitivity": dict(sorted(sensitivity_counts.items())),
            "priority": dict(sorted(priority_counts.items())),
            "tier": dict(sorted(tier_counts.items())),
        },
        "skills": skills,
    }


def write_yaml_json(path: Path, data: dict[str, object]) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def write_markdown(path: Path, index: dict[str, object]) -> None:
    skills = index["skills"]
    families = index["families"]
    summary = index["summary_counts"]

    lines = [
        "# AgentInvestigate Master Taxonomy v1.0",
        "",
        "Status: `READY`",
        "",
        "Completion token:",
        "",
        "```text",
        TOKEN,
        "```",
        "",
        "## Canonical Source",
        "",
        "`docs/architecture/taxonomy-index.yaml` is the canonical taxonomy source.",
        "This markdown file is a human-readable projection of that index.",
        "",
        "AI-02 found no standalone approved 212-skill taxonomy file outside the roadmap.",
        "The canonical in-repository taxonomy is therefore reconstructed from `ROADMAP.md`, the explicitly named roadmap skills, the AI-01 domain contract, and the roadmap's stated 212-skill count.",
        "",
        "This is a planning and routing contract. It does not mean any skill has been implemented.",
        "",
        "## Required Fields",
        "",
        "Every taxonomy entry in the canonical index includes:",
        "",
        "- `name`",
        "- `family`",
        "- `tier`",
        "- `sensitivity`",
        "- `jurisdiction_requirement`",
        "- `authority_requirement`",
        "- `freshness_requirement`",
        "- `priority`",
        "- `dependencies`",
        "- `professional_skillsets`",
        "",
        "## Summary",
        "",
        f"- Skills: `{summary['skills']}`",
        f"- Families: `{summary['families']}`",
        f"- Sensitivity counts: `{summary['sensitivity']}`",
        f"- Priority counts: `{summary['priority']}`",
        f"- Tier counts: `{summary['tier']}`",
        "",
        "## Family Counts",
        "",
        "| Family | Branch | Skills |",
        "|---|---|---:|",
    ]

    for family in families:
        lines.append(f"| `{family['slug']}` | {family['branch']} | {family['skill_count']} |")

    lines.extend([
        "",
        "## Skill Registry",
        "",
        "| Skill | Family | Tier | Sensitivity | Priority |",
        "|---|---|---|---|---|",
    ])
    for skill in skills:
        lines.append(
            f"| `{skill['name']}` | `{skill['family']}` | {skill['tier']} | "
            f"{skill['sensitivity']} | {skill['priority']} |"
        )

    lines.extend([
        "",
        "## Gate Result",
        "",
        "```text",
        "Exactly one canonical taxonomy source exists: docs/architecture/taxonomy-index.yaml",
        "```",
        "",
        "## AI-02 Sources",
        "",
        "- `ROADMAP.md`",
        "- `docs/architecture/domain-contract.md`",
        "- `docs/architecture/scope-boundaries.md`",
        "- `docs/architecture/prohibited-capabilities.md`",
        "- `docs/development/handoffs/AI-01-final-handoff.md`",
        "- ChatGPT task `Plan AgentLogistics Skills`, used only as roadmap provenance.",
        "",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    architecture_dir = repo_root / "docs" / "architecture"
    architecture_dir.mkdir(parents=True, exist_ok=True)

    skills = build_skills()
    index = build_index(skills)

    write_yaml_json(architecture_dir / "taxonomy-index.yaml", index)
    write_markdown(architecture_dir / "master-taxonomy-v1.md", index)
    print(f"Generated {len(skills)} AgentInvestigate taxonomy entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
