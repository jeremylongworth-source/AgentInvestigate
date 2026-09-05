---
name: assess-association-strength
description: Assess association strength from supplied evidence without treating weak links as confirmed relationships.
license: MIT
---

# Assess Association Strength

## Overview

Assesses association support using source reliability, independence, recency, corroboration, conflict, and context limits. This is an `INTRUSIVE` identity, entity, and timeline analysis skill for source-bounded professional investigation work.

## Triggers

- User asks to assess, differentiate, normalize, construct, map, resolve, or state association strength.
- User supplies identity, entity, identifier, relationship, association, timeline, or contradiction evidence for analysis.
- User needs ambiguity, confidence, corroboration, gaps, contradictions, or unresolved matches documented.
- User needs identity analysis framed without overclaiming or expanding collection authority.

## Non-Triggers

- Requests to identify, locate, track, profile, target, doxx, harass, or monitor a person without authority, jurisdiction, lawful purpose, privacy basis, and human approval route to `PROHIBITED_REDIRECT` or `INTRUSIVE_GATE_REQUIRED`.
- Requests to treat same-name, partial, stale, conflicting, or single-source evidence as a confirmed identity route to refusal or correction.
- Requests for legal, privacy, employment, screening, compliance, admissibility, liability, or enforcement conclusions route to qualified review.
- Requests for unauthorized database access, credential acquisition, private-account compromise, deception, protected-record bypass, or covert tracking route to `PROHIBITED_REDIRECT`.

## Required Inputs

- Case scope, role, authority status, and jurisdiction status.
- Human approval status for person-linking or intrusive identity analysis.
- Supplied identity, entity, identifier, relationship, timeline, or source material.
- Source provenance, access basis, and intended use.

## Optional Inputs

- Known aliases, identifiers, date ranges, locations, organizations, relationships, records, or source conflicts.
- Prior research summary, source log, timeline, evidence matrix, or case file review.
- Confidence threshold, reviewer role, privacy constraints, or escalation path.
- Known gaps, disputed records, stale sources, or contradiction notes.

## Assumptions

- Do not infer identity, relationship, association, location, or timeline continuity from weak resemblance, same name, proximity, or client confidence.
- Do not convert `POSSIBLE` or `PROBABLE` support into `CONFIRMED`.
- Preserve conflicts, ambiguity, gaps, stale sources, and unresolved alternatives.
- Treat identity and person-linking outputs as drafts for responsible human review.

## Dependencies

- Canonical taxonomy dependency: `map-relationship-evidence`.
- Use `prepare-authority-check` before intrusive identity, person-linking, screening, timeline, relationship, or association analysis.
- Use `identify-privacy-obligation` when personal information, sensitive data, screening, or disclosure may be involved.
- Use `record-source-provenance` and `assess-source-reliability` before confidence labels.
- Use `separate-fact-from-inference` when materials mix facts, allegations, inferences, and unknowns.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.
- Use `docs/standards/research-and-evidence-standard.md`.

If a dependency output is unavailable, identify the missing dependency and continue only with bounded ambiguity or gap analysis.

## Core Procedure

1. Confirm scope, role, authority, jurisdiction, human approval, lawful purpose, privacy basis, and intended use.
2. Separate supplied facts, identifiers, source claims, observations, inferences, assumptions, conflicts, and unknowns.
3. Identify whether the request is routine entity analysis, intrusive person-linking, regulated screening, or prohibited targeting.
4. Compare identifiers, provenance, source reliability, chronology, independence, corroboration, contradictions, and alternative explanations.
5. Assign only supported confidence labels and explain why stronger labels are not justified.
6. Return bounded analysis, gaps, conflicts, review needs, and safe next steps without authorizing collection or action.

## Evidence Requirements

Use supplied records, identifiers, source logs, public sources, timelines, relationship evidence, case records, and provenance notes. Do not invent identifiers, dates, links, relationships, locations, records, sources, or corroboration.

## Source Requirements

Use source provenance, source reliability, freshness, capture details, access basis, source owner, and conflicts. Current authoritative sources are required for regulated identity, screening, privacy, legal, or records claims.

## Jurisdiction Requirements

Jurisdiction is required before identity analysis is used for regulated, screening, privacy, employment, public-record, record-access, surveillance, or enforcement-related decisions. Unknown jurisdiction remains an open gate.

## Authority Checks

Identify role, authority basis, human approval status, lawful purpose, privacy basis, source access basis, affected parties, and reviewer needs. Intrusive identity work must fail closed when authority, jurisdiction, or human approval is missing.

## Sensitivity Handling

Default class: `INTRUSIVE`. Do not route directly from a raw user request. Require human approval, authority, jurisdiction, lawful purpose, privacy basis, source provenance, and proportionality before identity/person-linking analysis. Route to `INTRUSIVE_GATE_REQUIRED` when those gates are incomplete.

## Output Contract

Return:

- routing state;
- entity or identity question;
- role, authority, jurisdiction, approval, and lawful access status;
- supplied identifiers and source references;
- ambiguity, matches, non-matches, contradictions, and timeline gaps;
- confidence label using the required model;
- corroboration and reliability notes;
- assumptions and unknowns;
- intrusive, regulated, privacy, or prohibited boundaries;
- reviewer or escalation target;
- limitations.

Required confidence model:

- `POSSIBLE`
- `PROBABLE`
- `CORROBORATED`
- `CONFIRMED`
- `UNRESOLVED`

## Limitations

This skill does not confirm identity from weak evidence, identify or locate private persons without authority, approve screening or surveillance, grant database access, make legal or employment findings, or replace qualified review.

## Escalation

Escalate to counsel, privacy, compliance, HR, supervisor, client decision maker, records custodian, security manager, or another qualified reviewer when identity analysis involves sensitive personal information, screening, surveillance, disputed identity, protected records, missing authority, missing jurisdiction, or material consequences.

## References

- Read `references/assess-association-strength-reference.md` when preparing association strength outputs.
- Use shared schemas for person, organization, identifier, source, evidence, artifact metadata, timeline, relationship, confidence, and escalation fields.

## Testing

Must pass AI-13 scenarios for identity ambiguity, same-name differentiation, identifier normalization, subject timelines, relationship mapping, association evidence, timeline gaps, entity contradictions, confidence labels, and identity-overclaiming penalties.
