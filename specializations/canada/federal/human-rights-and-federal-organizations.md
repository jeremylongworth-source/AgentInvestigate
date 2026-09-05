# Human Rights And Federal Organizations

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_27_CANADA_FEDERAL_READY
```

## Scope

This reference covers federal human-rights considerations and federally regulated organizations issue spotting for AgentInvestigate. It is relevant when work involves federally regulated employers, federal services, federal workplaces, discrimination, harassment, accommodation, screening, workplace investigation, security operations, or program management.

It does not decide whether the Canadian Human Rights Act, Canada Labour Code, or another federal framework applies to a particular organization or event.

## Source Basis

Use `source-log.yaml` entries:

- `canada-federal-human-rights-act`
- `chrc-discrimination`
- `canada-federally-regulated-workplaces`
- `canada-federal-labour-code`

Freshness: `HIGH`. Recheck current official sources before relying on any federal human-rights, labour, or federally regulated workplace claim.

## Federal Human-Rights Issue Map

Flag federal human-rights issues when supplied facts involve:

- employment, services, accommodation, harassment, or screening in a possible federal jurisdiction context;
- discrimination or differential treatment connected to protected grounds;
- disability, accommodation, religious accommodation, pregnancy/family status, age, sex, race, national or ethnic origin, colour, marital status, genetic characteristics, conviction record, or other protected-ground issues raised by supplied facts;
- workplace investigation scope, interview planning, evidence review, report writing, or corrective action that may affect protected rights;
- security screening, access control, loss prevention, surveillance, or incident response that may create differential impact.

Do not infer discrimination from demographic facts alone. Do not decide liability, compliance, accommodation sufficiency, discipline, or employment action.

## Federally Regulated Organization Issue Map

Flag federal jurisdiction uncertainty when supplied facts involve sectors commonly associated with federal regulation, such as banking, telecommunications, broadcasting, interprovincial or international transportation, federal Crown corporations, First Nations governance contexts, ports, airports, rail, shipping, pipelines, or federal public-sector work.

This is issue spotting only. Organization status and applicable law require current source verification and qualified review.

## Required Output Boundary

Any output relying on this reference must state:

- the source and verification date;
- why federal jurisdiction may be relevant based only on supplied facts;
- what province or territory may still need review;
- what human-rights, labour, privacy, employment, screening, security, or accommodation questions remain unresolved;
- that federal human-rights and labour sources do not replace provincial/territorial private investigation or security licensing requirements.
