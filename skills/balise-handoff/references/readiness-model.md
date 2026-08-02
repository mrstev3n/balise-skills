# Readiness model

Use this reference to select gates, qualify evidence, prioritize findings, and decide the verdict.

## Contents

1. Applicability
2. Ten readiness dimensions
3. Evidence levels
4. Severity
5. Verdict algorithm
6. Anti-patterns

## 1. Applicability

Start by identifying what is being handed off and to whom. A gate is applicable only when its subject can affect implementation of the selected scope.

For each gate, record one state:

- **Pass:** adequate evidence resolves the implementation question.
- **Conditional:** work may begin under an explicit condition with owner and timing.
- **Blocked:** safe implementation requires a decision or dependency that is unresolved.
- **Unknown:** evidence is absent, inaccessible, contradictory, or not assessed.
- **Not applicable:** the trigger cannot occur or the concern is genuinely outside scope; state why.

Do not convert Unknown to Pass because a team usually handles it later. Do not create work for Not applicable gates.

## 2. Ten readiness dimensions

### A. Scope, version, and ownership

Check:

- selected frames, components, flows, routes, and platforms;
- inclusions, exclusions, release, branch, version, and last relevant review;
- intended implementation team and final decision owner;
- relation between exploratory, approved, deprecated, and shipped artifacts;
- known work in progress that can invalidate the candidate.

Block when the team cannot identify what should be built or which version controls.

### B. Component architecture

Check:

- main component, instance, local component, library origin, or intentional one-off;
- detached instances and overrides that materially change behavior;
- properties, variants, slots, nested instances, and component boundaries;
- semantic purpose and naming shared across design and code;
- existing code component, story, API, or deliberate gap;
- supported and unsupported combinations.

Do not require one-to-one component parity. Require a clear mapping or an explicit implementation decision.

### C. Variables, styles, tokens, and modes

Check:

- semantic versus raw values;
- collections, aliases, themes, density, locale, brand, and platform modes;
- Figma-to-code token mapping and transformation pipeline;
- source canon, version, deprecation, and fallback;
- values intentionally outside the system.

Names should express purpose rather than current value. A token attachment does not prove the code consumes the same token.

### D. Layout and adaptation

Check:

- Auto Layout or equivalent structural intent;
- fixed, fill, hug, min/max, wrapping, clipping, ordering, and aspect ratio;
- container behavior between sampled viewports;
- text enlargement, zoom, reflow, reduced motion, device insets, and input method where relevant;
- content-driven growth, density, localization, and data extremes;
- non-negotiable relationships versus implementation freedom.

Screens at three breakpoints are examples, not a responsive rule.

### E. States, interactions, and data

Check:

- triggers, transitions, pending, success, error, empty, access, offline, timeout, sync, and recovery states;
- data source, schema, nullability, cardinality, validation, permissions, and failure behavior;
- persistence, optimistic behavior, duplicate-action protection, undo, rollback, and back navigation;
- analytics or audit events when contractually important;
- backend and product decisions still needed.

Delegate systematic state design to `complete-ui-states` when coverage is incomplete.

### F. Content, semantics, accessibility, and localization

Check:

- approved or provisional content and terminology;
- heading, label, link, button, list, table, landmark, image, and status intent;
- accessible names, descriptions, relationships, error association, reading order, focus movement, and announcements;
- language, locale, plural, number, date, currency, bidirectionality, and expansion behavior;
- content owner and source.

Static design can document accessibility intent; runtime evidence is needed for execution claims.

### G. Assets and production

Check:

- asset owner, origin, rights, source file, sensitivity, and expiration;
- required format, resolution, color space, compression, crop, theme, and locale variations;
- export settings versus canonical asset pipeline;
- icon mapping, font availability and licensing;
- placeholder or generated assets that must not ship.

An export preset is not proof of rights or production optimization.

### H. Decisions and acceptance

Check:

- user and business goal;
- relevant alternatives and why the current direction was chosen;
- technical, policy, research, time, or system constraints;
- non-negotiables and acceptable variance;
- approval owner and unresolved decisions;
- observable acceptance criteria and target verification environment.

Do not describe a hypothesized user benefit as research evidence.

### I. Ecosystem links and support

Check:

- product requirement, ticket, specification, API, content source, repository, story, token source, and analytics plan;
- link access, version, owner, and freshness;
- support channel and escalation owner;
- relationship to other releases or migrations.

Link presence alone is insufficient. Open and verify material sources when possible.

### J. Change and verification

Check:

- how changes are detected, compared, communicated, accepted, and revalidated;
- dependencies that do not trigger normal design-status changes;
- visual, interaction, unit, integration, accessibility, device, and user tests required;
- accepted baseline and responsibility for reviewing differences;
- evidence retained after implementation.

Readiness is versioned. A previous Ready verdict does not automatically survive dependency changes.

## 3. Evidence levels

Assign evidence to a claim, not to the artifact as a whole.

| Level | Meaning | Examples | Limit |
| --- | --- | --- | --- |
| E0 Unknown | No trustworthy evidence | inaccessible source, contradiction, missing decision | supports only a question |
| E1 Visible | Static example exists | frame, screenshot, copy, asset | does not establish a rule |
| E2 Structured | Intent is encoded structurally | component property, token alias, Auto Layout, type schema | does not prove runtime parity |
| E3 Documented | Rule and rationale are explicit | annotation, ADR, ticket criterion, specification | can be stale or unimplemented |
| E4 Simulated | Scenario was exercised | Figma prototype, test fixture, interactive mock | may omit runtime constraints |
| E5 Linked | Canonical systems are mapped | Code Connect, Storybook, source token, component path | must verify version and coverage |
| E6 Runtime verified | Behavior passed a named check | browser, device, automated test, assistive technology | applies only to tested conditions |

Use the lowest accurate claim. Example: a Code Connect mapping is E5 for provenance, not E6 for keyboard support.

## 4. Severity

### Critical blocker

Use when guessing can plausibly cause:

- irreversible user action, data loss, or duplicate transaction;
- unauthorized access, privacy or security exposure;
- inaccessible completion of a core task;
- invalid money, identity, permission, or policy behavior;
- architectural incompatibility or unbounded rework;
- implementation of the wrong release scope.

### Major condition

Use when work can start only if an owner, deadline, fallback, or bounded assumption is explicit. A condition without an owner is usually a blocker.

### Minor improvement

Use for clarification that reduces friction or rework without changing safe implementation.

### Observation

Use for contextual information with no requested action.

## 5. Verdict algorithm

1. If target scope or version cannot be established, return **Not assessable**.
2. If access prevents inspection of evidence required for a critical gate, return **Not assessable** or **Not ready** depending on whether the missing evidence is an audit limitation or a known delivery deficiency. Explain the distinction.
3. If any applicable critical gate is Blocked, return **Not ready**.
4. If material gates are Conditional and each condition has owner, timing, impact, and safe treatment, return **Ready with conditions**.
5. If required gates pass and residual unknowns fit normal collaboration, return **Ready**.

Do not average gate states. Do not let many Pass results cancel one critical Blocked result.

## 6. Anti-patterns

- Checking every layer name while missing an unresolved data contract.
- Requiring zero detached instances without understanding why they differ.
- Treating design-system adoption as an outcome rather than a means.
- Requiring annotations that repeat inspectable properties.
- Marking a design ready because a developer attended a review.
- Marking a design not ready because implementation details are intentionally left to engineering.
- Treating pixel equality as intent equality.
- Recording open questions without impact, owner, or next action.
- Calling a design accessible, performant, secure, or production-ready from static evidence.
