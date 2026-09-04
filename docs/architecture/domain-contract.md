# AgentInvestigate Domain Contract

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_01_DOMAIN_CONTRACT_READY
```

## Scope And Audience

This document defines the professional domain boundaries for AgentInvestigate. It is for maintainers, contributors, evaluators, and AI agents that need to decide whether a proposed skill belongs in this repository.

AgentInvestigate is a decision-support repository for lawful professional work in:

- private investigation;
- investigative research;
- evidence management;
- interviewing and statements;
- investigative analysis;
- corporate and workplace investigations;
- background screening and due diligence;
- private security operations;
- incident response;
- access and patrol operations;
- physical security;
- security risk assessment;
- loss prevention;
- security program management.

AgentInvestigate does not grant authority, licensing, certification, police powers, legal authority, use-of-force qualification, weapons qualification, engineering approval, or emergency-response qualification.

## Source Of Truth

Current repository source of truth:

- `ROADMAP.md`
- `docs/development/AI-00-baseline-audit.md`
- `docs/development/handoffs/AI-00-final-handoff.md`
- this AI-01 domain contract and companion scope documents

Planned source of truth:

- AI-02 must add the canonical `AgentInvestigate Master Taxonomy v1.0` in repository form.
- AI-03 must define sensitivity and authority routing in greater detail.
- AI-05 must define source freshness and regulatory source handling before regulated skill authoring.

## Current Versus Planned State

Current state:

- The repository has baseline governance files and AI-00/AI-01 architecture docs.
- No skills, skillsets, jurisdiction modules, source maps, shared schemas, or evaluation fixtures exist yet.

Planned state:

- Atomic skills will live under domain families.
- Skillsets will compose atomic skills into role-level professional systems.
- Jurisdiction specializations will isolate legal, licensing, privacy, and regulatory details.
- Shared assets will be added only when real skills consume them.

## Private Investigation

Private investigation is the branch for authorized fact-finding and information development performed to answer investigative questions, assess evidence, document findings, and support lawful decision making.

In AgentInvestigate, private-investigation skills may support:

- case intake and scope definition;
- authority and lawful-purpose checks;
- investigative planning;
- investigative research and open-source research;
- identity and entity ambiguity analysis;
- interview and statement preparation;
- evidence organization;
- chronology and hypothesis analysis;
- workplace and corporate investigation support;
- background-screening and due-diligence support;
- investigative reporting.

Private-investigation skills must not imply:

- law-enforcement authority;
- power to compel cooperation;
- authority to access private accounts or protected systems;
- authority to trespass, enter, search, seize, detain, threaten, coerce, or impersonate;
- permission to conduct intrusive work without jurisdiction, authority, privacy, necessity, proportionality, and human-approval gates.

## Private Security

Private security is the branch for authorized protection, observation, access control, incident response, patrol, loss prevention, security assessment, and security program work performed to protect people, property, assets, facilities, and operations.

In AgentInvestigate, private-security skills may support:

- post orders and shift planning;
- patrol and observation logs;
- access event documentation;
- incident recognition and notification;
- emergency-service support and scene preservation;
- communication and de-escalation planning;
- physical-security risk assessment;
- security-system requirements and event analysis;
- loss-prevention incident analysis;
- security policy, audit, training-requirement review, and program improvement.

Private-security skills must not imply:

- police authority;
- authority to use force;
- weapons, restraint, or combat instruction;
- emergency-response certification;
- alarm, lock, camera, credential, or access-control bypass;
- structural, electrical, fire-code, life-safety, or engineering approval.

## Shared Professional Core

The two branches may share:

- ethics;
- role-boundary analysis;
- conflict-of-interest checks;
- jurisdiction identification;
- licensing issue spotting;
- privacy and confidentiality handling;
- documentation standards;
- evidence terminology;
- case and incident logs;
- source reliability assessment;
- fact, allegation, inference, and finding separation;
- report quality controls;
- escalation rules.

Shared core material must not collapse private investigation and private security into a single generic role. Shared skills should be neutral, reusable procedures. Role-specific obligations belong in skillsets or jurisdiction modules.

## Overlap Rules

An AgentInvestigate skill may sit at the overlap of private investigation and private security only when the task is genuinely common to both branches.

Valid overlap examples:

- documenting an incident;
- building an evidence matrix;
- preserving uncertainty in a chronology;
- identifying whether jurisdiction is missing;
- preparing a neutral status update;
- identifying escalation requirements.

Invalid overlap examples:

- treating a security patrol as an investigation without authority;
- treating private investigation as permission to perform protective services;
- treating loss prevention as authority for coercive questioning;
- treating physical security assessment as permission to bypass controls;
- treating background screening as general person investigation without consent and legal basis.

## Professional Role Boundaries

AgentInvestigate may eventually compose atomic skills into professional skillsets, including:

- `private-investigator`;
- `investigative-analyst`;
- `investigative-case-manager`;
- `corporate-investigator`;
- `workplace-investigator`;
- `background-screening-specialist`;
- `security-officer`;
- `mobile-patrol-officer`;
- `loss-prevention-officer`;
- `physical-security-analyst`;
- `security-risk-assessor`;
- `incident-response-coordinator`;
- `security-program-manager`;
- `corporate-security-manager`.

Skillsets compose existing skills. They must not duplicate procedures or create authority beyond the user, organization, jurisdiction, license, contract, policy, and professional role.

## Decision-Support Limits

AgentInvestigate may help users:

- classify requests;
- identify missing authority, jurisdiction, consent, scope, evidence, or source support;
- structure plans and documents;
- compare evidence and hypotheses;
- draft professional outputs with limitations and uncertainty;
- route to human, legal, compliance, regulator, emergency, engineering, or qualified professional review.

AgentInvestigate must not decide:

- legal liability;
- criminal guilt;
- employee discipline or termination;
- admissibility as a binding legal conclusion;
- licensing eligibility as a final determination;
- regulatory compliance as a final determination;
- whether force should be used;
- whether emergency services are required when immediate danger is present;
- engineering, fire, electrical, or life-safety approval.

## Regulated Activity Boundaries

Regulated material must be jurisdiction-aware. The source scan for AI-01 confirmed that licensing and permitted work differ across jurisdictions. For example:

- Ontario publishes licence guidance distinguishing private investigator and security guard work.
- British Columbia's Security Services Act and related government guidance regulate security workers and security businesses, including categories such as private investigator and security guard services.
- California's Bureau of Security and Investigative Services licenses and regulates alarm, locksmith, private investigator, private security services, and repossession industries.
- U.S. employment background screening can trigger Fair Credit Reporting Act obligations, including notice, written permission, pre-adverse-action, adverse-action, investigative-report, and disposal requirements.

AgentInvestigate must treat these areas as regulated until proven otherwise:

- private investigator licensing;
- security guard, security worker, security business, and private patrol licensing;
- background screening and consumer reports;
- workplace investigations;
- privacy and personal information handling;
- recording, monitoring, and surveillance;
- public-record and court-record use;
- evidence collection, continuity, and retention;
- alarm, access-control, video surveillance, and security-system work;
- use-of-force, restraint, firearms, weapons, and protective services;
- emergency, fire, life-safety, structural, electrical, and building-code-adjacent work.

AI-01 does not encode jurisdiction-specific rules. It establishes that these topics require routing, source, freshness, and human-review controls before implementation.

## Specialist Boundaries

Specialist areas are not automatically in core scope merely because they involve investigation or security.

Candidate specialist areas require later architecture approval:

- insurance investigations;
- legal investigations;
- fraud;
- healthcare security;
- event security;
- hospitality security;
- critical infrastructure;
- retail asset protection;
- digital evidence.

High-sensitivity specialist candidates require separate review before roadmap admission:

- executive protection;
- technical surveillance;
- digital forensic acquisition;
- missing-person location work;
- undercover operations;
- counter-surveillance;
- international field investigations.

## Taxonomy Family Mapping

The roadmap's development waves imply 20 initial taxonomy families. AI-01 maps each family to the domain contract as follows:

| Family | Roadmap Area | Primary Branch | Domain Fit |
|---|---|---|---|
| 01 | Professional Core & Ethics | Shared | In scope as shared guardrail content. |
| 02 | Case Intake, Scope & Authority | Shared | In scope as the entry control layer. |
| 03 | Law, Licensing, Privacy & Compliance | Shared | In scope as regulated issue spotting and routing, not final legal advice. |
| 04 | Investigation Planning & Case Management | Private Investigation | In scope when authority and lawful purpose are established. |
| 05 | Research, OSINT & Public Records | Private Investigation | In scope for lawful public/open-source research with source and access boundaries. |
| 06 | Identity, Entity & Timeline Analysis | Private Investigation | In scope with uncertainty controls and anti-overclaiming rules. |
| 07 | Interviewing, Witnesses & Statements | Private Investigation | In scope for neutral preparation and documentation, not coercion or deception. |
| 08 | Evidence & Chain of Custody | Shared | In scope for organization and issue spotting, not final admissibility determinations. |
| 09 | Investigative Analysis | Private Investigation | In scope with fact/inference/allegation/finding separation. |
| 10 | Observation & Surveillance Governance | Private Investigation | In scope only as intrusive governance with human approval; no evasion tactics. |
| 11 | Reporting, Findings & Case Presentation | Shared | In scope for professional output drafting with limitations. |
| 12 | Corporate & Workplace Investigations | Private Investigation | In scope with policy, HR, legal, privacy, and authority boundaries. |
| 13 | Background Screening & Due Diligence | Private Investigation | In scope with consent, purpose, source, privacy, and jurisdiction gates. |
| 14 | Security Operations, Access & Patrol | Private Security | In scope for authorized operations documentation and planning. |
| 15 | Incident Response | Private Security | In scope for recognition, notification, preservation, documentation, and escalation. |
| 16 | Communication & De-escalation | Private Security | In scope for verbal planning and reporting, not physical intervention. |
| 17 | Physical Security & Risk Assessment | Private Security | In scope for conceptual risk assessment, not engineering or code approval. |
| 18 | Security Systems & Technology | Private Security | In scope for requirements and event analysis, not bypass or defeat. |
| 19 | Loss Prevention & Asset Protection | Hybrid | In scope where evidence, authority, privacy, and non-coercion controls hold. |
| 20 | Investigation & Security Program Management | Shared | In scope for policy, audit, KPI, training-requirement review, and improvement planning. |

Gate result:

```text
Every roadmap taxonomy family maps cleanly to the domain contract.
```

## Key Decisions And Tradeoffs

Decision:

```text
Keep Private Investigation and Private Security as separate branches with shared core controls.
```

Tradeoff:

- This creates more routing and taxonomy complexity.
- It prevents role collapse, authority confusion, and misuse-prone generalization.

Decision:

```text
Treat regulated and intrusive topics as architecture-gated, not ordinary knowledge content.
```

Tradeoff:

- Early development is slower.
- Later skill authoring should be safer, more testable, and easier to update when sources change.

## Validation Notes

AI-01 validates domain fit on paper. Behavioral tests begin in later waves after taxonomy, sensitivity routing, authoring standards, and evaluation standards exist.

## Open Questions

- Where is the full approved `AgentInvestigate Master Taxonomy v1.0` source text? AI-02 must either recover it or reconstruct it from the approved roadmap source with explicit provenance.
- Which jurisdiction should receive the first full regulatory implementation after the core architecture matures? The roadmap currently prioritizes Canada federal, then Ontario, British Columbia, and Alberta.
- What public contribution policy should govern high-sensitivity specialist proposals before v1?

## AI-01 Sources

- AgentInvestigate `ROADMAP.md`.
- Ontario security guard/private investigator licence guidance: https://www.ontario.ca/page/security-guard-or-private-investigator-licence-individuals
- Ontario Private Security and Investigative Services Act, 2005: https://www.ontario.ca/laws/statute/05p34
- British Columbia Security Services Act: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/07030_01
- British Columbia security industry licensing guidance: https://www2.gov.bc.ca/gov/content/employment-business/business/security-services/security-industry-licensing
- California Bureau of Security and Investigative Services: https://www.bsis.ca.gov/
- FTC employer consumer-report guidance: https://www.ftc.gov/business-guidance/resources/using-consumer-reports-what-employers-need-know
- ASIS Investigations Standard overview: https://www.asisonline.org/security-news/standards-guidelines/investigations-standard/
- ASIS Security Risk Assessment Standard overview: https://www.asisonline.org/security-news/standards-guidelines/security-risk-assessment-standard/
