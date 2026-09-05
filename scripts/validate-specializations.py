from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


AI27_TOKEN = "AGENTINVESTIGATE_AI_27_CANADA_FEDERAL_READY"
AI28_TOKEN = "AGENTINVESTIGATE_AI_28_ONTARIO_READY"
AI29_TOKEN = "AGENTINVESTIGATE_AI_29_BRITISH_COLUMBIA_READY"
AI30_TOKEN = "AGENTINVESTIGATE_AI_30_ALBERTA_READY"
AI31_TOKEN = "AGENTINVESTIGATE_AI_31_CANADA_EXPANSION_FRAMEWORK_READY"

AI27_FILES = (
    "specializations/canada/federal/README.md",
    "specializations/canada/federal/source-log.yaml",
    "specializations/canada/federal/privacy-and-information-handling.md",
    "specializations/canada/federal/criminal-law-interaction.md",
    "specializations/canada/federal/evidence-and-records.md",
    "specializations/canada/federal/human-rights-and-federal-organizations.md",
    "specializations/canada/federal/routing-boundaries.md",
    "tests/regulatory/AI-27-canada-federal-specialization.json",
)

AI28_FILES = (
    "specializations/canada/ontario/README.md",
    "specializations/canada/ontario/source-log.yaml",
    "specializations/canada/ontario/licensing-and-registration.md",
    "specializations/canada/ontario/training-testing-and-conduct.md",
    "specializations/canada/ontario/authority-restrictions-and-security-operations.md",
    "specializations/canada/ontario/privacy-reporting-and-records.md",
    "specializations/canada/ontario/provincial-laws-map.md",
    "specializations/canada/ontario/routing-boundaries.md",
    "tests/regulatory/AI-28-ontario-specialization.json",
)

AI29_FILES = (
    "specializations/canada/british-columbia/README.md",
    "specializations/canada/british-columbia/source-log.yaml",
    "specializations/canada/british-columbia/licensing-and-registration.md",
    "specializations/canada/british-columbia/training-and-conduct.md",
    "specializations/canada/british-columbia/authority-restrictions-and-security-operations.md",
    "specializations/canada/british-columbia/privacy-reporting-and-records.md",
    "specializations/canada/british-columbia/provincial-laws-map.md",
    "specializations/canada/british-columbia/routing-boundaries.md",
    "tests/regulatory/AI-29-british-columbia-specialization.json",
)

AI30_FILES = (
    "specializations/canada/alberta/README.md",
    "specializations/canada/alberta/source-log.yaml",
    "specializations/canada/alberta/licensing-and-registration.md",
    "specializations/canada/alberta/training-examination-and-conduct.md",
    "specializations/canada/alberta/authority-restrictions-and-security-operations.md",
    "specializations/canada/alberta/privacy-reporting-and-records.md",
    "specializations/canada/alberta/provincial-laws-map.md",
    "specializations/canada/alberta/routing-boundaries.md",
    "tests/regulatory/AI-30-alberta-specialization.json",
)

AI31_FILES = (
    "docs/architecture/canadian-jurisdiction-roadmap.md",
    "tests/regulatory/AI-31-canadian-jurisdiction-framework.json",
)

AI27_RESEARCH_AREAS = {
    "federal privacy",
    "criminal-law interaction",
    "evidence-related federal concepts",
    "federal human-rights considerations",
    "information handling",
    "federally regulated organizations",
    "federal criminal prohibitions relevant to investigative/security work",
}

AI27_SOURCE_IDS = {
    "canada-federal-pipeda",
    "canada-federal-privacy-act",
    "opc-pipeda-private-sector",
    "canada-federal-criminal-code",
    "canada-federal-evidence-act",
    "canada-federal-human-rights-act",
    "chrc-discrimination",
    "canada-federally-regulated-workplaces",
    "canada-federal-labour-code",
}

AI28_REQUIRED_COVERAGE = {
    "investigator licensing",
    "security licensing",
    "training",
    "professional conduct",
    "permitted authorities",
    "restrictions",
    "privacy interaction",
    "reporting",
    "security operations",
    "provincial laws materially relevant to scoped skills",
}

AI28_SOURCE_IDS = {
    "ontario-psisa-act",
    "ontario-individual-licence-guidance",
    "ontario-agency-corporation-licence-guidance",
    "ontario-requirements-individuals-guidance",
    "ontario-basic-training-guidance",
    "ontario-testing-guidance",
    "ontario-training-testing-regulation",
    "ontario-code-of-conduct-regulation",
    "ontario-recordkeeping-regulation",
    "ontario-information-to-registrar-regulation",
    "ontario-uniforms-regulation",
    "ontario-equipment-regulation",
    "ontario-clean-criminal-record-regulation",
    "ontario-exemptions-regulation",
    "ontario-fippa",
    "ontario-mfippa",
    "ontario-phipa",
    "ontario-ipc-video-surveillance",
    "ontario-human-rights-code",
    "ontario-ohsa",
    "ontario-trespass-to-property-act",
    "ontario-employment-standards-act",
    "ontario-aoda",
}

AI29_REQUIRED_COVERAGE = {
    "security worker licensing",
    "private investigator licence types",
    "security guard licence types",
    "security business licensing",
    "training",
    "professional conduct",
    "permitted authorities",
    "restrictions",
    "privacy interaction",
    "reporting",
    "security operations",
    "provincial laws materially relevant to scoped skills",
}

AI29_SOURCE_IDS = {
    "bc-security-services-act",
    "bc-security-services-regulation",
    "bc-security-worker-licence-guidance",
    "bc-security-worker-application-guidance",
    "bc-security-worker-training-guidance",
    "bc-security-worker-rules-guidance",
    "bc-security-business-licence-guidance",
    "bc-security-business-application-guidance",
    "bc-security-business-rules-guidance",
    "bc-licensing-process-policies",
    "bc-security-licensing-enforcement",
    "bc-pipa",
    "bc-fippa",
    "bc-oipc-overt-video-private-sector",
    "bc-oipc-public-sector-surveillance",
    "bc-oipc-employee-privacy",
    "bc-human-rights-code",
    "bc-workers-compensation-act",
    "bc-ohs-regulation",
    "bc-trespass-act",
    "bc-employment-standards-act",
    "bc-body-armour-control-act",
    "bc-body-armour-control-regulation",
    "bc-body-armour-possession-guidance",
}

AI30_REQUIRED_COVERAGE = {
    "investigator licensing",
    "security service worker licensing",
    "security business licensing",
    "training",
    "provincial examinations",
    "professional conduct",
    "permitted authorities",
    "restrictions",
    "privacy interaction",
    "reporting",
    "security operations",
    "body armour",
    "provincial laws materially relevant to scoped skills",
}

AI30_SOURCE_IDS = {
    "alberta-ssia-act",
    "alberta-ssia-regulation",
    "alberta-ssia-ministerial-regulation",
    "alberta-security-licences-permits-guidance",
    "alberta-security-service-worker-licence-guidance",
    "alberta-investigator-licence-guidance",
    "alberta-security-licences-registries-guidance",
    "alberta-security-investigation-locksmith-business-resources",
    "alberta-ssia-policy-manual",
    "alberta-approved-training-courses",
    "alberta-provincial-examination-process",
    "alberta-guidelines-code-conduct",
    "alberta-guidelines-licensing-training-courses",
    "alberta-body-armour-permit-guidance",
    "alberta-body-armour-control-act",
    "alberta-body-armour-control-regulation",
    "alberta-pipa",
    "alberta-pipa-regulation",
    "alberta-popa",
    "alberta-protection-of-privacy-act-guidance",
    "alberta-atia",
    "alberta-access-to-information-act-guidance",
    "alberta-hia",
    "alberta-health-information-act-guidance",
    "alberta-oipc-video-surveillance-private",
    "alberta-oipc-privacy-laws-overview",
    "alberta-oipc-privacy-impact-assessments",
    "alberta-human-rights-act",
    "alberta-human-rights-commission",
    "alberta-ohs-act",
    "alberta-ohs-act-regulation-code-guidance",
    "alberta-employment-standards-code",
    "alberta-employment-standards-guidance",
    "alberta-trespass-to-premises-act",
    "alberta-petty-trespass-act",
}

AI27_BOUNDARY_TERMS = {
    "Federal rules alone do not determine whether private investigative or security work is authorized",
    "Occupational licensing is often provincial or territorial",
    "REGULATED_RESEARCH_ONLY",
    "PROHIBITED_REDIRECT",
    "freshness: `HIGH`",
}

AI28_BOUNDARY_TERMS = {
    "Ontario sources can identify provincial issue areas, but they do not by themselves authorize private investigative or security work without current licensing, authority, role, purpose, and qualified review",
    "Federal privacy, criminal-law, evidence, human-rights, federally regulated workplace, or labour issues may also apply",
    "REGULATED_RESEARCH_ONLY",
    "INTRUSIVE_GATE_REQUIRED",
    "CERTIFICATION_ESCALATION",
    "PROHIBITED_REDIRECT",
    "freshness: `HIGH`",
}

AI29_BOUNDARY_TERMS = {
    "British Columbia sources can identify provincial issue areas, but they do not by themselves authorize private investigative or security work without current security worker licence status, security business licence status, role, purpose, authority, and qualified review",
    "Federal privacy, criminal-law, evidence, human-rights, federally regulated workplace, or labour issues may also apply",
    "REGULATED_RESEARCH_ONLY",
    "INTRUSIVE_GATE_REQUIRED",
    "CERTIFICATION_ESCALATION",
    "PROHIBITED_REDIRECT",
    "freshness: `HIGH`",
}

AI30_BOUNDARY_TERMS = {
    "Alberta sources can identify provincial issue areas, but they do not by themselves authorize private investigative or security work without current individual licence status, business licence status, role, purpose, authority, and qualified review",
    "Federal privacy, criminal-law, evidence, human-rights, federally regulated workplace, or labour issues may also apply",
    "REGULATED_RESEARCH_ONLY",
    "INTRUSIVE_GATE_REQUIRED",
    "CERTIFICATION_ESCALATION",
    "PROHIBITED_REDIRECT",
    "freshness: `HIGH`",
}

AI31_CANDIDATE_JURISDICTIONS = {
    "quebec",
    "manitoba",
    "saskatchewan",
    "nova-scotia",
    "new-brunswick",
    "newfoundland-and-labrador",
    "prince-edward-island",
    "northwest-territories",
    "nunavut",
    "yukon",
}

AI31_BASELINE_FILES = {
    "README.md",
    "source-log.yaml",
    "licensing-and-registration.md",
    "training-examination-and-conduct.md",
    "authority-restrictions-and-security-operations.md",
    "privacy-reporting-and-records.md",
    "provincial-laws-map.md",
    "routing-boundaries.md",
}

AI31_REQUIRED_COVERAGE = {
    "investigator licensing",
    "security worker or security guard licensing",
    "security business or agency licensing",
    "training",
    "examinations, tests, or competency requirements",
    "professional conduct",
    "permitted authorities",
    "restrictions",
    "privacy interaction",
    "reporting",
    "security operations",
    "provincial or territorial laws materially relevant to scoped skills",
    "federal overlap through AI-27",
}

AI31_FRAMEWORK_TERMS = {
    "This wave builds the extension contract. It does not create additional provincial or territorial modules.",
    "specializations/canada/<jurisdiction-slug>/",
    "HIGH-freshness claims",
    "New modules must not create jurisdiction-specific routing states.",
    "Federal privacy, criminal-law, evidence, human-rights, federally regulated workplace, or labour issues may also apply and must be checked against the Canada federal specialization.",
    "No additional provincial or territorial modules beyond Ontario, British Columbia, and Alberta.",
}

REGULATORY_METADATA_FIELDS = {
    "source_title:",
    "organization:",
    "jurisdiction:",
    "authority_level:",
    "source_url:",
    "publication_date:",
    "effective_date:",
    "accessed_date:",
    "last_verified:",
    "applicability:",
    "supersession_risk:",
    "used_by:",
}


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_ai27(repo_root: Path) -> list[str]:
    errors: list[str] = []
    for relative in AI27_FILES:
        path = repo_root / relative
        if not path.is_file():
            errors.append(f"Missing AI-27 file: {relative}")

    combined_text = ""
    for relative in AI27_FILES:
        path = repo_root / relative
        if path.is_file() and path.suffix.lower() != ".json":
            combined_text += "\n" + path.read_text(encoding="utf-8-sig")

    if AI27_TOKEN not in combined_text:
        errors.append("AI-27 specialization files missing completion token")

    for term in AI27_RESEARCH_AREAS:
        if term not in combined_text:
            errors.append(f"AI-27 specialization missing research area: {term}")
    for term in AI27_BOUNDARY_TERMS:
        if term not in combined_text:
            errors.append(f"AI-27 specialization missing boundary term: {term}")

    source_log = repo_root / "specializations/canada/federal/source-log.yaml"
    if source_log.is_file():
        source_text = source_log.read_text(encoding="utf-8-sig")
        for source_id in AI27_SOURCE_IDS:
            if source_id not in source_text:
                errors.append(f"AI-27 source log missing source id: {source_id}")
        for field in REGULATORY_METADATA_FIELDS:
            if field not in source_text:
                errors.append(f"AI-27 source log missing metadata field: {field}")
        if source_text.count("source_id:") != len(AI27_SOURCE_IDS):
            errors.append("AI-27 source log source count mismatch")
        for url in (
            "https://laws-lois.justice.gc.ca/eng/acts/P-8.6/",
            "https://laws-lois.justice.gc.ca/eng/acts/P-21/",
            "https://www.priv.gc.ca/",
            "https://laws-lois.justice.gc.ca/eng/acts/C-46/",
            "https://laws-lois.justice.gc.ca/eng/acts/C-5/",
            "https://laws-lois.justice.gc.ca/eng/acts/H-6/",
            "https://www.chrc-ccdp.gc.ca/",
            "https://www.canada.ca/en/services/jobs/workplace/federally-regulated-industries.html",
            "https://laws-lois.justice.gc.ca/eng/acts/L-2/",
        ):
            if url not in source_text:
                errors.append(f"AI-27 source log missing source URL: {url}")

    fixture_path = repo_root / "tests/regulatory/AI-27-canada-federal-specialization.json"
    if fixture_path.is_file():
        try:
            fixture = load_json(fixture_path)
        except json.JSONDecodeError as exc:
            errors.append(f"AI-27 regulatory fixture invalid JSON: {exc}")
            fixture = None
        if isinstance(fixture, dict):
            if fixture.get("completion_token") != AI27_TOKEN:
                errors.append("AI-27 regulatory fixture missing completion token")
            if fixture.get("specialization_path") != "specializations/canada/federal/":
                errors.append("AI-27 regulatory fixture has wrong specialization path")
            if fixture.get("freshness") != "HIGH":
                errors.append("AI-27 regulatory fixture must be HIGH freshness")
            if set(fixture.get("research_areas", [])) != AI27_RESEARCH_AREAS:
                errors.append("AI-27 regulatory fixture research area mismatch")
            if set(fixture.get("required_sources", [])) != AI27_SOURCE_IDS:
                errors.append("AI-27 regulatory fixture source id mismatch")
            routing_tests = fixture.get("routing_tests")
            if not isinstance(routing_tests, list) or len(routing_tests) < 3:
                errors.append("AI-27 regulatory fixture must include at least 3 routing tests")
            else:
                seen_states = {str(test.get("expected_routing_state")) for test in routing_tests if isinstance(test, dict)}
                if "REGULATED_RESEARCH_ONLY" not in seen_states:
                    errors.append("AI-27 fixture missing REGULATED_RESEARCH_ONLY routing test")
                if "PROHIBITED_REDIRECT" not in seen_states:
                    errors.append("AI-27 fixture missing PROHIBITED_REDIRECT routing test")

    return errors


def validate_ai28(repo_root: Path) -> list[str]:
    errors: list[str] = []
    for relative in AI28_FILES:
        path = repo_root / relative
        if not path.is_file():
            errors.append(f"Missing AI-28 file: {relative}")

    combined_text = ""
    for relative in AI28_FILES:
        path = repo_root / relative
        if path.is_file() and path.suffix.lower() != ".json":
            combined_text += "\n" + path.read_text(encoding="utf-8-sig")

    if AI28_TOKEN not in combined_text:
        errors.append("AI-28 specialization files missing completion token")

    for term in AI28_REQUIRED_COVERAGE:
        if term not in combined_text:
            errors.append(f"AI-28 specialization missing required coverage: {term}")
    for term in AI28_BOUNDARY_TERMS:
        if term not in combined_text:
            errors.append(f"AI-28 specialization missing boundary term: {term}")

    source_log = repo_root / "specializations/canada/ontario/source-log.yaml"
    if source_log.is_file():
        source_text = source_log.read_text(encoding="utf-8-sig")
        for source_id in AI28_SOURCE_IDS:
            if source_id not in source_text:
                errors.append(f"AI-28 source log missing source id: {source_id}")
        for field in REGULATORY_METADATA_FIELDS:
            if field not in source_text:
                errors.append(f"AI-28 source log missing metadata field: {field}")
        if source_text.count("source_id:") != len(AI28_SOURCE_IDS):
            errors.append("AI-28 source log source count mismatch")
        for url in (
            "https://www.ontario.ca/laws/statute/05p34",
            "https://www.ontario.ca/page/security-guard-or-private-investigator-licence-individuals",
            "https://www.ontario.ca/page/security-guard-or-private-investigator-licence-agency-corporation",
            "https://www.ontario.ca/page/requirements-security-guards-and-private-investigators",
            "https://www.ontario.ca/page/security-guard-and-private-investigator-basic-training",
            "https://www.ontario.ca/page/security-guard-and-private-investigator-testing",
            "https://www.ontario.ca/laws/regulation/100026",
            "https://www.ontario.ca/laws/regulation/070363",
            "https://www.ontario.ca/laws/regulation/070434",
            "https://www.ontario.ca/laws/regulation/r07361",
            "https://www.ontario.ca/laws/regulation/070362",
            "https://www.ontario.ca/laws/regulation/070366",
            "https://www.ontario.ca/laws/regulation/080037",
            "https://www.ontario.ca/laws/regulation/070435",
            "https://www.ontario.ca/laws/statute/90f31",
            "https://www.ontario.ca/laws/statute/90m56",
            "https://www.ontario.ca/laws/statute/04p03",
            "https://www.ipc.on.ca/en/resources-and-decisions/guidelines-use-video-surveillance",
            "https://www.ontario.ca/laws/statute/90h19",
            "https://www.ontario.ca/laws/statute/90o01",
            "https://www.ontario.ca/laws/statute/90t21",
            "https://www.ontario.ca/laws/statute/00e41",
            "https://www.ontario.ca/laws/statute/05a11",
        ):
            if url not in source_text:
                errors.append(f"AI-28 source log missing source URL: {url}")

    fixture_path = repo_root / "tests/regulatory/AI-28-ontario-specialization.json"
    if fixture_path.is_file():
        try:
            fixture = load_json(fixture_path)
        except json.JSONDecodeError as exc:
            errors.append(f"AI-28 regulatory fixture invalid JSON: {exc}")
            fixture = None
        if isinstance(fixture, dict):
            if fixture.get("completion_token") != AI28_TOKEN:
                errors.append("AI-28 regulatory fixture missing completion token")
            if fixture.get("specialization_path") != "specializations/canada/ontario/":
                errors.append("AI-28 regulatory fixture has wrong specialization path")
            if fixture.get("jurisdiction") != "Ontario":
                errors.append("AI-28 regulatory fixture has wrong jurisdiction")
            if fixture.get("freshness") != "HIGH":
                errors.append("AI-28 regulatory fixture must be HIGH freshness")
            if set(fixture.get("required_coverage", [])) != AI28_REQUIRED_COVERAGE:
                errors.append("AI-28 regulatory fixture required coverage mismatch")
            if set(fixture.get("required_sources", [])) != AI28_SOURCE_IDS:
                errors.append("AI-28 regulatory fixture source id mismatch")
            routing_tests = fixture.get("routing_tests")
            if not isinstance(routing_tests, list) or len(routing_tests) < 6:
                errors.append("AI-28 regulatory fixture must include at least 6 routing tests")
            else:
                seen_states = {str(test.get("expected_routing_state")) for test in routing_tests if isinstance(test, dict)}
                for state in (
                    "REGULATED_RESEARCH_ONLY",
                    "INTRUSIVE_GATE_REQUIRED",
                    "CERTIFICATION_ESCALATION",
                    "PROHIBITED_REDIRECT",
                ):
                    if state not in seen_states:
                        errors.append(f"AI-28 fixture missing {state} routing test")

    return errors


def validate_ai29(repo_root: Path) -> list[str]:
    errors: list[str] = []
    for relative in AI29_FILES:
        path = repo_root / relative
        if not path.is_file():
            errors.append(f"Missing AI-29 file: {relative}")

    combined_text = ""
    for relative in AI29_FILES:
        path = repo_root / relative
        if path.is_file() and path.suffix.lower() != ".json":
            combined_text += "\n" + path.read_text(encoding="utf-8-sig")

    if AI29_TOKEN not in combined_text:
        errors.append("AI-29 specialization files missing completion token")

    for term in AI29_REQUIRED_COVERAGE:
        if term not in combined_text:
            errors.append(f"AI-29 specialization missing required coverage: {term}")
    for term in AI29_BOUNDARY_TERMS:
        if term not in combined_text:
            errors.append(f"AI-29 specialization missing boundary term: {term}")

    source_log = repo_root / "specializations/canada/british-columbia/source-log.yaml"
    if source_log.is_file():
        source_text = source_log.read_text(encoding="utf-8-sig")
        for source_id in AI29_SOURCE_IDS:
            if source_id not in source_text:
                errors.append(f"AI-29 source log missing source id: {source_id}")
        for field in REGULATORY_METADATA_FIELDS:
            if field not in source_text:
                errors.append(f"AI-29 source log missing metadata field: {field}")
        if source_text.count("source_id:") != len(AI29_SOURCE_IDS):
            errors.append("AI-29 source log source count mismatch")
        for url in (
            "https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/07030_01",
            "https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/10_207_2008",
            "https://www2.gov.bc.ca/gov/content/employment-business/business/security-services/security-industry-licensing/workers",
            "https://www2.gov.bc.ca/gov/content/employment-business/business/security-services/security-industry-licensing/workers/application",
            "https://www2.gov.bc.ca/gov/content/employment-business/business/security-services/security-industry-licensing/workers/training",
            "https://www2.gov.bc.ca/gov/content/employment-business/business/security-services/security-industry-licensing/workers/rules",
            "https://www2.gov.bc.ca/gov/content/employment-business/business/security-services/security-industry-licensing/businesses",
            "https://www2.gov.bc.ca/gov/content/employment-business/business/security-services/security-industry-licensing/businesses/application-and-licence-management-process",
            "https://www2.gov.bc.ca/gov/content/employment-business/business/security-services/security-industry-licensing/businesses/rules",
            "https://www2.gov.bc.ca/gov/content/employment-business/business/security-services/security-industry-licensing/about/law-policy/licensing-process-licence-conditions-policies",
            "https://www2.gov.bc.ca/gov/content/employment-business/business/security-services/security-industry-licensing/about/enforcement",
            "https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/03063_01",
            "https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96165_00",
            "https://www.oipc.bc.ca/guidance-documents/1453",
            "https://www.oipc.bc.ca/documents/guidance-documents/3072",
            "https://www.oipc.bc.ca/guidance-documents/2098",
            "https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96210_01",
            "https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/19001_02",
            "https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/296_97_00",
            "https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18003",
            "https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96113_01",
            "https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/09024_01",
            "https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/203_2010",
            "https://www2.gov.bc.ca/gov/content/employment-business/business/security-services/body-armour/possessing",
        ):
            if url not in source_text:
                errors.append(f"AI-29 source log missing source URL: {url}")

    fixture_path = repo_root / "tests/regulatory/AI-29-british-columbia-specialization.json"
    if fixture_path.is_file():
        try:
            fixture = load_json(fixture_path)
        except json.JSONDecodeError as exc:
            errors.append(f"AI-29 regulatory fixture invalid JSON: {exc}")
            fixture = None
        if isinstance(fixture, dict):
            if fixture.get("completion_token") != AI29_TOKEN:
                errors.append("AI-29 regulatory fixture missing completion token")
            if fixture.get("specialization_path") != "specializations/canada/british-columbia/":
                errors.append("AI-29 regulatory fixture has wrong specialization path")
            if fixture.get("jurisdiction") != "British Columbia":
                errors.append("AI-29 regulatory fixture has wrong jurisdiction")
            if fixture.get("freshness") != "HIGH":
                errors.append("AI-29 regulatory fixture must be HIGH freshness")
            if set(fixture.get("required_coverage", [])) != AI29_REQUIRED_COVERAGE:
                errors.append("AI-29 regulatory fixture required coverage mismatch")
            if set(fixture.get("required_sources", [])) != AI29_SOURCE_IDS:
                errors.append("AI-29 regulatory fixture source id mismatch")
            routing_tests = fixture.get("routing_tests")
            if not isinstance(routing_tests, list) or len(routing_tests) < 7:
                errors.append("AI-29 regulatory fixture must include at least 7 routing tests")
            else:
                seen_states = {str(test.get("expected_routing_state")) for test in routing_tests if isinstance(test, dict)}
                for state in (
                    "REGULATED_RESEARCH_ONLY",
                    "INTRUSIVE_GATE_REQUIRED",
                    "CERTIFICATION_ESCALATION",
                    "PROHIBITED_REDIRECT",
                ):
                    if state not in seen_states:
                        errors.append(f"AI-29 fixture missing {state} routing test")

    return errors


def validate_ai30(repo_root: Path) -> list[str]:
    errors: list[str] = []
    for relative in AI30_FILES:
        path = repo_root / relative
        if not path.is_file():
            errors.append(f"Missing AI-30 file: {relative}")

    combined_text = ""
    for relative in AI30_FILES:
        path = repo_root / relative
        if path.is_file() and path.suffix.lower() != ".json":
            combined_text += "\n" + path.read_text(encoding="utf-8-sig")

    if AI30_TOKEN not in combined_text:
        errors.append("AI-30 specialization files missing completion token")

    for term in AI30_REQUIRED_COVERAGE:
        if term not in combined_text:
            errors.append(f"AI-30 specialization missing required coverage: {term}")
    for term in AI30_BOUNDARY_TERMS:
        if term not in combined_text:
            errors.append(f"AI-30 specialization missing boundary term: {term}")

    source_log = repo_root / "specializations/canada/alberta/source-log.yaml"
    if source_log.is_file():
        source_text = source_log.read_text(encoding="utf-8-sig")
        for source_id in AI30_SOURCE_IDS:
            if source_id not in source_text:
                errors.append(f"AI-30 source log missing source id: {source_id}")
        for field in REGULATORY_METADATA_FIELDS:
            if field not in source_text:
                errors.append(f"AI-30 source log missing metadata field: {field}")
        if source_text.count("source_id:") != len(AI30_SOURCE_IDS):
            errors.append("AI-30 source log source count mismatch")
        for url in (
            "https://open.alberta.ca/publications/s04p7",
            "https://open.alberta.ca/publications/2010_052",
            "https://open.alberta.ca/publications/2010_055",
            "https://www.alberta.ca/security-profession-licences-permits",
            "https://www.alberta.ca/security-service-worker-licence",
            "https://www.alberta.ca/investigator-licence",
            "https://www.alberta.ca/security-licences-registries",
            "https://www.alberta.ca/security-investigation-locksmith-business-resources",
            "https://open.alberta.ca/publications/security-services-and-investigators-act-security-programs-policy-manual",
            "https://open.alberta.ca/publications/security-services-and-investigators-act-approved-training-courses",
            "https://open.alberta.ca/publications/security-services-and-investigators-act-provincial-examination-process",
            "https://open.alberta.ca/publications/security-services-and-investigators-act-guidelines-for-developing-code-of-conduct",
            "https://open.alberta.ca/publications/security-services-and-investigators-act-guidelines-for-licensing-training-courses",
            "https://www.alberta.ca/body-armour-permit",
            "https://open.alberta.ca/publications/b04p8",
            "https://open.alberta.ca/publications/2012_032",
            "https://open.alberta.ca/publications/p06p5",
            "https://open.alberta.ca/publications/2003_366",
            "https://open.alberta.ca/publications/p28p5",
            "https://www.alberta.ca/protection-of-privacy-act",
            "https://open.alberta.ca/publications/a01p4",
            "https://www.alberta.ca/access-to-information-act",
            "https://open.alberta.ca/publications/h05",
            "https://www.alberta.ca/health-information-act",
            "https://oipc.ab.ca/resource/video-surveillance/",
            "https://oipc.ab.ca/overview-privacy-laws/",
            "https://oipc.ab.ca/resources/privacy-impact-assessments/",
            "https://open.alberta.ca/publications/a25p5",
            "https://albertahumanrights.ab.ca/",
            "https://open.alberta.ca/publications/o02p2",
            "https://www.alberta.ca/ohs-act-regulation-code",
            "https://open.alberta.ca/publications/e09",
            "https://www.alberta.ca/employment-standards",
            "https://open.alberta.ca/publications/t07",
            "https://open.alberta.ca/publications/p11",
        ):
            if url not in source_text:
                errors.append(f"AI-30 source log missing source URL: {url}")

    fixture_path = repo_root / "tests/regulatory/AI-30-alberta-specialization.json"
    if fixture_path.is_file():
        try:
            fixture = load_json(fixture_path)
        except json.JSONDecodeError as exc:
            errors.append(f"AI-30 regulatory fixture invalid JSON: {exc}")
            fixture = None
        if isinstance(fixture, dict):
            if fixture.get("completion_token") != AI30_TOKEN:
                errors.append("AI-30 regulatory fixture missing completion token")
            if fixture.get("specialization_path") != "specializations/canada/alberta/":
                errors.append("AI-30 regulatory fixture has wrong specialization path")
            if fixture.get("jurisdiction") != "Alberta":
                errors.append("AI-30 regulatory fixture has wrong jurisdiction")
            if fixture.get("freshness") != "HIGH":
                errors.append("AI-30 regulatory fixture must be HIGH freshness")
            if set(fixture.get("required_coverage", [])) != AI30_REQUIRED_COVERAGE:
                errors.append("AI-30 regulatory fixture required coverage mismatch")
            if set(fixture.get("required_sources", [])) != AI30_SOURCE_IDS:
                errors.append("AI-30 regulatory fixture source id mismatch")
            routing_tests = fixture.get("routing_tests")
            if not isinstance(routing_tests, list) or len(routing_tests) < 7:
                errors.append("AI-30 regulatory fixture must include at least 7 routing tests")
            else:
                seen_states = {str(test.get("expected_routing_state")) for test in routing_tests if isinstance(test, dict)}
                for state in (
                    "REGULATED_RESEARCH_ONLY",
                    "INTRUSIVE_GATE_REQUIRED",
                    "CERTIFICATION_ESCALATION",
                    "PROHIBITED_REDIRECT",
                ):
                    if state not in seen_states:
                        errors.append(f"AI-30 fixture missing {state} routing test")

    return errors


def validate_ai31(repo_root: Path) -> list[str]:
    errors: list[str] = []
    for relative in AI31_FILES:
        path = repo_root / relative
        if not path.is_file():
            errors.append(f"Missing AI-31 file: {relative}")

    combined_text = ""
    for relative in AI31_FILES:
        path = repo_root / relative
        if path.is_file():
            combined_text += "\n" + path.read_text(encoding="utf-8-sig")

    if AI31_TOKEN not in combined_text:
        errors.append("AI-31 framework files missing completion token")

    for slug in AI31_CANDIDATE_JURISDICTIONS:
        if slug not in combined_text:
            errors.append(f"AI-31 framework missing candidate jurisdiction: {slug}")
    for filename in AI31_BASELINE_FILES:
        if filename not in combined_text:
            errors.append(f"AI-31 framework missing baseline module file: {filename}")
    for term in AI31_REQUIRED_COVERAGE:
        if term not in combined_text:
            errors.append(f"AI-31 framework missing required coverage: {term}")
    for term in AI31_FRAMEWORK_TERMS:
        if term not in combined_text:
            errors.append(f"AI-31 framework missing required term: {term}")
    for state in (
        "PROCEED_ROUTINE",
        "CLARIFY_SCOPE",
        "REGULATED_RESEARCH_ONLY",
        "INTRUSIVE_GATE_REQUIRED",
        "CERTIFICATION_ESCALATION",
        "PROHIBITED_REDIRECT",
    ):
        if state not in combined_text:
            errors.append(f"AI-31 framework missing routing state: {state}")

    fixture_path = repo_root / "tests/regulatory/AI-31-canadian-jurisdiction-framework.json"
    if fixture_path.is_file():
        try:
            fixture = load_json(fixture_path)
        except json.JSONDecodeError as exc:
            errors.append(f"AI-31 regulatory framework fixture invalid JSON: {exc}")
            fixture = None
        if isinstance(fixture, dict):
            if fixture.get("completion_token") != AI31_TOKEN:
                errors.append("AI-31 fixture missing completion token")
            if fixture.get("artifact_path") != "docs/architecture/canadian-jurisdiction-roadmap.md":
                errors.append("AI-31 fixture has wrong artifact path")
            if fixture.get("framework") != "Canadian Jurisdiction Expansion Framework":
                errors.append("AI-31 fixture has wrong framework name")
            if fixture.get("scope") != "extension contract only":
                errors.append("AI-31 fixture must remain extension contract only")
            if set(fixture.get("candidate_jurisdiction_slugs", [])) != AI31_CANDIDATE_JURISDICTIONS:
                errors.append("AI-31 fixture candidate jurisdictions mismatch")
            if set(fixture.get("baseline_module_files", [])) != AI31_BASELINE_FILES:
                errors.append("AI-31 fixture baseline module files mismatch")
            if set(fixture.get("required_coverage", [])) != AI31_REQUIRED_COVERAGE:
                errors.append("AI-31 fixture required coverage mismatch")
            routing_states = set(fixture.get("routing_states", []))
            expected_states = {
                "PROCEED_ROUTINE",
                "CLARIFY_SCOPE",
                "REGULATED_RESEARCH_ONLY",
                "INTRUSIVE_GATE_REQUIRED",
                "CERTIFICATION_ESCALATION",
                "PROHIBITED_REDIRECT",
            }
            if routing_states != expected_states:
                errors.append("AI-31 fixture routing states mismatch")
            routing_tests = fixture.get("routing_tests")
            if not isinstance(routing_tests, list) or len(routing_tests) < 5:
                errors.append("AI-31 framework fixture must include at least 5 routing tests")

    return errors


def validate(repo_root: Path) -> list[str]:
    return (
        validate_ai27(repo_root)
        + validate_ai28(repo_root)
        + validate_ai29(repo_root)
        + validate_ai30(repo_root)
        + validate_ai31(repo_root)
    )


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
    print("Validated AgentInvestigate AI-27 Canada federal through AI-31 Canadian jurisdiction framework.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
