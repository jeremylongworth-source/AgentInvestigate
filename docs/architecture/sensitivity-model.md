# Sensitivity Model

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_03_SENSITIVITY_ROUTING_READY
```

## Purpose

This document defines the four sensitivity classes used by AgentInvestigate and how they control skill authoring, routing, source requirements, and review requirements.

The sensitivity model applies to the taxonomy in `docs/architecture/taxonomy-index.yaml`. It is a routing control, not a statement that a skill has been implemented.

## Sensitivity Classes

### ROUTINE

Routine skills perform ordinary analytical, administrative, documentation, planning, or reporting work where the work does not materially depend on current law, licensing, privacy obligations, intrusive collection, emergency action, force, or professional certification.

Typical examples:

- `build-evidence-matrix`
- `construct-event-chronology`
- `prepare-case-status-update`
- `review-security-log`

Minimum gates:

- confirm task scope;
- identify available evidence or input material;
- preserve facts, assumptions, unknowns, and limitations;
- avoid legal, regulatory, intrusive, or certification claims unless routed upward.

Default behavior:

```text
Proceed when scope and inputs are sufficient.
Clarify when inputs are incomplete.
Escalate upward if regulated, intrusive, or certification-boundary facts appear.
```

### REGULATED

Regulated skills depend materially on jurisdiction, law, licensing, privacy, workplace rules, consumer-report rules, professional requirements, source freshness, or compliance obligations.

Typical examples:

- `identify-licensing-requirement`
- `identify-recording-law-issue`
- `review-training-requirements`
- `prepare-compliance-escalation`

Minimum gates:

- identify jurisdiction;
- identify the user's role and authority;
- use authoritative or documented sources;
- record source date and verification date where source material is used;
- avoid final legal, regulatory, licensing, or compliance determinations;
- route material consequences to qualified review.

Default behavior:

```text
Do not answer as universal advice.
Clarify missing jurisdiction or authority.
Provide issue spotting and source-backed research framing.
Escalate final determinations to qualified human review.
```

### INTRUSIVE

Intrusive skills involve surveillance, observation, sensitive personal information, identity analysis, background screening, workplace allegations, personal reputation, employment consequences, private life, location, or other work that can materially affect a person's privacy, safety, liberty, employment, or reputation.

Typical examples:

- `assess-observation-authorization`
- `assess-observation-proportionality`
- `assess-background-screening-authority`
- `verify-screening-consent`
- `analyze-video-event-log`

Minimum gates:

- classify request type;
- identify jurisdiction;
- validate user, client, or organizational authority;
- assess lawful purpose;
- identify privacy obligations;
- assess information-collection basis;
- assess necessity and proportionality;
- assess less-intrusive alternatives;
- define scope boundaries;
- require human approval before any bounded intrusive task;
- block prohibited conduct.

Default behavior:

```text
Fail closed until all required gates are satisfied.
Do not route directly from a raw request to operational execution.
Prefer lower-risk documentation, authority checks, or escalation when gates are missing.
```

### CERTIFICATION_BOUNDARY

Certification-boundary skills are adjacent to activities requiring licensed, certified, qualified, trained, authorized, or emergency personnel. AgentInvestigate may support recognition, documentation, planning, handoff, and escalation, but must not substitute for required training or professional authority.

Typical examples:

- `determine-emergency-escalation`
- `support-emergency-service-access`
- `document-alarm-response`
- `assess-conflict-risk`
- `analyze-alarm-event`
- `identify-security-system-failure`

Minimum gates:

- identify whether immediate danger, emergency, life safety, use of force, weapons, restraints, alarm systems, fire systems, electrical systems, structural systems, or other qualified work is involved;
- route emergencies to emergency services;
- route technical or professional determinations to qualified review;
- limit output to recognition, documentation, communication, preservation, and escalation;
- avoid operational tactics, force, weapons, restraint, system bypass, or certification substitutes.

Default behavior:

```text
Support recognition and escalation.
Do not provide operational substitutes for certified, licensed, emergency, engineering, or force-related work.
```

## Classification Rules

Use the highest applicable sensitivity class. A request can start as routine and become regulated, intrusive, or certification-boundary when facts emerge.

Classification precedence:

```text
PROHIBITED
CERTIFICATION_BOUNDARY
INTRUSIVE
REGULATED
ROUTINE
```

`PROHIBITED` is not a taxonomy sensitivity class. It is a stop condition defined in `docs/architecture/prohibited-capabilities.md`.

## Taxonomy Distribution

AI-02 classifies 212 taxonomy skills as:

| Sensitivity | Count |
|---|---:|
| `ROUTINE` | 131 |
| `REGULATED` | 44 |
| `INTRUSIVE` | 27 |
| `CERTIFICATION_BOUNDARY` | 10 |

This distribution is a planning baseline. If later source work shows a skill is more sensitive than expected, the skill must be upgraded before implementation.

## Reclassification Triggers

Upgrade a request or skill classification when it includes:

- jurisdiction-specific licensing, law, regulation, privacy, records, or employment consequences;
- collection, analysis, or disclosure of personal information;
- observation, surveillance, monitoring, location, video, or identity work;
- workplace allegations, discipline, termination, background screening, or reputation impacts;
- emergency response, alarm response, force, restraints, weapons, fire, life safety, engineering, or security-system operation;
- any prohibited capability or misuse framing.

Downgrading is allowed only when the sensitive element is removed from scope and the remaining task is independently safe and useful.

## Output Requirements By Class

Routine outputs must include:

- task scope;
- supplied evidence or source material;
- analysis or document output;
- assumptions and unknowns when material;
- limitations.

Regulated outputs must also include:

- jurisdiction;
- source type and freshness need;
- issue-spotting posture;
- qualified-review need;
- no final legal or regulatory conclusion unless supplied by an authoritative source and still framed as source-backed information.

Intrusive outputs must also include:

- authority status;
- lawful purpose;
- privacy basis;
- necessity;
- proportionality;
- less-intrusive alternatives;
- human-approval status;
- bounded scope;
- stop condition when gates are missing.

Certification-boundary outputs must also include:

- emergency or qualified-review trigger;
- allowed support;
- prohibited substitute;
- handoff or escalation target;
- documentation needed for the responsible human.

## Validation Notes

This model is validated on paper in `docs/architecture/authority-routing.md`. Later waves must convert these rules into tests and fixtures.
