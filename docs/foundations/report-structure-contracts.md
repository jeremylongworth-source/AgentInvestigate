# AgentInvestigate Report Structure Contracts

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_07_SHARED_FOUNDATIONS_READY
```

## Purpose

This foundation defines common report structures and template contracts for future AgentInvestigate skills. These are contracts for expected sections and fields, not filled template assets.

## Materialization Rule

Do not create a reusable template file, form, fixture, or shared asset from these contracts unless at least one implemented skill consumes it and names it in `Dependencies` or `References`.

## Universal Sections

Most AgentInvestigate artifacts should include these sections when material:

- scope;
- inputs used;
- facts;
- allegations;
- analysis or issues;
- assumptions;
- unknowns;
- limitations;
- review or escalation needs;
- next actions.

## Template Contracts

### case-intake

Purpose: Capture initial matter scope before analysis.

Fields:

- request summary;
- user role;
- client or organization;
- jurisdiction;
- lawful purpose;
- subject or affected parties;
- requested output;
- known evidence;
- authority status;
- privacy or consent issues;
- prohibited-capability check;
- next action.

### conflict-check

Purpose: Identify potential conflict, bias, role, confidentiality, or independence concerns.

Fields:

- parties;
- relationships;
- prior involvement;
- competing duties;
- confidentiality issues;
- bias indicators;
- unresolved questions;
- escalation target.

### authority-check

Purpose: Record whether the user, client, or organization has authority for the requested work.

Fields:

- user role;
- client authority;
- jurisdiction;
- lawful purpose;
- approved scope;
- consent status;
- privacy basis;
- human approval;
- source of approval;
- stop conditions.

### investigation-plan

Purpose: Draft a bounded investigation plan after authority, scope, and source checks.

Fields:

- objective;
- scope;
- exclusions;
- evidence to review;
- witness or stakeholder categories;
- source plan;
- privacy limits;
- timeline;
- review gates;
- escalation triggers.

### case-action-log

Purpose: Track professional actions and decisions.

Fields:

- action id;
- date or time;
- actor;
- action taken;
- evidence or source used;
- decision rationale;
- authority note;
- next action;
- review status.

### research-source-log

Purpose: Record source material used for research and regulated issue spotting.

Fields:

- source id;
- source title;
- organization;
- jurisdiction;
- authority level;
- URL or supplied identifier;
- publication or effective date;
- accessed date;
- last verified;
- applicability;
- supersession risk;
- used by.

### interview-plan

Purpose: Prepare a non-coercive interview or statement-gathering plan.

Fields:

- interview objective;
- witness or participant role;
- authority and consent basis;
- topics;
- open questions;
- documents to reference;
- accommodations or support needs;
- boundaries;
- escalation triggers.

### evidence-log

Purpose: Record evidence items without changing or overstating them.

Fields:

- item id;
- source id;
- evidence type;
- date or time range;
- supplied fact;
- allegation or issue supported;
- custody or integrity note;
- sensitivity note;
- limitation.

### chain-of-custody

Purpose: Track custody and handling of evidence when custody facts are supplied.

Fields:

- item id;
- handler;
- transfer date or time;
- transfer method;
- storage location;
- integrity note;
- gap or unknown;
- reviewer.

### evidence-matrix

Purpose: Map evidence to allegations, issues, elements, or questions.

Fields:

- matrix row id;
- allegation or issue;
- fact;
- source id;
- support level;
- inference;
- contradiction;
- unknown;
- limitation;
- next action.

### case-chronology

Purpose: Order events, records, and evidence in time.

Fields:

- event id;
- date or time range;
- event summary;
- source id;
- fact or allegation;
- confidence or support;
- contradiction;
- unknown;
- related issue.

### incident-report

Purpose: Document a security or investigative incident without replacing emergency or supervisory procedures.

Fields:

- incident summary;
- date and location;
- people or roles involved;
- observations;
- actions taken;
- notifications;
- evidence preserved;
- safety or escalation issues;
- limitations;
- next action.

### shift-handoff

Purpose: Transfer security or case-status information between responsible personnel.

Fields:

- shift or handoff period;
- status summary;
- open incidents;
- access or patrol issues;
- evidence or logs;
- pending actions;
- escalation contacts;
- limitations.

### risk-register

Purpose: Track risks, controls, owners, and review needs.

Fields:

- risk id;
- risk statement;
- cause or trigger;
- impact;
- likelihood;
- controls;
- owner;
- due date;
- review need;
- status.

### case-closure

Purpose: Close a matter or prepare closure for human review.

Fields:

- closure summary;
- scope completed;
- evidence reviewed;
- unresolved issues;
- findings or non-findings;
- limitations;
- records retained;
- required approvals;
- follow-up actions.

## Usage

Future skills should adapt these contracts to the skill's output. A skill may omit fields that do not apply, but it must preserve AI-04 output requirements, AI-05 source requirements, and AI-06 testability.
