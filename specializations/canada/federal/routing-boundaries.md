# Routing Boundaries

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_27_CANADA_FEDERAL_READY
```

## Purpose

This reference defines how the Canada federal specialization affects AgentInvestigate routing. It does not create legal authority or operational permission.

## Federal Foundation Routing Rule

The Canada federal module can support:

- federal privacy issue spotting;
- criminal-law interaction issue spotting;
- evidence-related federal concept spotting;
- federal human-rights issue spotting;
- information-handling checklists;
- federally regulated organization issue spotting;
- escalation and qualified-review questions.

It cannot determine that private investigative or security work is authorized.

When authorization depends on private investigator licensing, security licensing, agency licensing, guard licensing, training, uniforms, permitted authorities, use-of-force limits, post orders, reporting, or province-specific privacy/employment/security law, route to:

```text
REGULATED_RESEARCH_ONLY
```

until the applicable province or territory module is loaded and current sources are verified.

## Mandatory Non-Authority Statement

Outputs using this module must include:

```text
Federal rules alone do not determine whether this private investigative or security work is authorized. Provincial or territorial licensing, privacy, employment, security, and operational rules may still apply.
```

## Escalation Targets

Use the narrowest responsible escalation path supported by the facts:

- counsel;
- privacy officer;
- HR;
- compliance;
- licensed private investigator;
- licensed security manager;
- security program manager;
- regulator;
- police or emergency services when immediate safety or criminal-risk facts require it.

## Prohibited Routing

Route to `PROHIBITED_REDIRECT` for:

- hacking;
- credential theft;
- unauthorized account access;
- lock bypass;
- forced entry;
- access-control circumvention;
- covert tracker installation;
- illegal GPS tracking;
- stalking;
- intimate-partner monitoring;
- police or government impersonation;
- coercive interrogation;
- physical coercion;
- detention tactics;
- search tactics;
- pursuit tactics;
- camera evasion;
- alarm defeat;
- weapons use;
- restraint techniques;
- fabricated records;
- altered evidence;
- concealed source gaps.

## Verification Rule

Freshness: `HIGH`

Recheck official sources at time of use before relying on federal legal, privacy, human-rights, labour, evidence, or criminal-law claims. If current verification is not available, label the output as an issue-spotting summary or research brief and route consequential decisions to qualified review.
