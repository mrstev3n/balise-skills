# Figma execution

Use this reference when auditing or preparing a Figma selection, file, component set, prototype, or Dev Mode handoff.

## Contents

1. Inspect before acting
2. Mutation rules
3. Use native structure
4. Status and version evidence
5. Code and development links
6. Suggested handoff area
7. Verification

## 1. Inspect before acting

Start from the user selection. Inspect only necessary context:

- parent frame, section, page, and adjacent flow;
- alternate states, responsive examples, prototypes, and annotations;
- main components, instances, component sets, properties, overrides, detachments, and library origin;
- variables, collections, modes, aliases, text and color styles;
- Auto Layout, constraints, dimensions, min/max, wrapping, clipping, and layout guides;
- layer naming where it conveys semantic intent;
- Dev Mode status, version history, comparison, and change notes;
- Dev resources, Code Connect mappings, Storybook links, tickets, and specifications;
- assets and export settings.

Do not infer production behavior from layer names or prototype appearance. Do not assume the nearest component is the canonical component.

## 2. Mutation rules

- Audit and Verify are read-only.
- Prepare requires explicit edit intent.
- Create a labeled handoff area or copy by default.
- Edit source frames, main components, variables, annotations, links, or statuses only when explicitly requested.
- Preserve component bindings, properties, variables, styles, Auto Layout, and prototype evidence.
- Do not detach instances to make edits easier.
- Do not mark Ready for dev or clear Changed automatically.
- Do not delete exploratory or obsolete work until its status and owner are verified and deletion is authorized.

## 3. Use native structure

Prefer:

- Auto Layout and constraints for spatial relationships and content growth;
- component properties for intended variation;
- variables, modes, and aliases for semantic decisions;
- interactive components and prototypes for inspectable sequences;
- annotations for intent, exceptions, accessibility, content, and development rules that structure cannot express;
- Dev resources for canonical external artifacts;
- Code Connect or Storybook for existing implementation provenance.

Avoid annotations that restate dimensions, colors, or property values already inspectable. Structure is easier to keep consistent than prose duplicated across frames.

### Responsive intent

Document behavior, not only snapshots:

- container and content priorities;
- fill, hug, fixed, min, max, wrap, reorder, hide, and overflow rules;
- behavior between displayed viewports;
- text enlargement, localization, bidirectionality, and data extremes;
- non-negotiables versus implementation freedom.

### Component mapping

For each material component, identify:

- semantic purpose;
- Figma origin and version;
- supported properties and combinations;
- existing code component or explicit absence;
- property mapping and accepted design-code variance;
- deprecated or provisional status.

A Figma component and code component may have different boundaries. Require conceptual and behavioral alignment, not forced one-to-one structure.

## 4. Status and version evidence

Treat Ready for dev, Completed, and Changed as workflow signals.

Important limitations documented by Figma:

- an instance update from a shared library does not necessarily mark the design Changed;
- a changed value of an attached variable does not necessarily mark it Changed;
- a changed value of an attached style does not necessarily mark it Changed.

Therefore:

- record relevant library, variable, and style versions separately;
- inspect dependency changes when the release depends on them;
- compare the intended handoff revision with the current selection;
- identify who can accept a change and who must be notified;
- never use the absence of Changed as proof of freshness.

## 5. Code and development links

### Generated snippets

Use Dev Mode snippets as inspection aids. Do not treat them as production architecture, semantic markup, tested responsive behavior, or evidence that the target stack will implement the design literally.

### Code Connect

When available, verify:

- mapping targets the correct published component;
- version or branch is relevant;
- props and variants map to real code props;
- unsupported design combinations are visible;
- slots, instance swaps, or nested content are represented honestly.

Code Connect strengthens provenance. It does not prove full behavior or accessibility.

### Storybook

When available, inspect the published story and branch, not only the link. Compare supported states, interactions, viewport behavior, content, accessibility results, and version. A live story is stronger implementation evidence than a static frame, but only for what the story exercises.

### MCP context

Figma MCP can provide design context, metadata, screenshots, variables, and mappings. It does not generate final code, understand the design system by default, or adapt implementation automatically. Report unavailable context rather than fabricating it.

## 6. Suggested handoff area

When the user asks to prepare the canvas, use a structure such as:

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

Keep source frames in place. Link to them from the handoff area or use labeled copies only when comparison is needed.

## 7. Verification

Before delivering:

- confirm the selected scope and version still match the report;
- inspect links and mappings that control critical claims;
- check that annotations agree with structure;
- test prototype paths that are cited as evidence;
- inspect narrow and wide frames, longer content, modes, and critical states;
- confirm no source frame or shared component changed without authorization;
- mark runtime behavior, data, semantics, focus, announcements, performance, security, and permissions as unverified unless actually tested.

Use this formulation when appropriate: “The Figma evidence communicates the intended design and implementation constraints; runtime behavior remains to be verified against the listed acceptance criteria.”
