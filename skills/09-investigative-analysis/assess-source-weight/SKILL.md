---
name: assess-source-weight
description: Assess evidence-bounded source weight using supplied source reliability, provenance, and corroboration context.
license: MIT
---

# Assess Source Weight

## Overview

Assesses source weight from reliability, provenance, directness, corroboration, independence, and limitations. This is a `ROUTINE` investigative-analysis skill for professional investigation support.

## Triggers

- User asks to generate, test, compare, identify, construct, analyze, assess, or draft source weight assessment.
- User supplies case scope, evidence matrices, allegations, facts, statements, chronologies, source records, hypotheses, draft findings, or unresolved questions.
- User needs plausible but incorrect hypotheses considered against disconfirming evidence.
- User needs investigative analysis that keeps facts, inferences, allegations, and findings separate.

## Non-Triggers

- Requests to fabricate, alter, conceal, overstate, or selectively ignore evidence route to `PROHIBITED_REDIRECT`.
- Requests to force a preferred conclusion, suppress plausible alternatives, or ignore disconfirming evidence route to `PROHIBITED_REDIRECT`.
- Requests for legal, employment, disciplinary, licensing, privacy, liability, guilt, or admissibility conclusions route to qualified review.
- Requests involving intrusive collection, surveillance, sensitive personal data, regulated screening, emergency threats, or certified forensic determinations require the appropriate gate and human review.

## Required Inputs

- Case scope, investigative question, allegation, hypothesis, chronology, source set, evidence matrix, or draft finding relevant to source weight assessment.
- Supplied facts, evidence records, source references, statements, timelines, contradictions, and known limitations.
- Authority and jurisdiction status when analysis could affect legal, employment, privacy, screening, or other material consequences.
- The requested output audience and decision boundary, if known.

## Optional Inputs

- Existing evidence matrix, chain-of-custody summary, source reliability assessment, case timeline, statement comparison, or prior analysis.
- Candidate hypotheses, alternative explanations, confidence labels, support thresholds, reviewer instructions, or report structure.
- Known disconfirming evidence, unresolved questions, contradictory evidence, source gaps, or follow-up constraints.
- Applicable policy, regulatory source, legal review note, or escalation path.

## Assumptions

- `FACT ≠ INFERENCE ≠ ALLEGATION ≠ FINDING` is mandatory.
- Do not convert allegations, hypotheses, suspicion, patterns, correlations, or inferences into facts.
- Do not treat absence of evidence as proof unless the scope and source limits support that wording.
- Do not ignore plausible but incorrect hypotheses; explain why they remain unsupported, contradicted, unresolved, or less consistent with supplied evidence.
- Treat outputs as draft analytical support requiring responsible human review before consequential use.

## Dependencies

- Canonical taxonomy dependency: `assess-source-reliability`.
- Use `build-evidence-matrix` when evidence needs structured mapping.
- Use `separate-fact-from-inference` when supplied material mixes facts, allegations, assumptions, inferences, and findings.
- Use `identify-investigative-bias` when a preferred hypothesis, selective evidence use, or confirmation bias is possible.
- Use `assess-source-reliability` and `assess-source-weight` when source strength affects analysis.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.
- Use `docs/foundations/report-structure-contracts.md`.

If a dependency output is unavailable, identify the missing dependency and continue only with bounded issue spotting, gap identification, or draft analysis clearly marked as preliminary.

## Core Procedure

1. Confirm scope, authority, jurisdiction context, requested analytical output, and decision boundary.
2. Separate all material into:

- `FACT`
- `INFERENCE`
- `ALLEGATION`
- `FINDING`

3. Identify the supplied evidence, sources, chronology, allegations, hypotheses, contradictions, unresolved questions, and limitations.
4. Generate or evaluate plausible alternative explanations, including plausible but incorrect hypotheses.
5. Test each explanation against supporting evidence, contradictory evidence, missing evidence, source limits, and disconfirming evidence.
6. Organize the output around evidence matrix, hypothesis generation, hypothesis testing, alternative explanations, evidence contradiction, event chronology, pattern analysis, source weight, finding confidence, unresolved question, investigative finding.
7. State confidence, if requested, as evidence-bounded and provisional, with source limits and unresolved questions.
8. Return only findings or draft findings that are supported by the supplied evidence and remain inside scope.

## Evidence Requirements

Use only supplied or cited facts, evidence records, source records, statements, chronologies, and analysis inputs. Preserve source links, contradictions, disconfirming evidence, alternative explanations, confidence limits, and unresolved questions.

Do not invent evidence, hide contradictions, exclude inconvenient facts, assume intent, or treat unsupported allegations as findings.

## Source Requirements

External sources are optional for routine analysis of supplied material. Regulated claims, jurisdiction-specific conclusions, professional standards, legal tests, employment decisions, privacy conclusions, or forensic claims require AI-05 source standards and qualified review.

## Jurisdiction Requirements

Jurisdiction is contextual for routine investigative analysis and required before legal, employment, disciplinary, privacy, screening, admissibility, liability, or regulatory conclusions. Unknown jurisdiction remains an open gate.

## Authority Checks

Confirm the user is asking for analysis of supplied or authorized material. If authority to use records is unclear and the material involves personal information, employment, screening, surveillance, private records, or other material consequences, route upward before analysis.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` when analysis depends on regulated sources, sensitive personal information, surveillance, screening, legal conclusions, employment action, emergency response, forensic determinations, or qualified professional judgment.

## Output Contract

Return:

- routing state;
- scope, authority, jurisdiction, source, and review status;
- facts, inferences, allegations, and findings as separate categories;
- evidence support, source references, contradictions, disconfirming evidence, and source limits;
- hypotheses or alternative explanations considered;
- analysis, chronology, pattern, source-weight, confidence, unresolved-question, or draft-finding output;
- plausible but incorrect hypotheses and why they are unsupported, contradicted, less consistent, or unresolved;
- confidence and limitations;
- follow-up or escalation needs.

Hard reasoning rule: `FACT ≠ INFERENCE ≠ ALLEGATION ≠ FINDING`.

## Limitations

This skill does not make legal findings, determine guilt, decide liability, approve discipline, establish admissibility, authenticate evidence, perform forensic analysis, ignore disconfirming evidence, or replace qualified legal, compliance, HR, forensic, supervisory, or investigator review.

## Escalation

Escalate to counsel, compliance, privacy, HR, forensics, supervisor, licensed investigator, safety lead, emergency services, or another qualified reviewer when analysis affects legal rights, employment outcomes, regulated screening, sensitive personal information, safety risk, forensic claims, admissibility, or material consequences.

## References

- Read `references/assess-source-weight-reference.md` when preparing source weight assessment outputs.
- Use shared schemas and report structure contracts for evidence, source, chronology, hypothesis, contradiction, confidence, unresolved-question, finding, and escalation fields.

## Testing

Must pass AI-16 scenarios for investigative analysis, `FACT ≠ INFERENCE ≠ ALLEGATION ≠ FINDING`, plausible but incorrect hypotheses, and disconfirming evidence.
