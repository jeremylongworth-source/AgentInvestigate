# AgentInvestigate

AgentInvestigate is an open-source AI skill repository for lawful professional work in private investigation, investigative research, evidence management, corporate and workplace investigations, background screening and due diligence, private security operations, incident response, physical security, loss prevention, and security program management.

The project is in initial repository setup. The current execution target is `AI-00 Repository Discovery & Baseline Audit`.

Core principles:

```text
AUTHORITY BEFORE ACTION
EVIDENCE BEFORE CONCLUSION
HUMAN CONTROL BEFORE INTRUSIVE WORK
```

AgentInvestigate does not confer investigator licensing, security licensing, law-enforcement authority, legal authority, regulatory approval, use-of-force qualification, weapons qualification, emergency-response certification, engineering approval, or professional certification.

## Current Status

- Roadmap: `ROADMAP.md`
- Current wave: `AI-00`
- Baseline audit: `docs/development/AI-00-baseline-audit.md`
- Final handoff: `docs/development/handoffs/AI-00-final-handoff.md`

## Development Approach

The repository is roadmap-wave driven. Early waves establish domain boundaries, taxonomy, sensitivity routing, source handling, testing, shared foundations, and four reference skill classes before bulk skill authoring.

Do not create placeholder skill folders or broad directory structures without active content and validation. Skills should remain atomic; professional roles belong in the skillset layer.

## Safety Boundaries

The roadmap excludes procedural assistance for hacking, credential theft, unauthorized access, lock bypass, forced entry, illegal tracking, stalking, intimate-partner monitoring, impersonation, coercive interrogation, access-control circumvention, camera or alarm defeat, weapons use, restraint techniques, combat techniques, and similar misuse-prone conduct.

Regulated, intrusive, and certification-boundary content requires jurisdiction, authority, source, and human-review controls before implementation.

## Validation

Run the current baseline checks:

```powershell
.\scripts\validate-all.ps1
```

## License

MIT. See `LICENSE`.
