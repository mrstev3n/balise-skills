---
name: balise-handoff
description: Audits and prepares selected Figma screens, components, prototypes, and flows for developer handoff using explicit scope, source-of-truth mapping, evidence levels, risk-based gates, open-decision ownership, and acceptance criteria. Use when a design needs a Ready for dev review, implementation-readiness verdict, handoff cleanup, design-to-code traceability, change revalidation, or a durable handoff contract.
---

# Handoff Readiness

Determine whether the selected design version can be implemented without unresolved critical ambiguity. Treat readiness as an evidence-based agreement—not as visual polish, layer hygiene, annotation volume, or a promise that future code will be correct.

## Core rules

1. Audit the user’s selection and its necessary context. Do not review the entire file by default.
2. Preserve source frames, components, variables, prototypes, links, annotations, and statuses unless the user explicitly asks to edit them.
3. Identify the exact scope, version, platform, implementation audience, release context, and risk before applying gates.
4. Inspect existing components, properties, variables, modes, styles, layout rules, prototypes, annotations, Dev resources, and design-system conventions before proposing additions.
5. Distinguish **observed**, **structurally inferred**, **documented**, **simulated**, **linked to code**, **runtime verified**, and **unknown**.
6. Never treat Ready for dev, the absence of Changed, a prototype, a generated snippet, a matching layer name, or visual similarity as production proof.
7. Never invent API behavior, data shape, permissions, breakpoints, semantics, analytics, asset rights, or engineering constraints as facts.
8. Use the smallest evidence that resolves the implementation question. Do not annotate inspectable properties or every pixel.
9. Apply gates proportionally. Never average away one unresolved critical blocker with many minor passes.
10. Give every critical open decision an impact, owner, next action, and fallback when one exists.
11. Reuse the existing product and design system. Do not create a parallel component or token system to make the handoff look cleaner.
12. Treat handoff as a continuing collaboration. Readiness is attached to a version and can be invalidated by later changes.

## Infer the mode

- **Audit:** inspect and issue a verdict without editing.
- **Prepare:** create or repair handoff structure after explicit edit intent.
- **Verify:** reinspect gates affected by corrections or changes without editing by default.
- **Contract:** summarize the handoff evidence and decisions without editing.
- **Complete:** audit, prepare authorized changes, reverify, and deliver the contract.

Default to **Audit** when edit intent is absent. Audit and Verify are read-only. In Prepare, create a labeled handoff area or work on copies by default. Edit source frames, main components, variables, Dev resources, annotations, or statuses only when explicitly requested.

## Workflow

### 1. Frame the handoff candidate

From the selection and surrounding canvas, identify:

- selected frames, components, states, or flow;
- stable link, section, page, and current status;
- included and excluded surfaces;
- platform, viewport families, release, and implementation audience;
- intended user and product outcome;
- design-system, data, content, asset, accessibility, and policy dependencies;
- final decision owner and communication channel;
- requested output.

Ask one focused question only when a missing fact would materially change the scope, risk, or verdict. If the target or controlling version cannot be established, return **Not assessable** rather than auditing arbitrary nearby work.

### 2. Choose a proportional profile

- **Quick:** small reversible change, known implementation, colocated team, low consequence.
- **Standard:** ordinary feature or component; inspect all ten dimensions and activate applicable gates.
- **Deep:** external team, new platform, wide reuse, migration, money, identity, permissions, sensitive data, safety, security, localization, or critical accessibility path.

State the profile and reason. A deeper profile raises evidence requirements; it does not broaden the selected scope.

### 3. Inspect the Figma system

Inspect:

- selected layers, parent frames and sections;
- adjacent flow, alternate branches, responsive examples, and states;
- main components, instances, component sets, properties, overrides, detachments, and library origin;
- variables, collections, modes, aliases, text styles, and color styles;
- Auto Layout, constraints, dimensions, min/max, wrapping, clipping, order, and layout guides;
- prototype connections and interactive components;
- annotations, measurements, names, and representative content;
- Ready for dev, Changed, version history, comparison, and status notes;
- Dev resources, Code Connect, Storybook, ticket, specification, repository, and asset links;
- export settings and asset sources.

Presence is not freshness. Open or inspect material links when available. If access is unavailable, mark the evidence Unknown.

### 4. Map sources of truth

For each critical domain, identify:

- canonical source;
- version or revision;
- owner;
- derived artifact;
- synchronization or transformation mechanism;
- accepted variance;
- freshness signal;
- change-notification path.

Domains can include:

- product intent and scope;
- visual composition;
- component behavior and API;
- variables and tokens;
- content and localization;
- data and permissions;
- accessibility behavior;
- assets and licensing;
- analytics;
- acceptance criteria and shipped behavior.

Do not assume Figma is canonical for every domain. Code can be canonical for existing runtime behavior; documentation can be canonical for intent or rules; a token repository can be canonical for transformed values.

### 5. Build the readiness matrix

For each applicable gate, mark **Pass**, **Conditional**, **Blocked**, **Unknown**, or **Not applicable**. Explain Conditional, Blocked, Unknown, and Not applicable.

#### A. Scope, version, and ownership

Check:

- exact selected scope and release;
- approved, exploratory, deprecated, or shipped status;
- current revision and known work in progress;
- implementation team and final decision owner;
- inclusions, exclusions, platforms, and viewports.

Block when the team cannot identify what should be built or which version controls.

#### B. Component architecture

Check:

- main component, instance, library origin, or intentional one-off;
- detachments and material overrides;
- properties, variants, slots, nested instances, and supported combinations;
- semantic purpose and naming;
- existing code component or explicit absence;
- intended design-to-code mapping and accepted variance.

Do not require one-to-one component boundaries. Require conceptual and behavioral alignment or an explicit implementation decision.

#### C. Variables, styles, tokens, and modes

Check:

- semantic values versus unexplained raw values;
- collections, aliases, themes, density, brand, locale, and platform modes;
- expected mapping to code tokens;
- canonical token source, transformation, version, and deprecation;
- intentional exceptions and fallback.

A variable attachment does not prove that code consumes the same token.

#### D. Layout and adaptation

Check:

- Auto Layout and content-driven sizing;
- fill, hug, fixed, min, max, wrap, reorder, hide, clip, and overflow rules;
- container behavior between sampled sizes;
- text enlargement, zoom, reflow, device inset, orientation, input method, and reduced motion when relevant;
- localization, bidirectionality, data extremes, and representative content;
- non-negotiable relationships versus implementation freedom.

Frames at several breakpoints are examples, not a complete responsive rule.

#### E. States, interactions, and data

Check:

- trigger, pending, success, error, empty, access, offline, timeout, sync, conflict, and recovery where applicable;
- data source, nullability, cardinality, ordering, validation, permissions, and failure behavior;
- persistence, duplicate-action protection, optimistic behavior, undo, rollback, and back navigation;
- prototype coverage and product or backend decisions still unknown.

If substantial states are missing, report state modeling as a separate follow-up. Do not invoke another skill or silently expand this audit into a full state-design exercise.

#### F. Content, semantics, accessibility, and localization

Check:

- approved versus provisional content and terminology;
- heading, label, button, link, list, table, landmark, image, and status intent;
- accessible names, descriptions, relationships, reading order, focus movement, error association, and announcement intent;
- locale, plural, number, date, currency, bidirectionality, and expansion behavior;
- content owner and source.

Figma can document accessibility intent. It cannot prove runtime semantics, keyboard operation, announcements, reflow, or assistive-technology behavior.

#### G. Assets and production

Check:

- origin, owner, rights, source file, sensitivity, and expiration;
- production format, resolution, color space, compression, crop, theme, and locale variants;
- export settings versus the canonical asset pipeline;
- icon mapping and font availability or license;
- placeholder, generated, or temporary assets that must not ship.

An export preset is not proof of rights or production optimization.

#### H. Decisions and acceptance

Check:

- user and product goal;
- alternatives considered and reason for the current direction;
- technical, policy, research, time, or system constraints;
- non-negotiables and accepted implementation freedom;
- approval owner and unresolved decisions;
- observable acceptance criteria and target verification environment.

Do not present a proposed user benefit as research evidence.

#### I. Ecosystem links and support

Check:

- requirement, ticket, specification, API, content source, repository, story, token source, analytics plan, and asset repository;
- access, version, branch, owner, and freshness;
- support and escalation channel;
- dependencies on other releases or migrations.

The presence of a link is not a Pass unless it resolves the relevant decision.

#### J. Change and verification

Check:

- how changes are detected, compared, communicated, accepted, and revalidated;
- dependencies not covered by normal status changes;
- visual, interaction, accessibility, browser, device, data, and user validation expected after build;
- accepted baseline and review owner;
- evidence that must persist after implementation.

### 6. Assign evidence levels

Assign a level to each material claim:

- **E0 — Unknown:** absent, inaccessible, contradictory, or not assessed.
- **E1 — Visible:** shown in a static frame, copy sample, or asset.
- **E2 — Structured:** encoded in properties, variables, modes, Auto Layout, constraints, or another inspectable structure.
- **E3 — Documented:** rule, rationale, exception, decision, or criterion is explicit and attributable.
- **E4 — Simulated:** exercised in an inspectable prototype or controlled scenario.
- **E5 — Linked:** mapped to a versioned component, token source, story, code artifact, or canonical system.
- **E6 — Runtime verified:** tested in a named environment against a stated criterion.

Higher is not always required. Match evidence to the claim. A prototype can be E4 for sequence but remains insufficient for keyboard behavior. Code Connect can be E5 for provenance but not E6 for accessibility.

### 7. Classify findings

- **Critical blocker:** guessing could cause irreversible action, data loss, unauthorized access, privacy or security exposure, financial error, inaccessible task completion, broken core behavior, wrong release scope, or unbounded architectural rework.
- **Major condition:** implementation can begin only with an explicit owner, deadline, rule, fallback, or bounded assumption.
- **Minor improvement:** clarification reduces rework without blocking safe implementation.
- **Observation:** useful context with no requested action.

For every blocker or condition, record:

- evidence and missing evidence;
- implementation consequence;
- affected surface or dependency;
- recommended owner;
- smallest next action;
- deadline or trigger;
- safe fallback, if one exists;
- gate to reverify.

### 8. Decide the verdict

Choose exactly one:

- **Ready:** no unresolved critical blocker; applicable required gates have adequate evidence; remaining questions fit normal implementation collaboration.
- **Ready with conditions:** work can begin because every material issue has an owner, timing, bounded impact, and safe treatment or fallback.
- **Not ready:** a critical decision would need to be guessed or an essential dependency remains unresolved.
- **Not assessable:** scope, version, context, or access is insufficient for an honest audit.

Do not calculate a universal readiness percentage. Finding counts may help prioritization, but one critical Blocked gate controls the verdict.

### 9. Prepare authorized improvements

When the user asks to prepare the file:

1. Create a clearly labeled handoff section near the source or in the team’s established handoff location.
2. Link to source frames; duplicate only when comparison or annotation requires it.
3. Encode repeatable relationships with Auto Layout, constraints, component properties, variables, modes, and prototype connections before adding prose.
4. Add annotations for intent, behavior, exceptions, accessibility, content, or engineering dependencies that structure cannot express.
5. Add verified Dev resources for tickets, specifications, API contracts, repositories, stories, assets, and decisions.
6. Preserve bindings and the existing design system.
7. Do not detach instances or change shared components merely to improve the audit result.
8. Do not set Ready for dev or clear Changed unless the user explicitly requests it and the controlling owner is known.
9. Reinspect every affected gate after preparation.

Suggested structure:

```text
Handoff Readiness — [feature or surface]
├── Scope and release
├── Approved source
├── Behavior and responsive rules
├── Components and token mapping
├── States and accessibility intent
├── Assets and external resources
├── Open decisions and conditions
├── Acceptance criteria
└── Change and revalidation notes
```

### 10. Handle Ready for dev and Changed honestly

Treat status as workflow evidence only.

Figma documents that a design may not be marked Changed when:

- an instance updates from a shared library;
- the value of an attached variable changes;
- the value of an attached style changes.

Therefore:

- inspect material library, variable, and style dependencies;
- record their relevant version or verification date;
- compare the intended handoff revision with the current selection;
- identify who accepts and communicates changes;
- never use the absence of Changed as proof that the handoff is current.

### 11. Use code links proportionally

#### Dev Mode snippets

Treat generated snippets as inspection aids, not production architecture, semantic markup, responsive proof, or tested implementation.

#### Code Connect

When present, verify the target component, relevant branch or version, property mapping, supported combinations, and accepted variance. A mapping strengthens provenance but does not prove full behavior or accessibility.

#### Storybook or implementation links

When accessible, compare the relevant story, state, viewport, content, interaction, and version. A live component is stronger evidence than a static frame only for what it actually exercises.

If code context is unavailable, do not invent it. Mark the mapping Unknown and identify the owner who can resolve it.

### 12. Revalidate changes

When a design, library, variable, style, requirement, code component, data contract, or asset changes:

1. identify the changed canonical source and revision;
2. classify impact as cosmetic, content, behavioral, structural, contractual, or critical;
3. list directly affected handoff claims and dependencies;
4. invalidate only affected evidence;
5. reopen the relevant gates and conditions;
6. notify or identify decision and implementation owners;
7. replay applicable acceptance criteria;
8. update verdict, contract, and residual risk.

Do not rerun a full-file audit mechanically. Do not preserve Ready when its controlling evidence is stale.

## Handoff contract

Deliver a compact contract containing:

### Decision

- verdict and rationale;
- mode and profile;
- review date and reviewer.

### Scope

- surface, user goal, platform, team, release, version;
- included and excluded work;
- final decision owner.

### Source map

For each material domain: canonical source, version, owner, derived artifact, accepted variance, and last verification.

### Gate results

For each applicable dimension: gate, state, evidence level, artifact, and note.

### Blockers and conditions

For each: severity, finding, consequence, owner, next action, due date or trigger, fallback, and gate to reverify.

### Implementation contract

- non-negotiables;
- accepted implementation freedom;
- component, token, data, content, asset, behavior, and accessibility intent;
- runtime behavior explicitly left to verify.

### Acceptance and change

- observable criteria, environment, required evidence, and owner;
- notification channel, dependencies outside the primary status signal, revalidation owner, and last accepted baseline.

## Claim language

Use:

- “Observed in the selected Figma revision.”
- “Encoded in the component property model.”
- “Documented in the linked specification.”
- “Simulated in the prototype; runtime behavior is unverified.”
- “Mapped to the published implementation.”
- “Verified in [environment] against [criterion].”
- “Not assessed because [scope or access limitation].”

Avoid:

- “Production-ready” after a design-only audit;
- “Accessible” after checking only contrast or annotations;
- “Uses the design system” because names look similar;
- “No changes” because Changed is absent;
- “Pixel-perfect” as the implementation goal.

## Boundaries with adjacent skills

This standalone Figma skill does not invoke other skills. It only identifies work that belongs to a separate specialist review.

- Complete UI States owns systematic state and recovery modeling.
- Content Stress Test owns content variability, overflow, localization, and truncation resilience.
- UX Writing owns comprehensive interface copy, terminology, voice, and content systems.
- Trustworthy Flows owns autonomy, consent, material disclosure, reversibility, and deceptive-pattern risk.
- Handoff Readiness records whether the needed evidence exists and assembles the implementation contract. Do not silently redo the specialist audits.

## Completion standard

Finish only when:

- scope, version, platform, profile, and audience are explicit;
- sources of truth and material divergences are mapped;
- applicable gates and evidence levels are honest;
- no critical ambiguity is hidden by a score, status, or tidy canvas;
- every blocker and condition has a consequence and next action;
- source designs remain preserved unless direct edits were authorized;
- acceptance criteria are observable and proportional to the claim;
- design intent, linked implementation, and runtime verification remain distinct;
- change handling and residual risk remain visible after handoff.
