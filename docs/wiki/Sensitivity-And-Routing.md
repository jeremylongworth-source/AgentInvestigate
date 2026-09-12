# Sensitivity And Routing

Routing is the control layer between a user request and any AgentInvestigate skill or skillset.

## Global Routing States

| State | Meaning | Required behavior |
| --- | --- | --- |
| `PROCEED_ROUTINE` | Routine work has enough scope and inputs. | Use the narrowest bounded skill and state assumptions. |
| `CLARIFY_SCOPE` | Material facts are missing and the request is not prohibited. | Ask for or identify the missing facts before proceeding. |
| `REGULATED_RESEARCH_ONLY` | Legal, licensing, privacy, employment, records, or compliance issues are material. | Use current authoritative sources; frame issue areas; do not make a final determination. |
| `INTRUSIVE_GATE_REQUIRED` | Surveillance, monitoring, screening, sensitive information, or identity work is intrusive. | Stop before operational execution until gates and human approval are satisfied. |
| `CERTIFICATION_ESCALATION` | The request touches emergency, force, weapons, restraints, alarm response, engineering, life safety, or qualified technical work. | Recognize, document, and escalate; do not certify, train, or substitute for qualified personnel. |
| `PROHIBITED_REDIRECT` | The requested conduct is prohibited. | Refuse procedural assistance and redirect to a lawful benign objective. |

## Decision Sequence

```text
request
  -> classify-request-type
  -> check-prohibited-capabilities
  -> identify-jurisdiction
  -> validate-investigative-authority
  -> assess-lawful-purpose
  -> identify-privacy-obligation
  -> assess-information-collection-basis
  -> assess-necessity-proportionality
  -> assess-less-intrusive-alternative
  -> define-scope-boundaries
  -> human approval
  -> bounded task or escalation
```

Not every request needs every step. The required path depends on sensitivity, jurisdiction, role, authority, requested output, source access, affected parties, consent or privacy basis, and urgency.

## Fail-Closed Conditions

Stop or escalate when:

- jurisdiction is required but unknown;
- role or authority is missing or conflicting;
- lawful purpose is not established;
- privacy or source-access basis is missing;
- a less intrusive alternative has not been considered;
- human approval is required but absent;
- the request seeks a prohibited capability;
- a certification boundary is presented as a routine task.

Professional framing does not override these gates. Investigation, OSINT, due diligence, safety, security assessment, penetration testing, interviewing, or training language can still describe prohibited or intrusive conduct.

## Output Expectations

A bounded output should separate:

- known facts;
- assumptions;
- unknowns;
- evidence and source quality;
- routing state;
- limitations;
- escalation or approval needed;
- next lawful action.

See [authority routing](https://github.com/jeremylongworth-source/AgentInvestigate/blob/main/docs/architecture/authority-routing.md) and [intrusive-task gate](https://github.com/jeremylongworth-source/AgentInvestigate/blob/main/docs/architecture/intrusive-task-gate.md).
