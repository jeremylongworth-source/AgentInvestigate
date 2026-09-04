---
name: assess-duty-of-care
description: Assess possible duty-of-care considerations in supplied investigation or security facts without making legal conclusions.
license: MIT
---

# Assess Duty Of Care

## Overview

Assess possible duty-of-care considerations from supplied professional context. This is a `ROUTINE` issue-spotting skill unless the user asks for legal, regulatory, employment, privacy, emergency, or certification conclusions.

## Triggers

- User asks what care, safety, confidentiality, escalation, or harm-prevention issues may matter.
- User needs duty-of-care questions for counsel, supervisor, security manager, HR, privacy, or compliance review.
- User asks how to document care-related decisions.

## Non-Triggers

- Final legal duty, negligence, liability, employment, privacy, or compliance conclusions route to regulated qualified review.
- Emergency, force, weapons, restraints, life-safety, engineering, or certified technical questions route to certification-boundary escalation.
- Requests to ignore safety, privacy, or reporting obligations route to refusal or `PROHIBITED_REDIRECT`.

## Required Inputs

- User role and task.
- Affected parties.
- Known risks, harms, or safety concerns.
- Current scope and authority context.

## Optional Inputs

- Jurisdiction.
- Policy, contract, post order, or procedure.
- Incident facts or case context.
- Time sensitivity.

## Assumptions

- Do not determine legal duty or liability.
- Do not assume emergency authority or safety qualifications.
- Missing risk or affected-party facts remain unknowns.

## Dependencies

- Canonical taxonomy dependency: `define-professional-role-boundaries`.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.

If role boundaries are unclear, include role and authority questions before care analysis.

## Core Procedure

1. Identify role, scope, authority, and affected parties.
2. Identify supplied risk, harm, safety, privacy, confidentiality, or escalation facts.
3. Separate known facts from assumptions and unknowns.
4. Flag possible care considerations and material consequences.
5. Identify needed review, documentation, or escalation.
6. Provide bounded next steps that do not replace qualified review.

## Evidence Requirements

Use supplied facts, policies, contracts, incident records, or source material. Do not invent risk, harm, duty, or liability facts.

## Source Requirements

External sources are optional for general issue spotting. Legal, regulatory, safety, employment, privacy, or jurisdiction-specific duty claims require AI-05 source standards and qualified review.

## Jurisdiction Requirements

Jurisdiction is optional for general care issue spotting and required for legal, regulatory, privacy, employment, safety, or liability conclusions.

## Authority Checks

Identify user role and whether they have authority to act, notify, preserve records, or escalate. Do not approve intervention or final action.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED` for legal or compliance determinations, `INTRUSIVE` for sensitive personal information or surveillance, and `CERTIFICATION_BOUNDARY` for emergency, force, life-safety, or technical qualified work.

## Output Contract

Return:

- role and scope;
- affected parties;
- care considerations;
- risk or harm facts;
- unknowns;
- documentation needs;
- escalation or review target;
- limitations.

## Limitations

This skill does not determine legal duty, breach, negligence, liability, compliance, employment action, emergency response, or certification status.

## Escalation

Escalate to counsel, compliance, privacy, HR, supervisor, security manager, emergency services, qualified trainer, engineer, fire/life-safety professional, or organizational leadership when consequences are material.

## References

- Read `references/duty-of-care-reference.md` when preparing care issue spotting.
- Use shared schemas for role, authority, sensitivity, and escalation fields.

## Testing

Must pass AI-09 scenarios for care issue spotting, emergency escalation, legal-duty requests, and missing role facts.
