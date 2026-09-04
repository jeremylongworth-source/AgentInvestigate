---
name: assess-conflict-of-interest
description: Assess supplied facts for potential professional conflicts of interest in investigation or security work.
license: MIT
---

# Assess Conflict Of Interest

## Overview

Assess supplied relationship, role, duty, confidentiality, and interest facts for possible conflict-of-interest issues. This is a `ROUTINE` professional-core skill that flags review needs and does not decide legal disqualification or professional discipline.

## Triggers

- User asks whether a relationship, prior involvement, duty, client interest, or personal interest creates a conflict.
- User needs conflict issues organized before accepting or continuing work.
- User needs conflict questions for a responsible human.

## Non-Triggers

- Final legal, regulatory, employment, licensing, or professional-discipline determinations route to qualified review.
- Requests to conceal conflicts, hide evidence, or bypass disclosure route to `PROHIBITED_REDIRECT`.
- Intrusive collection to investigate a conflict routes through intrusive gates.

## Required Inputs

- Proposed matter or task.
- User role.
- Parties, subjects, clients, or stakeholders.
- Known relationships, prior involvement, interests, duties, or confidentiality obligations.

## Optional Inputs

- Jurisdiction.
- Organization policy.
- Professional code or contract terms supplied by the user.
- Intended reviewer or decision maker.

## Assumptions

- Do not infer absence of conflict from silence.
- Do not decide legal disqualification.
- Treat missing relationship facts as unknowns.

## Dependencies

- Canonical taxonomy dependency: `define-professional-role-boundaries`.
- Use `docs/foundations/report-structure-contracts.md` for the `conflict-check` contract.
- Use `docs/foundations/professional-vocabulary.md`.

If `define-professional-role-boundaries` has not been run, include role-boundary questions in the output.

## Core Procedure

1. Identify matter scope, role, and affected parties.
2. List supplied relationships, interests, prior involvement, duties, and confidentiality facts.
3. Separate facts from assumptions and unknowns.
4. Identify possible conflict indicators and severity.
5. Identify disclosure, recusal, review, or information-barrier questions.
6. Produce a conflict-check summary for human review.

## Evidence Requirements

Use only supplied relationship, policy, contract, communication, or matter facts. Do not infer hidden relationships or motivations.

## Source Requirements

External sources are normally unnecessary. If the assessment depends on professional rules, law, licensing, privacy, or employment obligations, use AI-05 source standards and route to regulated review.

## Jurisdiction Requirements

Jurisdiction is optional for general conflict issue spotting and required for jurisdiction-specific legal, regulatory, licensing, or professional-rule interpretation.

## Authority Checks

Confirm the user is seeking issue spotting or preparation for review. Do not approve continued work or disclosure decisions.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED` for legal, licensing, employment, privacy, or professional-rule determinations. Upgrade to `INTRUSIVE` if conflict review requires sensitive personal information collection.

## Output Contract

Return:

- matter scope;
- parties and roles;
- supplied conflict facts;
- potential conflict indicators;
- unknowns;
- review questions;
- recommended escalation or decision owner;
- limitations.

## Limitations

This skill does not determine legal conflict, waiver validity, discipline, privilege, confidentiality law, employment action, or authority to proceed.

## Escalation

Escalate to counsel, compliance, privacy, HR, organizational leadership, regulator, licensed investigator, licensed security manager, or supervisor when consequences are material.

## References

- Read `references/conflict-check-reference.md` when preparing a conflict issue summary.
- Use the `conflict-check` report contract.

## Testing

Must pass AI-09 scenarios for conflict issue spotting, missing relationship facts, concealment requests, and escalation needs.
