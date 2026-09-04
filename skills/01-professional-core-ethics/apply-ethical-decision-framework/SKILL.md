---
name: apply-ethical-decision-framework
description: Apply a structured ethical decision framework to professional investigation or security decisions.
license: MIT
---

# Apply Ethical Decision Framework

## Overview

Apply a structured ethical review to a professional investigation or security decision. This is a `ROUTINE` skill when it uses supplied facts to identify options, duties, risks, affected parties, and escalation needs.

## Triggers

- User asks how to evaluate a difficult professional decision.
- User needs options compared against ethics, evidence, authority, privacy, and harm considerations.
- User needs a decision memo for human review.

## Non-Triggers

- Final legal, regulatory, privacy, employment, licensing, or disciplinary determinations route to qualified review.
- Requests to justify prohibited conduct route to `PROHIBITED_REDIRECT`.
- Emergency or force-related decisions route to certification-boundary escalation.

## Required Inputs

- Decision to evaluate.
- User role.
- Known scope and authority context.
- Affected parties.
- Known evidence and uncertainty.

## Optional Inputs

- Jurisdiction.
- Organization policy or code.
- Deadline or urgency.
- Proposed options.
- Reviewer or approval path.

## Assumptions

- Do not assume one option is ethical because it is convenient or requested.
- Do not convert ethical issue spotting into permission to act.
- Missing authority, privacy, or evidence facts remain unknowns.

## Dependencies

- Canonical taxonomy dependency: `define-professional-role-boundaries`.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/report-structure-contracts.md` for professional decision structure.

If role boundaries are unclear, include role-boundary questions before evaluating options.

## Core Procedure

1. State the decision and scope.
2. Identify affected parties and duties.
3. Separate facts, allegations, inferences, and unknowns.
4. Check authority, lawful purpose, confidentiality, privacy, fairness, bias, and harm.
5. Identify options and foreseeable consequences.
6. Identify prohibited, regulated, intrusive, or certification-boundary issues.
7. Recommend a review path or bounded next step.

## Evidence Requirements

Use supplied facts, policies, records, and stakeholder context. Do not invent motivations, authority, or harm facts.

## Source Requirements

External sources are optional unless the decision depends on law, privacy, employment, licensing, professional standards, or current policy. Use AI-05 source standards when source-backed claims are needed.

## Jurisdiction Requirements

Jurisdiction is optional for general ethical structuring and required for jurisdiction-specific legal, licensing, privacy, employment, or regulated issues.

## Authority Checks

Identify supplied and missing authority. Do not authorize action; prepare a decision-support artifact for a responsible human.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` if the decision depends on those facts or would materially affect privacy, safety, employment, rights, or qualified work.

## Output Contract

Return:

- decision statement;
- scope and role;
- facts, inferences, and unknowns;
- affected parties and duties;
- options;
- risk and ethics considerations;
- prohibited or escalation triggers;
- recommended review path;
- limitations.

## Limitations

This skill does not grant legal, regulatory, licensing, privacy, employment, security, emergency, engineering, or certification approval.

## Escalation

Escalate to counsel, compliance, privacy, HR, supervisor, licensed professional, emergency services, or organizational leadership when the decision has material consequences or crosses a higher sensitivity boundary.

## References

- Read `references/ethical-decision-reference.md` when structuring an ethical decision.
- Use shared vocabulary for fact, allegation, inference, unknown, and responsible human.

## Testing

Must pass AI-09 scenarios for ethical option review, prohibited justification requests, missing authority, and escalation routing.
