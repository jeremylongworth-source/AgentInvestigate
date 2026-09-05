---
name: identify-program-governance-gap
description: Identify investigation or security program governance gaps from supplied audit, policy, procedure, KPI, and review context.
license: MIT
---

# Identify Program Governance Gap

## Overview

Identifies governance gaps, ownership gaps, policy/procedure gaps, audit gaps, KPI gaps, and escalation needs. This is a `REGULATED` investigation and security program management skill.

AI-26 program management elements:

- `investigative policy`
- `security post orders`
- `procedure review`
- `file audits`
- `program audits`
- `kpis`
- `training requirements`
- `corrective action`
- `improvement measurement`

AI-26 composition targets:

- `investigative-case-manager`
- `security-supervisor`
- `security-operations-manager`
- `security-program-manager`
- `corporate-security-manager`

AI-26 prohibited outputs:

- `legal conclusion`
- `licensing approval`
- `compliance certification`
- `policy approval`
- `disciplinary decision`
- `use-of-force training`
- `weapons training`
- `fabricated audit`

Investigation and security program management skills support governance, documentation, review, audit, KPI, training requirement, corrective action, and improvement measurement work only. They do not provide legal conclusion, licensing approval, compliance certification, policy approval, disciplinary decision, use-of-force training, weapons training, or fabricated audit output.

## Triggers

- User asks to draft, review, audit, select, track, measure, prepare, or identify program governance gap.
- User supplies investigative policy, security post orders, procedure review, file audits, program audits, KPIs, training requirements, corrective action, or improvement measurement material.
- User needs support for investigative-case-manager, security-supervisor, security-operations-manager, security-program-manager, corporate-security-manager.
- User needs program governance support without final legal, licensing, compliance, HR, force, weapons, or audit-certification decisions.

## Non-Triggers

- Requests for legal conclusion, licensing approval, compliance certification, policy approval, disciplinary decision, use-of-force training, weapons training, fabricated audit, or final authority signoff route to qualified review or `PROHIBITED_REDIRECT`.
- Requests to create force tactics, weapons procedures, restraint techniques, tactical confrontation, pursuit, detention, search, or emergency-response training route to `PROHIBITED_REDIRECT`.
- Requests to fabricate, alter, conceal, backdate, sanitize, or selectively omit policy gaps, procedure gaps, audit findings, file deficiencies, KPI results, training gaps, corrective actions, or improvement results route to `PROHIBITED_REDIRECT`.
- Requests to decide employment discipline, legal liability, criminal guilt, regulatory compliance, licensing sufficiency, or certification status route to qualified review.

## Required Inputs

- Program scope, user role, authority basis, jurisdiction when required, purpose, affected investigative or security function, and reviewer boundary.
- Supplied facts relevant to program governance gap, including investigative policy, security post orders, procedure review, file audits, program audits, KPIs, training requirements, corrective action, and improvement measurement where applicable.
- Source records such as policies, post orders, procedures, case files, audit notes, incident data, KPI definitions, training matrices, corrective-action records, status reports, governance documents, and review comments.
- Known limitations, missing facts, disputed facts, privacy constraints, employment implications, licensing implications, training implications, certification boundaries, and required human approvals.

## Optional Inputs

- Current policy text, post orders, procedure drafts, case-file checklist, audit criteria, program charter, KPI dashboard, training requirement matrix, corrective-action tracker, improvement baseline, status-report template, or governance register.
- Role descriptions, service contract terms, licensing notes, jurisdiction notes, privacy notes, HR guidance, stakeholder comments, risk register, incident trend, quality target, review cadence, or decision log.
- Preferred output format, audience, severity labels, ownership fields, due-date fields, metric definitions, review-status labels, or implementation constraints.

## Assumptions

- Do not invent policies, post orders, procedure requirements, audit findings, file deficiencies, KPI results, training requirements, corrective actions, improvement outcomes, governance gaps, approvals, or certifications.
- Keep investigative policy, security post orders, procedure review, file audits, program audits, KPIs, training requirements, corrective action, and improvement measurement visible where relevant.
- Do not convert a draft policy, procedure review, audit observation, KPI trend, training gap, or corrective action into a legal conclusion, licensing approval, compliance certification, policy approval, disciplinary decision, or final management decision.
- Do not provide legal conclusion, licensing approval, compliance certification, policy approval, disciplinary decision, use-of-force training, weapons training, fabricated audit.
- Treat outputs as draft program-management support requiring responsible human review before consequential use.

## Dependencies

- Canonical taxonomy dependency: `audit-security-program`.
- Use `define-professional-role-boundaries`, policy drafts, post orders, and procedure reviews before program audits or governance-gap analysis.
- Use `conduct-case-file-review` before case-file audits when file review has not been completed.
- Use `select-investigation-kpis` and `select-security-kpis` before program status reports.
- Use `track-corrective-action` before measuring improvement results.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.
- Use `docs/foundations/report-structure-contracts.md`.

If a dependency output is unavailable, identify the missing dependency and continue only with bounded drafting, review structure, audit criteria, KPI framing, gap notes, or review questions.

## Core Procedure

1. Confirm program scope, role, authority, jurisdiction if required, purpose, affected function, sensitivity, and reviewer boundary.
2. Identify applicable AI-26 program management elements: investigative policy, security post orders, procedure review, file audits, program audits, KPIs, training requirements, corrective action, and improvement measurement.
3. Check for legal conclusion, licensing approval, compliance certification, policy approval, disciplinary decision, use-of-force training, weapons training, fabricated audit, final signoff, or consequential employment/legal decisions.
4. Separate supplied facts, source records, policy text, procedure text, post orders, audit criteria, KPI definitions, training evidence, corrective-action status, improvement baselines, assumptions, contradictions, and limitations.
5. Preserve governance owners, roles, decision rights, audit criteria, source support, KPI definitions, training gaps, corrective-action status, improvement measures, review cadence, and open questions.
6. Route regulated, legal, HR, privacy, licensing, training-certification, force, weapons, unclear-authority, or material-consequence work to management review, legal review, HR review, privacy review, licensing review, qualified training review.
7. Return bounded program-management output without legal conclusions, licensing approval, compliance certification, policy approval, disciplinary decisions, force or weapons training, fabricated audit findings, or final signoff.

## Evidence Requirements

Use only supplied policies, post orders, procedures, case files, case logs, audit notes, incident data, KPI definitions, training matrices, corrective-action records, improvement baselines, status reports, governance records, review comments, and source material. Do not invent findings, metrics, training completion, corrective-action completion, approvals, certifications, or reviewer decisions.

## Source Requirements

External sources are optional for routine organization of supplied program material. Legal, licensing, privacy, employment, training, regulatory, compliance, certification, force, weapons, or jurisdiction-specific requirements need AI-05 source standards and qualified review.

## Jurisdiction Requirements

Jurisdiction is required for regulated policies, post orders, procedure reviews, program audits, training requirements, licensing implications, privacy implications, employment consequences, legal conclusions, compliance conclusions, and certification implications. Unknown jurisdiction remains an open gate for regulated or consequential work.

## Authority Checks

Confirm user role, organization authority, program ownership, document ownership, access to files, lawful purpose, privacy basis, reviewer role, management approval path, and human approval where needed. Missing authority routes to `REGULATED_RESEARCH_ONLY`, `INTRUSIVE_GATE_REQUIRED`, `CERTIFICATION_ESCALATION`, or `PROHIBITED_REDIRECT` depending on the request.

## Sensitivity Handling

Default class: `REGULATED`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` when program work involves personal information, employee allegations, surveillance records, access logs, suspected crime, legal review, licensing implications, training certification, force/weapons topics, privacy issues, or material consequences.

## Output Contract

Return:

- routing state;
- program scope, role, authority, jurisdiction, purpose, source, privacy, employment, licensing, and reviewer status;
- AI-26 element status for investigative policy, security post orders, procedure review, file audits, program audits, KPIs, training requirements, corrective action, and improvement measurement;
- supplied facts, documents, audit criteria, evidence, KPI definitions, training records, corrective-action records, improvement baselines, assumptions, contradictions, and limitations;
- composition target fit for investigative-case-manager, security-supervisor, security-operations-manager, security-program-manager, or corporate-security-manager use;
- gaps, missing records, unclear authority, privacy constraints, employment constraints, licensing questions, training questions, governance questions, and qualified-review needs;
- prohibited output check for legal conclusion, licensing approval, compliance certification, policy approval, disciplinary decision, use-of-force training, weapons training, and fabricated audit;
- escalation or qualified-review target;
- limitations and safe next steps.

Do not provide legal conclusions, licensing approval, compliance certification, policy approval, disciplinary decisions, use-of-force training, weapons training, fabricated audit findings, final HR decisions, final management signoff, regulatory certification, or professional certification.

## Limitations

This skill does not replace counsel, HR, privacy, compliance, licensing authority, security management, investigation management, training authority, regulator, auditor, or qualified reviewer judgment. It does not approve policies, certify compliance, certify licensing sufficiency, qualify personnel, authorize discipline, or provide force or weapons instruction.

## Escalation

Escalate to management, legal review, HR review, privacy review, licensing review, qualified training review, compliance, security leadership, investigation leadership, regulator, auditor, or another qualified reviewer when facts involve management review, legal review, HR review, privacy review, licensing review, qualified training review, personal information, employee consequences, licensing or training requirements, force or weapons topics, suspected crime, unclear authority, audit disputes, or material consequences.

## References

- Read `references/identify-program-governance-gap-reference.md` when preparing program governance gap outputs.
- Use shared schemas and report structure contracts for investigative policy, security post orders, procedure review, file audits, program audits, KPIs, training requirements, corrective action, improvement measurement, assumptions, confidence, and escalation fields.

## Testing

Must pass AI-26 scenarios for investigative policy, security post orders, procedure review, file audits, program audits, KPIs, training requirements, corrective action, improvement measurement, composition targets, and prohibited output boundaries.
