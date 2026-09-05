---
name: review-report-quality
description: Review investigative reports for completeness, source support, reasoning boundaries, and report quality.
license: MIT
---

# Review Report Quality

## Overview

Reviews reports for facts, sources, evidence, inference, limitations, unresolved questions, confidence, bias, and unsupported conclusions. This is a `ROUTINE` reporting, findings, and case-presentation skill for professional investigation support.

## Triggers

- User asks to write, prepare, summarize, review, present, outline, or identify report quality review.
- User supplies case scope, report material, evidence summaries, chronologies, findings matrices, executive summaries, source records, or presentation notes.
- User needs report outputs that identify facts, sources, evidence, inference, limitations, unresolved questions, and confidence.
- User needs concise case presentation support without overstating findings or hiding limitations.

## Non-Triggers

- Requests to fabricate, alter, conceal, sanitize, exaggerate, or selectively omit facts, sources, evidence, limitations, unresolved questions, or confidence route to `PROHIBITED_REDIRECT`.
- Requests to turn allegations, inferences, hypotheses, or unsupported claims into findings route to `PROHIBITED_REDIRECT`.
- Requests to coach testimony, script false testimony, evade cross-examination, mislead a tribunal, or suppress material weaknesses route to `PROHIBITED_REDIRECT`.
- Requests for legal, employment, disciplinary, licensing, privacy, liability, guilt, admissibility, privilege, or compliance conclusions route to qualified review.
- Requests involving testimony, legal process, regulated records, sensitive personal data, employment consequences, emergency threats, or certified forensic conclusions require the appropriate gate and human review.

## Required Inputs

- Case scope, report purpose, audience, user role, and requested output.
- Supplied facts, sources, evidence records, chronology, findings, allegations, inferences, limitations, unresolved questions, and confidence context relevant to report quality review.
- Authority and jurisdiction status when the report could affect legal, employment, privacy, screening, regulatory, testimony, or other material consequences.
- Review status, reviewer role, or approval boundary, if known.

## Optional Inputs

- Existing investigative report, incident report, chronology, evidence summary, findings matrix, executive summary, report QA notes, presentation deck outline, testimony-support outline, or limitation list.
- Preferred report structure, audience level, tone, citation format, exhibit labels, source IDs, confidence labels, or decision deadline.
- Known contradictions, source gaps, disputed facts, unresolved questions, confidence limits, disclosure needs, or escalation path.
- Applicable policy, reporting standard, legal review note, regulatory source, or professional reviewer instruction.

## Assumptions

- Do not invent facts, sources, evidence, chronology events, findings, citations, exhibits, limitations, unresolved questions, confidence levels, or reviewer approvals.
- Keep facts, evidence, allegations, inferences, findings, limitations, unresolved questions, and confidence separate.
- Preserve source links and report limitations even when preparing concise summaries or presentations.
- Treat reports, presentations, and testimony-support outlines as draft support requiring responsible human review before consequential use.

## Dependencies

- Canonical taxonomy dependency: `write-investigative-report`.
- Use `draft-investigative-finding` when findings need evidence-bounded wording.
- Use `build-evidence-matrix` and `summarize-evidence` when report evidence needs structured support.
- Use `construct-event-chronology` or `prepare-case-chronology` when chronology affects the report.
- Use `separate-fact-from-inference` when report material mixes facts, allegations, assumptions, inferences, and findings.
- Use `identify-investigative-bias` when report framing, omissions, or presentation choices may overstate a preferred conclusion.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.
- Use `docs/foundations/report-structure-contracts.md`.

If a dependency output is unavailable, identify the missing dependency and continue only with bounded drafting, QA, limitation identification, or structure recommendations clearly marked as preliminary.

## Core Procedure

1. Confirm scope, authority, jurisdiction context, report purpose, audience, requested output, and review boundary.
2. Separate supplied material into facts, sources, evidence, allegations, inference, findings, limitations, unresolved questions, confidence, and reviewer notes.
3. Check for requests to fabricate, alter, conceal, sanitize, exaggerate, omit weaknesses, coach testimony, or claim unsupported certainty.
4. Organize the output around investigative reports, incident reports, chronology, evidence summaries, findings matrices, executive summaries, report QA, case presentations, testimony-support outlines, report limitations.
5. Ensure every report or report-like output identifies:

- `facts`
- `sources`
- `evidence`
- `inference`
- `limitations`
- `unresolved questions`
- `confidence`

6. Preserve contradictions, source gaps, unresolved questions, confidence limits, and qualified-review needs.
7. Return a report, summary, matrix, QA review, presentation outline, testimony-support outline, or limitation list without deciding legal, employment, disciplinary, admissibility, liability, guilt, or compliance outcomes.

## Evidence Requirements

Use only supplied or cited facts, evidence records, source records, statements, chronologies, findings, matrices, report drafts, and presentation materials. Preserve source IDs, citations, exhibit labels, contradictions, limitations, unresolved questions, and confidence limits.

Do not invent citations, exhibits, findings, reviewer approvals, source support, testimony, or missing facts. Do not hide weak evidence, gaps, or disconfirming material.

## Source Requirements

External sources are optional for routine drafting from supplied material. Legal, testimony, employment, regulatory, privacy, forensic, admissibility, or jurisdiction-specific reporting requirements require AI-05 source standards and qualified review.

## Jurisdiction Requirements

Jurisdiction is contextual for routine report drafting and required before legal, employment, disciplinary, privacy, testimony, admissibility, liability, regulatory, or compliance conclusions. Unknown jurisdiction remains an open gate.

## Authority Checks

Confirm the user is asking for reporting support on supplied or authorized material. If authority to use records is unclear and the material involves personal information, employment, screening, surveillance, protected records, legal process, testimony, or other material consequences, route upward before drafting.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` when reporting involves testimony, legal process, employment action, regulated records, sensitive personal information, surveillance, screening, forensic conclusions, emergency response, or qualified professional judgment.

## Output Contract

Return:

- routing state;
- report purpose, audience, scope, authority, jurisdiction, source, and review status;
- facts, sources, evidence, inference, limitations, unresolved questions, and confidence;
- allegations, findings, chronology, evidence summaries, matrices, presentation points, or testimony-support sections as applicable;
- source IDs, citations, exhibit labels, contradictions, gaps, and disconfirming material;
- report QA notes, reviewer questions, escalation needs, or approval limits;
- final limitations and safe next steps.

Reports must identify: facts, sources, evidence, inference, limitations, unresolved questions, and confidence.

## Limitations

This skill does not fabricate reports, hide weaknesses, coach testimony, write false testimony, decide legal conclusions, determine admissibility, determine guilt, decide liability, approve discipline, authenticate evidence, provide certified forensic opinions, or replace qualified legal, compliance, HR, forensic, supervisory, or investigator review.

## Escalation

Escalate to counsel, compliance, privacy, HR, forensics, supervisor, licensed investigator, records custodian, court officer, safety lead, emergency services, or another qualified reviewer when reporting affects legal rights, testimony, employment outcomes, regulated screening, protected records, sensitive personal information, safety risk, forensic claims, admissibility, or material consequences.

## References

- Read `references/review-report-quality-reference.md` when preparing report quality review outputs.
- Use shared schemas and report structure contracts for report, incident, chronology, evidence-summary, findings-matrix, executive-summary, QA, presentation, testimony-support, limitation, source, confidence, and escalation fields.

## Testing

Must pass AI-17 scenarios for investigative reports, incident reports, chronology, evidence summaries, findings matrices, executive summaries, report QA, case presentations, testimony-support outlines, report limitations, and report field coverage.
