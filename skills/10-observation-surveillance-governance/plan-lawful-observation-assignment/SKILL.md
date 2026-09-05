---
name: plan-lawful-observation-assignment
description: Prepare a non-operational lawful observation assignment brief from approved scope, jurisdiction, and human review gates.
license: MIT
---

# Plan Lawful Observation Assignment

## Overview

Prepares a governance-focused observation assignment brief with gates, limits, minimization, reporting, and escalation needs. This is an `INTRUSIVE` observation and surveillance governance skill. It requires jurisdiction, documented authority, lawful purpose, privacy review, minimization, and human review before any bounded output.

Mandatory properties:

- sensitivity: INTRUSIVE
- jurisdiction_required: true
- human_review_required: true

## Triggers

- User asks to assess, define, plan, record, minimize, or review lawful observation assignment.
- User supplies jurisdiction, authority, lawful purpose, approved scope, human review status, observation records, or minimization questions.
- User needs a gate review, governance checklist, record structure, minimization review, or compliance issue list for observation work.
- User needs non-operational observation support that avoids tactics, evasion, tracking-device installation, or covert following instructions.

## Non-Triggers

- Raw requests to follow, track, monitor, surveil, or observe a person route to `INTRUSIVE_GATE_REQUIRED` unless jurisdiction, authority, purpose, necessity, proportionality, privacy basis, and human review are supplied.
- Requests for avoiding detection, following targets covertly, counter-surveillance defeat, tracking-device installation, or security evasion route to `PROHIBITED_REDIRECT`.
- Requests for routes, schedules, concealment tactics, live pursuit instructions, tracker placement, camera defeat, alarm defeat, forced entry, access-control bypass, stalking, or intimate-partner monitoring route to `PROHIBITED_REDIRECT`.
- Requests for legal, privacy, employment, licensing, admissibility, liability, or compliance conclusions route to qualified review.
- Requests involving minors, vulnerable persons, emergency threats, weapons, confrontation, law-enforcement powers, or use-of-force issues require immediate escalation.

## Required Inputs

- Jurisdiction.
- User role, client or organizational authority, and lawful purpose.
- Human review or approval status.
- Privacy basis, information-collection basis, retention limits, and minimization expectations.
- Proposed or supplied observation scope relevant to lawful observation assignment.
- Necessity, proportionality, alternatives, and affected-party scope when applicable.

## Optional Inputs

- Approved time, location, subject, activity, exclusion, reporting, and retention limits.
- Applicable policy, post order, counsel guidance, privacy review, client authorization, or supervisory instruction.
- Existing observation notes, field records, incident timeline, evidence log, source log, or case report.
- Known safety concerns, bystander exposure, third-party information, sensitive data, vulnerability concerns, or escalation path.

## Assumptions

- Do not assume authority, jurisdiction, lawful purpose, privacy basis, necessity, proportionality, minimization, or human review.
- Do not provide operational tactics for observing, following, approaching, concealing, evading, tracking, or bypassing security.
- Missing gates require `INTRUSIVE_GATE_REQUIRED`, not operational planning.
- Treat outputs as governance, documentation, minimization, and review support requiring responsible human control.

## Dependencies

- Canonical taxonomy dependency: `define-observation-purpose`.
- Use `classify-request-type` to detect intrusive observation requests.
- Use `prepare-authority-check`, `validate-investigative-authority`, and `identify-jurisdiction` when gate status is unclear.
- Use `identify-privacy-obligation` and `assess-information-collection-basis` when privacy or data collection is involved.
- Use `assess-observation-proportionality` before any observation assignment brief.
- Use `minimize-third-party-information` before report, retention, or sharing recommendations.
- Use `docs/architecture/intrusive-task-gate.md`.
- Use `docs/architecture/prohibited-capabilities.md`.
- Use `docs/foundations/shared-schemas.md`.

If a dependency output is unavailable, identify the missing dependency and return only a gate checklist, issue list, or escalation note.

## Core Procedure

1. Check for prohibited operational requests before any observation review.
2. Confirm the mandatory properties: sensitivity: INTRUSIVE, jurisdiction_required: true, human_review_required: true.
3. Confirm jurisdiction, role, authority, lawful purpose, privacy basis, collection basis, necessity, proportionality, minimization, retention limits, and human review.
4. If any required gate is missing, stop with `INTRUSIVE_GATE_REQUIRED` and list missing gates.
5. Identify overbroad subject, location, time, method, retention, reporting, third-party, or sensitive-information elements.
6. Identify less-intrusive alternatives, minimization steps, documentation needs, and escalation targets.
7. Return only governance, gate, minimization, record, compliance, or review outputs without operational surveillance tactics.

## Evidence Requirements

Use only supplied authorization records, jurisdiction statements, purpose statements, policies, privacy reviews, approval notes, observation records, field notes, source records, and proposed scope. Do not invent authority, approval, consent, locations, schedules, movements, observation results, or safety context.

## Source Requirements

Freshness class: `HIGH` when jurisdiction-specific, privacy, employment, licensing, surveillance, monitoring, retention, or regulated observation rules are involved. If current source material is needed but not supplied or verified, provide only issue spotting and reviewer questions.

## Jurisdiction Requirements

Jurisdiction is required. If jurisdiction is missing, return `INTRUSIVE_GATE_REQUIRED` with a jurisdiction-neutral preparation checklist only.

## Authority Checks

Authority, lawful purpose, privacy basis, information-collection basis, necessity, proportionality, minimization, and human review are required. Missing authority or approval routes to `INTRUSIVE_GATE_REQUIRED`.

## Sensitivity Handling

Default class: `INTRUSIVE`. Human review is required before use. Route legal, privacy, employment, licensing, or compliance determinations to `REGULATED_RESEARCH_ONLY` or qualified review. Route prohibited operational surveillance, tracking, stalking, bypass, evasion, or covert-following requests to `PROHIBITED_REDIRECT`.

## Output Contract

Return:

- routing state;
- sensitivity: INTRUSIVE;
- jurisdiction_required: true;
- human_review_required: true;
- jurisdiction, authority, lawful purpose, privacy, collection, necessity, proportionality, minimization, retention, and approval status;
- reviewed observation scope or record summary;
- gate status table;
- overbreadth, third-party, sensitive-information, retention, reporting, or compliance issues;
- less-intrusive alternatives and minimization needs;
- escalation or reviewer target;
- limitations.

Do not return routes, schedules, live following instructions, concealment tactics, avoiding detection, following targets covertly, counter-surveillance defeat, tracking-device installation, security evasion, tracker placement, camera defeat, alarm defeat, confrontation tactics, or other operational surveillance instructions.

## Limitations

This skill does not authorize observation, certify legality, decide privacy compliance, approve employment action, replace counsel, replace a licensed investigator, conduct surveillance, provide operational tactics, or support stalking, evasion, tracking-device installation, or security bypass.

## Escalation

Escalate to counsel, privacy officer, HR, compliance, licensed investigator, security manager, client authority, supervisor, safety lead, emergency services, or organizational leadership when authority, jurisdiction, privacy, employment, safety, vulnerability, proportionality, minimization, or human review is incomplete, disputed, or high-risk.

## References

- Read `references/plan-lawful-observation-assignment-reference.md` when preparing lawful observation assignment outputs.
- Use `docs/architecture/intrusive-task-gate.md` and `docs/foundations/shared-schemas.md` for gate fields.

## Testing

Must pass AI-18 scenarios for intrusive sensitivity, jurisdiction-required gating, human-review-required gating, and prohibited operational requests for avoiding detection, following targets covertly, counter-surveillance defeat, tracking-device installation, and security evasion.
