---
name: map-existing-controls
description: Map supplied physical security controls to protected assets, threats, vulnerabilities, and limitations.
license: MIT
---

# Map Existing Controls

## Overview

Maps current controls, coverage, ownership, dependencies, assumptions, evidence, and apparent limits. This is a `ROUTINE` physical security and risk assessment skill for professional security support.

AI-23 required reasoning chain:

- `assets`
- `threats`
- `vulnerabilities`
- `consequences`
- `likelihood`
- `risk`
- `controls`
- `gaps`
- `options`
- `prioritized improvements`

AI-23 composition targets:

- `physical-security-analyst`
- `security-risk-assessor`

Conceptual security analysis must not be presented as structural engineering, electrical approval, fire-code approval, or life-safety certification.

## Triggers

- User asks to define, identify, assess, build, map, compare, prioritize, or prepare existing controls.
- User supplies site scope, protected assets, threat context, vulnerability notes, consequence data, likelihood inputs, risk register material, existing controls, control gaps, improvement options, or assessment-summary material.
- User needs the AI-23 reasoning chain organized across assets, threats, vulnerabilities, consequences, likelihood, risk, controls, gaps, options, prioritized improvements.
- User needs physical-security-analyst or security-risk-assessor support without engineering approval, fire-code approval, life-safety certification, or bypass detail.

## Non-Triggers

- Requests for structural engineering, electrical approval, fire-code approval, life-safety certification, code compliance certification, engineering signoff, or professional design approval route to qualified review.
- Requests for attack instructions, bypass instructions, forced entry, lock bypass, alarm defeat, camera evasion, access-control circumvention, exploit sequencing, or adversary playbooks route to `PROHIBITED_REDIRECT`.
- Requests to defeat, disable, evade, or circumvent locks, barriers, cameras, alarms, sensors, access controls, or monitoring route to `PROHIBITED_REDIRECT`.
- Requests for emergency response, fire response, medical response, use-of-force, weapons, restraints, tactical confrontation, or building-clearing instruction route to `CERTIFICATION_ESCALATION` or `PROHIBITED_REDIRECT`.
- Requests to fabricate, hide, exaggerate, or selectively omit assets, threats, vulnerabilities, consequences, likelihood, risks, controls, gaps, options, limitations, or prioritized improvements route to `PROHIBITED_REDIRECT`.

## Required Inputs

- Site or facility scope, user role, authority basis, jurisdiction if required, assessment purpose, protected asset context, and review boundary.
- Supplied facts relevant to existing controls, including assets, threats, vulnerabilities, consequences, likelihood, risk, controls, gaps, options, and prioritized improvements where applicable.
- Existing controls, known constraints, incident history if supplied, operational context, occupancy or business-impact context, and qualified-review needs.
- Known limitations, missing facts, uncertain assumptions, safety concerns, fire or life-safety implications, engineering questions, and required human approvals.

## Optional Inputs

- Existing site survey, risk register, control inventory, incident trend, operations brief, floor-plan excerpt, asset list, maintenance issue, security-system summary, or prior assessment.
- Risk-rating scale, consequence categories, likelihood criteria, control categories, budget constraints, implementation constraints, owner list, or preferred prioritization method.
- Known dependencies, open work orders, vendor notes, insurance requirements, policy requirements, accessibility needs, privacy considerations, or stakeholder questions.
- Preferred output format, audience, risk labels, table format, assumptions format, or assessment destination.

## Assumptions

- Do not invent assets, threats, vulnerabilities, consequences, likelihood, controls, gaps, options, costs, approvals, engineering facts, fire-code facts, or life-safety facts.
- Preserve the reasoning chain: assets, threats, vulnerabilities, consequences, likelihood, risk, controls, gaps, options, and prioritized improvements.
- Keep conceptual security analysis distinct from structural engineering, electrical approval, fire-code approval, and life-safety certification.
- Do not provide attack instructions, bypass instructions, forced entry, alarm defeat, camera evasion, access-control circumvention.
- Treat outputs as draft physical security assessment support requiring responsible human review before consequential use.

## Dependencies

- Canonical taxonomy dependency: `define-protected-assets`.
- Use `validate-security-service-authority` before physical security assessment work when authority, site scope, licensing, or client mandate is unclear.
- Use `define-protected-assets`, `identify-security-threats`, `assess-physical-vulnerabilities`, `assess-security-consequences`, and `assess-risk-likelihood` before building risk registers or assessment summaries.
- Use `build-security-risk-register`, `map-existing-controls`, `identify-control-gaps`, `compare-security-improvement-options`, and `prioritize-security-improvements` for risk, controls, gaps, options, and prioritized improvements.
- Use `prepare-physical-security-assessment-summary` for regulated summaries that may influence material security decisions.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.
- Use `docs/foundations/report-structure-contracts.md`.

If a dependency output is unavailable, identify the missing dependency and continue only with bounded conceptual analysis, draft structure, or qualified-review notes.

## Core Procedure

1. Confirm site scope, role, authority, jurisdiction if required, assessment purpose, protected-asset context, sensitivity, and reviewer boundary.
2. Place supplied material in the AI-23 reasoning chain: assets, threats, vulnerabilities, consequences, likelihood, risk, controls, gaps, options, and prioritized improvements.
3. Check for requests to provide attack instructions, bypass instructions, forced entry, alarm defeat, camera evasion, access-control circumvention, structural engineering, electrical approval, fire-code approval, life-safety certification, or fabricated assessment claims.
4. Separate supplied facts, assumptions, observations, evidence, uncertainty, constraints, source limits, qualified-review questions, and recommendations.
5. Preserve links between assets, threats, vulnerabilities, consequences, likelihood, risks, controls, gaps, options, and prioritized improvements.
6. Route engineering, electrical, fire-code, life-safety, emergency, legal, licensing, regulated, or unclear-authority work to qualified review.
7. Return bounded conceptual physical security risk assessment support without certifying engineering, electrical, fire-code, life-safety, legal, regulatory, or final safety outcomes.

## Evidence Requirements

Use only supplied site scope, asset lists, observations, incident history, risk criteria, control inventories, vulnerability notes, consequence estimates, likelihood inputs, risk registers, improvement options, and source material. Do not invent site conditions, vulnerabilities, costs, approvals, certifications, controls, or implementation outcomes.

## Source Requirements

External sources are optional for routine organization of supplied physical security material. Engineering, electrical, fire-code, life-safety, legal, licensing, privacy, security-system, accessibility, or jurisdiction-specific requirements need AI-05 source standards and qualified review.

## Jurisdiction Requirements

Jurisdiction is contextual for routine conceptual analysis and required for regulated summaries, security-service authority, privacy, fire-code, life-safety, electrical, structural, accessibility, legal, licensing, or compliance implications. Unknown jurisdiction remains an open gate for regulated or certification-adjacent work.

## Authority Checks

Confirm user role, site authority, client or organizational authority, lawful purpose, assessment scope, permitted records, site-access basis, reviewer role, and qualified-review requirements. Missing authority routes to `CLARIFY_SCOPE`, `REGULATED_RESEARCH_ONLY`, or `PROHIBITED_REDIRECT` depending on the request.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` when physical security assessment work involves critical infrastructure, sensitive floor plans, camera or alarm layouts, access credentials, private areas, security-system weaknesses, emergency planning, fire or life-safety systems, electrical or structural questions, suspected crime, privacy issues, or material consequences.

## Output Contract

Return:

- routing state;
- site scope, role, authority, jurisdiction, assessment purpose, source, and reviewer status;
- AI-23 reasoning-chain status for assets, threats, vulnerabilities, consequences, likelihood, risk, controls, gaps, options, and prioritized improvements;
- supplied facts, assumptions, observations, evidence, constraints, source limits, uncertainty, confidence, and limitations;
- risk register or assessment elements relevant to existing controls;
- boundary check for structural engineering, electrical approval, fire-code approval, and life-safety certification;
- prohibited detail check for attack instructions, bypass instructions, forced entry, alarm defeat, camera evasion, and access-control circumvention;
- escalation or qualified-review target;
- limitations and safe next steps.

Do not present conceptual security analysis as structural engineering, electrical approval, fire-code approval, life-safety certification, legal compliance, final safety certification, or implementation approval.

## Limitations

This skill does not replace counsel, security manager, licensed security professional, structural engineer, electrical professional, fire-code authority, life-safety authority, accessibility professional, alarm or security-system technician, insurer, emergency services, or qualified reviewer judgment. It does not certify safety, approve design, authorize construction, or provide technical bypass, exploit, or defeat guidance.

## Escalation

Escalate to a security manager, client authority, qualified security consultant, structural engineer, electrical professional, fire-code authority, life-safety authority, accessibility professional, alarm or security-system technician, counsel, compliance, insurer, emergency services, or another qualified reviewer when assessment facts involve engineering, electrical, fire-code, life-safety, emergency, legal, licensing, critical infrastructure, sensitive security details, unclear authority, or material consequences.

## References

- Read `references/map-existing-controls-reference.md` when preparing existing controls outputs.
- Use shared schemas and report structure contracts for assets, threats, vulnerabilities, consequences, likelihood, risk, controls, gaps, options, prioritized improvements, assumptions, confidence, and escalation fields.

## Testing

Must pass AI-23 scenarios for the required reasoning chain, composition targets physical-security-analyst and security-risk-assessor, and boundaries against structural engineering, electrical approval, fire-code approval, and life-safety certification.
