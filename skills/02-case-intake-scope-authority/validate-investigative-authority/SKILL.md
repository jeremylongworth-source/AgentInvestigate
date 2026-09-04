---
name: validate-investigative-authority
description: Issue-spot claimed investigative authority from supplied facts without granting legal or licensing authority.
license: MIT
---

# Validate Investigative Authority

## Overview

Check whether supplied facts support claimed investigative authority and identify missing authority evidence or review needs. This is a `REGULATED` control-layer skill for intake, authority, law, licensing, privacy, and compliance routing.

## Triggers

- User asks to classify, scope, validate, or prepare review for investigative authority.
- User supplies intake facts and needs bounded next-step routing.
- User needs missing authority, jurisdiction, privacy, licensing, consent, or compliance facts identified.
- User needs a safe review package before downstream investigative or security work.

## Non-Triggers

- Requests for final legal, licensing, privacy, employment, compliance, liability, or admissibility conclusions route to qualified review.
- Requests for surveillance, monitoring, screening, record access, or other sensitive action without authority and jurisdiction fail closed.
- Requests to impersonate, coerce, bypass consent, bypass access controls, hide conflicts, alter evidence, conceal reportable issues, or evade required review route to `PROHIBITED_REDIRECT`.

## Required Inputs

- User role and relationship to the matter.
- Requested activity or decision.
- Available authority basis.
- Jurisdiction or jurisdiction facts, if known.
- Affected parties, subjects, records, or information categories, if known.

## Optional Inputs

- Client, employer, contract, policy, post order, or mandate.
- Prior approvals, consent, notice, or review records.
- Relevant source material.
- Time sensitivity, escalation path, or reviewer role.

## Assumptions

- Do not accept claimed authority without supporting facts.
- Do not infer jurisdiction from user location alone.
- Missing authority, jurisdiction, consent, or privacy facts remain unknowns.
- Do not convert issue spotting into permission to act.

## Dependencies

- Canonical taxonomy dependency: `identify-client-role`.
- Canonical taxonomy dependency: `identify-jurisdiction`.
- Use `define-professional-role-boundaries` for role limits when role or authority is unclear.
- Use `separate-fact-from-inference` when supplied intake facts contain allegations or unsupported conclusions.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.

If any dependency output is unavailable, list the dependency as missing and continue only with bounded issue spotting.

## Core Procedure

1. Restate the requested activity, user role, jurisdiction status, and authority claim.
2. Separate supplied facts, claims, assumptions, unknowns, and unsupported conclusions.
3. Identify the applicable sensitivity class and authority requirement.
4. Check whether authority, jurisdiction, lawful purpose, consent, privacy basis, and review facts are present.
5. Identify regulated, intrusive, certification-boundary, or prohibited routing issues.
6. Return only bounded next steps, missing facts, source needs, and reviewer or escalation targets.

## Evidence Requirements

Use supplied intake facts, policies, contracts, mandates, approvals, consent records, source material, and case records. Do not invent authority, jurisdiction, consent, privacy basis, or compliance facts.

## Source Requirements

Use AI-05 source standards for legal, licensing, privacy, compliance, employment, or jurisdiction-specific claims. Prefer current primary sources and identify source freshness. Do not treat generic summaries as authority.

## Jurisdiction Requirements

Jurisdiction is required before regulated conclusions, source-backed legal research, privacy analysis, licensing analysis, or compliance escalation. Unknown or conflicting jurisdiction routes to `CLARIFY_SCOPE` or `REGULATED_RESEARCH_ONLY`.

## Authority Checks

Identify the user role, claimed authority, evidence of authority, affected parties, permitted scope, excluded scope, missing approvals, and required reviewer. Sensitive work must fail closed when authority or jurisdiction is missing.

## Sensitivity Handling

Default class: `REGULATED`. Provide source-backed issue spotting and fail closed when jurisdiction, authority, lawful purpose, privacy basis, or qualified review is missing. Do not make final legal, licensing, privacy, employment, or compliance determinations.

## Output Contract

Return:

- routing state;
- request classification;
- role and authority summary;
- jurisdiction status;
- supplied facts;
- assumptions and unknowns;
- required sources or records;
- gate status;
- escalation or reviewer target;
- prohibited boundaries;
- limitations.

## Limitations

This skill does not confer authority, approve investigative or security action, certify compliance, issue legal advice, or replace counsel, privacy, compliance, licensing, HR, supervisor, emergency, or qualified professional review.

## Escalation

Escalate to counsel, compliance, privacy, licensing authority, HR, supervisor, security manager, client decision maker, emergency services, or another qualified reviewer when authority, jurisdiction, consent, privacy, safety, regulated activity, intrusive work, or reporting duties are unclear or material.

## References

- Read `references/validate-investigative-authority-reference.md` when preparing investigative authority outputs.
- Use shared schemas for role, authority, jurisdiction, sensitivity, source, evidence, and escalation fields.

## Testing

Must pass AI-10 scenarios for ordinary research, workplace investigation, surveillance, personal background screening, unknown jurisdiction, prohibited requests, and conflicting client authority.
