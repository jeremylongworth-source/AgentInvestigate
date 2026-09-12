# Jurisdiction Model

Jurisdiction is a routing input, not a footnote. It is required whenever the answer depends on licensing, privacy, employment screening, workplace investigation, recording or monitoring, record access, evidence handling, security authority, emergency boundaries, alarm response, force, weapons, restraints, fire, life safety, or another regulated requirement.

## Current Canadian Foundations

AgentInvestigate currently includes:

- `specializations/canada/federal/`
- `specializations/canada/ontario/`
- `specializations/canada/british-columbia/`
- `specializations/canada/alberta/`

These modules are source-backed architecture foundations. They do not grant authority, licensing, legal advice, privacy compliance certification, or professional approval.

## Applying A Jurisdiction Module

1. Identify the location, organization type, professional role, activity, and affected parties.
2. Determine whether federal and provincial or territorial rules may overlap.
3. Read the relevant module's `README.md`, routing boundaries, and source log.
4. Verify current official sources before relying on a regulated claim.
5. Route unresolved or consequential questions to qualified legal, privacy, licensing, HR, safety, or professional review.

A jurisdiction module can identify issue areas and research paths. It must not turn incomplete facts into a final legal conclusion or authorization.

## Source Freshness

Regulatory, licensing, privacy, evidence, safety, and professional-requirement claims are high-freshness by default. Source logs record access and verification dates.

If a source may be stale or superseded, the result is `REVERIFICATION REQUIRED`. A stale source does not automatically prove that a skill is wrong, but it must not be treated as current without review.

## Federal Overlap

Federal privacy, criminal-law, evidence, human-rights, federally regulated workplace, or labour issues may overlap with provincial or territorial rules. AgentInvestigate must identify the overlap and preserve uncertainty; it must not resolve conflicts as final legal conclusions.

## Expansion

Future Canadian modules follow `docs/architecture/canadian-jurisdiction-roadmap.md` and inherit the global routing states. Future sector and specialist modules follow `docs/architecture/specialization-roadmap.md`.
