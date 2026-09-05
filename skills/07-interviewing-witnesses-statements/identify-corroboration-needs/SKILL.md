---
name: identify-corroboration-needs
description: Identify corroboration needs for supplied statements, claims, gaps, and inconsistencies.
license: MIT
---

# Identify Corroboration Needs

## Overview

Identifies evidence, sources, records, witnesses, timelines, and review steps needed to corroborate claims. This is a `ROUTINE` interviewing, witnesses, and statements skill for neutral professional investigation support.

## Triggers

- User asks to define, prepare, sequence, identify, summarize, compare, corroborate, follow up, or review corroboration needs.
- User supplies interview objectives, questions, notes, statements, case facts, or source material for neutral handling.
- User needs information gaps, consistency, corroboration, follow-up, or bias risks organized.
- User needs interview or statement support without coercion, deception, credibility overclaiming, or unsupported behavioral inference.

## Non-Triggers

- Requests for coercive interviewing, interrogation tactics, intimidation, deception, impersonation, witness coaching, false statement drafting, or pressure scripts route to `PROHIBITED_REDIRECT`.
- Requests to infer deception solely from body language, eye contact, nervousness, personality, or unsupported behavioral stereotypes route to refusal or correction.
- Requests for legal, employment, disciplinary, credibility, admissibility, liability, or compliance conclusions route to qualified review.
- Requests involving minors, vulnerable persons, trauma, emergency threats, or legally protected interviews require human review and escalation.

## Required Inputs

- Case scope, interview purpose, and user role.
- Authority and jurisdiction status, if known.
- Interview objective, question set, statement, note, or source material relevant to corroboration needs.
- Witness, participant, or statement role, if known.

## Optional Inputs

- Existing interview plan, topic sequence, case notes, evidence matrix, source log, or prior statement summary.
- Known information gaps, inconsistencies, corroboration needs, timelines, or follow-up constraints.
- Applicable policy, procedure, reviewer role, consent, notice, accommodation, or support-person requirement.
- Known bias risks, language needs, vulnerability concerns, or escalation path.

## Assumptions

- Do not invent statements, admissions, observations, demeanor, context, or corroboration.
- Do not infer deception, credibility, intent, or culpability from behavioral cues.
- Keep facts, allegations, statement claims, interviewer notes, inferences, unknowns, and follow-up needs separate.
- Treat interview outputs as drafts for responsible human review.

## Dependencies

- Canonical taxonomy dependency: `compare-statement-consistency`.
- Use `define-professional-role-boundaries` when role limits are unclear.
- Use `prepare-authority-check` when interview authority, consent, jurisdiction, privacy, or employment context is unclear.
- Use `separate-fact-from-inference` when notes or statements mix facts, allegations, inferences, and unknowns.
- Use `identify-investigative-bias` when questions, sequencing, summaries, or comparisons may encode bias.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.
- Use `docs/foundations/report-structure-contracts.md`.

If a dependency output is unavailable, identify the missing dependency and continue only with bounded neutral drafting or review.

## Core Procedure

1. Confirm scope, role, authority, jurisdiction, participant role, purpose, and requested interview or statement output.
2. Separate supplied facts, statement claims, questions, notes, observations, assumptions, inferences, gaps, and unknowns.
3. Check for coercion, deception, intimidation, witness coaching, false statements, protected interview issues, or unsupported behavioral inference.
4. Organize the output around neutral questioning, objectives, sequencing, information gaps, statements, notes, consistency, corroboration, follow-up, bias.
5. Preserve inconsistencies, gaps, limitations, corroboration needs, and bias risks.
6. Return neutral questions, summaries, comparisons, follow-ups, or review notes without deciding deception, credibility, liability, discipline, or legal consequences.

## Evidence Requirements

Use supplied interview plans, questions, statements, notes, transcripts, recordings described by the user, source logs, case notes, and case records. Do not invent words spoken, demeanor, admissions, contradictions, corroboration, or context.

## Source Requirements

External sources are optional for routine interview planning and statement handling. Legal, employment, privacy, trauma-informed, child/vulnerable-person, or jurisdiction-specific interview requirements require AI-05 source standards and qualified review.

## Jurisdiction Requirements

Jurisdiction is optional for general neutral question drafting and required before legal, employment, privacy, consent, recording, disciplinary, protected-interview, or compliance conclusions. Unknown jurisdiction remains an open gate.

## Authority Checks

Identify role, authority basis, participant relationship, consent or notice status when relevant, privacy basis, and reviewer needs. Do not proceed into sensitive interviewing or statement use when authority, jurisdiction, consent, or human review is missing.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` when interviews or statements involve legal, employment, privacy, protected persons, trauma, sensitive personal information, surveillance, emergency threats, safety risks, or qualified professional determinations.

## Output Contract

Return:

- routing state;
- interview or statement objective;
- role, authority, jurisdiction, consent, and review status;
- supplied facts, statement claims, notes, and source references;
- neutral questions, topic sequence, summary, consistency comparison, corroboration needs, or follow-up items;
- information gaps, inconsistencies, assumptions, and unknowns;
- bias and prohibited-inference checks;
- escalation or reviewer target;
- limitations.

Prohibited inference: do not infer deception solely from:

- `body language`
- `eye contact`
- `nervousness`
- `personality`
- `unsupported behavioral stereotypes`

## Limitations

This skill does not conduct interviews, coerce statements, coach testimony, infer deception from behavior, decide credibility, make findings, determine legal admissibility, approve discipline, or replace qualified review.

## Escalation

Escalate to counsel, HR, privacy, compliance, supervisor, trauma-informed professional, child/vulnerable-person specialist, emergency services, or another qualified reviewer when interviews or statements involve protected rights, employment action, safety risk, vulnerable participants, minors, trauma, regulated recording, or material consequences.

## References

- Read `references/identify-corroboration-needs-reference.md` when preparing corroboration needs outputs.
- Use shared schemas and report structure contracts for interview-plan, statement, case-note, evidence, source, corroboration, bias, and escalation fields.

## Testing

Must pass AI-14 scenarios for neutral questioning, objectives, sequencing, information gaps, statements, notes, consistency, corroboration, follow-up, bias, and prohibited deception inference.
