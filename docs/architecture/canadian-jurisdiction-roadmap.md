# Canadian Jurisdiction Roadmap

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_31_CANADA_EXPANSION_FRAMEWORK_READY
```

## Scope And Audience

This document defines the extension contract for adding Canadian provincial and territorial specializations after the Canada federal, Ontario, British Columbia, and Alberta modules.

It is for AgentInvestigate maintainers, contributors, reviewers, evaluators, and future AI agents that need to add jurisdiction modules without changing the core architecture.

This wave builds the extension contract. It does not create additional provincial or territorial modules.

No additional provincial or territorial modules beyond Ontario, British Columbia, and Alberta.

## Source Of Truth

Current repository source of truth for Canadian jurisdiction expansion:

- `ROADMAP.md`
- `docs/architecture/domain-contract.md`
- `docs/architecture/scope-boundaries.md`
- `docs/architecture/authority-routing.md`
- `docs/architecture/intrusive-task-gate.md`
- `docs/architecture/certification-boundaries.md`
- `docs/standards/regulatory-source-standard.md`
- `docs/standards/source-freshness-standard.md`
- `specializations/canada/federal/README.md`
- `specializations/canada/ontario/README.md`
- `specializations/canada/british-columbia/README.md`
- `specializations/canada/alberta/README.md`

## Current Versus Planned State

Current state:

- Canada federal architecture exists at `specializations/canada/federal/`.
- Ontario implementation exists at `specializations/canada/ontario/`.
- British Columbia implementation exists at `specializations/canada/british-columbia/`.
- Alberta implementation exists at `specializations/canada/alberta/`.
- Core routing states exist in `docs/architecture/authority-routing.md`.
- Regulatory source metadata and freshness rules exist in `docs/standards/regulatory-source-standard.md` and `docs/standards/source-freshness-standard.md`.

Planned state:

- Additional Canadian provinces and territories can be added as standalone modules.
- New jurisdiction modules must reuse the core routing states instead of creating local routing vocabularies.
- New modules must add source logs, routing fixtures, handoffs, README/changelog updates, and validation updates.
- New modules must preserve federal overlap handling through the Canada federal specialization.

## Candidate Jurisdictions

The roadmap candidates are:

```text
quebec
manitoba
saskatchewan
nova-scotia
new-brunswick
newfoundland-and-labrador
prince-edward-island
northwest-territories
nunavut
yukon
```

These slugs are canonical for future file paths unless a later architecture decision changes the naming standard.

## Module Path Contract

Each future Canadian jurisdiction module must live at:

```text
specializations/canada/<jurisdiction-slug>/
```

Required files for a full provincial or territorial module:

- `README.md`
- `source-log.yaml`
- `licensing-and-registration.md`
- `training-examination-and-conduct.md`
- `authority-restrictions-and-security-operations.md`
- `privacy-reporting-and-records.md`
- `provincial-laws-map.md`
- `routing-boundaries.md`

If a jurisdiction's official structure requires a different topic split, the module may add supplemental files, but the eight baseline files must remain present so validators and downstream consumers have a stable contract.

## Source Metadata Contract

Every new module must include `source-log.yaml` entries that follow `docs/standards/regulatory-source-standard.md`.

Each source entry must identify:

- `source_id`
- `source_title`
- `organization`
- `jurisdiction`
- `authority_level`
- `source_url`
- `publication_date`
- `effective_date`
- `accessed_date`
- `last_verified`
- `applicability`
- `supersession_risk`
- `used_by`

Canadian provincial and territorial investigation, security, privacy, access, workplace, trespass, and body-armour claims are HIGH-freshness claims unless a later source standard explicitly lowers the class.

## Required Coverage Contract

Each future provincial or territorial module must independently verify and document whether the jurisdiction has applicable sources for:

- investigator licensing
- security worker or security guard licensing
- security business or agency licensing
- training
- examinations, tests, or competency requirements
- professional conduct
- permitted authorities
- restrictions
- privacy interaction
- reporting
- security operations
- provincial or territorial laws materially relevant to scoped skills

Where applicable, the module must also explicitly check:

- body armour
- baton, weapon, or restraint restrictions
- patrol dog or dog-handler restrictions
- locksmith or automotive lock bypass boundaries
- public-sector privacy and access law
- private-sector privacy law
- health-information law
- human-rights law
- employment standards
- occupational health and safety
- trespass or property-access law
- municipal by-law exposure
- Indigenous governance or reserve-specific escalation needs
- federal overlap through AI-27

If no directly applicable official source is found for a coverage area, the module must say that source coverage was not found during the documented verification window and route consequential decisions to qualified review.

## Routing Contract

Future Canadian jurisdiction modules must inherit these routing states:

```text
PROCEED_ROUTINE
CLARIFY_SCOPE
REGULATED_RESEARCH_ONLY
INTRUSIVE_GATE_REQUIRED
CERTIFICATION_ESCALATION
PROHIBITED_REDIRECT
```

New modules must not create jurisdiction-specific routing states. Jurisdiction files may add local examples and required statements, but the state vocabulary remains global.

Use `REGULATED_RESEARCH_ONLY` when authorization depends on licensing, registration, privacy, employment, records, public-sector access, private security authority, investigative authority, body armour, equipment, uniform, business licence, training, examination, source currentness, or similar regulated facts.

Use `INTRUSIVE_GATE_REQUIRED` when the facts involve surveillance, monitoring, location, biometrics, health information, high-impact screening, sensitive workplace allegations, covert observation, persistent observation, or third-party incidental capture.

Use `CERTIFICATION_ESCALATION` when the user asks AgentInvestigate to certify, approve, sign off, guarantee, or substitute for a regulator, counsel, trainer, licensed professional, privacy officer, HR, insurer, engineer, fire/life-safety professional, or emergency authority.

Use `PROHIBITED_REDIRECT` when the request asks for bypass, evasion, impersonation, unauthorized access, lock bypass, forced entry, unlawful tracking, stalking, coercive questioning, physical intervention tactics, detention tactics, search tactics, use-of-force instruction, weapon instruction, patrol-dog tactics, evidence alteration, fabricated records, or concealment.

## Federal Overlap Contract

Every provincial or territorial module must include a federal overlap rule:

```text
Federal privacy, criminal-law, evidence, human-rights, federally regulated workplace, or labour issues may also apply and must be checked against the Canada federal specialization.
```

Where federal and local sources overlap, outputs must:

- identify the overlap;
- cite current local source verification when available;
- cite current federal source verification when available;
- avoid resolving conflicts as a legal conclusion;
- route unresolved or consequential issues to qualified review.

## Naming And Slug Rules

Use lowercase ASCII jurisdiction slugs with hyphens between words:

- `quebec`
- `manitoba`
- `saskatchewan`
- `nova-scotia`
- `new-brunswick`
- `newfoundland-and-labrador`
- `prince-edward-island`
- `northwest-territories`
- `nunavut`
- `yukon`

Do not use abbreviations such as `qc`, `mb`, `sk`, `nwt`, or `pei` for canonical paths.

## Control Flow For Adding A Jurisdiction

```text
select roadmap jurisdiction
create jurisdiction path
verify official source set independently
create source-log.yaml
create baseline module files
define non-authority statement
define federal overlap statement
create regulatory fixture
extend documentation validation
extend specialization validation
update README and CHANGELOG
write final handoff
run full validation
commit as one roadmap wave
```

## Validation Contract

Each future module must update:

- `scripts/validate-docs.py`
- `scripts/validate-specializations.py`
- `tests/regulatory/AI-<wave>-<jurisdiction-slug>-specialization.json`
- `docs/development/handoffs/AI-<wave>-final-handoff.md`

The fixture must verify:

- completion token;
- specialization path;
- jurisdiction display name;
- HIGH freshness;
- required coverage;
- required source IDs;
- routing scenarios for `REGULATED_RESEARCH_ONLY`;
- routing scenarios for `INTRUSIVE_GATE_REQUIRED`;
- routing scenarios for `CERTIFICATION_ESCALATION`;
- routing scenarios for `PROHIBITED_REDIRECT`;
- federal overlap behavior.

## Key Decisions And Tradeoffs

Decision:

```text
Add each Canadian province or territory as a standalone specialization module.
```

Tradeoff:

- This duplicates some file structure across jurisdictions.
- It keeps local law, privacy, licensing, training, source metadata, and routing examples isolated and independently updatable.

Decision:

```text
Keep Canadian jurisdiction modules source-backed and HIGH freshness by default.
```

Tradeoff:

- Each wave requires independent verification.
- Later outputs are less likely to rely on stale or universalized regulatory claims.

Decision:

```text
Use one global routing vocabulary across all Canadian modules.
```

Tradeoff:

- Local modules cannot invent finer-grained states.
- Routing remains testable, composable, and consistent with existing AgentInvestigate architecture.

## Constraints And Risks

- Provincial and territorial law can change after a module is committed.
- Official guidance, regulator pages, training providers, fees, forms, licence classes, exemptions, and privacy procedures may change without a repository architecture change.
- Some jurisdictions may not organize investigation and security regulation the same way as Ontario, British Columbia, or Alberta.
- Quebec may require bilingual or French-first source handling and review.
- Northern territories may have smaller source footprints and more reliance on official legislation, regulator contact, or qualified review.
- Indigenous governance, reserve-specific rules, municipal by-laws, public bodies, federally regulated organizations, and sector-specific rules may overlap with local modules.

## Open Questions

- Which candidate jurisdiction should AI-32 or a later regulatory wave prioritize if professional skillset composition is delayed?
- Should Quebec require a separate bilingual-source validation rule before authoring begins?
- Should future modules include a structured `jurisdiction-profile.json` in addition to Markdown and YAML once repeated implementation patterns stabilize?
- Should municipal by-law handling become a separate extension layer after province and territory coverage matures?

## Acceptance Criteria

AI-31 is complete when:

- `docs/architecture/canadian-jurisdiction-roadmap.md` exists;
- the candidate jurisdiction slugs are canonicalized;
- future module paths and required files are defined;
- source metadata and HIGH-freshness expectations are defined;
- required coverage is defined;
- routing inheritance is defined;
- federal overlap handling is defined;
- validation requirements are defined;
- AI-31 docs and fixture are covered by repository validation;
- the handoff records that no additional province or territory module was created.
