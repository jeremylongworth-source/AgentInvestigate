# AgentInvestigate Development Roadmap

**Project:** AgentInvestigate  
**Provisional repository:** `D:\AgentInvestigate`  
**Roadmap version:** 0.1  
**Taxonomy authority:** AgentInvestigate Master Taxonomy v1.0  
**Audited atomic skills:** 212  
**Primary branches:** Private Investigation + Private Security  
**Current execution target:** `AI-00`

---

# 1. Mission

AgentInvestigate will be an open-source AI skill repository for lawful professional work involving:

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

The repository should give general-purpose AI agents structured professional procedures, evidence requirements, reasoning frameworks, output contracts, legal and privacy gates, safety boundaries, and escalation rules.

AgentInvestigate does **not** confer:

- investigator licensing;
- security licensing;
- law-enforcement authority;
- regulatory approval;
- legal authority;
- use-of-force qualification;
- weapons qualification;
- professional certification;
- engineering approval;
- emergency-response certification.

Core principle:

```text
AUTHORITY BEFORE ACTION
EVIDENCE BEFORE CONCLUSION
HUMAN CONTROL BEFORE INTRUSIVE WORK
```

---

# 2. Development Principles

## 2.1 Atomic skills first

Good:

```text
build-evidence-matrix
validate-investigative-authority
write-investigative-report
triage-security-incident
assess-physical-vulnerabilities
```

Avoid:

```text
conduct-investigation
do-surveillance
manage-security
investigate-person
perform-background-check
```

Professional roles belong in the skillset layer.

---

## 2.2 Two professional branches

AgentInvestigate must maintain a structural distinction between:

```text
PRIVATE INVESTIGATION
```

and:

```text
PRIVATE SECURITY
```

They may share:

- ethics;
- legal routing;
- privacy;
- documentation;
- communication;
- evidence concepts;
- incident handling;
- program governance.

They must not be collapsed into a single generic "security investigator" model.

---

# 3. Sensitivity Model

Every skill must receive one sensitivity classification.

```text
ROUTINE
REGULATED
INTRUSIVE
CERTIFICATION_BOUNDARY
```

## ROUTINE

Examples:

```text
build-evidence-matrix
construct-event-chronology
prepare-case-status-update
```

Ordinary analytical or administrative professional work.

## REGULATED

Examples:

```text
identify-licensing-requirement
identify-recording-law-issue
review-training-requirements
```

Correct behavior depends materially on current law, regulation, professional requirements, or jurisdiction.

## INTRUSIVE

Examples:

```text
assess-observation-authorization
plan-background-screening
assess-information-collection-basis
```

Work involving surveillance, sensitive personal information or invasive investigative activity.

## CERTIFICATION_BOUNDARY

Work adjacent to activities requiring qualified or formally trained personnel.

Examples:

```text
support-emergency-service-access
determine-emergency-escalation
```

AgentInvestigate may assist with recognition, planning, documentation and escalation but must not provide operational substitutes for required professional training.

---

# 4. Intrusive Work Gate

No intrusive skill should route directly from a raw user request.

Required logical chain:

```text
REQUEST
   ↓
classify-request-type
   ↓
identify-jurisdiction
   ↓
validate-investigative-authority
   ↓
assess-lawful-purpose
   ↓
identify-privacy-obligation
   ↓
assess-information-collection-basis
   ↓
assess-necessity-proportionality
   ↓
assess-less-intrusive-alternative
   ↓
define-scope-boundaries
   ↓
HUMAN APPROVAL
   ↓
BOUNDED INTRUSIVE TASK
```

Codex must preserve this architecture throughout development.

---

# 5. Hard Repository Exclusions

The roadmap does not authorize procedural skill development for:

```text
hacking
credential theft
unauthorized account access
lock bypass
forced entry
access-control circumvention
covert tracker installation
illegal GPS tracking
stalking
intimate-partner monitoring
police impersonation
government impersonation
coercive interrogation
physical coercion
counter-surveillance evasion
camera evasion
alarm defeat
weapons use
firearm use
baton use
restraint techniques
combat techniques
```

Potential specialist areas not listed here still require explicit architecture approval before implementation.

---

# 6. Provisional Repository Architecture

Do not create empty directories simply to match this structure.

```text
AgentInvestigate/
│
├── README.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── SECURITY.md
│
├── docs/
│   ├── architecture/
│   ├── standards/
│   ├── research/
│   ├── evaluation/
│   └── development/
│
├── skills/
│   ├── professional-core/
│   ├── intake-authority/
│   ├── law-privacy-compliance/
│   ├── case-management/
│   ├── research-osint/
│   ├── identity-entity-analysis/
│   ├── interviewing/
│   ├── evidence/
│   ├── investigative-analysis/
│   ├── observation-governance/
│   ├── reporting/
│   ├── workplace-investigations/
│   ├── screening-due-diligence/
│   ├── security-operations/
│   ├── incident-response/
│   ├── communication-deescalation/
│   ├── physical-security/
│   ├── security-systems/
│   ├── loss-prevention/
│   └── program-management/
│
├── skillsets/
│
├── specializations/
│   └── canada/
│
├── shared/
│   ├── glossaries/
│   ├── legal/
│   ├── evidence/
│   ├── schemas/
│   └── templates/
│
├── tests/
│   ├── skills/
│   ├── routing/
│   ├── safety/
│   ├── regulatory/
│   ├── integration/
│   └── fixtures/
│
└── scripts/
```

---

# 7. Development Gate Model

Every development wave ends with:

```text
READY
PARTIALLY_READY
BLOCKED
```

Every closed wave must produce:

```text
completion token
final handoff
validation evidence
known limitations
recommended next wave
```

A later wave must not silently absorb unresolved work.

---

# WAVE AI-00
# Repository Discovery & Baseline Audit

## Objective

Establish repository truth.

## Codex tasks

1. Locate or verify `D:\AgentInvestigate`.
2. Inspect:
   - repository initialization;
   - current branch;
   - remote configuration;
   - tracked files;
   - untracked files;
   - documentation;
   - tooling;
   - existing skill content.
3. Inspect AgentSkills, ChefSkills and AgentLogistics only as architectural references where accessible.
4. Record useful reusable patterns.
5. Identify patterns that should **not** be copied because AgentInvestigate has different risk characteristics.
6. Make no broad implementation changes.

## Required artifact

```text
docs/development/AI-00-baseline-audit.md
```

## Gate

Repository truth and assumptions are documented.

## Completion token

```text
AGENTINVESTIGATE_AI_00_BASELINE_READY
```

---

# WAVE AI-01
# Domain & Scope Contract

## Objective

Freeze the professional boundaries of AgentInvestigate.

## Define

- private investigation;
- private security;
- overlap;
- exclusions;
- professional roles;
- decision-support limits;
- regulated activity boundaries;
- specialist boundaries.

## Required artifacts

```text
docs/architecture/domain-contract.md
docs/architecture/scope-boundaries.md
docs/architecture/prohibited-capabilities.md
```

## Gate

Every taxonomy family maps cleanly to the domain contract.

## Completion token

```text
AGENTINVESTIGATE_AI_01_DOMAIN_CONTRACT_READY
```

---

# WAVE AI-02
# Master Taxonomy Integration

## Objective

Convert the approved 212-skill taxonomy into repository development authority.

## Required artifacts

```text
docs/architecture/master-taxonomy-v1.md
docs/architecture/taxonomy-index.yaml
```

Each skill entry should identify:

```text
name
family
tier
sensitivity
jurisdiction_requirement
authority_requirement
freshness_requirement
priority
dependencies
professional_skillsets
```

## Gate

Exactly one canonical taxonomy source exists.

## Completion token

```text
AGENTINVESTIGATE_AI_02_MASTER_TAXONOMY_READY
```

---

# WAVE AI-03
# Sensitivity, Authority & Routing Contract

## Objective

Implement the architectural feature that distinguishes AgentInvestigate from ordinary knowledge repositories.

## Define

```text
ROUTINE
REGULATED
INTRUSIVE
CERTIFICATION_BOUNDARY
```

Create routing rules for:

- jurisdiction;
- licensing;
- lawful purpose;
- privacy;
- information collection;
- human approval;
- prohibited activity;
- escalation.

## Required artifacts

```text
docs/architecture/sensitivity-model.md
docs/architecture/authority-routing.md
docs/architecture/intrusive-task-gate.md
docs/architecture/certification-boundaries.md
```

## Gate

Representative requests from all four sensitivity classes route correctly on paper.

## Completion token

```text
AGENTINVESTIGATE_AI_03_SENSITIVITY_ROUTING_READY
```

---

# WAVE AI-04
# Skill Authoring Standard

## Objective

Define how every AgentInvestigate skill is authored.

## Standard must define

- naming;
- frontmatter;
- description;
- triggers;
- non-triggers;
- inputs;
- assumptions;
- dependencies;
- procedure;
- evidence requirements;
- source requirements;
- jurisdiction requirements;
- authority checks;
- sensitivity handling;
- outputs;
- limitations;
- escalation;
- references;
- testing requirements.

## Required artifacts

```text
docs/standards/skill-authoring-standard.md
docs/standards/skill-naming-standard.md
docs/standards/output-contract-standard.md
```

## Completion token

```text
AGENTINVESTIGATE_AI_04_SKILL_STANDARD_READY
```

---

# WAVE AI-05
# Legal, Regulatory & Evidence Source Standard

## Objective

Create source-handling requirements before regulated skills are authored.

## Define source hierarchy

```text
1. legislation / regulations / courts
2. government regulators
3. privacy authorities
4. recognized standards organizations
5. professional associations
6. academic / technical literature
7. specialist material
8. secondary summaries
```

## Regulatory metadata

```yaml
source_title:
organization:
jurisdiction:
authority_level:
source_url:
publication_date:
effective_date:
accessed_date:
last_verified:
applicability:
supersession_risk:
used_by:
```

## Required artifacts

```text
docs/standards/research-and-evidence-standard.md
docs/standards/regulatory-source-standard.md
docs/standards/source-freshness-standard.md
```

## Gate

A source-backed regulated skill can be updated without rewriting the repository architecture.

## Completion token

```text
AGENTINVESTIGATE_AI_05_SOURCE_STANDARD_READY
```

---

# WAVE AI-06
# Validation & Evaluation Framework

## Objective

Build quality controls before authoring at scale.

## Required test classes

```text
correct routing
incorrect routing
missing jurisdiction
missing authority
missing consent
prohibited request
regulated request
intrusive request
certification-boundary request
missing evidence
contradictory evidence
unsupported inference
source freshness
incorrect source jurisdiction
output-format compliance
```

## Evaluation model

Compare:

```text
general model
vs.
general model + AgentInvestigate skill
```

Evaluate:

- correctness;
- evidence discipline;
- uncertainty;
- source use;
- routing;
- privacy behavior;
- safety boundaries;
- usefulness.

## Required artifacts

```text
docs/standards/testing-standard.md
docs/standards/evaluation-standard.md
tests/
scripts/
```

## Completion token

```text
AGENTINVESTIGATE_AI_06_VALIDATION_FRAMEWORK_READY
```

---

# WAVE AI-07
# Shared Professional Foundations

## Objective

Create genuinely reusable material.

Candidate shared resources:

```text
professional terminology
evidence terminology
case status vocabulary
confidence vocabulary
source reliability vocabulary
jurisdiction schema
authority schema
sensitivity schema
common report structures
```

## Potential templates

```text
case-intake
conflict-check
authority-check
investigation-plan
case-action-log
research-source-log
interview-plan
evidence-log
chain-of-custody
evidence-matrix
case-chronology
incident-report
shift-handoff
risk-register
case-closure
```

## Rule

Do not create a shared asset unless a real skill consumes it.

## Completion token

```text
AGENTINVESTIGATE_AI_07_SHARED_FOUNDATIONS_READY
```

---

# WAVE AI-08
# Four-Class Reference Implementation

## Objective

Prove the repository architecture before bulk authoring.

Create at least one complete skill from each sensitivity class.

## Recommended ROUTINE skill

```text
build-evidence-matrix
```

## Recommended REGULATED skill

```text
identify-licensing-requirement
```

## Recommended INTRUSIVE skill

```text
assess-observation-proportionality
```

## Recommended CERTIFICATION_BOUNDARY skill

```text
determine-emergency-escalation
```

Each must include:

- complete metadata;
- references;
- tests;
- negative-routing tests;
- output contract;
- dependency checks.

## Hard gate

**Mass authoring is not authorized until AI-08 closes READY.**

## Completion token

```text
AGENTINVESTIGATE_AI_08_REFERENCE_SKILLS_READY
```

---

# WAVE AI-09
# Professional Core & Ethics

## Objective

Build Family 01.

Implement:

```text
define-professional-role-boundaries
assess-conflict-of-interest
apply-ethical-decision-framework
identify-investigative-bias
separate-fact-from-inference
assess-duty-of-care
protect-confidential-information
identify-escalation-requirement
document-professional-decision
```

## Composition

Begin shared professional-core routing.

## Completion token

```text
AGENTINVESTIGATE_AI_09_PROFESSIONAL_CORE_READY
```

---

# WAVE AI-10
# Intake, Authority, Law & Privacy

## Objective

Build Families 02 and 03 as the repository's principal control layer.

## Priority

All 22 skills in:

```text
Case Intake, Scope & Authority
Law, Licensing, Privacy & Compliance
```

## Critical integration tests

Test requests involving:

- ordinary research;
- workplace investigation;
- surveillance;
- personal background screening;
- unknown jurisdiction;
- prohibited request;
- conflicting client authority.

## Gate

Sensitive work must fail closed when authority or jurisdiction is missing.

## Completion token

```text
AGENTINVESTIGATE_AI_10_AUTHORITY_COMPLIANCE_READY
```

---

# WAVE AI-11
# Investigation Planning & Case Management

## Objective

Build Family 04.

Implement the 13 skills covering:

- investigation plans;
- investigative questions;
- timelines;
- leads;
- resources;
- milestones;
- case logs;
- notes;
- status;
- retention;
- review;
- gaps;
- closure.

## Composition target

Foundation for:

```text
private-investigator
investigative-case-manager
```

## Completion token

```text
AGENTINVESTIGATE_AI_11_CASE_MANAGEMENT_READY
```

---

# WAVE AI-12
# Research, OSINT & Public Records

## Objective

Build Family 05.

Implement 14 skills covering:

- research planning;
- public records;
- open sources;
- corporate records;
- court records;
- regulatory records;
- source reliability;
- provenance;
- corroboration;
- source conflict;
- organization research;
- property context;
- litigation research;
- research summaries.

## Hard boundary tests

Verify refusal or rerouting for:

```text
unauthorized database access
credential acquisition
private-account compromise
protected-record acquisition through deception
```

## Completion token

```text
AGENTINVESTIGATE_AI_12_RESEARCH_OSINT_READY
```

---

# WAVE AI-13
# Identity, Entity & Timeline Analysis

## Objective

Build Family 06.

## Required capabilities

```text
identity ambiguity
same-name differentiation
identifier normalization
subject timelines
relationship mapping
association evidence
timeline gaps
entity contradictions
```

## Required confidence model

```text
POSSIBLE
PROBABLE
CORROBORATED
CONFIRMED
UNRESOLVED
```

## Gate

Tests must detect and penalize identity overclaiming.

## Completion token

```text
AGENTINVESTIGATE_AI_13_ENTITY_ANALYSIS_READY
```

---

# WAVE AI-14
# Interviewing, Witnesses & Statements

## Objective

Build Family 07.

## Required emphasis

- neutral questioning;
- objectives;
- sequencing;
- information gaps;
- statements;
- notes;
- consistency;
- corroboration;
- follow-up;
- bias.

## Prohibited inference

Do not infer deception solely from:

```text
body language
eye contact
nervousness
personality
unsupported behavioral stereotypes
```

## Completion token

```text
AGENTINVESTIGATE_AI_14_INTERVIEWING_READY
```

---

# WAVE AI-15
# Evidence & Chain of Custody

## Objective

Build Family 08.

## Implement

All 12 evidence skills.

## Representative test

Create a fictional case containing:

- original evidence item;
- transfer;
- missing signature;
- duplicate copy;
- disputed timestamp;
- partial continuity record.

The skillset should identify the continuity issue without claiming admissibility as a legal conclusion.

## Completion token

```text
AGENTINVESTIGATE_AI_15_EVIDENCE_READY
```

---

# WAVE AI-16
# Investigative Analysis

## Objective

Build Family 09.

Implement:

```text
build-evidence-matrix
generate-investigative-hypotheses
test-investigative-hypothesis
compare-alternative-explanations
identify-evidence-contradiction
construct-event-chronology
analyze-pattern-of-events
assess-source-weight
assess-finding-confidence
identify-unresolved-question
draft-investigative-finding
```

## Hard reasoning rule

```text
FACT ≠ INFERENCE ≠ ALLEGATION ≠ FINDING
```

## Gate

Integration tests must include plausible but incorrect hypotheses.

The agent must consider disconfirming evidence.

## Completion token

```text
AGENTINVESTIGATE_AI_16_INVESTIGATIVE_ANALYSIS_READY
```

---

# WAVE AI-17
# Reporting, Findings & Case Presentation

## Objective

Build Family 11.

## Outputs

- investigative reports;
- incident reports;
- chronology;
- evidence summaries;
- findings matrices;
- executive summaries;
- report QA;
- case presentations;
- testimony-support outlines.

## Gate

Reports must identify:

```text
facts
sources
evidence
inference
limitations
unresolved questions
confidence
```

## Completion token

```text
AGENTINVESTIGATE_AI_17_REPORTING_READY
```

---

# WAVE AI-18
# Observation & Surveillance Governance

## Objective

Build Family 10.

This is a controlled, high-sensitivity wave.

## Implement only

```text
assess-observation-authorization
assess-observation-necessity
assess-observation-proportionality
define-observation-purpose
plan-lawful-observation-assignment
record-field-observation
minimize-third-party-information
review-observation-record-for-compliance
```

## Mandatory properties

```text
sensitivity: INTRUSIVE
jurisdiction_required: true
human_review_required: true
```

## Explicitly prohibited

No operational skills for:

```text
avoiding detection
following targets covertly
counter-surveillance defeat
tracking-device installation
security evasion
```

## Completion token

```text
AGENTINVESTIGATE_AI_18_OBSERVATION_GOVERNANCE_READY
```

---

# WAVE AI-19
# Corporate & Workplace Investigations

## Objective

Build Family 12.

## End-to-end test

```text
allegation
→ scope
→ allegations matrix
→ policy mapping
→ interview planning
→ evidence analysis
→ statement comparison
→ evidentiary support
→ findings
→ report
```

## Boundary

The AI does not decide:

```text
discipline
termination
legal liability
criminal guilt
```

## Completion token

```text
AGENTINVESTIGATE_AI_19_WORKPLACE_INVESTIGATIONS_READY
```

---

# WAVE AI-20
# Background Screening & Due Diligence

## Objective

Build Family 13.

## Required split

Distinguish:

```text
PERSON SCREENING
```

from:

```text
ENTITY DUE DILIGENCE
```

Personal screening requires stronger privacy and authority controls.

## Integration requirements

Test:

- consent;
- relevance;
- public records;
- conflicting identities;
- adverse information;
- unresolved records;
- bias risk.

## Completion token

```text
AGENTINVESTIGATE_AI_20_SCREENING_DUE_DILIGENCE_READY
```

---

# WAVE AI-21
# Security Operations, Access & Patrol

## Objective

Build Family 14.

Implement all 15 skills.

## Representative operational lifecycle

```text
post orders
→ shift plan
→ patrol
→ observation
→ access event
→ alarm
→ occurrence
→ handoff
→ log review
```

## Composition target

```text
security-officer
mobile-patrol-officer
```

## Completion token

```text
AGENTINVESTIGATE_AI_21_SECURITY_OPERATIONS_READY
```

---

# WAVE AI-22
# Incident Response, Communication & De-escalation

## Objective

Build Families 15 and 16.

## Incident capabilities

```text
recognition
escalation
notification
scene preservation
emergency-service support
documentation
post-incident review
```

## Communication capabilities

```text
conflict avoidance
de-escalation
radio communication
incident notification
audience adaptation
bias review
```

## Certification boundary

No physical intervention instruction.

## Completion token

```text
AGENTINVESTIGATE_AI_22_INCIDENT_COMMUNICATION_READY
```

---

# WAVE AI-23
# Physical Security & Risk Assessment

## Objective

Build Family 17.

## Required reasoning chain

```text
assets
→ threats
→ vulnerabilities
→ consequences
→ likelihood
→ risk
→ controls
→ gaps
→ options
→ prioritized improvements
```

## Boundary

Conceptual security analysis must not be presented as:

```text
structural engineering
electrical approval
fire-code approval
life-safety certification
```

## Composition target

```text
physical-security-analyst
security-risk-assessor
```

## Completion token

```text
AGENTINVESTIGATE_AI_23_PHYSICAL_SECURITY_READY
```

---

# WAVE AI-24
# Security Systems & Technology

## Objective

Build Family 18.

Implement system-analysis skills for:

- access control;
- video surveillance;
- intrusion detection;
- alarm monitoring;
- event analysis;
- coverage;
- failures;
- requirements.

## Explicit prohibition tests

Ensure the repository does not provide:

```text
alarm bypass
camera defeat
credential cloning
access-control circumvention
monitoring evasion
```

## Completion token

```text
AGENTINVESTIGATE_AI_24_SECURITY_SYSTEMS_READY
```

---

# WAVE AI-25
# Loss Prevention & Asset Protection

## Objective

Build Family 19.

## Implement

```text
assess-asset-protection-risk
analyze-loss-event
analyze-shrink-pattern
triage-loss-prevention-incident
map-loss-event-evidence
identify-process-control-weakness
prepare-loss-prevention-case-summary
build-asset-protection-improvement-plan
```

## Composition targets

```text
loss-prevention-officer
loss-prevention-investigator
asset-protection-specialist
```

## Completion token

```text
AGENTINVESTIGATE_AI_25_LOSS_PREVENTION_READY
```

---

# WAVE AI-26
# Investigation & Security Program Management

## Objective

Build Family 20.

## Implement

- investigative policy;
- security post orders;
- procedure review;
- file audits;
- program audits;
- KPIs;
- training requirements;
- corrective action;
- improvement measurement.

## Composition targets

```text
investigative-case-manager
security-supervisor
security-operations-manager
security-program-manager
corporate-security-manager
```

## Completion token

```text
AGENTINVESTIGATE_AI_26_PROGRAM_MANAGEMENT_READY
```

---

# WAVE AI-27
# Canadian Federal Regulatory Foundation

## Objective

Create the first jurisdiction specialization.

## Path

```text
specializations/canada/federal/
```

## Research areas

As applicable:

- federal privacy;
- criminal-law interaction;
- evidence-related federal concepts;
- federal human-rights considerations;
- information handling;
- federally regulated organizations;
- federal criminal prohibitions relevant to investigative/security work.

## Critical requirement

Do not imply that federal rules alone determine whether private investigative or security work is authorized.

Occupational licensing is often provincial.

## Completion token

```text
AGENTINVESTIGATE_AI_27_CANADA_FEDERAL_READY
```

---

# WAVE AI-28
# Ontario Investigation & Security Module

## Objective

Build the first provincial specialization.

## Path

```text
specializations/canada/ontario/
```

## Required coverage

Research current requirements for:

- investigator licensing;
- security licensing;
- training;
- professional conduct;
- permitted authorities;
- restrictions;
- privacy interaction;
- reporting;
- security operations;
- provincial laws materially relevant to scoped skills.

## Freshness

All regulatory references:

```text
freshness: HIGH
```

## Completion token

```text
AGENTINVESTIGATE_AI_28_ONTARIO_READY
```

---

# WAVE AI-29
# British Columbia Investigation & Security Module

## Objective

Build a separately sourced B.C. specialization.

## Path

```text
specializations/canada/british-columbia/
```

Do not mechanically clone Ontario assumptions.

## Completion token

```text
AGENTINVESTIGATE_AI_29_BRITISH_COLUMBIA_READY
```

---

# WAVE AI-30
# Alberta Investigation & Security Module

## Objective

Build Alberta-specific occupational and regulatory coverage.

## Path

```text
specializations/canada/alberta/
```

Again, independently verify Alberta requirements.

## Completion token

```text
AGENTINVESTIGATE_AI_30_ALBERTA_READY
```

---

# WAVE AI-31
# Canadian Jurisdiction Expansion Framework

## Objective

Define how additional provinces and territories are added without rewriting core architecture.

## Candidates

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

This wave builds the extension contract, not necessarily every jurisdiction.

## Required artifact

```text
docs/architecture/canadian-jurisdiction-roadmap.md
```

## Completion token

```text
AGENTINVESTIGATE_AI_31_CANADA_EXPANSION_FRAMEWORK_READY
```

---

# WAVE AI-32
# Professional Skillset Composition

## Objective

Compose existing atomic skills into role-level professional systems.

## Investigation skillsets

```text
private-investigator
investigative-analyst
investigative-case-manager
corporate-investigator
workplace-investigator
background-screening-specialist
loss-prevention-investigator
```

## Security skillsets

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

## Hybrid

```text
corporate-security-investigator
asset-protection-specialist
corporate-security-manager
```

## Each skillset must define

```text
purpose
included skills
routing triggers
dependencies
jurisdiction requirements
authority requirements
sensitivity limits
escalation rules
expected outputs
excluded responsibilities
```

## Rule

Skillsets compose skills.

They must not duplicate underlying procedures.

## Completion token

```text
AGENTINVESTIGATE_AI_32_PROFESSIONAL_SKILLSETS_READY
```

---

# WAVE AI-33
# Multi-Skill Integration Evaluation

## Objective

Prove AgentInvestigate works as a coherent professional system.

## Scenario A: Workplace allegation

```text
intake
→ jurisdiction
→ authority
→ scope
→ allegations
→ evidence
→ interviews
→ contradictions
→ findings
→ report
```

## Scenario B: Background-screening discrepancy

```text
scope
→ consent
→ source
→ identity ambiguity
→ conflicting record
→ corroboration
→ relevance
→ report
```

## Scenario C: Physical-security concern

```text
protected assets
→ threats
→ vulnerabilities
→ controls
→ gaps
→ options
→ improvement plan
```

## Scenario D: Security incident

```text
alarm
→ incident triage
→ escalation
→ scene preservation
→ evidence
→ timeline
→ report
→ corrective action
```

## Scenario E: Intrusive observation request

Test both:

```text
AUTHORIZED
```

and:

```text
INSUFFICIENT AUTHORITY
```

versions.

The second must stop before operational execution.

## Scenario F: Identity ambiguity

Provide two plausible same-name individuals.

The system must preserve uncertainty and avoid collapsing them into one person.

## Completion token

```text
AGENTINVESTIGATE_AI_33_INTEGRATION_VALIDATED
```

---

# WAVE AI-34
# Adversarial Safety & Misuse Evaluation

## Objective

Explicitly test whether legitimate investigative functionality can be redirected into prohibited behavior.

## Test families

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

## Expected behavior

```text
recognize misuse risk
stop prohibited procedure
retain benign professional assistance
redirect toward lawful alternatives
```

## Completion token

```text
AGENTINVESTIGATE_AI_34_SAFETY_EVALUATION_READY
```

---

# WAVE AI-35
# Specialized Investigation Framework

## Objective

Determine how specialist capabilities may be added after core maturity.

## Candidate modules

```text
insurance-investigations
legal-investigations
fraud
healthcare-security
event-security
hospitality-security
critical-infrastructure
retail-loss-prevention
digital-evidence
```

For each candidate record:

```text
professional need
new skills required
existing core dependencies
regulatory impact
privacy impact
sensitivity
safety concerns
professional qualification requirements
recommended priority
```

## Required artifact

```text
docs/architecture/specialization-roadmap.md
```

## Completion token

```text
AGENTINVESTIGATE_AI_35_SPECIALIZATION_FRAMEWORK_READY
```

---

# WAVE AI-36
# Public Documentation & Repository Readiness

## Objective

Prepare the repository for public use.

## Required public files

```text
README.md
ROADMAP.md
CONTRIBUTING.md
CHANGELOG.md
LICENSE
SECURITY.md
CODE_OF_CONDUCT.md
```

README should explain:

- what AgentInvestigate is;
- who it is for;
- supported domains;
- skill examples;
- sensitivity model;
- jurisdiction model;
- installation/use;
- validation;
- limitations;
- prohibited capabilities;
- contribution process.

## Completion token

```text
AGENTINVESTIGATE_AI_36_PUBLIC_READINESS_READY
```

---

# WAVE AI-37
# v1 Release Candidate Audit

## Objective

Determine whether AgentInvestigate deserves a v1 release.

## Audit dimensions

```text
taxonomy implementation
skill completeness
routing correctness
authority gating
privacy gating
regulatory freshness
source integrity
jurisdiction isolation
safety boundaries
evidence reasoning
identity-confidence behavior
tests
integration
professional skillsets
documentation
repository hygiene
licensing
```

## Possible verdicts

```text
V1_READY
V1_PARTIALLY_READY
V1_BLOCKED
```

Do not equate file existence with readiness.

## Completion token

```text
AGENTINVESTIGATE_AI_37_V1_RC_AUDIT_COMPLETE
```

---

# 8. Post-v1 Candidate Tracks

These should not automatically enter the v1 critical path.

```text
AGENTINVESTIGATE-US-JURISDICTIONS
AGENTINVESTIGATE-UK
AGENTINVESTIGATE-INSURANCE
AGENTINVESTIGATE-LEGAL
AGENTINVESTIGATE-FRAUD
AGENTINVESTIGATE-DIGITAL-EVIDENCE
AGENTINVESTIGATE-HEALTHCARE-SECURITY
AGENTINVESTIGATE-EVENT-SECURITY
AGENTINVESTIGATE-HOSPITALITY-SECURITY
AGENTINVESTIGATE-CRITICAL-INFRASTRUCTURE
AGENTINVESTIGATE-RETAIL-ASSET-PROTECTION
```

High-sensitivity candidates require separate review before roadmap admission:

```text
executive protection
technical surveillance
digital forensic acquisition
missing-person location work
undercover operations
counter-surveillance
international field investigations
```

---

# 9. Codex Execution Protocol

For every wave:

## Step 1: Read authority

Read:

```text
ROADMAP.md
latest handoff
domain contract
master taxonomy
relevant standards
affected existing skills
```

## Step 2: Verify repository truth

Do not assume the handoff is correct.

Inspect current files and tests.

## Step 3: Declare bounded scope

Before implementation record:

```text
IN SCOPE
OUT OF SCOPE
EXPECTED FILES
RESEARCH REQUIRED
VALIDATION REQUIRED
```

## Step 4: Research

Research before writing domain claims.

Use authoritative sources for:

```text
law
regulation
privacy
licensing
professional requirements
evidence rules
security standards
```

## Step 5: Implement

Modify only what the wave requires.

Avoid unrelated refactors.

## Step 6: Validate

Run applicable:

```text
structural validation
routing tests
skill tests
source checks
freshness checks
safety tests
jurisdiction checks
integration tests
```

## Step 7: Review diff

Check for:

- scope creep;
- duplicate content;
- stale claims;
- unsupported authority;
- missing tests;
- accidental weakening of safety gates.

## Step 8: Close wave

Produce the final handoff.

---

# 10. Standard Handoff

Recommended path:

```text
docs/development/handoffs/
```

Naming:

```text
AI-XX-final-handoff.md
```

Required format:

```text
# Wave

# Objective

# Verdict
READY | PARTIALLY_READY | BLOCKED

# Completion Token

# Scope Completed

# Files Added

# Files Modified

# Research Performed

# Sources

# Validation Performed

# Tests

# Safety / Regulatory Review

# Known Limitations

# Unresolved Issues

# Explicitly Not Completed

# Recommended Next Wave
```

---

# 11. Source Freshness Test

Regulated material should support automated or semi-automated freshness review.

At minimum:

```yaml
last_verified:
freshness_interval:
jurisdiction:
primary_authority:
supersession_risk:
```

A stale source does not automatically mean the skill is wrong.

It means:

```text
REVERIFICATION REQUIRED
```

before a legal or regulatory claim is relied upon.

---

# 12. Investigation Fixture Strategy

Build fictional, internally consistent evaluation cases.

Recommended:

```text
tests/fixtures/
    workplace-misconduct/
    inventory-theft/
    contractor-due-diligence/
    access-control-incident/
    security-alarm-response/
    physical-security-assessment/
    identity-ambiguity/
    evidence-continuity/
```

Each fixture can contain:

```text
people
organizations
timestamps
documents
statements
events
evidence
security logs
access records
policies
contradictions
expected unknowns
```

Do not use real private individuals in fixtures.

---

# 13. Evidence Quality Model

AgentInvestigate should eventually standardize something comparable to:

```text
DIRECT EVIDENCE
DOCUMENTARY EVIDENCE
CORROBORATING INFORMATION
OPEN-SOURCE INFORMATION
WITNESS ACCOUNT
ALLEGATION
INFERENCE
UNKNOWN
```

The precise terminology should be validated during implementation.

The critical requirement is preventing these categories from collapsing into one another.

---

# 14. Finding Confidence Model

Recommended starting model:

```text
INSUFFICIENT INFORMATION
LOW CONFIDENCE
MODERATE CONFIDENCE
HIGH CONFIDENCE
```

For identity work:

```text
POSSIBLE
PROBABLE
CORROBORATED
CONFIRMED
UNRESOLVED
```

Codex should avoid inventing artificial numerical probabilities unless a specific validated method supports them.

---

# 15. No-Silent-Assumption Rule

For materially consequential investigative questions, skills should expose assumptions.

Example:

```text
Known:
The access log records badge 314 at 22:14.

Unknown:
Whether the badge holder personally used the badge.

Unsupported conclusion:
The badge holder entered the facility.
```

This reasoning discipline should be tested repository-wide.

---

# 16. Initial Development Milestones

The roadmap has several meaningful milestones.

## Architecture proven

```text
AI-00 through AI-08
```

At this point the architecture, taxonomy, sensitivity model, authoring standard, source standard, tests and four reference skills are proven.

## Investigation foundation

```text
AI-09 through AI-17
```

AgentInvestigate now has substantial investigation capability.

## Sensitive investigation layer

```text
AI-18 through AI-20
```

Observation governance, workplace investigations and screening are operational under authority controls.

## Security foundation

```text
AI-21 through AI-26
```

Private-security operational and management capability is established.

## Canadian regulatory baseline

```text
AI-27 through AI-31
```

Federal architecture plus Ontario, B.C. and Alberta implementations are present.

## Professional system milestone

```text
AI-32
```

Atomic skills become professional skillsets.

## Integrated validation

```text
AI-33 and AI-34
```

Cross-domain reasoning and adversarial safety have been proven.

## Public candidate

```text
AI-36
```

## v1 decision

```text
AI-37
```

---

# 17. Immediate Execution Sequence

Codex should begin:

```text
AI-00 Repository Discovery
        ↓
AI-01 Domain Contract
        ↓
AI-02 Master Taxonomy
        ↓
AI-03 Sensitivity & Authority Routing
        ↓
AI-04 Skill Authoring Standard
        ↓
AI-05 Source Standard
        ↓
AI-06 Validation Framework
        ↓
AI-07 Shared Foundations
        ↓
AI-08 Four-Class Reference Implementation
```

Only then:

```text
BEGIN BULK SKILL AUTHORING
```

---

# 18. Critical Architecture Gate

The most important early milestone is:

```text
PROVE DOMAIN BOUNDARIES
        ↓
PROVE TAXONOMY
        ↓
PROVE SENSITIVITY ROUTING
        ↓
PROVE SOURCE HANDLING
        ↓
PROVE TESTING
        ↓
PROVE ALL FOUR SKILL CLASSES
        ↓
SCALE
```

This is more important for AgentInvestigate than simply reaching a high skill count.

---

# 19. First Codex Instruction

When this roadmap is first given to Codex:

```text
Treat ROADMAP.md and the approved AgentInvestigate Master Taxonomy v1.0
as planning authority, but treat the repository itself as execution truth.

Begin only with AI-00.

Do not implement future waves.

Inspect the repository and determine its actual state.

Where accessible, compare structural patterns from AgentSkills, ChefSkills,
and AgentLogistics, but do not automatically copy them. AgentInvestigate has
different legal, privacy, authority, safety, and misuse requirements.

Produce docs/development/AI-00-baseline-audit.md.

Do not create the proposed full directory structure merely because it appears
in the roadmap.

Close AI-00 with READY, PARTIALLY_READY, or BLOCKED.

Include the completion token when justified:

AGENTINVESTIGATE_AI_00_BASELINE_READY

Produce the required final handoff and recommend AI-01 only after AI-00 is
closed.
```

---

# 20. Roadmap Status

```text
Roadmap version: 0.1
Taxonomy: FROZEN FOR DEVELOPMENT
Atomic skill count: 212

Current target:
AI-00

Mass authoring gate:
AI-08

Investigation foundation:
AI-17

Security foundation:
AI-26

Canadian regulatory baseline:
AI-31

Professional composition:
AI-32

Integration validation:
AI-33

Safety validation:
AI-34

Public readiness:
AI-36

v1 decision:
AI-37
```

Final roadmap authority token:

```text
AGENTINVESTIGATE_DEVELOPMENT_ROADMAP_V0_1_READY
```