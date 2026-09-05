---
name: identify-workplace-evidence-sources
description: Identify workplace evidence sources from supplied investigation plans under authority, jurisdiction, privacy, and human review gates.
license: MIT
---

# Identify Workplace Evidence Sources

## Overview

Identifies potential workplace evidence sources, access limits, privacy gates, proportionality issues, and approval needs. This is a `INTRUSIVE` corporate and workplace investigations skill for professional investigation support.

AI-19 end-to-end flow:

- `allegation`
- `scope`
- `allegations matrix`
- `policy mapping`
- `interview planning`
- `evidence analysis`
- `statement comparison`
- `evidentiary support`
- `findings`
- `report`

## Triggers

- User asks to classify, map, build, plan, identify, prepare, compare, assess, draft, or report workplace evidence sources.
- User supplies a workplace allegation, scope, policy, allegations matrix, interview plan, evidence analysis, statement comparison, evidentiary support, draft finding, or report material.
- User needs the workplace investigation flow organized from allegation through report.
- User needs workplace investigation support without deciding discipline, termination, legal liability, or criminal guilt.

## Non-Triggers

- Requests to decide discipline, termination, legal liability, or criminal guilt route to qualified human review.
- Requests to fabricate, alter, conceal, sanitize, exaggerate, suppress, or selectively omit workplace evidence, statements, policy gaps, limitations, unresolved questions, or confidence route to `PROHIBITED_REDIRECT`.
- Requests to coerce witnesses, coach testimony, infer deception from behavior alone, retaliate, intimidate, or force a preferred finding route to `PROHIBITED_REDIRECT`.
- Requests for legal, employment, disciplinary, privacy, labor, human-rights, accommodation, admissibility, liability, or compliance conclusions route to qualified review.
- Requests involving protected classes, harassment, discrimination, retaliation, safety threats, medical information, minors, union/collective-bargaining issues, surveillance, private records, or sensitive personal information require the appropriate gate and human review.

## Required Inputs

- Workplace allegation, matter scope, user role, authority basis, jurisdiction, and investigation purpose.
- Supplied policy, allegation classification, allegations matrix, interview plan, evidence sources, statements, evidentiary support, findings, or report material relevant to workplace evidence sources.
- Review boundary for HR, legal, compliance, privacy, labor relations, investigator, or management review.
- Known limitations, unresolved questions, sensitive information, protected characteristics, retaliation risks, and required human approvals.

## Optional Inputs

- Existing case scope, authority check, workplace policy, allegations matrix, witness interview plan, evidence matrix, statement comparison, findings matrix, or draft report.
- Applicable procedure, collective agreement, HR guidance, legal review note, privacy review, retention rule, reporting format, or reviewer instruction.
- Known source gaps, policy gaps, contradictions, credibility limits, accommodation needs, notice constraints, consent status, or escalation path.
- Preferred output format, audience, confidence labels, issue taxonomy, exhibit labels, or case-management destination.

## Assumptions

- Do not invent allegations, policies, evidence, witness statements, interview notes, source support, findings, approvals, or legal standards.
- Keep allegations, scope, policy mapping, interview planning, evidence analysis, statement comparison, evidentiary support, findings, and report sections separate.
- Do not convert allegations, suspicions, policy questions, or inferences into findings.
- Do not decide discipline, termination, legal liability, or criminal guilt.
- Treat outputs as draft workplace investigation support requiring responsible human review before consequential use.

## Dependencies

- Canonical taxonomy dependency: `plan-workplace-investigation`.
- Use `define-case-scope` and `prepare-authority-check` when scope or authority is unclear.
- Use `classify-workplace-allegation`, `map-allegation-to-policy`, and `build-allegations-matrix` before planning or findings.
- Use `prepare-witness-interview-plan` and `compare-statement-consistency` for interview and statement work.
- Use `build-evidence-matrix`, `assess-evidentiary-support`, and `draft-investigative-finding` for evidence and finding support.
- Use `write-investigative-report` and `review-report-quality` before final report presentation.
- Use `separate-fact-from-inference` and `identify-investigative-bias` when materials blend facts, allegations, inferences, findings, or preferred outcomes.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.
- Use `docs/foundations/report-structure-contracts.md`.

If a dependency output is unavailable, identify the missing dependency and continue only with bounded issue spotting, draft structure, or escalation notes.

## Core Procedure

1. Confirm scope, role, authority, jurisdiction, policy context, investigation purpose, sensitivity, and review boundary.
2. Separate supplied material into allegation, scope, policy mapping, interview planning, evidence analysis, statement comparison, evidentiary support, findings, report, limitations, unresolved questions, and confidence.
3. Check for requests to decide discipline, termination, legal liability, criminal guilt, fabricate evidence, coerce witnesses, suppress limitations, or force a preferred outcome.
4. Organize the output around the AI-19 flow: allegation, scope, allegations matrix, policy mapping, interview planning, evidence analysis, statement comparison, evidentiary support, findings, report.
5. Preserve policy gaps, evidence gaps, statement conflicts, source limits, protected-status concerns, privacy issues, retaliation risks, unresolved questions, confidence limits, and reviewer needs.
6. Route regulated or intrusive work to the appropriate authority, jurisdiction, privacy, human-review, and source gates.
7. Return bounded workplace investigation support without deciding discipline, termination, legal liability, criminal guilt, admissibility, compliance, or final employment outcomes.

## Evidence Requirements

Use only supplied allegations, policies, case notes, authority checks, interview plans, witness statements, evidence records, source logs, timelines, matrices, findings, and report drafts. Do not invent admissions, policy clauses, witness statements, corroboration, source support, findings, or reviewer approvals.

## Source Requirements

External sources are optional for routine organization of supplied workplace materials. Legal, employment, labor, privacy, human-rights, harassment, discrimination, retaliation, accommodation, surveillance, or jurisdiction-specific requirements need AI-05 source standards and qualified review.

## Jurisdiction Requirements

Jurisdiction is required for regulated workplace classification, investigation planning, intrusive evidence source identification, and any employment, legal, privacy, labor, human-rights, disciplinary, or compliance implication. Unknown jurisdiction remains an open gate.

## Authority Checks

Confirm client or organizational authority, user role, lawful purpose, HR/legal/compliance/privacy review status, evidence access basis, witness-interview authority, retaliation safeguards, and human approval where needed. Missing authority routes to `REGULATED_RESEARCH_ONLY` or `INTRUSIVE_GATE_REQUIRED` depending on sensitivity.

## Sensitivity Handling

Default class: `INTRUSIVE`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` when workplace work involves legal process, employment outcomes, harassment, discrimination, retaliation, protected characteristics, medical or disability information, union issues, surveillance, private records, sensitive personal information, safety risks, or qualified professional determinations.

## Output Contract

Return:

- routing state;
- workplace allegation, scope, authority, jurisdiction, policy, privacy, and review status;
- AI-19 flow status for allegation, scope, allegations matrix, policy mapping, interview planning, evidence analysis, statement comparison, evidentiary support, findings, and report;
- supplied facts, allegations, policy references, evidence, statements, inferences, findings, limitations, unresolved questions, and confidence;
- gaps, contradictions, source limits, policy gaps, interview needs, corroboration needs, evidentiary support, and reviewer questions;
- prohibited decision check for discipline, termination, legal liability, and criminal guilt;
- escalation or reviewer target;
- limitations and safe next steps.

Do not decide discipline, termination, legal liability, or criminal guilt.

## Limitations

This skill does not replace HR, counsel, labor relations, compliance, privacy, management, licensed investigator, or qualified reviewer judgment. It does not decide discipline, termination, legal liability, criminal guilt, employment outcomes, legal compliance, admissibility, credibility, or final findings beyond evidence-bounded draft support.

## Escalation

Escalate to HR, counsel, labor relations, compliance, privacy, management, workplace investigator, safety lead, emergency services, or another qualified reviewer when workplace allegations involve harassment, discrimination, retaliation, protected characteristics, medical information, union issues, safety threats, criminal allegations, surveillance, private records, discipline, termination, legal liability, or material consequences.

## References

- Read `references/identify-workplace-evidence-sources-reference.md` when preparing workplace evidence sources outputs.
- Use shared schemas and report structure contracts for workplace allegation, scope, policy, interview, evidence, statement, support, finding, report, confidence, and escalation fields.

## Testing

Must pass AI-19 scenarios for the end-to-end workplace flow from allegation to report and boundary checks against deciding discipline, termination, legal liability, or criminal guilt.
