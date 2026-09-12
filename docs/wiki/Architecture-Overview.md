# Architecture Overview

AgentInvestigate is a validation-backed repository of atomic AI skills and professional compositions.

## Repository Layers

| Layer | Responsibility |
| --- | --- |
| `skills/` | Atomic skill packages. Each package contains a bounded `SKILL.md`. |
| `skillsets/` | Professional role composition that references existing atomic skills. |
| `specializations/` | Jurisdiction-specific foundations, currently Canada federal, Ontario, British Columbia, and Alberta. |
| `docs/architecture/` | Domain, taxonomy, routing, boundary, jurisdiction, and extension contracts. |
| `docs/standards/` | Skill authoring, naming, output, source, evidence, testing, and evaluation standards. |
| `docs/foundations/` | Shared terminology, schemas, and report structures consumed by real skills. |
| `tests/` | Routing, validation, integration, regulatory, and adversarial safety fixtures. |
| `scripts/` | Reproducible validators and generators. |

## Core Design Decisions

- Skills stay atomic and bounded.
- Professional roles are composed in `skillsets/professional-skillsets.json`; role names do not justify broad omnibus skills.
- Private investigation and private security remain distinct professional branches.
- Jurisdiction modules isolate local regulatory claims.
- Source, evidence, privacy, authority, human-review, certification, and prohibited-capability gates remain explicit.
- A shared asset is added only when a real skill consumes it.

## Request Control Flow

```text
user request
  -> classify request type
  -> check prohibited capabilities
  -> identify sensitivity
  -> identify jurisdiction when needed
  -> validate authority and lawful purpose when needed
  -> check privacy and source-access basis when needed
  -> route to skill, skillset, clarification, escalation, or redirect
  -> produce a bounded output with evidence and limitations
```

Intrusive work cannot move directly from a raw request to execution. See [[Sensitivity And Routing]] and the repository contracts for [authority routing](https://github.com/jeremylongworth-source/AgentInvestigate/blob/main/docs/architecture/authority-routing.md) and [intrusive-task gating](https://github.com/jeremylongworth-source/AgentInvestigate/blob/main/docs/architecture/intrusive-task-gate.md).

## Extension Rules

Before adding a capability:

- read `ROADMAP.md` and the latest handoff;
- confirm the capability is not already covered;
- classify sensitivity, jurisdiction, authority, source freshness, and professional boundaries;
- add tests and validator coverage with the behavior;
- preserve the private investigation/private security distinction;
- document known limitations and escalation requirements.

New Canadian jurisdictions follow `docs/architecture/canadian-jurisdiction-roadmap.md`. Future specialist modules follow `docs/architecture/specialization-roadmap.md`.
