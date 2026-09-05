---
name: assess-observation-proportionality
description: Assess whether a proposed observation activity is proportionate within supplied authority, purpose, privacy, and scope limits.
license: MIT
---

# Assess Observation Proportionality

## Overview

Assess proportionality for proposed observation or surveillance-governance work. This is an `INTRUSIVE` skill because observation can affect privacy, safety, employment, reputation, or lawful rights.

The skill does not create operational surveillance plans. It supports gate review, less-intrusive alternatives, documentation, and escalation.

Mandatory properties:

- sensitivity: INTRUSIVE
- jurisdiction_required: true
- human_review_required: true

## Triggers

- User asks whether proposed observation is proportionate.
- User asks to compare observation scope against purpose, authority, privacy, time, place, or alternatives.
- User supplies an approved observation concept and wants a review-ready proportionality assessment.
- User needs non-operational observation support that avoids tactics, evasion, tracking-device installation, or covert following instructions.

## Non-Triggers

- Raw requests to follow, track, monitor, surveil, or observe a person route through earlier intrusive gates first.
- Requests for avoiding detection, following targets covertly, counter-surveillance defeat, tracking-device installation, or security evasion route to `PROHIBITED_REDIRECT`.
- Requests for tactics, routes, schedules, concealment, evasion, tracker placement, camera defeat, alarm defeat, forced entry, access-control bypass, or stalking route to `PROHIBITED_REDIRECT`.
- Legal, privacy, employment, or licensing determinations route to qualified regulated review.

## Required Inputs

- Jurisdiction.
- User role and client or organizational authority.
- Lawful purpose.
- Subject or affected-party scope.
- Proposed observation scope.
- Privacy basis or review status.
- Information-collection basis.
- Necessity assessment.
- Less-intrusive alternatives considered.
- Human approval status.
- Human review status.

## Optional Inputs

- Approved time limits.
- Approved locations or exclusions.
- Retention and reporting limits.
- Applicable policy, post order, or counsel guidance.
- Known safety or vulnerability concerns.

## Assumptions

- Do not assume authority, consent, privacy basis, necessity, proportionality, or human approval.
- Do not infer lawful purpose from suspicion alone.
- Missing gates require stop or escalation, not operational planning.
- Do not provide operational tactics for avoiding detection, following targets covertly, counter-surveillance defeat, tracking-device installation, or security evasion.

## Dependencies

- Canonical taxonomy dependency: `assess-observation-necessity`.
- Required upstream gates include `classify-request-type`, `identify-jurisdiction`, `validate-investigative-authority`, `assess-lawful-purpose`, `identify-privacy-obligation`, `assess-information-collection-basis`, and `assess-observation-authorization`.
- Use `docs/architecture/intrusive-task-gate.md`.
- Use `docs/foundations/shared-schemas.md` for authority and sensitivity fields.

If dependencies are not implemented or the user has not supplied equivalent reviewed inputs, return `INTRUSIVE_GATE_REQUIRED`.

## Core Procedure

1. Check for prohibited conduct before evaluating proportionality.
2. Confirm the mandatory properties: sensitivity: INTRUSIVE, jurisdiction_required: true, human_review_required: true.
3. Confirm jurisdiction, role, authority, lawful purpose, privacy basis, collection basis, necessity, alternatives, and human review.
4. If any required gate is missing, stop and list the missing gates.
5. Compare proposed observation scope to the stated purpose.
6. Identify overbroad subject, location, time, method, retention, reporting, third-party, or sensitive-information elements.
7. Identify less-intrusive alternatives and whether they were considered.
8. Produce a review-ready proportionality assessment with limitations and no operational surveillance tactics.

## Evidence Requirements

Use only supplied authorization records, purpose statements, policy constraints, privacy review notes, source descriptions, and proposed scope. Do not add operational details or infer approval from incomplete evidence.

## Source Requirements

Freshness class: `HIGH` when privacy, employment, surveillance, monitoring, licensing, or jurisdiction-specific rules are involved.

If source material is needed but not supplied or currently verified, provide an issue-spotting or preparation checklist only.

## Jurisdiction Requirements

Jurisdiction is required before substantive proportionality assessment. If jurisdiction is missing, stop and request it or route to a jurisdiction-neutral preparation checklist.

## Authority Checks

Authority, lawful purpose, privacy basis, collection basis, necessity, less-intrusive alternatives, and human review are required before any bounded proportionality assessment. Missing authority or approval routes to `INTRUSIVE_GATE_REQUIRED`.

## Sensitivity Handling

Default class: `INTRUSIVE`.

Use `INTRUSIVE_GATE_REQUIRED` until all gates are satisfied. Human review is required before use. Route legal, privacy, employment, or licensing determinations to `REGULATED_RESEARCH_ONLY` or qualified review. Route prohibited tracking, stalking, bypass, evasion, covert following, or tracking-device installation to `PROHIBITED_REDIRECT`.

## Output Contract

Return:

- sensitivity: INTRUSIVE;
- jurisdiction_required: true;
- human_review_required: true;
- scope reviewed;
- gate status table;
- proportionality factors;
- overbreadth or minimization issues;
- less-intrusive alternatives;
- stop conditions;
- human-review or approval need;
- limitations.

Do not return observation routes, schedules, concealment, evasion guidance, avoiding detection, following targets covertly, counter-surveillance defeat, tracking-device installation, security evasion, tracker placement, camera defeat, alarm defeat, or confrontation tactics.

## Limitations

This skill does not authorize observation, certify legality, decide privacy compliance, approve employment action, replace counsel, replace a licensed investigator, or provide surveillance tactics, tracking-device installation, covert-following guidance, counter-surveillance defeat, or security evasion.

## Escalation

Escalate to counsel, privacy officer, HR, compliance, licensed investigator, client authority, or organizational leadership when authority, privacy, employment, legal, safety, proportionality, or human approval is incomplete or disputed.

## References

- Read `references/observation-proportionality-checklist.md` before producing a proportionality assessment.
- Use `docs/architecture/intrusive-task-gate.md`.
- Use `docs/foundations/shared-schemas.md` for gate fields.

## Testing

Must pass AI-08 scenarios for:

- complete-gate proportionality assessment;
- missing authority;
- missing consent or privacy basis;
- raw intrusive observation request;
- prohibited tracking or stalking;
- output omits operational surveillance tactics.

Must also pass AI-18 scenarios for sensitivity: INTRUSIVE, jurisdiction_required: true, human_review_required: true, and prohibited operational requests for avoiding detection, following targets covertly, counter-surveillance defeat, tracking-device installation, and security evasion.
