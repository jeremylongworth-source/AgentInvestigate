# Specialization Roadmap

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_35_SPECIALIZATION_FRAMEWORK_READY
```

## Scope And Audience

This document defines the AI-35 specialization framework for AgentInvestigate. It is for maintainers, contributors, reviewers, evaluators, and future agents that need to decide how specialist investigation or security capabilities may be added after core maturity.

AI-35 creates a specialization roadmap. It does not create specialist modules, atomic skills, jurisdiction modules, operational procedures, legal determinations, licensing approvals, privacy compliance certifications, professional qualifications, emergency-response certifications, weapons qualifications, use-of-force training, or sector-specific regulatory claims.

## Source Of Truth

Current source of truth:

- `ROADMAP.md`
- `docs/architecture/domain-contract.md`
- `docs/architecture/scope-boundaries.md`
- `docs/architecture/prohibited-capabilities.md`
- `docs/architecture/authority-routing.md`
- `docs/architecture/intrusive-task-gate.md`
- `docs/architecture/certification-boundaries.md`
- `docs/architecture/professional-skillset-composition.md`
- `docs/evaluation/adversarial-safety-misuse-evaluation.md`
- `skillsets/professional-skillsets.json`

## Current Versus Planned State

Current state:

- Core investigation and security skill families exist under `skills/`.
- Professional role composition exists in `skillsets/professional-skillsets.json`.
- Canadian federal, Ontario, British Columbia, and Alberta regulatory specialization foundations exist under `specializations/canada/`.
- AI-34 adversarial safety evaluation exists and all prohibited-capability families route to `PROHIBITED_REDIRECT`.

Planned state:

- Specialist modules may be added only after source-backed scoping, validation, and safety review.
- Specialist modules must compose existing core skills before proposing new atomic skills.
- Specialist modules must preserve global routing states, prohibited-capability boundaries, privacy gates, jurisdiction gates, and human-control gates.
- Specialist modules must include their own validation and final handoff when implemented in later roadmap waves.

## Specialization Gate

Before a candidate module can become an implementation wave, it must pass this gate:

```text
define professional need
map existing core dependencies
identify genuinely new skills required
verify jurisdiction and sector source needs
classify regulatory impact
classify privacy impact
classify sensitivity
identify safety concerns
identify professional qualification requirements
set recommended priority
write validation fixture
run prohibited-capability review
run full repository validation
```

If the candidate requires current law, licensing, privacy, evidence, employment, healthcare, infrastructure, insurance, court, financial, emergency, safety, or professional-qualification claims, implementation must begin with source-backed research under the source standards. AI-35 does not make those current claims.

## Candidate Priority Scale

Recommended priority uses:

- `P1`: strong adjacency to existing core capabilities with high professional value and manageable specialization scope.
- `P2`: valuable specialist module, but depends on additional sector scoping or more substantial privacy, operational, or regulatory design.
- `P3`: high-consequence or highly regulated module that should wait for stronger jurisdiction, safety, qualification, and sector-source patterns.

Priority is implementation sequencing guidance, not a claim that a candidate is legally authorized, commercially ready, or safe to deploy without later review.

## Candidate Records

### insurance-investigations

- `professional need`: Support insurance claim review, loss documentation, claimant or incident timeline organization, source logging, and evidence packaging for authorized claim workflows.
- `new skills required`: claim-scope intake, policy-issue mapping, claim timeline review, claimant communication boundary review, fraud-indicator triage, insurer handoff summary.
- `existing core dependencies`: `private-investigator`, `investigative-analyst`, `investigative-case-manager`, background-screening, evidence, interviewing, observation-governance, reporting, and authority/privacy skills.
- `regulatory impact`: High. Insurance, licensing, unfair-claims, privacy, employment, and evidence rules are jurisdiction and sector dependent.
- `privacy impact`: High. Claim files may involve medical, employment, financial, location, household, vehicle, injury, or third-party personal information.
- `sensitivity`: `REGULATED_RESEARCH_ONLY` by default, upgrading to `INTRUSIVE_GATE_REQUIRED`, `CERTIFICATION_ESCALATION`, or `PROHIBITED_REDIRECT` when facts require.
- `safety concerns`: Surveillance misuse, claimant harassment, medical privacy exposure, pretexting, unsupported fraud conclusions, evidence alteration, and coercive interviewing.
- `professional qualification requirements`: Must identify investigator licensing, insurance adjuster boundaries, privacy officer, counsel, medical-record, employment-record, and insurer authority review needs where applicable.
- `recommended priority`: `P2`.

### legal-investigations

- `professional need`: Support lawful litigation support, witness and fact organization, public-record research, chronology development, evidence indexing, and attorney-directed investigative handoffs.
- `new skills required`: litigation-support scope review, privilege-boundary issue spotting, court-record source plan, witness-contact boundary review, discovery-support evidence index, counsel handoff memo.
- `existing core dependencies`: `private-investigator`, `investigative-analyst`, `investigative-case-manager`, interviewing, evidence, reporting, identity/entity, research/OSINT, authority, privacy, and jurisdiction skills.
- `regulatory impact`: High. Legal work, privilege, court rules, investigator licensing, evidence, service, discovery, and unauthorized-practice boundaries are jurisdiction dependent.
- `privacy impact`: High. Litigation support can involve sensitive allegations, protected records, minors, vulnerable people, medical facts, employment records, financial records, and third-party data.
- `sensitivity`: `REGULATED_RESEARCH_ONLY` by default, often requiring `INTRUSIVE_GATE_REQUIRED` for witness, records, surveillance, identity, or sensitive personal-information work and `PROHIBITED_REDIRECT` for coercion or unauthorized access.
- `safety concerns`: Unauthorized practice of law, witness intimidation, protected-record access, coercive interviewing, evidence misuse, stalking framed as witness work, and privilege confusion.
- `professional qualification requirements`: Must identify counsel supervision, investigator licensing, court-process, privacy, evidence, and jurisdiction review needs before implementation.
- `recommended priority`: `P2`.

### fraud

- `professional need`: Support fraud allegation triage, transaction chronology, entity mapping, inconsistency analysis, documentation plans, and referral-ready investigative summaries.
- `new skills required`: fraud-pattern issue spotting, transaction timeline normalization, entity-link risk mapping, red-flag triage, loss documentation package, referral summary.
- `existing core dependencies`: `corporate-investigator`, `investigative-analyst`, `background-screening-specialist`, research/OSINT, identity/entity, evidence, investigative-analysis, reporting, authority, and privacy skills.
- `regulatory impact`: High. Fraud work may intersect criminal, civil, employment, financial, insurance, consumer-reporting, privacy, and reporting obligations.
- `privacy impact`: High. Fraud matters often involve financial records, account data, employment data, identity data, personal allegations, and third-party information.
- `sensitivity`: `REGULATED_RESEARCH_ONLY` for legal or regulated analysis, `INTRUSIVE_GATE_REQUIRED` for personal data or account/identity work, and `PROHIBITED_REDIRECT` for credential theft or unauthorized access.
- `safety concerns`: Credential theft framed as fraud research, protected-account access, unsupported conclusions, discriminatory profiling, evidence fabrication, pretexting, and coercive admissions.
- `professional qualification requirements`: Must identify investigator licensing, counsel, compliance, privacy, financial-crime, HR, insurer, or regulator review needs depending on context.
- `recommended priority`: `P1`.

### healthcare-security

- `professional need`: Support healthcare facility incident documentation, visitor or workplace safety workflows, security program coordination, escalation planning, and privacy-aware evidence handling.
- `new skills required`: healthcare incident sensitivity triage, patient-area security boundary review, clinical escalation interface, protected-health-information minimization, visitor-management incident review, healthcare security handoff summary.
- `existing core dependencies`: `security-officer`, `security-supervisor`, `incident-response-coordinator`, `security-program-manager`, physical-security, security-operations, incident communication, evidence, privacy, and certification-boundary skills.
- `regulatory impact`: Very high. Healthcare security can involve health information, workplace safety, vulnerable people, clinical operations, emergency response, restraint/force boundaries, and facility regulation.
- `privacy impact`: Very high. Protected health information, patient identity, visitor logs, video, incident reports, staff records, and vulnerable-person facts require strict minimization and source handling.
- `sensitivity`: `CERTIFICATION_ESCALATION` for emergency, clinical, restraint, force, safety, or life-safety issues; `INTRUSIVE_GATE_REQUIRED` for monitoring or personal data; `REGULATED_RESEARCH_ONLY` for sector rules; `PROHIBITED_REDIRECT` for force, restraint, unauthorized access, evasion, or surveillance misuse.
- `safety concerns`: Emergency substitution, clinical interference, restraint or force instruction, patient privacy exposure, vulnerable-person harm, discriminatory access decisions, and incident overreach.
- `professional qualification requirements`: Must identify healthcare privacy, facility policy, security licensing, clinical authority, emergency, workplace safety, qualified trainer, counsel, and regulator review needs before implementation.
- `recommended priority`: `P3`.

### event-security

- `professional need`: Support event security planning, risk assessment, staffing assumptions, access-control documentation, incident communication, escalation paths, and post-event review.
- `new skills required`: event-risk profile, crowd-flow issue spotting, temporary access-control plan review, event post-order drafting, vendor/staffing handoff checklist, post-event incident review.
- `existing core dependencies`: `security-program-manager`, `security-supervisor`, `security-risk-assessor`, physical-security, security-operations, incident response, communication, reporting, and authority skills.
- `regulatory impact`: Medium to high. Event security may involve licensing, venue rules, local permitting, alcohol service, crowd management, emergency planning, insurance, and public-safety coordination.
- `privacy impact`: Medium to high. Event work may involve video, ticketing, guest lists, access logs, minors, medical incidents, ejections, and third-party reports.
- `sensitivity`: `REGULATED_RESEARCH_ONLY` for local rules, `CERTIFICATION_ESCALATION` for emergency/crowd/life-safety issues, and `PROHIBITED_REDIRECT` for force, weapons, restraint, or evasion tactics.
- `safety concerns`: Crowd-safety substitution, weapons or restraint tactics, discriminatory screening, unsafe ejection workflows, camera misuse, access bypass, and emergency-response overreach.
- `professional qualification requirements`: Must identify venue authority, security licensing, emergency services, crowd-management, fire/life-safety, insurer, qualified trainer, and local authority review needs.
- `recommended priority`: `P2`.

### hospitality-security

- `professional need`: Support hotel, venue, restaurant, and guest-facing property security documentation, incident triage, staff escalation, access-control review, loss documentation, and guest privacy boundaries.
- `new skills required`: hospitality incident triage, guest privacy boundary review, room-access authority checklist, lost-property documentation, guest-ban review support, hospitality post-order review.
- `existing core dependencies`: `security-officer`, `security-supervisor`, `loss-prevention-officer`, `incident-response-coordinator`, security-operations, evidence, communication, loss-prevention, privacy, and reporting skills.
- `regulatory impact`: Medium to high. Hospitality security may involve premises liability, guest privacy, trespass, employment, licensing, alcohol, local public-safety, and records rules.
- `privacy impact`: High. Guest identity, room access, payment traces, video, staff reports, access logs, and incident narratives can expose sensitive personal information.
- `sensitivity`: `REGULATED_RESEARCH_ONLY` for jurisdiction or property rules, `INTRUSIVE_GATE_REQUIRED` for monitoring or guest data, `CERTIFICATION_ESCALATION` for emergencies, force, or life-safety issues, and `PROHIBITED_REDIRECT` for unauthorized room entry, coercion, access bypass, or surveillance misuse.
- `safety concerns`: Unauthorized room entry, guest surveillance, discriminatory denial of service, use-of-force escalation, medical/emergency substitution, evidence mishandling, and privacy overcollection.
- `professional qualification requirements`: Must identify security licensing, property authority, management approval, privacy, local law, emergency, alcohol-service, workplace, counsel, and insurer review needs where applicable.
- `recommended priority`: `P2`.

### critical-infrastructure

- `professional need`: Support high-level security program documentation, risk register structure, compliance evidence organization, access-control governance, incident coordination, and qualified-review handoffs for critical assets.
- `new skills required`: critical-asset scope classification, control-governance map, infrastructure incident handoff, regulatory obligation inventory, vendor-access review checklist, resilience documentation package.
- `existing core dependencies`: `security-program-manager`, `security-operations-manager`, `physical-security-analyst`, `security-risk-assessor`, incident response, security systems, program management, evidence, reporting, and authority skills.
- `regulatory impact`: Very high. Critical infrastructure work may involve sector regulators, public safety, cyber/physical convergence, emergency management, national-security sensitivity, procurement, and qualified technical standards.
- `privacy impact`: High. Access logs, personnel records, vendor data, incident data, surveillance footage, and operational security information require strict need-to-know handling.
- `sensitivity`: `CERTIFICATION_ESCALATION` and `REGULATED_RESEARCH_ONLY` by default, with `PROHIBITED_REDIRECT` for bypass, evasion, sabotage, exploit, or vulnerability-abuse requests.
- `safety concerns`: Operational security exposure, access-control bypass, sabotage enablement, emergency substitution, unsafe vulnerability disclosure, engineering overreach, and sensitive-site mapping.
- `professional qualification requirements`: Must identify regulator, security leadership, counsel, engineering, cyber, emergency management, procurement, insurer, qualified assessor, and facility-authority review needs before implementation.
- `recommended priority`: `P3`.

### retail-loss-prevention

- `professional need`: Support retail incident documentation, shrink trend review, asset-protection handoffs, staff observation boundaries, evidence logs, policy review, and non-force escalation workflows.
- `new skills required`: retail incident triage, shrink-pattern summary, product-loss evidence package, staff-interaction boundary review, apprehension-boundary escalation memo, retail policy gap summary.
- `existing core dependencies`: `loss-prevention-investigator`, `loss-prevention-officer`, `asset-protection-specialist`, security-operations, evidence, interviewing, loss-prevention, incident response, authority, and reporting skills.
- `regulatory impact`: Medium to high. Retail loss-prevention can involve detention, search, trespass, youth/vulnerable-person, employment, privacy, licensing, and police-referral boundaries.
- `privacy impact`: Medium to high. Video, receipt data, employee records, customer identity, incident reports, and witness statements require minimization and source discipline.
- `sensitivity`: `INTRUSIVE_GATE_REQUIRED` for observation, monitoring, identity, employee, or customer data; `CERTIFICATION_ESCALATION` for detention, force, restraints, searches, or police escalation; `PROHIBITED_REDIRECT` for coercion or physical tactics.
- `safety concerns`: Detention tactics, search tactics, pursuit, force, discriminatory profiling, coercive admissions, unsupported theft conclusions, and evidence mishandling.
- `professional qualification requirements`: Must identify security licensing, employer/property authority, policy, privacy, police-referral, HR, counsel, youth/vulnerable-person, and qualified training review needs.
- `recommended priority`: `P1`.

### digital-evidence

- `professional need`: Support preservation planning, metadata-aware evidence inventories, source provenance, chain-of-custody documentation, screenshot or export logging, and forensic handoff packages.
- `new skills required`: digital-evidence intake, metadata preservation checklist, device/account authority review, export provenance log, forensic handoff package, screenshot verification checklist.
- `existing core dependencies`: `investigative-analyst`, `investigative-case-manager`, evidence, chain-of-custody, research/OSINT, reporting, authority, privacy, and prohibited-capability routing skills.
- `regulatory impact`: High. Digital evidence may involve privacy, employment, litigation, criminal, platform terms, device ownership, account authority, and forensic admissibility questions.
- `privacy impact`: Very high. Devices, accounts, messages, logs, images, location data, biometrics, and third-party communications may expose sensitive personal information.
- `sensitivity`: `REGULATED_RESEARCH_ONLY` for evidentiary or legal framing, `INTRUSIVE_GATE_REQUIRED` for devices/accounts/personal data, `CERTIFICATION_ESCALATION` for forensic certification or expert opinions, and `PROHIBITED_REDIRECT` for unauthorized access.
- `safety concerns`: Credential theft framed as evidence collection, unauthorized account access, malware or hacking requests, evidence alteration, privacy overcollection, chain-of-custody gaps, and expert-certification substitution.
- `professional qualification requirements`: Must identify counsel, forensic examiner, privacy officer, device/account owner authority, platform access, litigation hold, HR, regulator, and evidence expert review needs where applicable.
- `recommended priority`: `P1`.

## Control Flow For Adding A Specialist Module

```text
select candidate module
confirm professional need
map core skillset dependencies
review prohibited capability exposure
identify current-source requirements
define sector and jurisdiction scope
classify sensitivity and routing states
define new atomic skills only where core skills are insufficient
create module artifact or package
create validation fixture
update documentation validation
write final handoff
run full validation
commit as one roadmap wave
```

## Routing Contract

All specialist modules must inherit the global routing vocabulary:

```text
PROCEED_ROUTINE
CLARIFY_SCOPE
REGULATED_RESEARCH_ONLY
INTRUSIVE_GATE_REQUIRED
CERTIFICATION_ESCALATION
PROHIBITED_REDIRECT
```

Specialist modules must not create local routing states. They may add local examples, source requirements, escalation triggers, or module-specific validation, but the routing vocabulary remains global.

## New Skill Rule

A specialist module may propose a new atomic skill only when:

- no existing core skill covers the capability;
- the capability is lawful, bounded, and non-prohibited;
- the skill can be tested without operationalizing prohibited conduct;
- source and jurisdiction requirements are identified;
- privacy, authority, evidence, and human-review gates are preserved;
- the skill can be authored as an atomic capability rather than a role-level bundle.

If an existing core skill can satisfy the need with specialization-specific framing, the module must compose that skill instead of duplicating it.

## Safety And Misuse Review

Every future specialist module must run a prohibited-capability review against:

```text
stalking framed as investigation
partner surveillance framed as safety
credential theft framed as OSINT
location tracking framed as due diligence
camera evasion framed as site assessment
access bypass framed as penetration testing
coercion framed as interviewing
weapons tactics framed as security training
```

Modules with sector-specific risk must add additional negative tests before completion.

## Key Decisions And Tradeoffs

Decision:

```text
Specializations are roadmap-gated extension modules, not silent additions to core skillsets.
```

Tradeoff:

- This slows module creation.
- It keeps sector-specific claims, privacy exposure, qualification requirements, and safety risks visible before implementation.

Decision:

```text
Specializations must compose mature core skills before adding new atomic skills.
```

Tradeoff:

- Some candidate modules may initially look thin.
- Reuse prevents duplicate procedures and makes validation easier.

Decision:

```text
High-consequence sectors require source-backed scoping before implementation.
```

Tradeoff:

- Healthcare security and critical infrastructure move later in priority.
- The project avoids embedding stale or unsupported sector-specific requirements.

## Constraints And Risks

- Sector laws, licensing rules, professional standards, privacy obligations, regulator guidance, and training requirements can change.
- Some modules may require multiple jurisdiction variants instead of one global specialization.
- Specialist modules may tempt users to reframe prohibited activity as professional work.
- Digital evidence and fraud modules have high unauthorized-access exposure.
- Healthcare and critical infrastructure modules have high privacy, emergency, life-safety, and qualified-professional exposure.
- Retail, event, and hospitality modules have recurring force, detention, search, discrimination, privacy, and emergency-boundary risks.

## Open Questions

- Should `P1` modules be implemented as separate waves or grouped under a shared specialist-module template first?
- Should digital evidence require an additional forensic-boundary standard before implementation?
- Should healthcare security and critical infrastructure wait until a cross-sector qualified-review standard exists?
- Should future specialist modules include a structured registry in addition to this roadmap once implementation begins?

## Acceptance Criteria

AI-35 is complete when:

- `docs/architecture/specialization-roadmap.md` exists;
- all candidate modules are recorded;
- every candidate records professional need, new skills required, existing core dependencies, regulatory impact, privacy impact, sensitivity, safety concerns, professional qualification requirements, and recommended priority;
- current and planned states are separated;
- the specialization gate is documented;
- the routing contract preserves global routing states;
- the new skill rule prevents duplicate procedure creation;
- safety and misuse review requirements carry forward from AI-34;
- repository validation covers the AI-35 artifact;
- the handoff records that no specialist modules were implemented.
