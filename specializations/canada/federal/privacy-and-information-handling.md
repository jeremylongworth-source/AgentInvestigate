# Privacy And Information Handling

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_27_CANADA_FEDERAL_READY
```

## Scope

This reference covers federal Canada privacy and information-handling issue spotting for AgentInvestigate. It does not decide whether a collection, use, disclosure, retention, monitoring practice, surveillance practice, background check, workplace investigation, or security operation is lawful.

## Source Basis

Use `source-log.yaml` entries:

- `canada-federal-pipeda`
- `canada-federal-privacy-act`
- `opc-pipeda-private-sector`

Freshness: `HIGH`. Recheck current official sources before relying on any federal privacy claim.

## PIPEDA Issue Map

PIPEDA is the main federal private-sector privacy statute for personal information in commercial activity and certain federally regulated contexts, subject to scope limits and provincial privacy-law interaction. Use it for issue spotting around:

- accountability and accountable organization;
- identifying purposes;
- consent and consent limits;
- collection limits;
- use, disclosure, and retention limits;
- accuracy;
- safeguards;
- openness;
- individual access;
- complaint and challenge handling;
- appropriate purpose analysis;
- cross-border, third-party, vendor, or service-provider handling where raised by supplied facts.

Do not infer that PIPEDA alone authorizes investigative or security activity. PIPEDA can constrain or structure information handling, but occupational licensing, employment law, human-rights obligations, criminal prohibitions, contractual authority, and provincial/territorial law and occupational licensing may still govern the work.

## Privacy Act Issue Map

The Privacy Act is federal public-sector privacy law. Use it only for issue spotting when the source context involves federal government institutions or federal public-sector personal information handling.

Do not apply the Privacy Act as the general private-sector privacy regime. Do not treat access to federal records, government-held personal information, or public-sector disclosure as available without a lawful process and qualified review.

## Information Handling Rules For AgentInvestigate

Federal privacy references may support:

- issue spotting;
- source-backed privacy checklists;
- consent and purpose questions;
- personal-information inventory prompts;
- retention and safeguarding questions;
- privacy-officer, counsel, or compliance escalation packets.

Federal privacy references must not support:

- privacy compliance certification;
- covert monitoring approval;
- hidden collection approval;
- workplace surveillance approval;
- background-screening approval;
- disclosure approval;
- credentialed database access;
- unauthorized account access;
- pretexting to obtain protected records.

## Required Output Boundary

Any output relying on this reference must state:

- jurisdiction: Canada federal, plus any province or territory still needed;
- source checked and verification date;
- whether the organization appears private-sector, public-sector, or federally regulated based only on supplied facts;
- what personal information, purpose, consent basis, collection/use/disclosure, retention, safeguarding, access, and complaint issues are unresolved;
- that provincial/territorial law and occupational licensing may still determine authority.
