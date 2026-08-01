# Implementation and handoff

Use this reference when working in code or preparing engineering decisions.

## Discover the state owner

Trace:

- route and component entry point;
- canonical data source and cache;
- query and mutation lifecycle;
- form and schema validation;
- authentication and authorization;
- local persistence or offline queue;
- error boundaries and fallback components;
- translations and content source;
- analytics and logging;
- existing unit, component, and end-to-end tests.

Change the layer that owns the state. Do not patch rendered copy in one component when the behavior belongs to the data or routing layer.

## Model valid combinations

Prefer a discriminated union, reducer, state machine, or explicit query status when boolean combinations permit impossible states such as `loading && success && error`.

Separate independent regions when they can load or fail independently. Avoid one page-level status that erases usable content.

## API questions

Record unknowns rather than guessing:

- Can the action be retried safely?
- Is the operation idempotent?
- Does timeout mean failure or unknown completion?
- Which validation comes from client, server, or policy?
- Is stale data acceptable, and for how long?
- What is persisted across refresh, back navigation, or offline use?
- How are conflicts detected and resolved?
- Which permissions can users request or change?

## Acceptance proof

For each critical transition, define observable evidence:

| Transition | Proof |
| --- | --- |
| Loading → ideal | Resolved fixture renders expected data without focus loss. |
| Loading → empty | Confirmed empty response renders the correct empty subtype. |
| Submit → error | Failure preserves input and permits safe retry. |
| Optimistic → rollback | Rejected mutation restores prior data and explains reversal. |
| Offline → sync | Queued work survives reconnect and reports outcome. |
| Restricted → granted | Access change refreshes the surface without losing destination. |

Use project-native tests. Verify the rendered product when claims involve layout, focus, routing, persistence, or network behavior.

## Handoff packet

Include:

- state matrix and applicability decisions;
- state contracts;
- prototype or code links;
- copy and localization considerations;
- tokens and reusable components;
- API and permission assumptions;
- accessibility behavior;
- analytics or monitoring needs;
- acceptance tests;
- unresolved decisions with owners.

Keep implementation suggestions separate from confirmed backend behavior.
