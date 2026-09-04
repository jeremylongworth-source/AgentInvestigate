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
| `limitation` | Boundary on use, source quality, scope, or review. |
| `next_action` | Evidence request, review step, or safe escalation. |

## Stop Conditions

Stop or route upward when the user asks the skill to:

- fabricate, alter, hide, or strengthen evidence;
- state a finding from unsupported allegation;
- decide legal, licensing, privacy, employment, or disciplinary outcome;
- use unauthorized private records;
- analyze intrusive collection without authority, purpose, privacy basis, and human approval.

## Output Quality

A good matrix is neutral, source-linked, and explicit about unknowns. It should make reviewer burden lower without making the case look stronger than the evidence supports.
