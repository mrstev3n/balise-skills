# Test Library

Use this reference when planning a test matrix, choosing representative values, or limiting combinatorial coverage.

## Contents

- Test profiles
- Content-source risk
- Case families
- Selection algorithm
- Representative combinations
- Synthetic-data rules

## Test Profiles

### Quick

Use for a first pass, a simple component, or a narrow request.

Cover:

1. baseline;
2. plausible minimum;
3. plausible maximum;
4. absent or unavailable value when valid.

Target 3–5 cases per component family.

### Global

Use for international, multilingual, or localized products.

Cover:

- pseudo-expansion;
- a relevant non-Latin writing system;
- RTL composition and a mixed-direction value;
- regional number, currency, unit, date, and time formats;
- font fallback and missing-glyph risk;
- plural-sensitive values beyond singular versus plural.

Read `localization-unicode.md` before generating cases.

### Accessible

Use for dense layouts, mobile, critical content, or accessibility-related requests.

Cover where the available artifact permits:

- text enlargement up to 200%;
- increased text spacing;
- narrow reflow pressure;
- keyboard focus and disclosure;
- touch targets and non-hover alternatives;
- loss of content, meaning, order, or action.

Read `accessibility-runtime.md`. Do not convert a visual simulation into a compliance claim.

### Deep

Use for central, highly variable, repeated, or previously failing components.

Cover:

1. isolated important boundaries;
2. selected two-factor interactions;
3. at most one high-risk three-factor scenario by default;
4. a content resilience contract;
5. remediation alternatives when a failure is confirmed.

### Regression

Use after a repair.

Cover:

- the exact failing case;
- original or typical content;
- the opposite support when relevant, such as desktop and touch;
- related variants affected by shared structure;
- one neighboring boundary likely to expose an overfit correction.

## Content-Source Risk

Prioritize cases using both impact and control over the source.

| Source | Examples | Typical uncertainty |
| --- | --- | --- |
| Fixed product copy | labels, headings, help | wording changes, localization |
| User-generated | names, comments, file names | length, line breaks, scripts, unsafe assumptions |
| Server-provided | statuses, catalog values, totals | missing fields, unknown bounds, delayed values |
| Computed | percentages, durations, aggregates | rounding, sign, overflow, special values |
| Localized | translations, plurals, formats | expansion, grammar, direction, font coverage |
| External media | avatars, uploads, remote images | missing source, ratio, contrast, crop |

Increase test depth when the source is weakly controlled, the value is decision-critical, or the same component is reused widely.

## Case Families

### Length and Structure

- plausible minimum, including a one-character or one-word value only when valid;
- long plausible label or name;
- multi-line description;
- long unbroken URL, identifier, e-mail address, path, hashtag, or token;
- user-entered line breaks;
- repeated or leading/trailing whitespace when the product may preserve it.

Look for clipping, unexpected wrapping, fixed-height failure, displaced actions, unstable alignment, and loss of the distinguishing segment.

### Numbers and Quantities

- 0 and 1;
- a high but plausible value;
- negative value only when valid;
- decimal and rounded value;
- percentage, unit, or currency;
- exact value versus approved abbreviation;
- digit grouping and alternative separators.

Look for alignment, width assumptions, ambiguous units, incorrect sign placement, and semantic changes such as replacing an exact total with `99+`.

### Presence and Data State

Keep these states distinct:

- empty but valid;
- absent or not supplied;
- unknown;
- unavailable;
- redacted or masked;
- delayed or loading;
- invalid;
- error.

Do not use `0`, an empty string, and “Unavailable” interchangeably.

### Locale and Direction

- pseudo-localized expansion;
- long translated form representative of a target locale;
- RTL container and reading order;
- mixed-direction name, number, identifier, URL, or extension;
- locale-specific address or personal name structure;
- plural categories and decimal-sensitive forms.

### Unicode and Typography

- combining marks and diacritics;
- emoji sequences with modifiers or joiners;
- multilingual personal or organization names;
- CJK or other text without Latin-style spaces;
- font fallback with different metrics;
- unsupported glyph or tofu.

### Media

- missing source and fallback;
- portrait, square, landscape, and panoramic ratios when valid;
- very light and very dark imagery under overlays;
- unexpected crop or focal point;
- variable media beside variable text.

### Viewport and Component

- narrow supported viewport;
- resizable side panel or column;
- repeated cards with variable heights;
- dense list or table with mixed lengths;
- component variants using shared internal structure;
- text enlargement combined with content-driven height.

## Selection Algorithm

1. Identify the user task and decision-critical content.
2. Record confirmed bounds and mark unknown bounds.
3. Select the highest-impact family for each variable content role.
4. Add plausible minimum and maximum cases.
5. Add absence or error only when the data model permits it.
6. Test important variables separately before combining them.
7. Choose pairs whose factors plausibly interact.
8. Add at most one three-factor scenario unless broader coverage is requested.
9. Exclude impossible or redundant combinations.
10. Announce the number of cases before generating substantial artifacts.

Do not use pairwise selection as a formal guarantee. It is a canvas and execution budget technique.

## Representative Interactions

High-value pairs often include:

- long text + narrow width;
- long text + text enlargement;
- RTL + numbers;
- RTL + directional icon;
- fallback font + multi-line content;
- missing data + dependent label;
- error state + long recovery instruction;
- variable image + long overlay;
- high numeric value + localized unit;
- deep hierarchy + resizable panel.

A high-risk three-factor case might be:

- RTL + numeric extreme + narrow mobile layout;
- enlarged text + long error + fixed-height component;
- fallback font + long localized label + dense table.

## Synthetic-Data Rules

- Preserve the semantic type and internal coherence of values.
- Make difficult values plausible for the domain.
- Label fabricated values as synthetic in persistent artifacts.
- Never use real personal, client, medical, financial, authentication, or confidential data.
- Do not present invented bounds as product constraints.
- Keep pseudo-localized strings visibly distinguishable from approved translations.
