# Validation And Testing

AgentInvestigate uses repository contracts and scenario fixtures to make structural and safety expectations reviewable.

## Full Gate

From the repository root:

```powershell
.\scripts\validate-all.ps1
```

The full gate checks:

- baseline documentation;
- taxonomy integrity;
- routing contracts;
- skill, evidence, source, testing, and evaluation standards;
- shared foundations;
- implemented skill packages;
- Canadian regulatory specialization foundations;
- professional skillset composition;
- multi-skill integration scenarios;
- adversarial safety scenarios;
- specialization roadmap candidates;
- public documentation readiness;
- v1 release-candidate records;
- public release distribution readiness.

## Focused Checks

```powershell
python scripts\validate-routing.py --repo-root .
python scripts\validate-skills.py --repo-root .
python scripts\validate-specializations.py --repo-root .
python scripts\validate-skillsets.py --repo-root .
python scripts\validate-integration.py --repo-root .
python scripts\validate-safety.py --repo-root .
```

Use a focused check while iterating, then run the full gate before a pull request or release decision.

## What A Pass Means

A passing run confirms required files, text contracts, metadata, references, routing states, fixture coverage, and safety boundaries are present and internally consistent.

It does not prove live model behavior, legal correctness, privacy compliance, licensing eligibility, professional competence, emergency readiness, forensic admissibility, or real-world operational safety.

## Release Evidence

The v1 release-candidate audit is:

```text
docs/evaluation/v1-release-candidate-audit.md
```

The public distribution record is:

```text
docs/release/public-release-distribution.md
```

A public distribution pass is not an unconditional v1 readiness decision.
