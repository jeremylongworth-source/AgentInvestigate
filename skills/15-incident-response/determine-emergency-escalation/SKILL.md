---
name: determine-emergency-escalation
description: Determine whether a security incident requires emergency or qualified escalation without replacing local procedures or responders.
license: MIT
---

# Determine Emergency Escalation

## Overview

Determine whether a reported security incident, alarm, threat, hazard, or urgent condition should route to emergency services, supervisor, post orders, qualified professionals, or documentation. This is a `CERTIFICATION_BOUNDARY` skill.

The skill supports recognition, documentation, communication, preservation, and handoff. It does not provide tactical response, force, weapons, restraint, search, clearing, pursuit, or confrontation instruction.

## Triggers

- User asks whether an incident requires emergency escalation.
- User reports an alarm, break-in possibility, injury, threat, fire, life-safety issue, system failure, or urgent security condition.
- User needs a handoff checklist for responsible personnel.

## Non-Triggers

- Requests for clearing tactics, confrontation, pursuit, detention, force, weapons, restraint, or combat route to `PROHIBITED_REDIRECT`.
- Technical signoff for alarm, fire, electrical, structural, camera, or access-control systems routes to qualified review.
- Routine incident documentation without emergency or qualified escalation may route to incident report or log skills.

## Required Inputs

- Incident summary.
- Location or site context.
- Current danger or emergency indicators.
- People affected or potentially at risk.
- Known local post orders, emergency plan, or supervisor path if supplied.
- Requested output.

## Optional Inputs

- Time of incident.
- Alarm or system status.
- Known injuries, threats, fire, intrusion, hazardous conditions, or vulnerable people.
- Notifications already made.
- Evidence or records to preserve.

## Assumptions

- Do not assume the scene is safe.
- Do not assume the user is trained, authorized, equipped, or allowed to intervene.
- If immediate danger may exist, prioritize emergency or supervisor escalation over analysis.

## Dependencies

- Canonical taxonomy dependency: `triage-security-incident`.
- Use `docs/architecture/certification-boundaries.md`.
- Use `docs/foundations/report-structure-contracts.md` for `incident-report` and `shift-handoff` contracts.
- Use `docs/standards/output-contract-standard.md`.

If `triage-security-incident` is not implemented or incident facts are incomplete, perform only escalation recognition and documentation support.

## Core Procedure

1. Check for prohibited tactical or force-related requests.
2. Identify immediate danger, injury, fire, intrusion, violence, vulnerable-person, or life-safety indicators.
3. Identify supplied local post orders, emergency plan, supervisor path, or qualified-review path.
4. Select escalation state: emergency services, supervisor or command, qualified technical review, documentation-only, or clarify missing safety facts.
5. Provide safe communication and documentation points.
6. State prohibited substitutes and limitations.

## Evidence Requirements

Use only supplied incident facts, alarm logs, observations, notifications, post orders, emergency plans, or system records. Preserve unknowns and do not infer that the site is safe.

## Source Requirements

Freshness class: `HIGH` for emergency contact paths, post orders, legal requirements, system procedures, life-safety requirements, or qualified technical guidance.

If local procedures are missing, provide general escalation recognition and ask for local post orders or supervisor direction.

## Jurisdiction Requirements

Jurisdiction may be needed for regulated security, emergency, reporting, or life-safety obligations. Missing jurisdiction does not block immediate emergency escalation recognition.

## Authority Checks

Identify user role, site authority, post orders, supervisor path, and whether the user is seeking operational intervention. Do not authorize force, entry, search, pursuit, detention, restraint, weapons use, or technical system work.

## Sensitivity Handling

Default class: `CERTIFICATION_BOUNDARY`.

Use `CERTIFICATION_ESCALATION` when emergency, force, alarm response, fire, life-safety, engineering, or qualified technical issues appear. Route prohibited tactics to `PROHIBITED_REDIRECT`. Routine documentation may proceed only inside supplied facts and local authority.

## Output Contract

Return:

- incident scope and known facts;
- emergency indicators;
- escalation route;
- communication or notification points;
- evidence or records to preserve;
- prohibited substitute statement;
- limitations and follow-up documentation needs.

## Limitations

This skill does not replace emergency services, post orders, supervisor direction, guard training, use-of-force training, weapons training, restraint training, engineering review, fire/life-safety review, or qualified technical work.

## Escalation

Escalate to emergency services, supervisor, security command, client authority, law enforcement contact path, fire/life-safety professional, alarm vendor, engineer, or other qualified professional as indicated by supplied facts and local procedures.

## References

- Read `references/emergency-escalation-checklist.md` before producing an escalation recommendation.
- Use `docs/architecture/certification-boundaries.md`.
- Use `docs/foundations/report-structure-contracts.md` for documentation fields.

## Testing

Must pass AI-08 scenarios for:

- active alarm or possible break-in;
- missing safety facts;
- routine documentation after escalation;
- prohibited clearing, confrontation, force, weapon, or restraint request;
- qualified technical system question;
- output omits tactical response instructions.
