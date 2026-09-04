---
name: identify-escalation-requirement
description: Identify when investigation or security work should escalate to a responsible human or qualified reviewer.
license: MIT
---

# Identify Escalation Requirement

## Overview

Identify whether supplied facts require escalation to a responsible human, qualified reviewer, supervisor, emergency services, or another function. This is a `ROUTINE` professional-core skill that supports routing and handoff.

## Triggers

- User asks who should review or approve a matter.
- User asks whether a case, incident, report, or decision needs escalation.
- User needs escalation triggers and handoff questions.

## Non-Triggers

- Emergency instructions, force, weapons, restraints, life-safety, or technical action route to certification-boundary escalation.
- Legal, privacy, employment, licensing, or compliance determinations route to regulated review.
- Requests to avoid escalation, reporting, or qualified review route to refusal or `PROHIBITED_REDIRECT`.

## Required Inputs

- Task or incident summary.
- User role.
- Known risk, consequence, or sensitivity.
- Available evidence or source context.

## Optional Inputs

- Jurisdiction.
- Policy, post order, contract, or approval path.
- Affected parties.
- Time sensitivity.

## Assumptions

- Do not assume escalation is unnecessary because the user prefers speed.
- Do not assume the user has authority to decide.
- Missing risk, authority, or jurisdiction facts may themselves require escalation.

## Dependencies

- Canonical taxonomy dependency: `assess-duty-of-care`.
- Use `docs/architecture/authority-routing.md`.
- Use `docs/foundations/shared-schemas.md`.

If duty-of-care analysis is missing, include care and consequence questions in the escalation output.

## Core Procedure

1. Identify the task, role, sensitivity, and potential consequences.
2. Check for prohibited, regulated, intrusive, emergency, certification, privacy, employment, safety, or evidence-integrity triggers.
3. Identify missing jurisdiction, authority, consent, source, or evidence facts.
4. Select likely escalation target.
5. State stop conditions and information to preserve.
6. Produce a concise escalation recommendation or checklist.

## Evidence Requirements

Use supplied case, incident, risk, authority, source, or policy facts. Preserve unknowns and do not invent escalation authority.

## Source Requirements

External sources are not needed for general escalation routing. Current source verification is required for jurisdiction-specific legal, regulatory, privacy, emergency, or technical escalation requirements.

## Jurisdiction Requirements

Jurisdiction is optional for general escalation issue spotting and required for jurisdiction-specific regulated obligations.

## Authority Checks

Identify whether the user can decide, notify, preserve, pause, or escalate. Do not authorize final action.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` when escalation depends on those higher-risk facts.

## Output Contract

Return:

- trigger summary;
- sensitivity or routing state;
- missing facts;
- escalation target;
- information to preserve;
- stop condition;
- safe next step;
- limitations.

## Limitations

This skill does not provide legal advice, emergency instructions, use-of-force guidance, technical signoff, licence approval, employment approval, or privacy compliance certification.

## Escalation

Escalation targets may include emergency services, counsel, compliance, privacy officer, HR, regulator, licensed investigator, licensed security manager, supervisor, security command, engineer, fire/life-safety professional, or organizational leadership.

## References

- Read `references/escalation-routing-reference.md` when selecting an escalation path.
- Use authority routing and certification-boundary contracts.

## Testing

Must pass AI-09 scenarios for routine escalation routing, missing authority, emergency triggers, regulated triggers, and anti-escalation requests.
