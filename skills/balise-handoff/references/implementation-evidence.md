# Implementation evidence

Use this reference when readiness depends on source code, data contracts, Storybook, tests, runtime behavior, assets, or acceptance proof.

## Contents

1. Inspect implementation context
2. Design-to-code mapping
3. Acceptance evidence
4. Accessibility and responsive proof
5. Data, assets, and operational dependencies
6. Claim language

## 1. Inspect implementation context

Locate the actual:

- route, feature flag, component, and composition owner;
- design-system package and version;
- token source and generated outputs;
- state management, data fetching, mutation, validation, and error handling;
- API schema, fixtures, permissions, and feature configuration;
- localization keys and content source;
- asset import and optimization pipeline;
- unit, integration, visual, interaction, accessibility, and end-to-end tests;
- Storybook stories, preview deployment, or runtime environment.

Inspect project conventions before proposing new abstractions. Handoff readiness is not permission to re-architect the codebase.

## 2. Design-to-code mapping

For each critical design pattern, record:

- design identifier and semantic purpose;
- code path, package, export, and version;
- design properties to code props or slots;
- token and mode mapping;
- expected states and unsupported combinations;
- intentional visual or structural variance;
- owner and update route.

Prefer the existing implementation when it satisfies intent. Escalate differences that change behavior, semantics, hierarchy, accessibility, or user outcome.

## 3. Acceptance evidence

Write observable criteria with a subject, condition, action, and result.

Weak:

- “Responsive behavior works.”
- “Matches Figma.”
- “Accessible.”

Stronger:

- “At 320 CSS px and 200% text zoom, the primary action remains reachable without two-dimensional scrolling.”
- “When the save request fails, entered values remain, focus moves to the error summary, and retry submits only once.”
- “The production button uses the established `Button` component with the mapped `danger` intent and exposes the visible label as its accessible name.”

For each criterion, record the environment and evidence required: inspection, automated test, Storybook interaction, browser, device, assistive technology, or production observation.

## 4. Accessibility and responsive proof

Figma can support intended:

- hierarchy, reading order, labels, relationships, visible focus, touch target, contrast, motion, and responsive priority.

Runtime or code evidence is generally required for:

- semantic elements and accessible names;
- keyboard order and operation;
- focus management and restoration;
- live-region and error announcements;
- zoom, reflow, orientation, reduced motion, and high contrast behavior;
- platform accessibility APIs and assistive technology output.

Do not claim conformance without an applicable standard, scope, method, and test result.

## 5. Data, assets, and operational dependencies

### Data

Confirm schema, nullability, cardinality, ordering, latency, permissions, failure, pagination, stale behavior, and sensitive-data treatment where applicable. A representative frame is not a data contract.

### Assets

Confirm source, rights, license, expiration, privacy, format, resolution, crop behavior, compression, theme or locale variants, and delivery path. Do not ship temporary MCP URLs, placeholders, screenshots of text, or unlicensed fonts as final assets.

### Operations

Confirm feature flags, environment differences, monitoring, analytics, migration, rollback, support, and release ownership when they can affect acceptance.

## 6. Claim language

Prefer:

- “Observed in the selected Figma revision.”
- “Encoded in the component property model.”
- “Documented in the linked specification.”
- “Simulated in the prototype; runtime handling is unverified.”
- “Mapped to the published code component.”
- “Verified in [environment] against [criterion].”
- “Not assessed because [access or scope limitation].”

Avoid:

- “Production-ready” when only design evidence was inspected.
- “Pixel-perfect” as an acceptance standard.
- “Accessible” based only on contrast or annotations.
- “Uses the design system” based only on matching names.
- “No changes” based only on a missing Changed badge.
