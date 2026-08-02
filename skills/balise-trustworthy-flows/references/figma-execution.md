# Figma execution

Use this reference when the source or deliverable is a Figma design, prototype, component set, or handoff.

## Inspect before acting

Inspect:

- selection, parent frame, section, and adjacent flow;
- source frames and alternate branches;
- main components, instances, component sets, variants, and properties;
- variables, modes, styles, and design tokens;
- Auto Layout, dimensions, constraints, and layout guides;
- prototype connections and interactive components;
- annotations, naming, and representative content.

Do not infer runtime behavior from layer names. Do not detach instances or replace the system to make an alternative easier.

## Mutation rules

- Audit and Verify are read-only.
- Repair and Design require explicit edit intent.
- Create a labeled copy or separate proposal area by default.
- Edit a source frame or shared main component only on explicit instruction.
- Preserve bindings, properties, variants, layout rules, and prototype evidence.

Suggested structure:

```text
Trustworthy Flows — [flow]
├── Source
├── Decision map
├── Findings
├── Cooperative alternative
├── Prototype evidence
└── Open product, technical, and legal questions
```

## Make the decision visible

- Align accept/refuse, enter/leave, subscribe/cancel, grant/revoke, and delete/recover branches for comparison.
- Place material disclosure beside the decision it changes.
- Show default, no-action result, delayed consequence, and post-decision control.
- Label every frame or annotation with its evidence level.
- Use representative synthetic data for price, identity, inventory, urgency, and activity.

## Reuse Figma primitives

- Use existing components, properties, variables, modes, styles, and tokens.
- Use variants only for genuinely reusable states with shared anatomy.
- Use Auto Layout and content-driven sizing to preserve decision-critical copy.
- Use sections and aligned frames for full-flow comparisons.
- Prototype only transitions that can be created and checked reliably.
- Annotate persistence, backend effect, data provenance, analytics, and accessibility behavior that Figma cannot prove.

## Decision annotations

For each critical moment, attach a compact contract containing:

- decision and user goal;
- options and default;
- material disclosure and timing;
- immediate and delayed consequence;
- exit and recovery;
- evidence level;
- runtime and legal dependencies.

## What Figma can support

Figma can demonstrate visible presence, hierarchy, approximate symmetry, sequence, proposed states, prototype links, annotations, and some measurable geometry.

Figma alone cannot prove:

- real price, stock, urgency, or social proof;
- persistence of refusal or consent;
- actual cancellation, revocation, deletion, undo, or recovery;
- data collection, retention, sharing, encryption, or authorization;
- runtime focus, semantics, keyboard behavior, announcements, or reflow;
- user comprehension or behavioral effect;
- legal compliance or absence of harm.

Use the formulation: “The design demonstrates the intended flow and visible safeguards; implementation and real-world effect remain to be verified.”

## Verify the proposal

Re-run both directions in the prototype:

- choose and refuse;
- proceed and leave;
- commit and correct;
- grant and revoke;
- delete and recover.

Check that every created route has a visible outcome, no dead end, and an explicit handoff for behavior that remains outside the file.
