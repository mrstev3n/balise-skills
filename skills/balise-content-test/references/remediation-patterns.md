# Remediation Patterns

Use this reference when repairing a confirmed issue or recommending an overflow, disclosure, responsive, or component-level pattern.

## Contents

- Content criticality
- Remediation hierarchy
- Component patterns
- Figma primitives
- Source and runtime patterns
- Regression rules

## Content Criticality

### Decision-critical

Examples: price, fee, consent, consequence, destructive action, permission, safety, legal information, error, recovery instruction.

Keep fully available and understandable. Do not rely on ellipsis, hover, or transient reveal.

### Identity-critical

Examples: person, organization, file, path, account, transaction reference, device, or unique identifier.

Preserve the distinguishing segment and provide reliable access to the full value. Middle truncation can be appropriate for paths, hashes, and extensions.

### Comparative

Examples: plan features, table values, prices across options, rankings, or statuses across records.

Preserve scanability, alignment, units, and the value that distinguishes one option from another.

### Explanatory

Examples: descriptions, guidance, contextual help, and supporting detail.

Prefer wrapping. Controlled clamping is acceptable when persistent expansion is available and the initial excerpt retains meaning.

### Supplementary

Examples: short, nonessential clarification.

A tooltip can be appropriate when it is available by pointer and focus and the information is not required to complete the task.

## Remediation Hierarchy

Compare solutions in this order:

1. **Absorb**: wrapping, content-driven height, flexible width, min/max dimensions, and adaptive tracks.
2. **Reorganize**: stack, reflow, change density, preserve priority, or move lower-priority content.
3. **Structure overflow**: scrolling, overflow menu, disclosure, adjustable panel, or progressive navigation.
4. **Truncate**: use an explicit rule and preserve full-value access.
5. **Annotate**: document intended runtime behavior and unresolved product constraints.

Do not shrink typography, compress spacing, hide data, or rewrite valid content merely to conceal layout fragility.

## Component Patterns

| Surface | Prefer | Avoid |
| --- | --- | --- |
| Button or action | grow, wrap cautiously, stack, or restructure | ellipsis on the action label |
| Error or warning | full reflow with recovery visible | tooltip-only message |
| Consent, fee, or consequence | complete persistent wording | collapsed or transient disclosure |
| Name or title | controlled wrapping or ellipsis with complete reveal | removing the identifying segment |
| File, path, hash, reference | middle truncation when it preserves identity | cutting the extension or discriminating suffix |
| Description | wrap or clamp with explicit “Show more” | paragraph-sized tooltip |
| Table | flexible/resizable column, focus reveal, or detail panel | destroying column comparison |
| Tabs | scroll, overflow menu, or responsive substitute | truncating several labels into ambiguity |
| Breadcrumbs | structured collapse and overflow menu | truncating several hierarchy levels |
| Picker | complete value in opened list; controlled closed-state truncation | hiding the full choice everywhere |
| Tree or sidebar | adjustable width or progressive navigation | increasingly aggressive ellipsis |
| Counter | flexible width or approved abbreviation with exact detail | unannounced conversion to `99+` |
| Card grid | content-driven height or consistent internal zones | fixed height that clips variable text |

## Tooltip and Disclosure Rules

Use a tooltip only for short, supplementary, noninteractive information.

A desktop tooltip should:

- trigger on hover and keyboard focus;
- remain available while hovered when needed;
- be dismissible with Escape when appropriate;
- keep focus on the trigger;
- expose the complete short value;
- have a non-hover path on touch.

Use an inline disclosure, popover, dialog, bottom sheet, or detail view for long, critical, comparative, or interactive content.

Do not invent a detail destination solely to hide overflow. Use it only when it fits the product’s information architecture.

## Figma Primitives

- **Auto Layout**: direction, wrapping, Hug contents, Fill container, padding, gaps, and content-driven growth.
- **Text resizing**: Auto width, Auto height/wrap, Fixed size, and max lines according to content role.
- **Min/max dimensions**: flexible envelopes without invented business constraints.
- **Constraints**: relative behavior tested by resizing the parent.
- **Layout guides**: alignment across frames, not proof of responsiveness.
- **Auto Layout grid**: adaptive tables, galleries, and tracks.
- **Components and properties**: text, icon, visibility, and disclosure without detaching instances.
- **Variants**: only meaningful states such as Default, Truncated, Hover/Focus, and Expanded.
- **Variables and modes**: reuse existing locale or fixture architecture; do not build infrastructure for a one-off test.
- **Prototype interactions**: verify connections when possible; otherwise prepare states and annotate behavior.

## Source and Runtime Patterns

When code is available:

- prefer natural layout and wrapping before JavaScript measurement;
- inspect fixed heights, absolute positioning, overflow, line clamps, grid tracks, flex shrink, and min-width behavior;
- use locale-aware number, date, currency, unit, and plural formatting;
- truncate at grapheme-aware boundaries when programmatic truncation is unavoidable;
- expose the full value in accessible text or a suitable disclosure;
- preserve semantic DOM and logical focus order when visual order changes;
- test actual breakpoints and zoom rather than inferring them from CSS alone.

Match the project’s architecture and design system. Do not introduce a new UI library or component abstraction solely for the repair.

## Regression Rules

After repair, re-test:

1. the exact failing content;
2. the original content;
3. the supported narrow and wide layouts affected;
4. related states and variants;
5. keyboard and touch disclosure when changed;
6. one adjacent boundary to detect an overfitted fix.

If a defect repeats across instances, identify it as a potential component-level problem. Do not change a shared component or published design-system asset without authorization.
