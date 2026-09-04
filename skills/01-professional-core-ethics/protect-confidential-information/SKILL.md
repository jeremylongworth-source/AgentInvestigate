---
name: protect-confidential-information
description: Identify confidentiality handling needs for supplied investigation or security information.
license: MIT
---

# Protect Confidential Information

## Overview

Identify confidentiality handling needs for investigation or security information. This is a `ROUTINE` professional-core skill when it provides safeguards, minimization, handling notes, and review questions without deciding legal or privacy compliance.

## Triggers

- User asks how to handle confidential case, client, employee, security, or incident information.
- User needs confidentiality notes for a report, handoff, source log, or case file.
- User asks what information should be minimized, restricted, redacted, or escalated for review.

## Non-Triggers

- Final legal, privacy, privilege, employment, records, or regulatory determinations route to qualified review.
- Requests to disclose, leak, misuse, bypass, or conceal protected information route to refusal or `PROHIBITED_REDIRECT`.
- Sensitive personal information collection, screening, surveillance, or monitoring routes through intrusive gates.

## Required Inputs

- Information type.
- Intended use or output.
- User role.
- Audience or recipient.
- Known sensitivity or confidentiality basis.

## Optional Inputs

- Jurisdiction.
- Policy, contract, NDA, privacy notice, or retention rule supplied by the user.
- Redaction or disclosure constraints.
- Storage, sharing, or retention context.

## Assumptions

- Do not assume disclosure is authorized.
- Do not assume information is non-confidential because it was supplied by the user.
- Treat personal, client, security-system, workplace, and case information as potentially sensitive until scoped.

## Dependencies

- Canonical taxonomy dependency: `define-professional-role-boundaries`.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.

If role boundaries are unclear, ask role and authority questions before suggesting handling.

## Core Procedure

1. Identify information type, audience, use, and scope.
2. Identify confidentiality, privacy, security, client, workplace, or source-sensitivity indicators.
3. Separate handling recommendations from legal or privacy determinations.
4. Identify minimization, redaction, access, retention, and sharing questions.
5. Flag regulated, intrusive, or prohibited disclosure risks.
6. Produce safe handling notes and escalation path.

## Evidence Requirements

Use only supplied information descriptions, policies, contracts, source labels, or records. Do not infer authorization, consent, or public status.

## Source Requirements

External sources are not needed for general handling notes. Current legal, privacy, employment, records, confidentiality, or privilege claims require AI-05 source standards and qualified review.

## Jurisdiction Requirements

Jurisdiction is optional for general confidentiality issue spotting and required for privacy, legal, employment, privilege, records, or regulatory conclusions.

## Authority Checks

Identify whether the user has authority to view, share, redact, retain, or disclose the information. Missing authority limits the output to questions and escalation.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED` for privacy, legal, employment, records, or privilege questions. Upgrade to `INTRUSIVE` for sensitive personal information, screening, surveillance, monitoring, or identity records.

## Output Contract

Return:

- information type and intended use;
- confidentiality indicators;
- authority or audience gaps;
- minimization or redaction considerations;
- access, sharing, retention, or handling questions;
- escalation target;
- limitations.

## Limitations

This skill does not decide privacy compliance, privilege, legal disclosure rights, records retention law, employment action, or permission to disclose information.

## Escalation

Escalate to privacy officer, counsel, compliance, HR, security manager, licensed investigator, client authority, supervisor, or organizational leadership when disclosure or handling has material consequences.

## References

- Read `references/confidentiality-handling-reference.md` when preparing confidentiality handling notes.
- Use shared schemas for authority, source, and artifact metadata.

## Testing

Must pass AI-09 scenarios for confidential handling notes, unauthorized disclosure requests, missing authority, and privacy escalation.
