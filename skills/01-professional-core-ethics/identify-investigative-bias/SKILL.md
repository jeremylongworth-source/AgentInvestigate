---
name: identify-investigative-bias
description: Identify investigative bias risks in supplied plans, notes, evidence summaries, or findings.
license: MIT
---

# Identify Investigative Bias

## Overview

Identify bias risks that could affect investigation or security analysis. This is a `ROUTINE` professional-core skill that flags risk, missing evidence, alternative explanations, and review needs.

## Triggers

- User asks whether a plan, finding, interview question, chronology, or report is biased.
- User asks for alternative explanations or evidence gaps.
- User needs bias notes before final review.

## Non-Triggers

- Requests to justify a predetermined conclusion route to evidence discipline or refusal.
- Requests to manipulate evidence, coach false statements, or hide contrary facts route to `PROHIBITED_REDIRECT`.
- Legal, employment, privacy, or discrimination determinations route to regulated review.

## Required Inputs

- Supplied plan, notes, evidence summary, finding, question set, or report language.
- Matter scope or allegation.
- Known evidence and unknowns.

## Optional Inputs

- Role and audience.
- Decision being supported.
- Known alternative explanations.
- Applicable policy or review standard supplied by the user.

## Assumptions

- Do not assume bias exists because a conclusion is unfavorable.
- Do not assume bias is absent because a user says the evidence is obvious.
- Treat intent and credibility conclusions as unsupported unless evidence is supplied.

## Dependencies

- Canonical taxonomy dependency: `apply-ethical-decision-framework`.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/standards/output-contract-standard.md`.

If the ethical decision framework has not been applied, include ethics and review questions where material.

## Core Procedure

1. Identify the conclusion, hypothesis, plan, or language being reviewed.
2. Separate facts, allegations, inferences, assumptions, and unknowns.
3. Look for confirmation bias, tunnel vision, loaded wording, unsupported intent inference, missing alternatives, omitted contrary evidence, and disproportionate focus.
4. Identify evidence gaps and alternative explanations.
5. Recommend neutral wording or review steps.
6. State limitations and escalation needs.

## Evidence Requirements

Use only supplied material and cited sources. Preserve contrary evidence, missing evidence, and uncertainty.

## Source Requirements

External sources are normally unnecessary. If bias review depends on legal, employment, discrimination, privacy, or regulated standards, use AI-05 source standards and route to qualified review.

## Jurisdiction Requirements

Jurisdiction is not required for routine bias issue spotting. Jurisdiction is required for legal, employment, discrimination, privacy, or regulated conclusions.

## Authority Checks

Confirm the user seeks review or revision support, not permission to target a person or justify a predetermined action.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED` for legal, employment, privacy, or discrimination issues. Upgrade to `INTRUSIVE` if bias review involves sensitive personal information collection or screening.

## Output Contract

Return:

- reviewed material;
- possible bias indicators;
- affected facts or assumptions;
- alternative explanations;
- missing evidence;
- neutral wording or review steps;
- limitations and escalation needs.

## Limitations

This skill does not determine discrimination, legal liability, credibility, guilt, employment action, discipline, or professional misconduct.

## Escalation

Escalate to counsel, HR, compliance, privacy, supervisor, licensed investigator, security manager, or organizational leadership when bias could materially affect rights, employment, privacy, or safety.

## References

- Read `references/bias-review-reference.md` when reviewing plans, reports, or findings for bias.
- Use shared vocabulary for facts, allegations, inferences, findings, and confidence labels.

## Testing

Must pass AI-09 scenarios for biased wording, unsupported intent inference, missing contrary evidence, and prohibited conclusion-shaping.
