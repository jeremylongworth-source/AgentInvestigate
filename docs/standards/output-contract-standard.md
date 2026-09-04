# AgentInvestigate Output Contract Standard

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_04_SKILL_STANDARD_READY
```

## Purpose

This standard defines the minimum output contract every AgentInvestigate skill must declare. Output contracts make skill responses reviewable, testable, and safe to route into downstream investigation, evidence, security, compliance, or escalation workflows.

## Core Rule

Every skill must define a predictable output shape in its `Output Contract` section.

The output contract must state:

- intended user-facing artifact;
- required fields or sections;
- required evidence references;
- assumptions and unknowns;
- limitations;
- escalation language when applicable;
- prohibited content the output must not include.

The contract may specify prose, tables, YAML, JSON, checklist format, report sections, matrix rows, or another structured shape. The shape must be concrete enough for scenario tests to evaluate.

## Universal Output Fields

Every AgentInvestigate skill output must preserve these elements when material:

| Element | Requirement |
|---|---|
| `scope` | State the task boundary, subject matter, time range, and included/excluded material when known. |
| `inputs_used` | Identify supplied records, sources, facts, logs, statements, or user-provided context used in the output. |
| `facts` | Keep sourced facts separate from allegations, assumptions, and inferences. |
| `analysis` | Explain reasoning at a level appropriate to the task without inventing missing evidence. |
| `assumptions` | State material assumptions and defaults. |
| `unknowns` | State missing facts that could change the output. |
| `limitations` | State what the output does not determine, authorize, certify, or replace. |
| `next_steps` | Provide bounded next steps, review needs, or escalation options where useful. |

Fields may be renamed in user-facing prose when the meaning is preserved.

## Evidence Output Requirements

Outputs involving evidence, allegations, sources, statements, media, logs, identities, screening records, or incidents must distinguish:

- fact;
- allegation;
- inference;
- contradiction;
- source;
- source date or event date when available;
- confidence or support level when useful;
- unresolved question.

The output must not:

- present unsupported allegation as finding;
- fabricate facts, sources, dates, or confidence;
- strengthen or weaken evidence for persuasion rather than accuracy;
- hide contradictions;
- omit material limitations.

## Source Output Requirements

Outputs using current external sources, jurisdiction-specific material, laws, regulations, government guidance, privacy authority material, standards, or professional guidance must include:

- source title or description;
- organization or publisher when known;
- jurisdiction when relevant;
- source URL or supplied-source identifier when available;
- publication, effective, or access date when available;
- verification date when the source was checked;
- whether the source supports a final statement, issue-spotting statement, or review need.

AI-05 will define the full source hierarchy, metadata model, and freshness standard. Until AI-05 is complete, skills must not encode universal legal, regulatory, licensing, privacy, employment, or compliance conclusions.

## Sensitivity Output Requirements

Minimum output requirements by sensitivity class:

| Class | Required output controls |
|---|---|
| `ROUTINE` | Include scope, inputs used, analysis or artifact, material assumptions, unknowns, and limitations. |
| `REGULATED` | Include jurisdiction, source posture, issue-spotting language, qualified-review need, and no unsupported final legal or regulatory conclusion. |
| `INTRUSIVE` | Include authority status, lawful purpose, privacy basis, collection basis, necessity, proportionality, less-intrusive alternatives, human-approval status, bounded scope, and stop condition when gates are missing. |
| `CERTIFICATION_BOUNDARY` | Include emergency or qualified-review trigger, allowed support, prohibited substitute, escalation or handoff target, and documentation needed for the responsible human. |

If multiple classes apply, use the highest applicable requirements.

## Authority And Jurisdiction Language

Outputs must state when jurisdiction, user role, client or organizational authority, consent, lawful purpose, privacy basis, or human approval is missing.

Permitted language:

```text
Based on the supplied information, this is an issue-spotting summary and not a final legal, licensing, privacy, employment, security, emergency, engineering, or certification determination.
```

Prohibited language:

```text
You are authorized.
This is legal.
This satisfies licensing.
This certifies compliance.
This replaces professional training.
```

Equivalent wording is allowed when it preserves the same boundary.

## Escalation Output Requirements

When escalation is required, the output must identify:

- escalation trigger;
- responsible human or function;
- information to preserve;
- immediate stop condition;
- safe handoff or review path.

Escalation targets may include emergency services, counsel, compliance, privacy officer, HR, regulator, licensed investigator, licensed security manager, qualified trainer, engineer, fire/life-safety professional, supervisor, client authority, or organizational leadership.

## Structured Artifact Requirements

For matrix, register, checklist, chronology, incident log, or handoff artifacts, the skill must define required columns or fields.

Common fields include:

- `item_id`
- `source_id`
- `date_or_time_range`
- `fact_or_allegation`
- `evidence_summary`
- `analysis_or_issue`
- `confidence_or_support`
- `authority_or_scope_note`
- `limitation`
- `next_action`

A skill may use a smaller field set only when the omitted fields are irrelevant to the atomic task.

## Testing Requirements

Every skill output contract must be testable through scenario evaluation.

Minimum checks:

- required fields are present;
- facts and inferences are separated;
- missing inputs produce questions, partial outputs, or stop conditions;
- regulated outputs avoid unsupported final determinations;
- intrusive outputs fail closed when gates are missing;
- certification-boundary outputs avoid operational substitutes;
- prohibited requests are redirected;
- output is usable without relying on hidden assumptions.

AI-04 defines the output standard only. AI-06 must turn these requirements into executable tests, fixtures, and acceptance criteria.
