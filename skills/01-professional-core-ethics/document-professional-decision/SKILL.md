---
name: document-professional-decision
description: Document a professional investigation or security decision with facts, reasoning, limitations, and review needs.
license: MIT
---

# Document Professional Decision

## Overview

Document a professional decision, routing choice, review result, or bounded next step with facts, assumptions, reasoning, limitations, and escalation needs. This is a `ROUTINE` professional-core skill when it records supplied information without approving regulated or intrusive action.

## Triggers

- User asks to document why a decision was made.
- User needs a decision note for a case file, incident log, report, or handoff.
- User wants facts, reasoning, unknowns, limitations, and next actions captured.

## Non-Triggers

- Requests to fabricate, backdate, alter, hide, or strengthen a decision record route to `PROHIBITED_REDIRECT`.
- Final legal, privacy, employment, licensing, compliance, or certification approvals route to qualified review.
- Intrusive action documentation does not substitute for required gates or human approval.

## Required Inputs

- Decision or proposed decision.
- Scope.
- Supplied facts and evidence.
- Decision maker or responsible human when known.
- Known limitations or review needs.

## Optional Inputs

- Date and status.
- Alternatives considered.
- Source IDs.
- Policy or procedure context.
- Approval record.

## Assumptions

- Do not invent decision maker, approval, date, evidence, rationale, or review.
- Do not clean up records to conceal uncertainty or make the decision look stronger.
- If the decision is not yet approved, label it as draft or pending review.

## Dependencies

- Canonical taxonomy dependency: `separate-fact-from-inference`.
- Use `docs/foundations/report-structure-contracts.md` for the `case-action-log` and professional decision structure.
- Use `docs/standards/output-contract-standard.md`.

If fact/inference separation has not been done, classify supplied facts and inferences before drafting the decision record.

## Core Procedure

1. Identify the decision, scope, and intended record.
2. Separate facts, allegations, assumptions, inferences, unknowns, and limitations.
3. Identify source IDs and evidence used.
4. Record alternatives considered when supplied.
5. Identify authority, review status, escalation, and stop conditions.
6. Draft a neutral decision record.

## Evidence Requirements

Use only supplied facts, evidence, source IDs, approvals, policy context, and decision rationale. Do not backfill missing rationale or approval.

## Source Requirements

External sources are normally unnecessary. Source-backed legal, regulatory, privacy, employment, licensing, or compliance rationale requires AI-05 source standards.

## Jurisdiction Requirements

Jurisdiction is optional for routine decision documentation and required when the decision depends on jurisdiction-specific law, licensing, privacy, employment, or regulated authority.

## Authority Checks

Identify decision maker, approval status, and authority basis if supplied. Missing authority must be shown as missing or pending.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` when the decision depends on those higher-sensitivity matters.

## Output Contract

Return:

- decision title;
- date or status;
- scope;
- decision maker or responsible human;
- facts and sources used;
- reasoning;
- assumptions and unknowns;
- alternatives considered;
- review or approval status;
- limitations and next action.

## Limitations

This skill documents a decision record. It does not create authority, approve action, certify compliance, erase uncertainty, or replace qualified review.

## Escalation

Escalate when the decision involves regulated issues, intrusive work, emergency or certified action, material consequences, missing authority, contradictory evidence, or possible prohibited conduct.

## References

- Read `references/professional-decision-record-reference.md` when drafting a decision record.
- Use shared report structure contracts for case-action-log and closure-style fields.

## Testing

Must pass AI-09 scenarios for neutral decision records, missing approval, unsupported rationale, prohibited record alteration, and output-format compliance.
