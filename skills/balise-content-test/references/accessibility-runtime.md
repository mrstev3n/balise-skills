# Accessibility and Runtime Verification

Use this reference for the Accessible profile, implemented interfaces, browser-based verification, zoom or reflow tests, focus disclosures, and touch-target analysis.

## Contents

- Evidence levels
- Static design stress
- Browser and application checks
- Text enlargement and spacing
- Reflow
- Hover, focus, and touch
- Reporting language

## Evidence Levels

Distinguish the available proof:

1. **Static design**: geometry, visible hierarchy, variants, annotations, and intended states.
2. **Source inspection**: layout rules, breakpoints, truncation code, semantic markup, formatter use, and test fixtures.
3. **Rendered runtime**: actual viewport behavior, zoom, text spacing, focus, keyboard operation, hover, touch emulation, and full-value disclosure.
4. **Assistive-technology or specialist review**: screen-reader output, platform behavior, cognitive accessibility, and formal conformance.

Never claim a higher evidence level than was inspected.

## Static Design Stress

In Figma, screenshots, or static artifacts, inspect:

- enlarged text variants or simulated scale;
- narrow frames and content-driven growth;
- overlapping, clipped, hidden, or reordered content;
- visual focus states and intended disclosure variants;
- whether hover-only information has a keyboard and touch counterpart;
- visible target dimensions and spacing;
- whether critical information is available without a transient overlay.

Describe these as risks or intended behaviors, not verified runtime accessibility.

## Browser and Application Checks

When a runnable interface is available and the request authorizes testing:

- inspect the actual DOM and computed styles before changing code;
- test supported viewport widths and responsive breakpoints;
- test browser zoom or platform text scaling as appropriate;
- apply text-spacing overrides when feasible;
- traverse interactive elements with the keyboard;
- trigger disclosures by both pointer and focus;
- dismiss additional content with Escape when the pattern requires it;
- verify that full truncated values are programmatically or visibly available;
- inspect touch-sized controls using the product’s actual CSS pixels;
- retain screenshots, test output, or exact reproduction steps as evidence.

Do not mutate production data or deploy changes without explicit authorization.

## Text Enlargement and Spacing

Use 200% text enlargement as an important stress point, not the only relevant size.

Look for:

- loss of content or controls;
- severe truncation without a full-value path;
- fixed-height clipping;
- overlapping labels and values;
- off-screen actions;
- broken reading order;
- text rendered inside images;
- controls that scale differently from their labels.

For text-spacing stress, use the WCAG reference values when applicable to the writing system:

- line height at least 1.5 times the font size;
- paragraph spacing at least 2 times the font size;
- letter spacing at least 0.12 times the font size;
- word spacing at least 0.16 times the font size.

The test passes only if content and functionality remain available. It does not by itself establish full WCAG conformance.

## Reflow

Use a narrow viewport around 320 CSS pixels as a common reflow stress point for web content, while respecting documented exceptions and product support.

Check:

- horizontal scrolling required for ordinary text or controls;
- columns that fail to stack or become unusable;
- sticky or fixed elements covering content;
- dialogs, tables, and toolbars with justified two-dimensional scrolling needs;
- zoom combined with a narrow viewport;
- hidden actions or lost context.

Static frames can simulate reflow pressure but cannot prove CSS behavior.

## Hover, Focus, and Touch

Additional content revealed on hover or focus should be:

- dismissible without moving focus when needed;
- hoverable when the pointer must move onto it;
- persistent until the trigger condition ends, the user dismisses it, or it is no longer valid;
- available through keyboard focus when hover triggers it;
- nonessential if presented as a simple tooltip.

Keep focus on the trigger for a tooltip. Use a disclosure, popover, or dialog when the revealed content contains interactive controls.

On touch surfaces:

- do not depend on hover;
- use tap, inline expansion, a disclosure, a bottom sheet, or a justified detail destination;
- verify that tapping a truncated value does not conflict with another action;
- use 24 × 24 CSS pixels as a WCAG minimum target-size reference or document the applicable exception; follow platform or design-system targets when they are larger.

## Reporting Language

Prefer:

- “The static design shows a likely clipping risk at enlarged text.”
- “The rendered interface was verified at 200% browser zoom in the tested viewport.”
- “Keyboard focus reveals the complete value in the tested build.”
- “Screen-reader behavior remains unverified.”

Avoid:

- “This design is accessible.”
- “The component is WCAG compliant” without a scoped conformance evaluation.
- “Mobile users can access the value” when only a desktop hover variant exists.
