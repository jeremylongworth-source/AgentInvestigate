---
name: select-screening-source-type
description: Select appropriate supplied or proposed screening source types from purpose, consent, relevance, and public-record constraints.
license: MIT
---

# Select Screening Source Type

## Overview

Selects source categories while distinguishing public records, supplied records, licensed databases, and barred sources. This is an `INTRUSIVE` background screening and due diligence skill for professional investigation support.

AI-20 required split:

- `PERSON SCREENING`
- `ENTITY DUE DILIGENCE`

Personal screening requires stronger privacy and authority controls than entity due diligence.

AI-20 integration requirements:

- `consent`
- `relevance`
- `public records`
- `conflicting identities`
- `adverse information`
- `unresolved records`
- `bias risk`

## Triggers

- User asks to define, assess, verify, select, evaluate, identify, resolve, prepare, or review screening source selection.
- User supplies a screening purpose, authority basis, consent record, public records, source list, record match, conflicting identities, adverse information, unresolved records, or due-diligence material.
- User needs the AI-20 flow organized across purpose, authority, consent, source selection, source reliability, record relevance, identity ambiguity, discrepancy resolution, adverse information review, summary.
- User needs PERSON SCREENING or ENTITY DUE DILIGENCE support without deciding eligibility, adverse action, legal liability, or criminal guilt.

## Non-Triggers

- Requests to decide employment eligibility, tenant eligibility, creditworthiness, criminal guilt, legal liability, adverse action, or final accept/reject outcomes route to qualified human review.
- Requests to run, obtain, scrape, buy, or access background checks, credit reports, protected records, private databases, credentials, private accounts, sealed records, or non-public personal information route to `PROHIBITED_REDIRECT` unless independently authorized and handled outside the skill by qualified users.
- Requests to invent consent, infer consent from silence, bypass consent, ignore relevance, suppress conflicting identities, hide unresolved records, or overstate adverse information route to `PROHIBITED_REDIRECT`.
- Requests for legal, employment, tenant, credit, criminal, regulatory, privacy, consumer-reporting, admissibility, compliance, or adverse-action conclusions route to qualified review.
- PERSON SCREENING work requires stronger privacy and authority controls than ENTITY DUE DILIGENCE, including clear consent, relevance, jurisdiction, identity, source, and human-review gates.

## Required Inputs

- Screening or due-diligence purpose, PERSON SCREENING or ENTITY DUE DILIGENCE classification, user role, authority basis, jurisdiction, consent status, and review boundary.
- Supplied records, public records, source descriptions, source provenance, identifiers, entity details, adverse information, conflicts, unresolved records, or draft summary relevant to screening source selection.
- Intended use, relevance criteria, source access basis, freshness expectations, and known legal, privacy, employment, tenant, credit, or consumer-reporting constraints.
- Known limitations, disputed identity matches, conflicting identities, bias risk, unresolved records, and required human approvals.

## Optional Inputs

- Existing case scope, authority check, consent form, record request, public-record source list, source-reliability assessment, relevance matrix, identity analysis, discrepancy log, or due-diligence summary.
- Applicable policy, engagement letter, jurisdiction note, privacy review, consumer-reporting review, retention rule, reporting format, or reviewer instruction.
- Known source gaps, disputed identifiers, record age, expungement/sealing concern, name-change context, entity aliases, beneficial ownership context, sanctions/watchlist note, or escalation path.
- Preferred output format, audience, confidence labels, issue taxonomy, exhibit labels, or case-management destination.

## Assumptions

- Do not invent consent, authority, jurisdiction, identifiers, public records, adverse information, source reliability, corroboration, approvals, or legal standards.
- Keep PERSON SCREENING distinct from ENTITY DUE DILIGENCE. Personal screening requires stronger privacy and authority controls.
- Keep consent, relevance, public records, conflicting identities, adverse information, unresolved records, and bias risk visible in the output.
- Do not convert public-record hits, same-name matches, allegations, unresolved records, or source conflicts into confirmed identity matches or adverse conclusions.
- Treat outputs as draft screening and due-diligence support requiring responsible human review before consequential use.

## Dependencies

- Canonical taxonomy dependency: `verify-screening-consent`.
- Use `define-screening-purpose`, `assess-background-screening-authority`, and `verify-screening-consent` before personal screening support.
- Use `select-screening-source-type`, `assess-screening-source-reliability`, and `evaluate-record-relevance` before using public records or adverse information.
- Use `assess-identity-ambiguity`, `identify-screening-identity-ambiguity`, and `resolve-screening-discrepancy` when records involve conflicting identities, same-name ambiguity, or unresolved records.
- Use `identify-investigative-bias` and `separate-fact-from-inference` when bias risk, adverse information, or unsupported inferences appear.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.
- Use `docs/foundations/report-structure-contracts.md`.

If a dependency output is unavailable, identify the missing dependency and continue only with bounded issue spotting, draft structure, or escalation notes.

## Core Procedure

1. Confirm purpose, user role, authority, jurisdiction, consent, intended use, sensitivity, and reviewer boundary.
2. Classify the work as PERSON SCREENING or ENTITY DUE DILIGENCE and apply stronger privacy and authority controls to PERSON SCREENING.
3. Check for requests to decide employment eligibility, tenant eligibility, creditworthiness, criminal guilt, legal liability, adverse action, bypass consent, ignore relevance, suppress conflicting identities, conceal unresolved records, or overstate adverse information.
4. Organize supplied material around the AI-20 flow: purpose, authority, consent, source selection, source reliability, record relevance, identity ambiguity, discrepancy resolution, adverse information review, summary.
5. Assess consent, relevance, public records, source reliability, conflicting identities, adverse information, unresolved records, and bias risk.
6. Preserve source limits, identity uncertainty, record age, stale records, jurisdiction gaps, consent gaps, proportionality concerns, unresolved records, and required reviewer questions.
7. Return bounded background-screening or due-diligence support without deciding eligibility, adverse action, legal compliance, criminal guilt, legal liability, or final suitability.

## Evidence Requirements

Use only supplied screening purpose, authority checks, consent records, public records, source logs, identity materials, relevance criteria, adverse information, discrepancy records, and due-diligence drafts. Do not invent consent, records, matches, identifiers, corroboration, adverse information, or approvals.

## Source Requirements

Public records and other screening sources must include provenance, access basis, date, jurisdiction, freshness, reliability, and relevance limits. Do not provide instructions for unauthorized database access, credential acquisition, private-account compromise, deceptive acquisition of protected records, or non-public personal information collection.

## Jurisdiction Requirements

Jurisdiction is required for PERSON SCREENING and ENTITY DUE DILIGENCE when records, consent, privacy, consumer reporting, employment, tenant, credit, criminal, regulatory, public-record, or adverse-information implications exist. Unknown jurisdiction remains an open gate.

## Authority Checks

Confirm lawful purpose, client authority, user role, consent status, source access basis, intended use, relevance standard, privacy review, human approval, and qualified review where needed. PERSON SCREENING requires stronger privacy and authority controls than ENTITY DUE DILIGENCE.

## Sensitivity Handling

Default class: `INTRUSIVE`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` routing when screening or due diligence involves consumer reports, employment or tenant decisions, credit, criminal records, protected characteristics, minors, medical or disability information, sealed or expunged records, sanctions/watchlists, non-public personal information, surveillance, adverse action, or material consequences.

## Output Contract

Return:

- routing state;
- PERSON SCREENING or ENTITY DUE DILIGENCE classification;
- purpose, authority, jurisdiction, consent, intended use, relevance, source, privacy, and review status;
- public records and supplied records used, with provenance, freshness, reliability, and limitations;
- identity match status, conflicting identities, unresolved records, adverse information, bias risk, and confidence limits;
- gaps, contradictions, source limits, relevance concerns, consent gaps, and reviewer questions;
- prohibited decision check for employment eligibility, tenant eligibility, creditworthiness, criminal guilt, legal liability, and adverse action;
- escalation or reviewer target;
- limitations and safe next steps.

Do not decide eligibility, suitability, adverse action, criminal guilt, legal liability, consumer-reporting compliance, privacy compliance, or final screening outcomes.

## Limitations

This skill does not replace counsel, compliance, privacy, HR, tenant-screening, credit, licensed investigator, or qualified reviewer judgment. It does not run background checks, access databases, obtain reports, decide eligibility, decide adverse action, certify legal compliance, or determine criminal guilt or legal liability.

## Escalation

Escalate to counsel, compliance, privacy, HR, client authority, licensed investigator, consumer-reporting specialist, or another qualified reviewer when work involves PERSON SCREENING, missing consent, unclear authority, adverse information, conflicting identities, unresolved records, bias risk, protected characteristics, sealed or expunged records, criminal records, credit, employment, tenant screening, sanctions/watchlists, privacy issues, or material consequences.

## References

- Read `references/select-screening-source-type-reference.md` when preparing screening source selection outputs.
- Use shared schemas and report structure contracts for purpose, consent, authority, source, record, relevance, identity, discrepancy, adverse-information, summary, confidence, and escalation fields.

## Testing

Must pass AI-20 scenarios for PERSON SCREENING versus ENTITY DUE DILIGENCE, stronger privacy and authority controls for personal screening, and integration checks covering consent, relevance, public records, conflicting identities, adverse information, unresolved records, and bias risk.
