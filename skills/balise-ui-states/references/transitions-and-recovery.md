# Transitions and recovery

Use this reference for asynchronous operations, retries, optimistic updates, and multi-step flows.

## Transition contract

For every edge between states, record:

- event or condition;
- source state;
- pending representation;
- content and controls preserved;
- cancellation behavior;
- success destination;
- failure destination;
- retry or rollback rule;
- announcement and focus behavior;
- instrumentation or test evidence when relevant.

## Common sequences

### Initial data

`unknown → loading → ideal | empty | error`

Do not render empty before the request resolves. Empty is confirmed absence; loading is unresolved availability.

### Search and filters

`ideal → updating → results | no-results | error`

Preserve the query and filters. Prefer retaining previous results during a background update when the product permits it.

### Form submission

`dirty → validating → submitting → success | field-error | form-error | unknown-outcome`

Prevent duplicate submission. Preserve valid fields. Focus the first error only when doing so will not disorient users, and offer a summary for long forms.

### Optimistic mutation

`ideal → optimistic-pending → confirmed | rollback`

Make pending status distinguishable without blocking unrelated work. On failure, restore the prior state, explain the reversal, and provide retry if safe.

### Offline queue

`online → offline → queued → syncing → confirmed | conflict | error`

State whether work is stored locally, whether leaving is safe, and how conflicts will be handled.

### Permission request

`restricted → requesting → pending → granted | denied | expired`

Do not offer request access unless the system supports it. Prevent repeated requests and clarify who decides.

## Recovery hierarchy

Prefer, in order:

1. automatic recovery without data loss;
2. scoped retry of the failed operation;
3. correction of a specific input or dependency;
4. alternate legitimate path;
5. return to a safe prior state;
6. escalation or support with useful context.

Never make refresh, restart, or re-entry the default if the product can preserve state.

## Unknown outcomes

Timeouts and interrupted payments, uploads, or destructive mutations may leave completion unknown. Do not label them failed until confirmed. Prevent duplicate action, offer status checking, and explain what users should do next.

## Motion and continuity

Use motion to preserve object continuity or communicate arrival, removal, and reordering. Avoid animation that delays recovery, masks uncertainty, or ignores reduced-motion preferences. Static prototypes should annotate timing and intent rather than imply runtime proof.
