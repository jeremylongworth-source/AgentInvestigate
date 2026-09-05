# Assess Association Strength Reference

## When To Read

Read this reference when using `assess-association-strength` for identity, entity, identifier, relationship, association, timeline, contradiction, or confidence analysis.

## Confidence Model

Use only these labels:

- `POSSIBLE`
- `PROBABLE`
- `CORROBORATED`
- `CONFIRMED`
- `UNRESOLVED`

## Review Questions

- What scope, authority, jurisdiction, human approval, lawful purpose, privacy basis, and intended use are supplied?
- Which identifiers, records, source claims, dates, relationships, or events are directly supplied?
- Which sources are independent, current, reliable, corroborated, conflicting, stale, or unresolved?
- What same-name, partial-identifier, alias, date, location, organization, or timeline ambiguity remains?
- What would be overclaimed if treated as `CONFIRMED`?

## Overclaiming Boundaries

- Do not treat same name, physical resemblance, proximity, shared organization, stale record, single-source claim, or client certainty as confirmed identity.
- Do not merge records when material identifiers conflict.
- Do not infer private relationships or associations from weak, incidental, or context-free signals.
- Do not fill timeline gaps or continuity breaks without source support.

## Output Boundary

Provide bounded ambiguity analysis, confidence labels, source limits, corroboration, contradictions, gaps, and review needs. Do not identify, track, profile, target, screen, or locate a person without the required authority and intrusive gates.
