# Intrusive Task Gate

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_03_SENSITIVITY_ROUTING_READY
```

## Purpose

This document defines the mandatory gate for intrusive investigative or security work. It prevents raw user requests from routing directly into surveillance, observation, background screening, identity analysis, sensitive personal information collection, workplace evidence collection, or video/location analysis.

## Gate Principle

```text
No intrusive skill routes directly from a raw user request.
```

An intrusive task may proceed only after authority, legality, privacy, necessity, proportionality, alternatives, boundaries, and human approval are established.

## Required Chain

```text
REQUEST
classify-request-type
identify-jurisdiction
validate-investigative-authority or validate-security-service-authority
assess-lawful-purpose
identify-privacy-obligation
assess-information-collection-basis
assess-necessity-proportionality
assess-less-intrusive-alternative
define-scope-boundaries
HUMAN APPROVAL
BOUNDED INTRUSIVE TASK
```

AI-02 does not yet include standalone `assess-necessity-proportionality` or `assess-less-intrusive-alternative` skills. Until AI-03 or a later taxonomy revision adds those exact skills, the gate is implemented through the closest existing taxonomy path:

```text
assess-observation-necessity
assess-observation-proportionality
define-scope-boundaries
```

For non-observation intrusive work, future authoring must either add the missing general gate skills or document why a domain-specific equivalent satisfies the gate.

## Intrusive Work Includes

- observation or surveillance;
- background screening;
- due diligence on a person;
- personal identity matching;
- relationship or association mapping;
- video event analysis involving identifiable people;
- workplace evidence source identification;
- sensitive workplace allegations;
- location or movement analysis;
- personal reputation, character, employment, or private-life analysis;
- third-party personal information collection.

## Required Gate Record

Before any bounded intrusive task proceeds, the skill output or handoff must record:

- request summary;
- intrusive elements;
- jurisdiction;
- user role;
- client or organizational authority;
- lawful purpose;
- subject or affected parties;
- privacy obligations;
- collection basis;
- approved sources;
- rejected sources;
- necessity rationale;
- proportionality rationale;
- less-intrusive alternatives considered;
- approved scope boundaries;
- human approver or required approver role;
- time, place, source, and method limits;
- escalation path;
- stop conditions.

## Fail-Closed Conditions

The gate fails closed when:

- jurisdiction is missing;
- user role or authority is unclear;
- client authority is missing;
- lawful purpose is missing or suspect;
- privacy basis is missing;
- consent is required and missing;
- source authorization is missing;
- requested collection is broader than necessary;
- less-intrusive alternatives have not been considered;
- human approval is absent;
- the request includes prohibited conduct;
- the task would create a final legal, employment, regulatory, or licensing conclusion without qualified review.

Allowed fail-closed outputs:

- identify missing gate elements;
- ask bounded clarifying questions;
- prepare an authority-check checklist;
- prepare a lawful-source plan;
- prepare an escalation note;
- redirect to non-intrusive documentation or policy review;
- recommend qualified human review.

Disallowed fail-closed outputs:

- operational observation plan;
- tracking method;
- covert collection tactic;
- target movement plan;
- private-account access guidance;
- invasive background-screening source list without consent and source authority;
- instructions to bypass controls;
- evidence collection beyond approved scope.

## Bounded Intrusive Task Definition

A bounded intrusive task must specify:

- who or what is in scope;
- why the task is authorized;
- where it may occur;
- when it may occur;
- what sources may be used;
- what sources may not be used;
- what personal information may be collected;
- what must be minimized or excluded;
- how records are documented;
- when the task stops;
- who reviews the result.

If any of these cannot be stated, the task is not bounded enough to proceed.

## Data Minimization

Intrusive outputs should prefer the minimum useful information:

- summarize instead of copying sensitive material where possible;
- separate direct evidence from inference;
- omit unrelated third-party details;
- mark unsupported assumptions;
- preserve uncertainty;
- document why retained sensitive details are necessary;
- identify retention and disposal review needs.

## Prohibited Intrusive Requests

The gate does not authorize:

- stalking;
- intimate-partner monitoring;
- illegal GPS tracking;
- covert tracker installation;
- counter-surveillance evasion;
- camera evasion;
- alarm defeat;
- unauthorized account access;
- credential theft;
- protected-record acquisition through deception;
- coercive interrogation;
- physical coercion.

These route to `PROHIBITED_REDIRECT`, not to an intrusive approval workflow.

## Human Approval Standard

Human approval must be explicit and role-appropriate. A vague statement such as "I am allowed" is not enough for a high-consequence intrusive task.

Approval should identify:

- approving role;
- basis for authority;
- jurisdiction;
- specific task;
- time and scope limits;
- source limits;
- privacy safeguards;
- escalation and review process.

## Validation Notes

This document defines the gate. AI-06 must later convert the gate into test classes for missing jurisdiction, missing authority, missing consent, intrusive request, prohibited request, source freshness, unsupported inference, and output-format compliance.
