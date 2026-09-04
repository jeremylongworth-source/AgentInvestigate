# AgentInvestigate Skill Naming Standard

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_04_SKILL_STANDARD_READY
```

## Purpose

Skill names must be predictable, searchable, stable, and honest about authority. They support routing, taxonomy review, testing, documentation, and future skillset composition.

## Format

Use lowercase hyphen-case:

```text
<verb>-<investigative-or-security-object>
```

Examples:

- `classify-request-type`
- `validate-investigative-authority`
- `build-evidence-matrix`
- `construct-event-chronology`
- `document-alarm-response`

Requirements:

- Use ASCII lowercase letters and numbers.
- Use hyphens as separators.
- Do not use spaces, underscores, punctuation, camelCase, or version suffixes.
- Match the `name` frontmatter value exactly to the skill directory.
- Keep names short enough to read but specific enough to route.
- Prefer the canonical name in `docs/architecture/taxonomy-index.yaml`.

## Verb Rules

Use the narrowest verb that matches the primary output.

| Verb | Use when the skill primarily |
|---|---|
| `analyze` | Interprets evidence, events, logs, patterns, risks, or causes. |
| `assess` | Weighs a bounded requirement, risk, authority question, proportionality question, or readiness condition. |
| `audit` | Checks a record, process, report, source set, control, or program against stated criteria. |
| `build` | Produces a structured artifact such as a matrix, tracker, register, or report section. |
| `classify` | Assigns a request, event, allegation, source, record, or risk to a category. |
| `compare` | Evaluates alternatives against consistent criteria. |
| `construct` | Assembles a chronology, case theory map, timeline, or other structured reconstruction from supplied evidence. |
| `define` | Establishes scope, terms, requirements, boundaries, or criteria. |
| `determine` | Identifies a bounded routing or escalation outcome from explicit criteria. |
| `document` | Produces a factual record, log entry, handoff, incident note, or case artifact. |
| `draft` | Creates editable language for human review. |
| `identify` | Finds constraints, gaps, risks, obligations, issues, entities, sources, or required next steps. |
| `map` | Converts relationships, evidence, allegations, events, sources, or workflows into a structured map. |
| `plan` | Produces a bounded professional plan, checklist, research path, or handoff. |
| `prepare` | Creates review-ready materials for another actor, reviewer, escalation, or process. |
| `prioritize` | Orders issues, risks, leads, actions, or sources by stated criteria. |
| `reconcile` | Compares expected and actual records, evidence, logs, or statements and identifies discrepancies. |
| `review` | Inspects material and returns findings, gaps, risks, or recommended revisions. |
| `support` | Assists recognition, documentation, communication, preservation, or handoff without taking over the responsible role. |
| `triage` | Sorts events, incidents, allegations, or requests by urgency, severity, routing, or escalation need. |
| `validate` | Checks whether required authority, consent, scope, input, evidence, or data-quality facts are present. |
| `verify` | Confirms a bounded fact against supplied or authorized sources. |

Avoid broad verbs such as `handle`, `do`, `manage`, `solve`, or `optimize` unless the taxonomy has explicitly approved the exact name.

## Object Rules

- Name the professional object or artifact, not the internal method.
- Use terms from the domain contract, taxonomy, sensitivity model, and routing contract.
- Avoid vague objects such as `case`, `issue`, `investigation`, `security`, `risk`, or `report` unless the full taxonomy name makes the boundary clear.
- Use singular nouns when the result is one artifact: `build-evidence-matrix`.
- Use plural nouns when the task naturally operates on a set: `compare-source-conflicts`.
- Do not include jurisdiction names, industries, employers, clients, vendors, databases, platforms, or tools in a universal core skill.
- Do not hide an intrusive, regulated, or certification-boundary dependency behind a routine-sounding object.

## Family And Path Rules

Future skill paths must use the taxonomy family slug:

```text
skills/<taxonomy-family>/<skill-name>/
```

Examples:

```text
skills/02-case-intake-scope-authority/validate-investigative-authority/
skills/08-evidence-chain-of-custody/build-evidence-matrix/
skills/15-incident-response/document-alarm-response/
```

The skill name itself remains the atomic capability. The family path supplies taxonomy context.

## Specialization Names

Specializations must make the boundary visible in the path or approved name:

```text
specializations/<jurisdiction-or-context>/<taxonomy-family>/<skill-name>/
```

Use a specialization only when the procedure truly depends on jurisdiction, sector, record type, system type, or professional context. Do not create a specialization to avoid source or authority checks.

If a specialization must appear in the name, place it after the object:

```text
identify-licensing-requirement-ontario
prepare-background-screening-notice-us
```

Universal core skills must not use jurisdiction-specific names.

## Disallowed Patterns

Do not create skill names that:

- promise legal, regulatory, licensing, investigative, security, emergency, engineering, or certification approval;
- imply law-enforcement authority;
- imply force, weapons, restraint, pursuit, confrontation, bypass, evasion, hacking, or unauthorized access;
- combine unrelated actions with `and`;
- use broad labels such as `complete-investigation`, `run-surveillance`, or `security-response`;
- duplicate an existing taxonomy row under a different phrase;
- use internal implementation names such as `run-script` or `call-api`;
- use brand, vendor, platform, database, or client names for universal capabilities;
- make intrusive work look routine.

## Naming Review

Before accepting a new skill name, confirm:

- the name exists in `docs/architecture/taxonomy-index.yaml` or has an approved taxonomy-change note;
- the verb matches the expected output;
- the object has one clear investigative or security meaning;
- the name does not conceal jurisdiction, authority, privacy, licence, source, emergency, or certification dependencies;
- nearby taxonomy skills have been checked for overlap;
- the name does not imply a prohibited capability.

AI-04 does not approve new taxonomy names. It defines how names must be reviewed when later waves author skills.
