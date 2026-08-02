# Decision contract, evidence, and findings

Use this reference to make an audit reproducible and to compare alternatives against the same facts.

## Decision contract

| Field | Record |
| --- | --- |
| Scope | selected surface and required adjacent flow |
| User goal | task underway before the request or interruption |
| Decision | choice the interface asks the person to make |
| Options | accept, refuse, defer, customize, exit, and no action where applicable |
| Material information | price, recurrence, data, recipients, terms, limits, loss, and rights |
| Disclosure timing | where each material fact appears relative to commitment |
| Default | initial selection and consequence of inaction |
| Immediate consequence | what changes after activation |
| Delayed consequence | renewal, retention, future charge, access, sharing, or loss |
| Comparative effort | steps, search, reading, time, authentication, channel, and delay per branch |
| Exit and revocation | refusal, cancellation, withdrawal, export, deletion, or session revocation |
| Recovery | undo, correction, grace period, restoration, or escalation |
| Provenance | source and date of price, stock, urgency, social proof, or recommendation |
| Affected people | documented audience and contextual vulnerability, without invented personas |
| Evidence | observed, runtime verified, declared, hypothetical, or proposed |
| Dependencies | product, engineering, data, content, accessibility, safety, or legal checks |

## Evidence levels

- **Observed**: visible in the inspected frames, prototype, screenshot, source, or rendered interface. Point to the exact location.
- **Runtime verified**: reproduced in the product or confirmed by dated technical evidence. State environment and scope.
- **Declared**: supplied by an annotation, specification, or stakeholder but not independently verified.
- **Hypothetical**: an explicit inference or missing-path question. Never present it as current behavior.
- **Proposed**: an alternative design or behavior not yet implemented.

Only Observed and Runtime verified support factual findings. Declared, Hypothetical, and Proposed remain qualified inputs.

## Finding chain

Write each finding as:

`localized observation → mechanism → affected dimension → plausible consequence → evidence or unknown → remediation`

Required fields:

- identifier and severity;
- exact location and flow step;
- observed fact;
- evidence level;
- exploitative mechanism and optional taxonomy label;
- trust dimension affected;
- plausible consequence and affected asset;
- affected branch or population context;
- smallest cooperative remediation;
- verification needed and residual risk.

Do not use a pattern name as the entire finding.

## Severity

### Critical

Use when evidence supports a plausible or observed grave consequence with high exposure or very difficult recovery, such as:

- unauthorized charge or commitment;
- irreversible loss;
- exposure of sensitive data;
- effective inability to withdraw or regain control;
- serious safety risk.

Recommend pausing validation and obtaining the relevant review. Do not claim authority to block unless granted.

### Major

Use when autonomy is substantially reduced but exit remains possible, for example:

- strong asymmetry;
- material information disclosed too late;
- repeated pressure;
- unnecessary obstruction;
- recovery that is available but costly or hard to find.

### Moderate

Use when trust or comprehension is weakened without a demonstrated grave consequence, for example:

- ambiguous label;
- questionable hierarchy;
- missing provenance;
- localized friction.

## Prioritization factors

Explain the factors rather than multiplying them into a false precision score:

- consequence;
- exposure;
- detectability;
- reversibility;
- recovery cost;
- contextual vulnerability;
- cumulative mechanisms;
- evidence strength.

The mere presence of cost, consent, deletion, or a vulnerable audience does not automatically make a finding Critical.

## Comparative review

When comparing versions, keep the decision contract fixed and compare:

- comprehension before commitment;
- branch visibility and effort;
- default and inaction;
- disclosure timing;
- predictability of controls;
- exit and recovery;
- unresolved runtime dependencies.

Do not declare the visually quieter or higher-converting version more trustworthy without this comparison.
