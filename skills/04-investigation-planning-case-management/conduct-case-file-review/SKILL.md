---
name: conduct-case-file-review
description: Conduct a structured case-file review from supplied logs, notes, evidence, and decisions.
license: MIT
---

# Conduct Case File Review

## Overview

Reviews case-file completeness, evidence links, decisions, gaps, inconsistencies, risks, and next actions. This is a `ROUTINE` case-planning and case-management skill for bounded professional investigation work.

## Triggers

- User asks to plan, structure, review, update, or close case file review.
- User supplies scoped matter facts and needs case-management output.
- User needs gaps, dependencies, tasks, milestones, status, retention, or closure points organized.
- User needs case-management support after intake, authority, and scope gates.

## Non-Triggers

- Requests for legal, licensing, privacy, employment, compliance, liability, or admissibility conclusions route to qualified review.
- Requests for surveillance, monitoring, screening, record access, or other sensitive action without authority and jurisdiction fail closed.
- Requests to fabricate, backdate, alter, conceal, overstate, or strengthen case records, notes, logs, timelines, findings, or closure summaries route to `PROHIBITED_REDIRECT`.

## Required Inputs

- Case scope or requested case-management output.
- User role and authority context.
- Available jurisdiction and authority status.
- Supplied facts, records, sources, actions, or decisions relevant to case file review.

## Optional Inputs

- Investigation plan, case log, evidence log, notes, or prior status update.
- Stakeholders, subjects, reviewers, deadlines, milestones, and resource constraints.
- Retention, privacy, legal hold, or closure requirements.
- Known gaps, risks, blockers, or escalation paths.

## Assumptions

- Do not infer authority, jurisdiction, or scope from silence.
- Do not create facts, records, dates, actions, sources, or findings not supplied.
- Distinguish planned work, completed work, open work, assumptions, and unknowns.
- Treat case-management outputs as drafts for responsible human review.

## Dependencies

- Canonical taxonomy dependency: `maintain-case-action-log`.
- Use `define-professional-role-boundaries` when role limits are unclear.
- Use `prepare-authority-check` before downstream sensitive work.
- Use `separate-fact-from-inference` when case materials mix facts, allegations, inferences, and unknowns.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.
- Use `docs/foundations/report-structure-contracts.md`.

If a dependency output is unavailable, identify the missing dependency and continue only with bounded case-management drafting.

## Core Procedure

1. Confirm case scope, role, jurisdiction status, authority status, and requested case-management output.
2. Separate supplied facts, actions, decisions, sources, assumptions, inferences, and unknowns.
3. Identify dependencies, constraints, deadlines, reviewers, risks, and open gates.
4. Organize the output using the relevant case-management structure.
5. Flag missing facts, unsupported conclusions, stale records, and required review.
6. Return bounded next steps that do not authorize intrusive, regulated, or prohibited action.

## Evidence Requirements

Use supplied case records, notes, logs, evidence references, source material, approvals, decisions, and prior outputs. Do not invent events, dates, actions, evidence, findings, resources, or closure status.

## Source Requirements

External sources are optional for routine case management. Legal, privacy, licensing, employment, compliance, retention, or jurisdiction-specific claims require AI-05 source standards and qualified review.

## Jurisdiction Requirements

Jurisdiction is optional for routine planning format and required before legal, privacy, licensing, retention, employment, compliance, or regulated-source conclusions. Unknown jurisdiction must be preserved as an open gate.

## Authority Checks

Identify the user role, authority status, scope basis, approval status, and review owner. Do not proceed from case-management drafting into sensitive action when authority, jurisdiction, lawful purpose, consent, or privacy basis is missing.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` when the output would affect legal, privacy, licensing, employment, surveillance, sensitive personal information, emergency, safety, force, or qualified technical work.

## Output Contract

Return:

- routing state;
- case scope;
- role and authority status;
- jurisdiction status;
- supplied facts and source references;
- planned, completed, open, and blocked work;
- assumptions and unknowns;
- gaps and risks;
- reviewer or escalation target;
- prohibited boundaries;
- limitations.

## Limitations

This skill does not approve investigative action, authorize surveillance or screening, certify compliance, create findings, determine liability, replace legal or professional review, or alter the evidentiary record.

## Escalation

Escalate to counsel, compliance, privacy, HR, supervisor, client decision maker, security manager, emergency services, or another qualified reviewer when case-management work exposes missing authority, unclear jurisdiction, sensitive personal information, regulated activity, intrusive work, safety risk, or reportable issues.

## References

- Read `references/conduct-case-file-review-reference.md` when preparing case file review outputs.
- Use shared schemas and report structure contracts for case-intake, investigation-plan, case-action-log, case-status, retention, review, gap, and closure fields.

## Testing

Must pass AI-11 scenarios for plans, questions, timelines, leads, resources, milestones, logs, notes, status, retention, review, gaps, closure, and prohibited record manipulation.
