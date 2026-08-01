# Figma patterns

Use this reference when auditing or creating states in Figma.

## Inspect before editing

Check the selection, parent section, adjacent frames, local components, component sets, properties, variables, text styles, layout guides, prototype connections, annotations, and naming patterns.

Do not infer runtime logic solely from layer names. Do not detach instances unless explicitly required.

## Choose the representation

### Component variants

Use a `State` property when variants share anatomy and represent a reusable component condition, such as default, loading, success, error, selected, or disabled.

Avoid forcing full-page loading, offline, permission, and error screens into one component set merely because they are visually related.

### Screen matrix

Use labeled frames for route- or screen-level states. Arrange source, existing states, proposed states, and transition notes in a readable section.

### Local region

For partial loading or inline error, keep surrounding content stable and change only the affected region. Use nested components when that matches the design system.

## Preserve structure

- Duplicate source frames for exploratory work.
- Reuse Auto Layout, min/max sizing, wrapping, and existing spacing tokens.
- Preserve component relationships and variable bindings.
- Keep copy in the language and tone of the product.
- Use real or representative data without exposing sensitive information.
- Label proposed content and technical assumptions.

## Prototypes and annotations

Build `Change to`, overlay, or navigation interactions only when the current Figma surface supports them and they can be verified. Otherwise annotate:

- trigger;
- scope;
- duration or completion signal;
- data preserved;
- allowed actions;
- next state;
- retry, rollback, or fallback;
- backend dependency.

## Suggested organization

```text
Complete UI States — [surface]
├── Source
├── Existing states
├── Required proposals
│   ├── Loading
│   ├── Empty / partial
│   ├── Error / recovery
│   └── Success / confirmation
├── Transition prototype
└── Open product and engineering questions
```

Generate only the applicable branches.

## Figma evidence levels

- **Observed:** present in the inspected file.
- **Created:** frame, variant, or annotation added.
- **Prototype-verified:** interaction played and inspected in Figma.
- **Proposed:** intended behavior represented but not executable.
- **Unknown:** product or technical rule not established.

Never label a Figma-created proposal as implemented.
