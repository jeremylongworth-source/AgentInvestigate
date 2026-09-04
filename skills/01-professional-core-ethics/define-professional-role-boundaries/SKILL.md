---
name: define-professional-role-boundaries
description: Define professional role boundaries for investigation or security work without expanding authority.
license: MIT
---

# Define Professional Role Boundaries

## Overview

Define the boundary between the user's role, the client or organization, the requested work, and the limits of AgentInvestigate. This is a `ROUTINE` shared professional-core skill unless the request depends on law, licensing, privacy, intrusive work, or certification-boundary action.

## Triggers

- User asks what role is appropriate for a task.
- User asks whether work belongs to private investigation, private security, or another reviewer.
- User needs a scope-safe role-boundary statement for a plan, report, or handoff.

## Non-Triggers

- Licensing, legal, privacy, employment, or regulatory determinations route to regulated issue spotting.
- Emergency, force, weapons, restraints, life-safety, engineering, or qualified technical action routes to certification-boundary escalation.
- Requests to impersonate, bypass authority, coerce, surveil without gates, or access private systems route to `PROHIBITED_REDIRECT`.

## Required Inputs

- User role or proposed role.
- Requested task or artifact.
- Professional branch: private investigation, private security, shared, or unclear.
- Known client, organization, or authority context.

## Optional Inputs

- Jurisdiction.
- Licence, policy, contract, post order, or supervisor context.
- Affected parties.
- Intended output and audience.

## Assumptions

- Do not infer authority from job title, confidence, or user preference.
- Do not collapse private investigation and private security into one generic role.
- If role or authority is unclear, return boundaries and questions rather than approval.

## Dependencies

- No canonical taxonomy dependencies.
- Use `docs/architecture/domain-contract.md`.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.

## Core Procedure

1. Identify the requested work and professional branch.
2. Identify the user's stated role and any client or organization context.
3. Separate allowed decision support from authority, licensing, or certification claims.
4. List work that requires qualified review or another role.
5. State prohibited or out-of-scope role expansion.
6. Produce a concise boundary statement and next questions.

## Evidence Requirements

Use only supplied role, policy, contract, post-order, case, or organizational facts. Preserve unknown role, authority, and jurisdiction facts.

## Source Requirements

External sources are normally unnecessary. If the boundary depends on current law, licensing, privacy, employment, or regulatory obligations, route to AI-05 source-backed issue spotting.

## Jurisdiction Requirements

Jurisdiction is optional for general role framing and required for jurisdiction-specific licensing, legal, privacy, or regulated authority questions.

## Authority Checks

Identify what authority is supplied, missing, or out of scope. Do not state that the user is authorized, licensed, certified, or approved.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` when role boundaries depend on those higher-sensitivity facts.

## Output Contract

Return:

- requested work;
- stated role and branch;
- allowed decision-support boundary;
- authority or role gaps;
- out-of-scope or prohibited role expansion;
- escalation or review target;
- concise boundary statement.

## Limitations

This skill does not grant authority, licence, certification, legal status, police power, emergency authority, employment authority, or security authority.

## Escalation

Escalate to counsel, compliance, privacy, HR, regulator, licensed investigator, licensed security manager, supervisor, emergency services, or qualified professional when role limits depend on those functions.

## References

- Read `references/role-boundary-checklist.md` when drafting a role-boundary statement.
- Use the domain contract for private investigation and private security boundaries.
- Use shared schemas for role, authority, jurisdiction, and sensitivity fields.

## Testing

Must pass AI-09 scenarios for routine role-boundary definition, unclear role, role expansion, and prohibited authority claims.
