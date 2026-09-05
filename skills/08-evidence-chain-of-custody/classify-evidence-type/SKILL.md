---
name: classify-evidence-type
description: Classify supplied evidence items by type without deciding legal admissibility or probative value.
license: MIT
---

# Classify Evidence Type

## Overview

Classifies evidence types while preserving source, format, original/copy status, and uncertainty. This is a `ROUTINE` evidence and chain-of-custody skill for professional investigation and security support.

## Triggers

- User asks to create, classify, record, assess, summarize, identify, track, compare, verify, map, or escalate evidence type classification.
- User supplies evidence descriptions, evidence logs, source records, transfer records, timestamps, original/copy records, allegations, or custody notes.
- User needs continuity issues identified without legal admissibility conclusions.
- User needs evidence handling support bounded by case scope, authority, source provenance, and human review.

## Non-Triggers

- Requests to fabricate, alter, destroy, conceal, backdate, forge, or sanitize evidence route to `PROHIBITED_REDIRECT`.
- Requests to fill in missing signatures, invent handlers, invent timestamps, or hide custody gaps route to `PROHIBITED_REDIRECT`.
- Requests to bypass access controls, obtain protected evidence unlawfully, impersonate a custodian, or defeat logging route to `PROHIBITED_REDIRECT`.
- Requests to decide legal admissibility, evidentiary privilege, discovery obligations, suppression risk, spoliation, liability, or sanctions route to qualified legal or compliance review.
- Requests involving live collection of regulated evidence, forensic acquisition, law-enforcement procedure, medical records, minors, weapons, hazardous materials, or emergency safety issues require qualified human review and escalation.

## Required Inputs

- Case scope, authority basis, user role, and evidence handling purpose.
- Jurisdiction or policy context when legal, regulated, employment, forensic, or chain-of-custody consequences are involved.
- Supplied evidence item details, source, original/copy status, custodian, transfer, timestamp, storage, or continuity record relevant to evidence type classification.
- Known limitations, gaps, disputes, or reviewer needs.

## Optional Inputs

- Existing evidence log, case notes, source provenance record, chain-of-custody form, transfer receipt, hash list, label, exhibit number, storage location, or allegation map.
- Applicable evidence handling policy, retention rule, legal hold, privacy requirement, or reviewer instruction.
- Known missing signature, duplicate copy, disputed timestamp, partial continuity record, damaged item, altered metadata, or preservation concern.
- Expected output format, reviewer role, escalation deadline, or case-management destination.

## Assumptions

- Do not invent evidence items, signatures, handlers, timestamps, locations, transfers, hashes, labels, or source details.
- Do not alter or normalize evidence records in a way that hides original wording, disputes, gaps, or uncertainty.
- Keep evidence facts, handling records, allegations, relevance assessments, continuity issues, assumptions, and legal/reviewer questions separate.
- Treat outputs as draft evidence-management support requiring responsible human review before consequential use.

## Dependencies

- Canonical taxonomy dependency: `create-evidence-log`.
- Use `define-professional-role-boundaries` when role limits are unclear.
- Use `prepare-authority-check` when evidence access, handling authority, jurisdiction, privacy, or policy basis is unclear.
- Use `record-source-provenance` when source provenance is incomplete or mixed with analysis.
- Use `separate-fact-from-inference` when evidence notes blend facts, allegations, assumptions, conclusions, and open questions.
- Use `identify-investigative-bias` when relevance or allegation mapping may overfit a preferred conclusion.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.
- Use `docs/foundations/report-structure-contracts.md`.

If a dependency output is unavailable, identify the missing dependency and continue only with bounded evidence logging, issue spotting, or escalation drafting.

## Core Procedure

1. Confirm scope, role, authority, jurisdiction or policy context, evidence purpose, and requested evidence output.
2. Separate supplied evidence facts, source records, custody events, transfers, timestamps, original/copy status, allegations, assumptions, disputes, gaps, and unknowns.
3. Check for requests to alter, fabricate, conceal, destroy, backdate, forge, sanitize, unlawfully obtain, or overstate evidence.
4. Organize the output around evidence log, evidence type, source, relevance, chain of custody, continuity gap, transfer, original and copy, timestamp, allegation mapping, continuity issue, handling escalation.
5. Preserve the representative continuity elements when present:

- `original evidence item`
- `transfer`
- `missing signature`
- `duplicate copy`
- `disputed timestamp`
- `partial continuity record`

6. Identify continuity issues, source limits, transfer gaps, missing signatures, duplicate-copy concerns, timestamp disputes, partial records, and reviewer needs.
7. Return bounded evidence-management output without deciding admissibility, privilege, legal sufficiency, sanctions, liability, guilt, discipline, or final findings.

## Evidence Requirements

Use only supplied evidence records, descriptions, logs, labels, chain-of-custody forms, transfer records, source records, metadata, timestamps, hashes, case notes, policies, and allegation maps. Do not invent missing custody events, signatures, storage conditions, source provenance, or technical verification.

## Source Requirements

External sources are optional for routine evidence logging and continuity issue spotting. Legal admissibility, regulated evidence handling, forensic collection, privacy-sensitive records, jurisdiction-specific chain-of-custody requirements, or policy-controlled escalation require AI-05 source standards and qualified review.

## Jurisdiction Requirements

Jurisdiction is contextual for routine evidence organization and required before legal, admissibility, law-enforcement, forensic, employment, privacy, discovery, retention, or compliance conclusions. Unknown jurisdiction remains an open gate.

## Authority Checks

Identify who supplied the evidence, who is authorized to access or handle it, the purpose for handling it, custody or transfer authority, privacy basis, and reviewer needs. Do not proceed into evidence acquisition, alteration, regulated handling, or legal conclusion when authority, jurisdiction, source provenance, or human review is missing.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` when evidence handling involves forensic acquisition, legal process, protected records, privacy-sensitive material, employment consequences, safety risk, emergency response, law-enforcement procedure, regulated retention, or qualified professional determinations.

## Output Contract

Return:

- routing state;
- evidence item, source, original/copy status, custodian, transfer, timestamp, storage, and continuity status;
- role, authority, jurisdiction, policy, privacy, and reviewer status;
- supplied facts, evidence records, source references, allegations, and handling notes;
- evidence log entry, classification, source record, relevance assessment, custody summary, transfer track, original/copy comparison, timestamp review, allegation map, continuity issue, or escalation note;
- gaps, disputes, missing signatures, duplicate-copy issues, timestamp conflicts, partial records, assumptions, and unknowns;
- preservation, handling, corroboration, and follow-up needs;
- escalation or reviewer target;
- limitations.

Do not claim admissibility as a legal conclusion. State continuity issues and reviewer questions instead.

## Limitations

This skill does not collect evidence, perform forensic acquisition, alter evidence, authenticate evidence, decide admissibility, establish legal sufficiency, make findings, determine sanctions, approve destruction, or replace qualified legal, compliance, forensic, or supervisory review.

## Escalation

Escalate to counsel, compliance, privacy, records management, forensics, supervisor, evidence custodian, HR, safety lead, emergency services, or another qualified reviewer when evidence involves legal process, protected records, missing custody, disputed timestamps, suspected alteration, preservation risk, safety risk, regulated retention, or material consequences.

## References

- Read `references/classify-evidence-type-reference.md` when preparing evidence type classification outputs.
- Use shared schemas and report structure contracts for evidence item, source, custody, transfer, timestamp, allegation, gap, continuity, and escalation fields.

## Testing

Must pass AI-15 scenarios for evidence logging, classification, source recording, relevance, chain of custody, transfer tracking, original/copy comparison, timestamp review, allegation mapping, continuity issue identification, handling escalation, and the representative continuity test without admissibility conclusions.
