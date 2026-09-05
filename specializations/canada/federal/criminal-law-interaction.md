# Criminal-Law Interaction

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_27_CANADA_FEDERAL_READY
```

## Scope

This reference covers federal Criminal Code issue spotting for private investigation, private security, workplace investigation, loss prevention, OSINT, physical security, security systems, and program-management work in Canada.

It does not provide criminal-law conclusions, charging advice, legal advice, law-enforcement authority, search authority, detention authority, or use-of-force authority.

## Source Basis

Use `source-log.yaml` entry:

- `canada-federal-criminal-code`

Freshness: `HIGH`. Recheck current official sources and route to counsel before relying on any Criminal Code claim.

## Federal Criminal-Law Risk Areas

federal criminal-law risk areas

AgentInvestigate outputs should flag possible federal criminal-law interaction when supplied facts involve:

- criminal harassment or stalking;
- threats, intimidation, extortion, coercion, or forced statements;
- assault, restraint, confinement, detention, weapons, or use of force;
- impersonating police, government, regulator, emergency services, employer, or another authority;
- obstruction, false statements, fabricated evidence, or altered records;
- fraud, identity fraud, false pretences, or misuse of identity information;
- unauthorized computer access or account access;
- interception of private communications;
- mischief to property, data, devices, cameras, alarms, locks, or access-control systems;
- possession or use of tools, credentials, devices, or methods for unauthorized entry or access.

## AgentInvestigate Routing

If a request asks for any prohibited operational detail, route to:

```text
PROHIBITED_REDIRECT
```

Examples include:

- hacking;
- credential theft;
- unauthorized account access;
- lock bypass;
- forced entry;
- access-control circumvention;
- camera or alarm defeat;
- counter-surveillance evasion;
- stalking or intimate-partner monitoring;
- police or government impersonation;
- coercive interrogation;
- detention, search, restraint, pursuit, weapons, or use-of-force tactics.

If a request describes possible criminal conduct, safety risk, emergency indicators, violence, threats, stalking, exploitation, abuse, or material legal consequences, route to qualified review, emergency services, counsel, or law enforcement as appropriate to the facts and user role.

## Required Output Boundary

Any output relying on this reference must:

- separate facts, allegations, inferences, and findings;
- avoid criminal guilt conclusions;
- avoid charging, detention, search, seizure, force, or law-enforcement referral approval;
- preserve source limitations and verification date;
- identify counsel, supervisor, law-enforcement, emergency, HR, privacy, or compliance review needs;
- state that federal criminal law does not replace provincial/territorial licensing and authority requirements.
