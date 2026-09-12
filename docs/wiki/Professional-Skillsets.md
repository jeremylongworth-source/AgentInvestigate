# Professional Skillsets

Professional skillsets compose existing atomic skills into role-level capability bundles. The canonical registry is:

```text
skillsets/professional-skillsets.json
```

A skillset is a composition record, not a second procedure library. It must preserve every underlying skill's routing, authority, privacy, source, evidence, certification, and escalation requirements.

## Investigation Skillsets

- `private-investigator`
- `investigative-analyst`
- `investigative-case-manager`
- `corporate-investigator`
- `workplace-investigator`
- `background-screening-specialist`
- `loss-prevention-investigator`

## Security Skillsets

- `security-officer`
- `mobile-patrol-officer`
- `loss-prevention-officer`
- `security-supervisor`
- `security-operations-manager`
- `physical-security-analyst`
- `security-risk-assessor`
- `incident-response-coordinator`
- `security-program-manager`

## Hybrid Skillsets

- `corporate-security-investigator`
- `asset-protection-specialist`
- `corporate-security-manager`

Hybrid composition coordinates branches; it does not erase the different authority models.

## Composition Contract

Every skillset must:

- reference taxonomy-backed atomic skills;
- declare its professional branch or branches;
- retain global routing states;
- identify role boundaries and escalation needs;
- avoid duplicating atomic procedures;
- remain subject to jurisdiction and current-source review.

## Validation

```powershell
python scripts\validate-skillsets.py --repo-root .
```

For architecture details, see [professional skillset composition](https://github.com/jeremylongworth-source/AgentInvestigate/blob/main/docs/architecture/professional-skillset-composition.md).
