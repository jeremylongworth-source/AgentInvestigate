# Validation And Testing

AgentInvestigate is validation-backed. The full validation suite is:

```powershell
.\scripts\validate-all.ps1
```

## What The Suite Checks

- baseline public documentation;
- taxonomy integrity;
- routing contracts;
- authoring, evidence, source, and testing standards;
- shared foundations;
- implemented skill packages;
- Canadian regulatory specialization foundations;
- professional skillset composition;
- multi-skill integration scenarios;
- adversarial safety scenarios;
- specialization roadmap candidates;
- public documentation readiness;
- v1 release candidate audit;
- public release distribution readiness.

## Important Limits

Most tests are repository contract and fixture checks. They confirm structure, required text, references, routing states, and safety gates.

They do not prove:

- live model behavior;
- legal correctness;
- privacy compliance;
- licensing eligibility;
- professional competence;
- emergency readiness;
- forensic admissibility;
- real-world operational safety.

## Release Evidence

The v1 release candidate audit is:

```text
docs/evaluation/v1-release-candidate-audit.md
```

The AI-38 public distribution readiness artifact is:

```text
docs/release/public-release-distribution.md
```
