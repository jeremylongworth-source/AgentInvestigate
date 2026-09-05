# Professional Skillset Composition

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_32_PROFESSIONAL_SKILLSETS_READY
```

## Scope And Audience

This document defines the AI-32 professional skillset composition layer for AgentInvestigate. It is for maintainers, contributors, evaluators, and future agents that need to route role-level investigative and security workflows through existing atomic skills.

AI-32 creates professional skillset definitions. It does not create new atomic skills, rewrite existing skill procedures, certify professional roles, or grant legal, licensing, regulatory, emergency, force, weapons, restraint, engineering, fire, or life-safety authority.

## Source Of Truth

Current source of truth:

- `ROADMAP.md`
- `docs/architecture/domain-contract.md`
- `docs/architecture/authority-routing.md`
- `docs/architecture/sensitivity-model.md`
- `docs/architecture/intrusive-task-gate.md`
- `docs/architecture/certification-boundaries.md`
- `docs/architecture/canadian-jurisdiction-roadmap.md`
- `docs/architecture/taxonomy-index.yaml`
- `skillsets/professional-skillsets.json`

The canonical skillset registry is `skillsets/professional-skillsets.json`.

## Current Versus Planned State

Current state:

- AI-01 through AI-31 created architecture, source standards, validators, atomic skill families, Canadian regulatory specialization foundations, and the Canadian jurisdiction expansion framework.
- Atomic skills exist under `skills/`.
- Skillset membership candidates exist in `docs/architecture/taxonomy-index.yaml` as `professional_skillsets`.

Planned state:

- AI-33 will evaluate multi-skill integration across representative professional scenarios.
- AI-34 will evaluate adversarial and misuse-resistance behavior.
- Later waves may add packaging, publication, or runtime orchestration.

## Composition Rule

```text
Skillsets compose skills.
They must not duplicate underlying procedures.
```

Skillsets may define role scope, sequencing, routing triggers, dependencies, jurisdiction requirements, authority requirements, sensitivity limits, escalation rules, expected outputs, and excluded responsibilities.

Skillsets must not copy atomic skill workflows into role files. Procedure details remain inside the underlying `skills/<family>/<skill>/SKILL.md` packages.

## Skillset Registry Contract

Each skillset entry in `skillsets/professional-skillsets.json` must define:

- `purpose`
- `included_skills`
- `routing_triggers`
- `dependencies`
- `jurisdiction_requirements`
- `authority_requirements`
- `sensitivity_limits`
- `escalation_rules`
- `expected_outputs`
- `excluded_responsibilities`

Each `included_skills` value must reference an existing atomic skill slug in `docs/architecture/taxonomy-index.yaml` and an implemented `SKILL.md` package under `skills/`.

## Investigation Skillsets

AI-32 defines these investigation skillsets:

```text
private-investigator
investigative-analyst
investigative-case-manager
corporate-investigator
workplace-investigator
background-screening-specialist
loss-prevention-investigator
```

Investigation skillsets must preserve investigative authority, lawful purpose, privacy, consent, source-access, evidence, interview, observation, screening, findings, report, and human-review boundaries.

## Security Skillsets

AI-32 defines these security skillsets:

```text
security-officer
mobile-patrol-officer
loss-prevention-officer
security-supervisor
security-operations-manager
physical-security-analyst
security-risk-assessor
incident-response-coordinator
security-program-manager
```

Security skillsets must preserve security service authority, site authority, post orders, licensing, privacy, incident escalation, supervisor review, emergency boundaries, operational non-force limits, engineering boundaries, fire/life-safety boundaries, and no-bypass rules.

## Hybrid Skillsets

AI-32 defines these hybrid skillsets:

```text
corporate-security-investigator
asset-protection-specialist
corporate-security-manager
```

Hybrid skillsets must keep private investigation and private security boundaries visible at the same time. A hybrid skillset must not collapse investigative authority into security authority or security authority into investigative authority.

## Derived Membership Decisions

Most skillset memberships are taken directly from `professional_skillsets` in `docs/architecture/taxonomy-index.yaml`.

Three roadmap skillsets did not have complete direct taxonomy tags and are derived from validated adjacent composition targets:

- `loss-prevention-officer`: derives from Family 19 loss-prevention and asset-protection skills.
- `security-operations-manager`: derives from `security-supervisor` tagged skills plus Family 20 program-management skills.
- `corporate-security-manager`: derives from `security-program-manager`, `security-supervisor`, `corporate-investigator`, `asset-protection-specialist`, and Family 20 program-management skills.

This is an explicit AI-32 composition decision, not a taxonomy rewrite.

## Routing Flow

```text
role-level request
classify request type
identify role fit
identify jurisdiction
validate authority
check licensing and regulatory issues
check privacy and source-access basis
check sensitivity and prohibited capabilities
select professional skillset
sequence included atomic skills
produce bounded role-level output
preserve limitations and escalation needs
```

## Sensitivity Limits

Every skillset inherits the global routing states:

```text
PROCEED_ROUTINE
CLARIFY_SCOPE
REGULATED_RESEARCH_ONLY
INTRUSIVE_GATE_REQUIRED
CERTIFICATION_ESCALATION
PROHIBITED_REDIRECT
```

Skillsets must route:

- missing jurisdiction, role, authority, source, scope, or subject facts to `CLARIFY_SCOPE`;
- legal, licensing, privacy, records, workplace, public-sector access, training, business, or compliance questions to `REGULATED_RESEARCH_ONLY`;
- surveillance, monitoring, identity, screening, sensitive workplace, health-information, or third-party capture questions to `INTRUSIVE_GATE_REQUIRED`;
- legal, licensing, emergency, force, weapons, restraint, alarm, engineering, fire, life-safety, training, compliance, or professional approval requests to `CERTIFICATION_ESCALATION`;
- hacking, credential theft, unauthorized access, lock bypass, forced entry, unlawful tracking, stalking, impersonation, coercion, evasion, alarm defeat, camera defeat, weapons use, restraint techniques, fabricated evidence, altered evidence, or concealed records to `PROHIBITED_REDIRECT`.

## Jurisdiction And Authority Requirements

Role-level outputs must identify:

- country, province, territory, state, or local jurisdiction before regulated work;
- user role and client or organizational authority;
- lawful purpose;
- scope boundaries;
- source and record access authority;
- licensing or registration issue areas;
- privacy and consent issues;
- human approval and escalation path;
- current-source verification needs.

Canadian role-level outputs must use `docs/architecture/canadian-jurisdiction-roadmap.md` and available Canadian specializations when federal, provincial, or territorial issues are present.

## Expected Outputs

Skillsets may produce:

- role-scoped intake questions;
- skill sequence plans;
- authority and jurisdiction gap lists;
- source and evidence checklists;
- investigation plan outlines;
- security operations workflows;
- incident and notification workflows;
- evidence and findings workflows;
- reporting workflows;
- program or assessment review workflows;
- limitations and escalation notes.

## Excluded Responsibilities

Skillsets must not provide:

- duplicated underlying skill procedures;
- legal advice or final legal conclusions;
- licensing approval or regulator substitution;
- privacy compliance certification;
- professional certification or training approval;
- law-enforcement authority;
- unauthorized investigation or surveillance;
- background screening without authority or required consent;
- coercive questioning;
- use-of-force instruction;
- weapon instruction;
- restraint techniques;
- detention tactics;
- search tactics;
- access-control bypass;
- lock bypass;
- alarm defeat;
- camera defeat;
- fabricated facts, fabricated records, altered evidence, or concealed source gaps.

## Validation Notes

AI-32 validation checks that:

- all 19 roadmap skillsets are present;
- each skillset defines the required fields;
- each included skill exists in the taxonomy and has an implemented `SKILL.md`;
- routing states are inherited from core architecture;
- derived membership rules are explicit;
- the composition rule prevents procedure duplication;
- documentation, fixture, and handoff files are present.

## Open Questions

- Should `professional_skillsets` in the taxonomy be updated later to include the three AI-32 derived roles directly?
- Should future packaging emit one runtime manifest per role in addition to the canonical registry?
- Should AI-33 integration evaluation use the full role registry or smaller scenario-specific role slices?
