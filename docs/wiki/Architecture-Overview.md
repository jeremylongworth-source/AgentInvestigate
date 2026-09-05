# Architecture Overview

AgentInvestigate is organized as a validation-backed skill repository.

## Main Components

- `skills/`: atomic skill packages, each with a `SKILL.md`.
- `skillsets/`: professional role composition that references existing atomic skills.
- `docs/architecture/`: domain, routing, boundary, taxonomy, jurisdiction, and specialization contracts.
- `docs/standards/`: authoring, naming, output, source, testing, and evaluation standards.
- `docs/foundations/`: shared vocabulary, schemas, and report contracts.
- `docs/evaluation/`: integration, safety, and release-candidate evaluation artifacts.
- `specializations/`: jurisdiction specialization foundations.
- `tests/`: JSON scenario and audit fixtures.
- `scripts/`: validators and generators.

## Design Decisions

Atomic skills stay narrow. Professional roles are composed through `skillsets/professional-skillsets.json` rather than duplicated as large procedural skills.

Private investigation and private security remain structurally distinct. Hybrid skillsets may coordinate both branches, but they must not collapse one authority model into the other.

Routing states are global and shared:

```text
PROCEED_ROUTINE
CLARIFY_SCOPE
REGULATED_RESEARCH_ONLY
INTRUSIVE_GATE_REQUIRED
CERTIFICATION_ESCALATION
PROHIBITED_REDIRECT
```

Jurisdiction modules are isolated so local regulatory claims do not silently become global claims.

## Control Flow

```text
user request
classify request type
check prohibited capabilities
identify sensitivity
identify jurisdiction if needed
validate authority and lawful purpose if needed
check privacy and source-access basis if needed
route to skill, skillset, escalation, or prohibited redirect
produce bounded output
record limitations and review needs
```

## Extension Model

Future extensions should follow the active roadmap and latest handoff.

New jurisdiction modules follow `docs/architecture/canadian-jurisdiction-roadmap.md`.

New specialist modules follow `docs/architecture/specialization-roadmap.md`.

No extension should weaken source, privacy, authority, safety, or prohibited-capability boundaries.
