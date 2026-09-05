---
name: identify-process-control-weakness
description: Identify process-control weaknesses linked to supplied loss evidence, shrink patterns, procedures, and operating constraints.
license: MIT
---

# Identify Process Control Weakness

## Overview

Identifies process-control weaknesses, contributing conditions, source support, severity, and corrective-action questions. This is a `ROUTINE` loss prevention and asset protection skill for professional investigative and security support.

AI-25 loss-prevention elements:

- `asset protection risk`
- `loss event`
- `shrink pattern`
- `loss prevention incident`
- `loss event evidence`
- `process control weakness`
- `case summary`
- `improvement plan`

AI-25 composition targets:

- `loss-prevention-officer`
- `loss-prevention-investigator`
- `asset-protection-specialist`

AI-25 prohibited conduct boundaries:

- `physical intervention instruction`
- `detention`
- `search`
- `pursuit`
- `restraint techniques`
- `coercive questioning`
- `unsupported theft conclusion`
- `criminal guilt`

Loss prevention and asset protection skills support documentation, analysis, evidence mapping, process-control review, and improvement planning only. They do not provide physical intervention instruction, detention, search, pursuit, restraint techniques, coercive questioning, unsupported theft conclusions, or criminal guilt conclusions.

## Triggers

- User asks to assess, analyze, triage, map, identify, prepare, or build process control weakness.
- User supplies asset protection risk, loss event, shrink pattern, loss prevention incident, loss event evidence, process control weakness, case summary, or improvement plan material.
- User needs support for loss-prevention-officer, loss-prevention-investigator, asset-protection-specialist.
- User needs loss prevention and asset protection analysis without enforcement, detention, search, pursuit, coercion, or unsupported guilt conclusions.

## Non-Triggers

- Requests for physical intervention instruction, detention, search, pursuit, restraint techniques, weapons use, tactical confrontation, force, or hands-on apprehension route to `PROHIBITED_REDIRECT`.
- Requests for coercive questioning, forced confession, intimidation, threats, deception to obtain a statement, or pressure tactics route to `PROHIBITED_REDIRECT`.
- Requests to assert unsupported theft conclusions, criminal guilt, employee discipline, termination eligibility, civil liability, restitution demand, or final legal conclusions route to qualified review.
- Requests to fabricate, alter, conceal, backdate, sanitize, or selectively omit loss events, inventory records, video records, access logs, evidence gaps, process weaknesses, or case limitations route to `PROHIBITED_REDIRECT`.
- Requests for live law-enforcement coordination, emergency response, trespass enforcement, physical removal, or suspect pursuit route to `CERTIFICATION_ESCALATION` or `PROHIBITED_REDIRECT`.

## Required Inputs

- Business or site scope, user role, authority basis, jurisdiction when required, purpose, affected assets, and reviewer boundary.
- Supplied facts relevant to process control weakness, including asset protection risk, loss event, shrink pattern, loss prevention incident, loss event evidence, process control weakness, case summary, and improvement plan where applicable.
- Source records such as inventory counts, sales records, exception reports, incident records, camera or access logs, witness or staff statements, evidence logs, policy excerpts, and control descriptions.
- Known limitations, missing facts, disputed facts, privacy constraints, employment implications, law-enforcement referral questions, safety issues, and required human approvals.

## Optional Inputs

- Existing incident report, evidence log, shrink report, control matrix, inventory variance report, exception report, case chronology, asset list, camera log summary, access-event summary, or prior risk assessment.
- Current procedures, cash-handling controls, receiving controls, returns controls, inventory controls, audit observations, training notes, corrective actions, or improvement backlog.
- Impact estimates, recurrence data, affected locations, ownership model, KPIs, severity labels, remediation constraints, budget constraints, and desired output format.

## Assumptions

- Do not invent loss events, shrink causes, asset values, evidence, records, video observations, access events, witness accounts, suspects, admissions, process weaknesses, or approvals.
- Keep asset protection risk, loss event, shrink pattern, loss prevention incident, loss event evidence, process control weakness, case summary, and improvement plan visible where relevant.
- Do not convert suspicion, variance, anomaly, pattern, or allegation into an unsupported theft conclusion, criminal guilt conclusion, legal conclusion, HR conclusion, or disciplinary recommendation.
- Do not provide physical intervention instruction, detention, search, pursuit, restraint techniques, coercive questioning, unsupported theft conclusion, criminal guilt.
- Treat outputs as draft loss-prevention analysis support requiring responsible human review before consequential use.

## Dependencies

- Canonical taxonomy dependency: `map-loss-event-evidence`.
- Use `define-protected-assets` before asset risk assessment when asset scope is unclear.
- Use `triage-security-incident` and `analyze-loss-event` before deeper loss-event, shrink, or process-control analysis.
- Use `create-evidence-log` and `map-loss-event-evidence` before case summaries that rely on evidence.
- Use `identify-process-control-weakness` before asset-protection improvement planning.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.
- Use `docs/foundations/report-structure-contracts.md`.

If a dependency output is unavailable, identify the missing dependency and continue only with bounded analysis, documentation structure, evidence-gap notes, or review questions.

## Core Procedure

1. Confirm business or site scope, role, authority, jurisdiction if required, purpose, affected assets, sensitivity, and reviewer boundary.
2. Identify applicable AI-25 loss-prevention elements: asset protection risk, loss event, shrink pattern, loss prevention incident, loss event evidence, process control weakness, case summary, and improvement plan.
3. Check for physical intervention instruction, detention, search, pursuit, restraint techniques, coercive questioning, unsupported theft conclusions, criminal guilt conclusions, fabricated records, hidden gaps, or consequential employment/legal decisions.
4. Separate supplied facts, source records, observations, event timing, inventory data, control evidence, allegations, assumptions, uncertainty, contradictions, and limitations.
5. Preserve asset scope, event chronology, evidence status, shrink indicators, process-control gaps, source limits, privacy or employment constraints, and confidence.
6. Route regulated, intrusive, legal, HR, law-enforcement referral, privacy, safety, physical intervention, unclear-authority, or material-consequence work to manager review, legal review, HR review, law-enforcement referral review.
7. Return bounded loss-prevention or asset-protection analysis without enforcement tactics, detention, search, pursuit, coercion, unsupported theft conclusions, criminal guilt conclusions, or final disciplinary/legal decisions.

## Evidence Requirements

Use only supplied inventory counts, exception reports, transaction records, incident reports, access logs, camera log summaries, evidence logs, staff statements, witness statements, control descriptions, policy excerpts, audit notes, and source material. Do not invent records, admissions, suspects, theft findings, shrink causes, process weaknesses, or approvals.

## Source Requirements

External sources are optional for routine organization of supplied loss-prevention material. Legal, employment, privacy, law-enforcement referral, regulated security, jurisdiction-specific, or consequential decision support needs AI-05 source standards and qualified review.

## Jurisdiction Requirements

Jurisdiction is required for regulated incident triage, privacy implications, employment consequences, law-enforcement referral, detention/search questions, use-of-force questions, legal conclusions, restitution demands, and compliance implications. Unknown jurisdiction remains an open gate for regulated, intrusive, or consequential work.

## Authority Checks

Confirm user role, business or site authority, lawful purpose, access to records, privacy basis, employment context, reviewer role, escalation path, and human approval where needed. Missing authority routes to `REGULATED_RESEARCH_ONLY`, `INTRUSIVE_GATE_REQUIRED`, `CERTIFICATION_ESCALATION`, or `PROHIBITED_REDIRECT` depending on the request.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` when loss-prevention work involves personal information, employee or customer allegations, surveillance records, access logs, suspected crime, law-enforcement referral, employment consequences, detention, search, pursuit, physical intervention, privacy issues, or material consequences.

## Output Contract

Return:

- routing state;
- business or site scope, role, authority, jurisdiction, purpose, source, privacy, employment, and reviewer status;
- AI-25 element status for asset protection risk, loss event, shrink pattern, loss prevention incident, loss event evidence, process control weakness, case summary, and improvement plan;
- supplied facts, records, chronology, inventory or exception data, evidence, allegations, controls, process weaknesses, assumptions, contradictions, and limitations;
- composition target fit for loss-prevention-officer, loss-prevention-investigator, or asset-protection-specialist use;
- gaps, missing records, unclear authority, privacy constraints, employment constraints, law-enforcement referral questions, process-control questions, and qualified-review needs;
- prohibited conduct check for physical intervention instruction, detention, search, pursuit, restraint techniques, coercive questioning, unsupported theft conclusion, and criminal guilt;
- escalation or qualified-review target;
- limitations and safe next steps.

Do not provide physical intervention instruction, detention instructions, search instructions, pursuit instructions, restraint techniques, coercive questioning, forced confession tactics, unsupported theft conclusions, criminal guilt conclusions, final HR decisions, final legal conclusions, restitution demands, or law-enforcement charging recommendations.

## Limitations

This skill does not replace counsel, HR, privacy, compliance, licensing authority, law enforcement, security manager, loss-prevention manager, asset-protection specialist, investigator, or qualified reviewer judgment. It does not authorize detention, search, pursuit, physical intervention, questioning, discipline, termination, restitution, criminal referral, or legal action.

## Escalation

Escalate to a security manager, loss-prevention manager, asset-protection specialist, HR, counsel, privacy reviewer, compliance, licensing authority, law enforcement, emergency services, or another qualified reviewer when facts involve manager review, legal review, HR review, law-enforcement referral review, suspected crime, employee or customer allegations, privacy-sensitive records, surveillance material, detention/search/pursuit questions, safety issues, unclear authority, or material consequences.

## References

- Read `references/identify-process-control-weakness-reference.md` when preparing process control weakness outputs.
- Use shared schemas and report structure contracts for asset protection risk, loss events, shrink patterns, loss prevention incidents, evidence mapping, process-control weaknesses, case summaries, improvement plans, assumptions, confidence, and escalation fields.

## Testing

Must pass AI-25 scenarios for asset protection risk, loss event, shrink pattern, loss prevention incident, loss event evidence, process control weakness, case summary, improvement plan, composition targets, and prohibited conduct boundaries.
