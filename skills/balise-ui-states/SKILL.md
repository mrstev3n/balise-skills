---
name: balise-ui-states
description: Audits, designs, implements, and verifies the relevant missing states of interfaces and flows, including ideal, empty, partial, loading, success, error, offline, permission, stale, optimistic, and interaction states. Use for Figma files, screenshots, specifications, prototypes, frontend code, design systems, or rendered products that cover only the happy path, leave users without feedback or recovery, or need an implementation-ready state model.
---

# UI States

Complete the state system around an interface without mechanically generating every possible state. Treat states as a temporal model with triggers, preserved context, exits, recovery, and transitions—not as a gallery of disconnected screens.

## Operating contract

- Preserve source designs, components, code, data, and behavior unless the user asks for direct edits.
- Scope work to the selected surface or requested flow. Ask one focused question only when the missing product fact would materially change the result.
- Reuse existing components, tokens, variables, copy conventions, error models, and state-management patterns.
- Distinguish **observed**, **implemented**, **statically verified**, **runtime verified**, **proposed**, and **unknown**.
- Never invent API behavior, permissions, timings, progress percentages, persistence guarantees, or recovery semantics as facts.
- Prefer the smallest state boundary that communicates the real operation. Do not block an entire screen for a component-level update.
- Keep user work and valid data when errors occur. Never use a reset as the default recovery.
- Do not claim accessibility, production behavior, or backend correctness from a static frame alone.

## Choose the mode

Infer the mode from the request. State the choice briefly when it changes what will be edited.

| Mode | Action |
| --- | --- |
| **Audit** | Inventory current states, identify material gaps, and prioritize them without editing. |
| **Design** | Create a proposed state matrix, transitions, and copy in a design artifact. |
| **Implement** | Add the state model to source code while preserving project architecture. |
| **Repair** | Correct incomplete, misleading, inaccessible, or dead-end states already present. |
| **Verify** | Exercise implemented states and report evidence, gaps, and untested paths. |
| **Complete** | Audit, design or implement, then verify within the available surface. |

## Load only the needed references

- Read [state-taxonomy.md](references/state-taxonomy.md) when choosing states or distinguishing empty, partial, error, access, and sync conditions.
- Read [transitions-and-recovery.md](references/transitions-and-recovery.md) for async work, retries, optimistic updates, rollbacks, timeouts, or multi-step flows.
- Read [accessibility-runtime.md](references/accessibility-runtime.md) when implementing or verifying focus, announcements, disabled controls, reduced motion, or runtime behavior.
- Read [figma-patterns.md](references/figma-patterns.md) for Figma component, variant, Auto Layout, prototype, and annotation decisions.
- Read [implementation-handoff.md](references/implementation-handoff.md) for source discovery, state machines, API dependencies, acceptance tests, or engineering handoff.
- Use [state-contract-template.md](assets/state-contract-template.md) when a durable state inventory or handoff is requested.

## Workflow

### 1. Frame the product moment

Identify:

- the selected screen, component, control, or flow;
- the user goal and the product value expressed by the ideal state;
- what happens immediately before and after the surface;
- data sources, user actions, permissions, network work, and persistence involved;
- the question being tested and the intended audience for the result.

Do not start with a universal checklist. A static settings page, a search result, a collaborative editor, and a payment submission require different matrices.

### 2. Inspect the real system

For design artifacts, inspect adjacent frames, sections, components, variants, properties, variables, libraries, prototype links, annotations, and naming conventions.

For code, locate the canonical component, route, state owner, data-fetching layer, mutations, form validation, error boundary, translations, analytics, tests, and design tokens. Trace rendered copy and behavior back to their source before editing.

Record what already exists. Similar-looking frames do not prove distinct runtime states; similarly, an absent frame does not prove an implementation is missing.

### 3. Build a proportional state matrix

Start with the ideal state as the value and hierarchy reference. Add a state only when its trigger is plausible and its omission could create confusion, loss, blocked progress, or implementation ambiguity.

Evaluate these families:

1. **Value:** ideal, first-use empty, user-cleared, no results, partial.
2. **Processing:** initial loading, inline loading, progress, updating, success.
3. **Failure:** validation, recoverable error, terminal error, timeout, offline.
4. **Access:** signed out, permission denied, restricted, request pending.
5. **Synchronization:** stale, optimistic, queued, conflict, rollback.
6. **Interaction:** default, hover, focus, active, selected, disabled, dirty.

Mark each candidate **required**, **conditional**, **already covered**, **not applicable**, or **unknown**. Explain required and unknown decisions; do not create not-applicable variants.

### 4. Define the state contract

For every required state, specify:

- trigger and scope;
- data and content shown;
- what remains visible and interactive;
- primary and secondary actions;
- user input or work preserved;
- exit condition and next state;
- retry, fallback, rollback, or escalation path;
- accessibility behavior;
- product or engineering dependency;
- evidence level.

An error without recovery, a loading state without scope, or a success state without a durable consequence is incomplete.

### 5. Create or implement

#### In design tools

- Work on labeled copies by default.
- Preserve the source frame and component set.
- Reuse the existing layout, content hierarchy, tokens, and component vocabulary.
- Use variants only when the states are genuinely one reusable component family.
- Group screen-level states in a readable matrix instead of forcing them into a giant component.
- Prototype only transitions that can be built and checked; annotate the rest.

#### In code

- Follow the existing architecture and state ownership.
- Model mutually exclusive states explicitly; avoid scattered booleans that permit impossible combinations.
- Preserve usable stale data during background refresh when the product model permits it.
- Keep validation close to the affected field while providing an actionable summary when needed.
- Prevent duplicate submissions and define optimistic rollback before assuming success.
- Add or update tests for the critical transitions, not only snapshots of final states.

### 6. Verify the path

Test the sequence, not just each endpoint:

- initial → loading → ideal;
- ideal → update → success;
- action → pending → error → retry → success;
- ideal → stale/offline → reconnect/refresh;
- edit → dirty → leave/cancel/save;
- optimistic → confirmed or rollback;
- signed out/restricted → legitimate access path.

Check narrow layouts, text enlargement, keyboard focus, announcements, preserved data, repeated actions, back navigation, refresh, and slow or failed responses when the available environment permits them.

### 7. Deliver evidence

Report:

1. scope and mode;
2. states found and created or changed;
3. transitions and recovery paths covered;
4. verification performed;
5. observations versus proposals;
6. unresolved product or engineering questions;
7. remaining risk.

Keep the summary compact. Link to edited artifacts and tests. Do not describe a prototype interaction as implemented production behavior.

## Decision rules

### Empty is not one state

Differentiate first use, user-cleared content, zero search results, failed loading, and denied access. Give each the explanation and action warranted by its cause. Do not hide an error or permission problem behind friendly empty-state language.

### Loading must match the operation

- Use a skeleton when structure is known and content is genuinely pending.
- Use inline progress for a local operation.
- Use determinate progress only when progress can be measured honestly.
- Preserve existing content during background refresh when safe.
- Avoid flicker for imperceptibly short operations, but never leave longer work without feedback.

### Success must earn attention

Use persistent confirmation when the result changes future decisions, toast or inline feedback for lightweight reversible actions, and a dedicated success state for consequential flow completion. Do not show success before confirmation unless the interface clearly models an optimistic action and rollback.

### Disabled is a last resort

Prefer an enabled action with clear validation when users need to discover what is missing. If disabling is necessary, preserve contrast, expose the reason, and never rely on color alone.

### Recovery must protect progress

Keep entered values, queued work, selection, scroll position, and recoverable data when feasible. Make retry specific to the failed operation. Provide an alternative only when it is legitimate.

## Boundaries

- Limit content-resilience checks to cases that determine state completeness; do not turn the work into a systematic content stress test.
- Write only the copy needed to make a state understandable and recoverable; do not expand the work into a comprehensive voice, terminology, or interface-copy review.
- Reserve deceptive patterns, consent equity, and destructive-action ethics for a dedicated trustworthy-flow review. Do not expand state completion into a general ethics audit.

## Completion standard

Finish only when:

- the chosen matrix is justified rather than exhaustive;
- source artifacts remain preserved unless direct editing was authorized;
- every added state has a trigger, scope, exit, and recovery rule;
- transitions are represented or explicitly annotated;
- accessible status and focus behavior are considered;
- product and technical assumptions are labeled;
- verification evidence is proportional to the claim;
- no user path ends in an unexplained dead end.
