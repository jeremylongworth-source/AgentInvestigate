---
name: identify-licensing-requirement
description: Identify source-backed licensing issues for investigation or security work without making final licensing determinations.
license: MIT
---

# Identify Licensing Requirement

## Overview

Identify whether a requested investigation or security activity may involve licensing or registration issues. This is a `REGULATED` skill and produces research briefs, issue-spotting summaries, source needs, or escalation questions only.

## Triggers

- User asks whether private investigation, private security, alarm response, patrol, screening, surveillance governance, or related work needs a licence.
- User supplies jurisdiction, role, activity, and source material for licensing review.
- User asks what sources should be checked before work proceeds.

## Non-Triggers

- Requests for final legal advice, licensing approval, eligibility certification, or compliance certification are outside this skill.
- Requests to evade licensing, reporting, training, consent, or regulator review route to `PROHIBITED_REDIRECT`.
- Emergency, force, weapons, restraints, fire, life-safety, or qualified technical work routes to certification-boundary escalation.

## Required Inputs

- Jurisdiction.
- User role and organization or client context.
- Activity or work type.
- Whether the output should be a research brief, issue-spotting summary, checklist, or escalation packet.

## Optional Inputs

- Current official sources or source URLs.
- Applicable regulator, licence class, registration category, or professional context.
- Dates, effective period, or planned work date.
- Known exemptions or local policy supplied by the user.

## Assumptions

- Do not infer jurisdiction, licensing eligibility, authority, exemption, or compliance.
- Do not treat user confidence or job title as proof of authority.
- If current sources are not available, limit output to source needs and issue spotting.

## Dependencies

- Canonical taxonomy dependency: `identify-jurisdiction`.
- Use `docs/standards/research-and-evidence-standard.md`.
- Use `docs/standards/regulatory-source-standard.md`.
- Use `docs/standards/source-freshness-standard.md`.
- Use `docs/foundations/shared-schemas.md` for jurisdiction, authority, and source fields.

If `identify-jurisdiction` has not been implemented, ask for jurisdiction or produce only jurisdiction-neutral source categories.

## Core Procedure

1. Classify the requested activity and professional branch.
2. Confirm jurisdiction and scope.
3. Identify whether licensing, registration, training, regulator, or qualified-review issues may apply.
4. Check for prohibited bypass framing.
5. Use the AI-05 source hierarchy and metadata requirements.
6. Separate source text from interpretation.
7. State issue-spotting points and source gaps.
8. Route final determinations to qualified review.

## Evidence Requirements

Use user-supplied activity descriptions, source material, regulator pages, statutes, regulations, court material, privacy authority material, standards, or professional guidance. Preserve source title, organization, jurisdiction, URL or source ID, publication or effective date when available, accessed date, last verified date, applicability, and supersession risk.

## Source Requirements

Freshness class: `HIGH` for licensing requirements, fees, forms, eligibility, regulator process, current obligations, exemptions, or enforcement posture.

Use the strongest applicable source:

1. legislation / regulations / courts;
2. government regulators;
3. privacy authorities when privacy or screening overlaps;
4. recognized standards organizations;
5. professional associations;
6. academic / technical literature;
7. specialist material;
8. secondary summaries.

Do not rely on secondary summaries for final licensing statements.

## Jurisdiction Requirements

Jurisdiction is required before jurisdiction-specific analysis. If jurisdiction is missing, ask for it or produce a jurisdiction-neutral research checklist.

## Authority Checks

Identify user role, client or organizational context, planned activity, and whether the user is seeking authorization to act. Do not state that the user is licensed, authorized, exempt, or compliant.

## Sensitivity Handling

Default class: `REGULATED`.

Route to `REGULATED_RESEARCH_ONLY` for source-backed issue spotting. Upgrade to `INTRUSIVE` when licensing analysis is tied to surveillance, screening, monitoring, sensitive personal information, or personal records. Route emergencies and qualified operational questions to `CERTIFICATION_ESCALATION`.

## Output Contract

Return:

- scope and jurisdiction;
- activity being reviewed;
- source posture and freshness status;
- source metadata table or source-needed list;
- licensing issue-spotting summary;
- authority and role gaps;
- qualified-review questions;
- limitations and no-final-determination statement.

## Limitations

This skill does not grant, deny, certify, or verify a licence. It does not determine legal compliance, eligibility, exemption, employment action, privacy compliance, security authority, or regulator approval.

## Escalation

Escalate final licensing, exemption, compliance, employment, privacy, or enforcement questions to counsel, regulator, compliance, privacy officer, licensed investigator, licensed security manager, or organizational leadership.

## References

- Read `references/licensing-source-checklist.md` before producing regulated licensing issue spotting.
- Use AI-05 source standards for metadata and freshness.
- Use `docs/foundations/shared-schemas.md` for source and jurisdiction fields.

## Testing

Must pass AI-08 scenarios for:

- jurisdiction-specific source-backed licensing issue spotting;
- missing jurisdiction;
- stale source;
- wrong source jurisdiction;
- licensing bypass request;
- no final licensing determination.
