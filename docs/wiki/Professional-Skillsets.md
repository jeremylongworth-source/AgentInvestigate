# Professional Skillsets

Professional skillsets compose existing atomic skills into role-level capabilities.

The canonical registry is:

```text
skillsets/professional-skillsets.json
```

## Rule

```text
Skillsets compose skills.
They must not duplicate underlying procedures.
```

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

## Required Role Boundaries

Skillset outputs must preserve:

- jurisdiction and authority requirements;
- lawful purpose;
- source and record access authority;
- privacy basis;
- sensitivity routing;
- human review before intrusive work;
- certification boundaries;
- prohibited-capability boundaries.

## Validation

Run:

```powershell
python scripts\validate-skillsets.py --repo-root .
```
