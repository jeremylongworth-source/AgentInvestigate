from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


AI27_TOKEN = "AGENTINVESTIGATE_AI_27_CANADA_FEDERAL_READY"
AI28_TOKEN = "AGENTINVESTIGATE_AI_28_ONTARIO_READY"

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


def validate(repo_root: Path) -> list[str]:
    return validate_ai27(repo_root) + validate_ai28(repo_root)


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
    print("Validated AgentInvestigate AI-27 Canada federal and AI-28 Ontario specializations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
