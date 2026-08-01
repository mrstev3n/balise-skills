# State taxonomy

Use this reference to select and distinguish states. Do not treat the list as a mandatory matrix.

## Contents

1. Value states
2. Processing states
3. Failure states
4. Access states
5. Synchronization states
6. Interaction states
7. Selection heuristics

## 1. Value states

### Ideal

The product delivers its intended value with representative, actionable data. Use it as the hierarchy and continuity reference, not as the only designed condition.

### First-use empty

No user-created data exists yet. Set expectations, demonstrate value, and offer the legitimate first step. Avoid overwhelming tours or decorative dead ends.

### User-cleared

The user completed, archived, or removed all items. Acknowledge the accomplishment and offer the next relevant action without pretending this is first use.

### No results

A query or filter returned no matches. Preserve the query context and offer clear filters, correction, or reset. Do not suggest creating content unless that is truly relevant.

### Partial

Some value exists, but the surface is sparse or incomplete. Keep real content primary and guide the next useful step. Do not fill the interface with fake data merely to make it look full.

## 2. Processing states

### Initial loading

No usable result is available yet. Communicate activity and preserve stable navigation when possible.

### Inline or partial loading

Only a component or region is pending. Keep unrelated controls and content available. Match placeholders to the expected structure.

### Progress

Work is measurable or staged. Use determinate progress only when the system can report it truthfully; otherwise use status milestones or indeterminate feedback.

### Updating

Usable data exists while a refresh or mutation runs. Preserve it when safe and expose freshness or pending status without replacing the whole screen.

### Success

An operation has been confirmed. Match persistence and prominence to consequence: inline, toast, persistent banner, receipt, or dedicated completion view.

## 3. Failure states

### Validation

User input is missing, malformed, incompatible, or outside permitted bounds. Identify the affected field, explain the correction, and preserve all other valid input.

### Recoverable error

An operation failed but can be retried or corrected. Explain impact, preserve context, and scope retry to the failed operation.

### Terminal error

The current path cannot continue. Explain what remains safe, offer a legitimate exit or escalation, and avoid fake retry actions.

### Timeout

The system did not complete within an expected window. Distinguish unknown completion from confirmed failure; repeated submission may duplicate work.

### Offline

Connectivity is absent or unreliable. Clarify what remains available, what is queued, and what requires reconnection.

## 4. Access states

### Signed out

Authentication is required. Preserve the intended destination and return users there after successful sign-in when appropriate.

### Permission denied

The identity is known but lacks access. Explain the boundary and offer request access only when such a mechanism exists.

### Restricted

A policy, plan, region, age, role, or device prevents use. State the actual constraint without disguising it as a technical failure.

### Request pending

An access request exists but is unresolved. Prevent duplicates, show status, and define refresh or notification behavior.

## 5. Synchronization states

### Stale

Displayed data may be outdated. Show freshness when it changes decisions and permit refresh without discarding usable content.

### Optimistic

The UI reflects an expected success before server confirmation. Define pending affordance, duplicate-action protection, failure messaging, and rollback.

### Queued

Work is stored for later transmission or processing. Clarify whether leaving is safe and how users can inspect or cancel the queue.

### Conflict

Local and remote versions cannot be reconciled automatically. Preserve both versions, identify the conflict, and provide an understandable resolution path.

### Rollback

An optimistic or partially applied change was reversed. Explain what changed and preserve recoverable user work.

## 6. Interaction states

Cover default, hover, focus-visible, active/pressed, selected, disabled/unavailable, read/unread, expanded/collapsed, and dirty/unsaved only where applicable.

Interaction variants are not substitutes for screen states. Keep keyboard focus visible. Avoid disabled controls that conceal requirements.

## 7. Selection heuristics

Prioritize a state when one or more apply:

- it is frequent or inevitable;
- omission risks data loss, duplicate action, blocked progress, or misinterpretation;
- implementation depends on an unresolved design decision;
- the state changes available actions or information hierarchy;
- a user needs recovery, reassurance, or a legitimate next step;
- the flow crosses a network, permission, persistence, or collaboration boundary.

Exclude or defer when:

- the trigger cannot occur in the product model;
- the state belongs to an unrelated surface;
- the same behavior is already covered by a reusable component;
- no reliable product rule exists and an annotation or question is more honest than a fabricated screen.
