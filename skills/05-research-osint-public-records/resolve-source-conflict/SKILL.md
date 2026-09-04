---
name: resolve-source-conflict
description: Analyze conflicts between supplied sources without forcing unsupported resolution.
license: MIT
---

# Resolve Source Conflict

## Overview

Identifies source conflicts, reliability differences, chronology issues, unresolved facts, and review needs. This is a `ROUTINE` research, OSINT, and public-records skill for lawful professional investigation work.

## Triggers

- User asks to plan, conduct, structure, assess, corroborate, or summarize source conflicts.
- User supplies public, open-source, or source-backed material and needs bounded research support.
- User needs source categories, provenance, reliability, corroboration, conflicts, or research gaps organized.
- User needs public-record or open-source research framed without expanding authority or access rights.

## Non-Triggers

- Requests for unauthorized database access, credential acquisition, private-account compromise, protected-record acquisition through deception, access-control bypass, scraping behind authentication, doxxing, stalking, or coercive collection route to `PROHIBITED_REDIRECT`.
- Requests for final legal, licensing, privacy, employment, compliance, admissibility, or liability conclusions route to qualified review.
- Requests for surveillance, monitoring, screening, record access, or sensitive personal data collection without authority, jurisdiction, and lawful access basis fail closed.

## Required Inputs

- Research question or requested research output.
- Case scope and user role.
- Authority and jurisdiction status, if known.
- Supplied source material, source categories, identifiers, or known public-record targets.
- Intended use and affected parties, if known.

## Optional Inputs

- Research plan, investigative question, case timeline, or prior source log.
- URLs, citations, documents, public-record references, capture dates, or access dates.
- Known source conflicts, reliability concerns, aliases, entities, or date ranges.
- Review owner, deadline, source freshness need, or escalation path.

## Assumptions

- Do not infer lawful access from public interest, curiosity, employment status, or client pressure.
- Do not access or advise access to private accounts, credentialed systems, protected databases, or records obtained through deception.
- Do not treat open-source visibility as permission to collect, republish, or use information without purpose, authority, and privacy review.
- Distinguish supplied facts, source claims, observations, inferences, unknowns, and unresolved conflicts.

## Dependencies

- Canonical taxonomy dependency: `corroborate-open-source-information`.
- Use `prepare-authority-check` before regulated public-records, protected-records, screening, or sensitive research.
- Use `identify-privacy-obligation` when research involves personal information or sensitive data.
- Use `separate-fact-from-inference` when research material mixes facts, allegations, inferences, and unknowns.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.
- Use `docs/foundations/report-structure-contracts.md`.
- Use `docs/standards/research-and-evidence-standard.md`.
- Use `docs/standards/regulatory-source-standard.md` for regulated sources.
- Use `docs/standards/source-freshness-standard.md`.

If a dependency output is unavailable, identify the missing dependency and continue only with bounded research framing.

## Core Procedure

1. Confirm research question, case scope, role, intended use, jurisdiction status, authority status, and lawful access basis.
2. Separate supplied facts, source claims, observations, inferences, assumptions, unknowns, and source conflicts.
3. Identify source categories, source hierarchy, freshness needs, access limits, and provenance requirements.
4. Check hard boundaries for unauthorized access, credential requests, private-account compromise, deception, stalking, and protected-record bypass.
5. Organize the research output with source reliability, corroboration, conflicts, gaps, and review needs.
6. Return bounded next steps that do not authorize regulated, intrusive, deceptive, or prohibited collection.

## Evidence Requirements

Use supplied sources, public records, open-source material, citations, access dates, capture notes, documents, screenshots, and case records. Do not invent sources, source contents, access rights, identifiers, facts, corroboration, or findings.

## Source Requirements

Use AI-05 source and evidence standards when summarizing source material. External sources are optional for general planning, but source-backed claims must include provenance, freshness, reliability limits, and conflicts.

## Jurisdiction Requirements

Jurisdiction is optional for general research planning and required before regulated public-records, protected-records, privacy, court, property, litigation, licensing, or compliance conclusions.

## Authority Checks

Identify role, scope, authority basis, lawful access basis, intended use, affected parties, source access limits, and reviewer needs. Sensitive research must fail closed when authority, jurisdiction, lawful purpose, consent, privacy basis, or lawful access basis is missing.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` when research would involve legal, privacy, licensing, employment, protected records, sensitive personal information, surveillance, safety, emergency, or qualified professional issues.

## Output Contract

Return:

- routing state;
- research question and scope;
- role, authority, jurisdiction, and lawful access status;
- source categories and source list;
- provenance and freshness notes;
- reliability and corroboration assessment;
- conflicts, gaps, assumptions, and unknowns;
- privacy, regulated, intrusive, or prohibited boundaries;
- reviewer or escalation target;
- limitations.

## Limitations

This skill does not grant database access, obtain credentials, bypass access controls, acquire protected records, approve surveillance or screening, certify compliance, issue legal advice, make final findings, or replace qualified review.

## Escalation

Escalate to counsel, compliance, privacy, records custodian, licensing authority, HR, supervisor, client decision maker, platform owner, or another qualified reviewer when research involves regulated records, protected data, missing jurisdiction, unclear authority, sensitive personal information, reportable issues, or disputed lawful access.

## References

- Read `references/resolve-source-conflict-reference.md` when preparing source conflicts outputs.
- Use shared schemas and report structure contracts for source, evidence, artifact metadata, research-source-log, reliability, corroboration, conflict, and summary fields.

## Testing

Must pass AI-12 scenarios for research planning, public records, open sources, corporate records, court records, regulatory records, source reliability, provenance, corroboration, source conflict, organization research, property context, litigation research, research summaries, and hard-boundary refusal or rerouting.
