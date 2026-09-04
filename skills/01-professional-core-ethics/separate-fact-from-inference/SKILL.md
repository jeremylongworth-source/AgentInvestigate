---
name: separate-fact-from-inference
description: Separate supplied facts, allegations, assumptions, inferences, contradictions, and unknowns in investigation or security material.
license: MIT
---

# Separate Fact From Inference

## Overview

Separate facts from allegations, assumptions, inferences, contradictions, and unknowns in supplied material. This is a `ROUTINE` foundational evidence-discipline skill.

## Triggers

- User asks to clean up notes, findings, summaries, timelines, matrices, or reports.
- User needs evidence separated from interpretation.
- User asks whether a statement is fact, allegation, inference, or unknown.

## Non-Triggers

- Requests to turn unsupported allegations into findings route to clarification or refusal.
- Requests to fabricate, alter, hide, or strengthen evidence route to `PROHIBITED_REDIRECT`.
- Legal, regulatory, privacy, employment, or disciplinary conclusions route to qualified review.

## Required Inputs

- Supplied text, notes, records, statements, or draft findings.
- Task scope or intended artifact.

## Optional Inputs

- Source IDs.
- Date or time range.
- Allegation or issue list.
- Preferred output format.

## Assumptions

- Treat unsupported claims as allegations or inferences, not facts.
- Do not infer intent, credibility, causation, or authority without evidence.
- Use `unknown` for material gaps.

## Dependencies

- No canonical taxonomy dependencies.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/standards/output-contract-standard.md`.

## Core Procedure

1. Identify the supplied material and scope.
2. Extract source-supported facts.
3. Identify allegations and who or what source makes them.
4. Identify assumptions and inferences separately.
5. Surface contradictions and unknowns.
6. Suggest neutral rewrites when useful.
7. State limitations and review needs.

## Evidence Requirements

Use only supplied text or cited sources. Preserve source labels where available and do not add facts.

## Source Requirements

External research is normally unnecessary. If classification depends on outside source material, cite or request it.

## Jurisdiction Requirements

Jurisdiction is not required unless the user asks for legal, regulatory, employment, privacy, or evidence-admissibility conclusions.

## Authority Checks

Confirm the output is evidence classification or drafting support. Do not authorize action based on the separated material.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade when the material involves regulated determinations, sensitive personal information, screening, surveillance, or certification-boundary action.

## Output Contract

Return:

- scope;
- facts;
- allegations;
- assumptions;
- inferences;
- contradictions;
- unknowns;
- neutral rewrite or next evidence request;
- limitations.

## Limitations

This skill does not determine truth, credibility, guilt, liability, legal status, employment action, privacy compliance, or admissibility.

## Escalation

Escalate when separated material reveals regulated issues, intrusive data, safety risk, prohibited conduct, or material consequences requiring qualified review.

## References

- Read `references/fact-inference-reference.md` when classifying statements.
- Use shared professional vocabulary for labels and support levels.

## Testing

Must pass AI-09 scenarios for fact/inference separation, unsupported finding requests, contradictions, and output-format compliance.
