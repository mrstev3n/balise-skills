---
name: balise-ui-states
description: Audits and completes the relevant missing states of selected Figma screens, components, and flows—including empty, partial, loading, success, error, offline, permission, synchronization, and interaction states—while preserving source designs, reusing the existing system, documenting transitions and recovery, and separating prototype evidence from product assumptions.
---

# UI States

Complete the state system around selected Figma screens, components, or flows. Do not generate a universal gallery. Choose only states that are plausible, consequential, and not already covered.

Treat every state as part of a flow with a trigger, preserved context, exit, recovery, and next state.

## Core rules

1. Preserve source frames and components unless the user explicitly asks to edit them.
2. Work inside the user’s selection and its necessary adjacent flow. Do not redesign unrelated screens.
3. Inspect existing components, variants, variables, styles, copy, prototype links, annotations, and naming before creating anything.
4. Reuse the product’s visual language and component system. Do not create a parallel design system.
5. Do not invent API behavior, permissions, timings, progress percentages, persistence guarantees, or recovery rules as facts.
6. Label **observed**, **created**, **prototype-verified**, **proposed**, and **unknown** behavior separately.
7. Prefer the smallest affected region. A component-level update should not become a full-page loading screen.
8. Preserve user input and valid data through errors whenever the product model permits it.
9. Never disguise an error, access restriction, or loading failure as a friendly empty state.
10. Do not claim accessibility or production behavior from a static frame alone.

## Infer the mode

- **Audit:** inventory existing states and prioritize gaps without editing.
- **Design:** create the relevant proposed states on labeled copies.
- **Repair:** correct incomplete, misleading, inaccessible, or dead-end states.
- **Complete:** audit, create or repair, connect what can be prototyped, and report evidence.

If the request is ambiguous, default to **Audit**. If the user asks to add, complete, fix, or design states, use **Complete**.

## Workflow

### 1. Frame the product moment

Identify from the selection and surrounding canvas:

- the screen, component, control, or flow being evaluated;
- the user goal and value of the ideal state;
- the screens or actions immediately before and after it;
- visible data sources, user input, permissions, network work, and persistence;
- the question the prototype or matrix should answer;
- the intended audience: design review, product decision, engineering handoff, or usability test.

Ask one focused question only when an unknown product fact would materially change the matrix. Otherwise make a labeled proposal.

### 2. Inspect the Figma system

Inspect:

- selected layers and parent section;
- adjacent frames and alternate screens;
- main components, instances, component sets, and variant properties;
- variables, modes, text and color styles;
- Auto Layout, dimensions, constraints, and layout guides;
- prototype connections and interactive components;
- annotations and naming conventions;
- product language and representative data.

Do not infer runtime behavior solely from layer names. Do not detach instances or overwrite the source by default.

### 3. Establish the ideal state

Use the ideal state as the reference for:

- product value;
- information hierarchy;
- stable navigation and actions;
- component anatomy;
- content that should remain visible in other states.

Do not polish the ideal state unless it prevents the other states from working or the user requests it.

### 4. Build a proportional matrix

Evaluate each family and mark candidates as **Required**, **Conditional**, **Covered**, **Not applicable**, or **Unknown**.

#### A. Value states

- **First-use empty:** no user-created data yet; explain value and offer the legitimate first step.
- **User-cleared:** the user completed, archived, or removed all content; acknowledge the result and offer the next relevant action.
- **No results:** a search or filter produced no matches; preserve query context and offer correction or reset.
- **Partial:** some real content exists but the surface is sparse or incomplete; keep real content primary and guide useful progress.

#### B. Processing states

- **Initial loading:** no usable result exists yet.
- **Inline or partial loading:** only a component or region is pending.
- **Progress:** the operation has honest measurable progress or meaningful stages.
- **Updating:** existing data remains usable during refresh or mutation.
- **Success:** an operation has been confirmed and needs proportionate feedback.

#### C. Failure states

- **Validation:** input needs correction; preserve valid values and identify the issue.
- **Recoverable error:** retry or correction is possible.
- **Terminal error:** the current path cannot continue; provide a safe exit or escalation.
- **Timeout:** completion is late or unknown; prevent unsafe duplicates.
- **Offline:** explain what remains available, queued, or blocked.

#### D. Access states

- **Signed out:** authentication is required and the intended destination may need preservation.
- **Permission denied:** the user is known but lacks access.
- **Restricted:** plan, role, region, policy, age, or device prevents use.
- **Request pending:** an access request exists and duplicates must be prevented.

#### E. Synchronization states

- **Stale:** displayed data may be outdated.
- **Optimistic:** success is shown before server confirmation.
- **Queued:** work is stored for later processing or connectivity.
- **Conflict:** local and remote versions compete.
- **Rollback:** an optimistic or partial change is reversed.

#### F. Interaction states

- default, hover, focus-visible, active or pressed;
- selected, read or unread, expanded or collapsed;
- disabled or unavailable;
- dirty or unsaved.

Do not turn every interaction variant into a screen-level state.

### 5. Prioritize

Create a state when at least one applies:

- it is frequent or inevitable;
- omission can cause data loss, duplicate action, blocked progress, or false interpretation;
- it changes the available actions or hierarchy;
- the user needs reassurance, recovery, or a legitimate next step;
- implementation depends on an unresolved design decision;
- the flow crosses a network, permission, persistence, or collaboration boundary.

Do not create a state when its trigger cannot occur, it belongs elsewhere, an existing component already covers it, or the product rule is too unknown to represent honestly. Annotate the question instead.

### 6. Define a state contract

Before drawing each required state, determine:

- **Trigger:** what causes it?
- **Scope:** screen, region, component, or control?
- **Content:** what is known, missing, pending, or failed?
- **Persistence:** what remains visible, interactive, or saved?
- **Actions:** what can the user legitimately do?
- **Exit:** what resolves the state?
- **Next state:** where does the flow go?
- **Recovery:** retry, correction, fallback, rollback, or escalation?
- **Accessibility:** how should status, focus, and controls work?
- **Dependency:** what product or engineering rule remains unknown?

An error without recovery, a loading state without scope, or a success state without consequence is incomplete.

### 7. Create the matrix

Create a clearly labeled section near the source:

```text
Complete UI States — [surface]
├── Source
├── Existing states
├── Required proposals
├── Transition prototype
└── Open product and engineering questions
```

Then:

- duplicate source frames for screen-level proposals;
- keep existing frame sizes and layout rules unless they cause the state failure;
- reuse components, instances, variables, styles, and copy conventions;
- bind variants through a `State` property only when they share reusable anatomy;
- use nested state components for independent regions;
- preserve Auto Layout and allow recovery copy to wrap;
- use representative non-sensitive data;
- name states consistently and visibly;
- avoid generating Not applicable variants.

### 8. Apply state-specific rules

#### Empty

Differentiate first use, user-cleared, no results, failed loading, and denied access. Explain the cause, set expectations, and provide the next legitimate action. Avoid generic illustrations, “No data,” and fake CTAs.

#### Partial

Do not replace real sparse content with placeholders. Preserve value and show a useful next step without coercive gamification.

#### Loading

- Use skeletons only when the expected structure is known.
- Use inline feedback for local operations.
- Preserve existing content during background updates when plausible.
- Use determinate progress only when measurement is credible.
- Do not leave longer work without feedback or show instant loading flicker unnecessarily.

#### Success

- Use inline feedback for small local changes.
- Use a toast for lightweight, reversible confirmation.
- Use persistent feedback when the result affects later decisions.
- Use a dedicated completion state for consequential flow completion.
- Do not claim success before confirmation unless optimistic behavior and rollback are explicit.

#### Error

Explain what happened in product language, state what was preserved, and provide a specific recovery. Keep entered values. Avoid codes as the primary message, blame, generic retry, and destructive resets.

#### Offline and timeout

Clarify what is available, queued, or unknown. Do not encourage repeated payment, upload, or destructive actions when completion status is uncertain.

#### Permission

Explain the actual boundary. Offer sign-in, request access, upgrade, or settings only if that path legitimately exists. Otherwise provide a safe exit or owner contact.

#### Optimistic and conflict

Represent pending confirmation, duplicate-action protection, failure, and rollback. Preserve both versions during a conflict until a resolution rule is known.

#### Disabled

Prefer an enabled action with visible validation when users need to discover requirements. If disabling is necessary, keep sufficient contrast, show the reason, and do not rely on color alone.

### 9. Connect transitions

Prototype only what can be built and inspected using available Figma interactions such as `Change to`, overlays, or navigation.

For each critical path, represent or annotate:

- event;
- pending state;
- success state;
- failure state;
- retry or rollback;
- focus and announcement intent;
- data preserved.

Useful sequences include:

- `unknown → loading → ideal | empty | error`;
- `ideal → updating → refreshed | error`;
- `dirty → submitting → success | validation | error`;
- `ideal → optimistic → confirmed | rollback`;
- `online → offline → queued → syncing → confirmed | conflict`.

If the Figma agent cannot create or verify the interaction, annotate it and mark it **Proposed**.

### 10. Verify

Inspect the created matrix and, where possible, play critical prototypes.

Check:

- source frames remain unchanged;
- states use the existing visual and component system;
- each state has a trigger, scope, exit, and recovery;
- loading does not erase unrelated usable content;
- empty, error, and access states are not conflated;
- input and valid data remain preserved;
- actions have clear availability and hierarchy;
- status is not communicated by color alone;
- keyboard focus and announcements are explicitly designed or annotated;
- narrow layouts and longer messages do not break;
- transitions do not lead to dead ends;
- assumptions are labeled.

Do not call a static review or Figma prototype production verification.

## Deliverable

Return a compact summary with:

1. mode and scope;
2. states found;
3. states created or repaired;
4. transitions prototyped or annotated;
5. key recovery decisions;
6. open product or engineering questions;
7. evidence level and remaining risk.

When auditing only, use a table with columns: **Surface**, **State**, **Status**, **Impact**, **Recommendation**, **Evidence**.

## Boundaries

- Limit content-resilience checks to cases that determine state completeness; do not turn the work into a systematic test of long, short, localized, numeric, or missing content.
- Write only the copy needed to make a state understandable and recoverable; do not expand the work into a comprehensive voice and terminology review.
- Do not expand into a general accessibility, ethical-pattern, or visual-design audit unless requested.
- Do not invent a new route, backend capability, or permission request merely to avoid a dead end. Propose and annotate it when legitimate.

## Completion standard

Finish only when the matrix is justified rather than exhaustive, the source is preserved, every created state has a complete contract, critical transitions are represented or annotated, uncertainty is explicit, and no designed path ends without explanation or recovery.
