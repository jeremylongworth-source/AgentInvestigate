# Evidence Matrix Reference

## When To Read

Read this reference when using `build-evidence-matrix` to define fields, support labels, and stop conditions.

## Matrix Fields

| Field | Meaning |
|---|---|
| `matrix_row_id` | Stable row ID for review and test references. |
| `allegation_or_issue` | Allegation, issue, element, question, or report point being mapped. |
| `source_id` | Supplied source, document, log, statement, image, or record identifier. |
| `supplied_fact` | Fact stated by the source. |
| `inference` | Reasoned interpretation, separately labeled from fact. |
| `support_level` | `high_support`, `moderate_support`, `low_support`, `unsupported`, `conflicting`, or `not_assessed`. |
| `contradiction_or_unknown` | Conflict or missing fact that could affect the row. |
| `disconfirming_evidence` | Supplied evidence that weakens, contradicts, or limits a hypothesis or draft finding. |
| `plausible_alternative` | A plausible but incorrect, unsupported, less consistent, or unresolved explanation to preserve for later analysis. |
| `limitation` | Boundary on use, source quality, scope, or review. |
| `next_action` | Evidence request, review step, or safe escalation. |

## Stop Conditions

Stop or route upward when the user asks the skill to:

- fabricate, alter, hide, or strengthen evidence;
- state a finding from unsupported allegation;
- force a preferred conclusion or ignore disconfirming evidence;
- decide legal, licensing, privacy, employment, or disciplinary outcome;
- use unauthorized private records;
- analyze intrusive collection without authority, purpose, privacy basis, and human approval.

## Family 09 Hard Reasoning Rule

`FACT ≠ INFERENCE ≠ ALLEGATION ≠ FINDING`

Keep these categories distinct:

- `FACT`
- `INFERENCE`
- `ALLEGATION`
- `FINDING`

When the matrix supports later analysis, preserve plausible but incorrect hypotheses and disconfirming evidence instead of smoothing them into a single preferred explanation.

## Output Quality

A good matrix is neutral, source-linked, and explicit about unknowns. It should make reviewer burden lower without making the case look stronger than the evidence supports.
