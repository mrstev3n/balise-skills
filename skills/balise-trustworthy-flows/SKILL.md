---
name: balise-trustworthy-flows
description: Audits, designs, and repairs consequential interface choices across consent, permissions, subscriptions, pricing, cancellation, destructive actions, and data sharing. Use for Figma files, prototypes, screenshots, specifications, frontend code, or rendered products that may hide material information, bias a choice, create asymmetric effort, obstruct exit or revocation, or need a trustworthy alternative with explicit evidence and runtime or legal handoff.
---

# Trustworthy Flows

Protect a person's ability to understand, choose, refuse, leave, revoke, and recover across consequential product flows. Audit the decision system, not the visual polish of one screen.

## Operating contract

- Preserve source designs, components, code, data, and behavior unless the user explicitly authorizes edits.
- Scope work to the selected decision and the adjacent path required to understand entry, commitment, outcome, exit, revocation, and recovery.
- Reuse the existing design system, product language, application architecture, and interaction conventions.
- Separate **observed**, **runtime verified**, **declared**, **hypothetical**, and **proposed** evidence.
- Never infer intent from an interface alone. Describe the observable mechanism and plausible consequence.
- Never invent price, stock, urgency, social proof, consent persistence, deletion, notification, permission, analytics, or backend behavior.
- Do not diagnose a person's cognitive bias. State that a presentation may exploit or amplify a known bias.
- Do not declare an interface legal, compliant, safe, accessible, or free of manipulation from a static artifact.
- Preserve legitimate protective friction. Remove friction that exists only to advance the product's commercial preference.
- Escalate serious legal, privacy, accessibility, financial, child-safety, or coercive-control risks to the appropriate specialist.

## Choose the mode

Infer the mode from the request. State it briefly when it changes what may be edited.

| Mode | Action |
| --- | --- |
| **Audit** | Reconstruct the flow and report localized risks without editing. |
| **Compare** | Compare alternatives, branches, or versions against the same decision contract. |
| **Repair** | Create or implement the smallest cooperative correction after explicit edit intent. |
| **Design** | Design a new consequential flow with disclosure, choice, exit, and recovery built in. |
| **Verify** | Exercise the available implementation and report evidence, unknowns, and residual risk. |

Default ambiguous review requests to **Audit**. Keep Audit and Verify read-only. In design artifacts, Repair and Design create labeled copies by default; edit the source only on explicit instruction.

## Load only the needed references

- Read [pattern-taxonomy.md](references/pattern-taxonomy.md) when classifying mechanisms, deceptive patterns, or cumulative effects.
- Read [decision-contract.md](references/decision-contract.md) when mapping a flow, assigning severity, comparing alternatives, or preparing a formal finding.
- Read [remediation-patterns.md](references/remediation-patterns.md) for pricing, consent, permissions, cancellation, destructive actions, recovery, protective friction, or safety routing.
- Read [figma-execution.md](references/figma-execution.md) when inspecting or editing a Figma file, component set, prototype, or design handoff.
- Read [runtime-legal-boundaries.md](references/runtime-legal-boundaries.md) when claims depend on implementation, accessibility, privacy, jurisdiction, regulation, or source attribution.
- Use [trustworthy-flow-report-template.md](assets/trustworthy-flow-report-template.md) when the user requests a durable audit, decision record, or engineering handoff.

## Workflow

### 1. Frame the decision

Identify:

- the person's documented goal before the request or interruption;
- the decision, available options, and option to defer or do nothing;
- the immediate and delayed consequences for money, data, access, time, rights, content, and relationships;
- the platform, audience, jurisdiction, sector, and vulnerability context when known;
- the mode, authorized surface, and expected deliverable.

Ask one focused question only when a missing fact would materially change the conclusion or authorize a mutation. Otherwise proceed with labeled unknowns.

### 2. Reconstruct the flow

Map the smallest complete path:

`entry → request → disclosure → choice → commitment → confirmation → outcome → exit → revocation → recovery`

Include alternate branches, back navigation, refusal, interruption, failure, re-entry, and post-decision controls when they affect the choice.

If entry, commitment, or exit is absent, produce a partial finding and a list of unknowns. Never invent a missing branch.

### 3. Inspect the real system

For design artifacts, inspect selected and adjacent frames, prototype links, components, variants, properties, variables, styles, annotations, layout rules, visible copy, and representative data.

For code or a rendered product, locate the canonical route and components, state ownership, mutations, validation, persistence, permissions, data sources, analytics, translations, tests, and recovery logic. Trace visible behavior back to implementation evidence before changing it.

Record what already exists. A frame proves visible intent, not production behavior. An absent frame does not prove that runtime behavior is absent.

### 4. Build the decision contract

For each consequential moment, record:

- user goal and decision;
- available choices, including refusal, deferral, exit, and no action;
- material information and when it appears;
- default and consequence of inaction;
- immediate and delayed consequences;
- comparative effort across branches;
- exit, revocation, correction, and recovery;
- provenance of price, urgency, stock, recommendation, or social proof;
- affected people and contextual vulnerabilities;
- evidence level and unresolved dependencies.

Use the detailed fields and finding format in [decision-contract.md](references/decision-contract.md).

### 5. Diagnose the mechanism

Evaluate eight dimensions:

1. **Comprehension** — Can the person understand the object, terms, options, and consequences when they matter?
2. **Autonomy** — Can they pursue their goal without an unnecessary forced detour, hidden penalty, or undue pressure?
3. **Symmetry** — Are accept, refuse, defer, leave, and revoke proportionate in visibility and effort?
4. **Transparency** — Are cost, recurrence, data use, recipients, conditions, and limits disclosed before commitment?
5. **Predictability** — Do labels, controls, and conventions truthfully announce their immediate effect?
6. **Reversibility** — Can the person undo, correct, cancel, revoke, or recover when the risk warrants it?
7. **Proportion** — Does friction protect the person against a concrete risk using the least restrictive approach?
8. **Protection** — Does the flow account for contextual vulnerability and plausible abuse without increasing exposure?

Then identify the exploitative mechanism: perception, comprehension, decision bias, violated expectation, resource depletion, forcing, emotional pressure, or compulsion. Add a taxonomy label only when useful; the label never replaces the causal explanation.

### 6. Prioritize without pseudo-scoring

Assess:

- plausible consequence and affected asset;
- exposure and recurrence;
- detectability by the affected person;
- reversibility and recovery cost;
- contextual vulnerability;
- cumulative effect of multiple mechanisms;
- strength of evidence.

Use **Critical**, **Major**, or **Moderate** as decision aids, not scientific scores. A consequential topic is not automatically Critical. Recommend a validation pause for a Critical finding; do not claim authority to block unless the user granted it.

### 7. Repair cooperatively

Preserve the legitimate product objective while restoring informed choice. Prefer the smallest durable change that:

- discloses material information before commitment;
- aligns labels, controls, and outcomes;
- gives opposing choices comparable access and clarity;
- requests an active choice for significant cost, subscription, data use, or waiver;
- respects refusal and avoids repeated pressure;
- provides a direct exit, cancellation, revocation, or export path;
- prevents, reverses, checks, or confirms consequential errors;
- documents runtime and legal dependencies.

Protective friction is acceptable only when it addresses a concrete risk, is necessary and minimally restrictive, applies consistently to comparable risks, does not merely serve conversion, and retains a clear exit.

### 8. Create or implement

In design tools, work on labeled copies, reuse the existing system, align opposing branches for comparison, prototype only credible transitions, and annotate invisible behavior.

In code, follow existing architecture, preserve data and state, implement the complete path, and add tests for the critical transitions. Do not solve an interface problem with copy alone when order, default, hierarchy, persistence, or backend logic causes the risk.

### 9. Verify both directions

Exercise, where available:

- accept and refuse;
- enter and leave;
- subscribe and cancel;
- grant and revoke;
- delete and recover;
- commit and correct;
- normal, error, interruption, back, refresh, and repeated-request paths.

Check narrow layouts, enlarged text, keyboard interaction, status feedback, preserved input, duplicate prevention, persistence, and real backend effects when the environment permits them. Label every untested dependency.

### 10. Deliver evidence

Report:

1. scope and mode;
2. reconstructed flow and missing branches;
3. findings by severity and exact location;
4. mechanism, affected dimension, consequence, and evidence level;
5. changes or proposed alternatives;
6. verification performed;
7. legal, technical, accessibility, or safety checks still required;
8. residual risk and open decisions.

Use this neutral formulation for regulated risk:

> This flow presents a deceptive-design risk compatible with category X in source Y. The observation is based on A, B, and C. The proposal reduces that risk by changing D. This design analysis is not legal advice or a compliance certification.

## Boundaries with adjacent work

- Use a content-resilience review for length, localization, Unicode, variable media, and overflow unless a failure hides a choice or consequence.
- Use a complete-state review for exhaustive loading, empty, error, partial, synchronization, and interaction coverage unless a state changes trust in a consequential transition.
- Use comprehensive UX writing work for voice, terminology, and editorial consistency. This skill rewrites only decision-critical language.
- Treat accessibility, privacy, legal, financial, child-safety, and coercive-control issues as specialist dependencies when the conclusion exceeds observable design evidence.

## Completion standard

Finish only when:

- the relevant flow, not one isolated screen, has been inspected;
- every finding is localized and evidence-labeled;
- mechanism and plausible consequence are explained without inventing intent;
- opposing paths and post-decision controls have been compared;
- the response distinguishes risk detection from legal qualification;
- source artifacts remain preserved unless direct editing was authorized;
- alternatives preserve a legitimate product objective without preserving exploitation;
- runtime, accessibility, data, and jurisdictional unknowns remain explicit;
- serious safety risks are routed rather than improvised;
- verification claims match the evidence actually collected.
