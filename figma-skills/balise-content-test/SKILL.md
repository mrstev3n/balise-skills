---
name: balise-content-test
description: Stress-tests selected Figma screens, frames, and components with difficult but realistic content and data. Use to audit, generate, or repair resilience cases involving text length, missing values, numeric extremes, localization, RTL, Unicode, text enlargement, variable media, narrow layouts, wrapping, truncation, and content-driven component behavior while preserving source designs and design-system conventions.
---

# Balise Content Test

Work as a content resilience tester inside the current Figma file. Replace ideal placeholder content with difficult but plausible content, observe what fails, propose the smallest durable correction, and preserve a visible trace of the test.

Treat content as any variable data rendered by the interface: text, names, identifiers, numbers, dates, currencies, units, statuses, missing or partial values, user-generated input, localized strings, and externally supplied media.

## Protect the Source

- Treat the selected layers, frames, component sets, or section as the working boundary.
- If neither the selection nor the prompt identifies a testable scope, ask the user to select one.
- Inspect parents, nearby states, related components, properties, variables, annotations, and layout conventions when useful. Do not edit them unless authorized.
- Never stress-test directly on source frames. Create clearly labeled duplicates.
- If duplication or editing is unavailable, perform a read-only audit and state the limitation.
- Preserve components, instances, variants, properties, bindings, styles, constraints, guides, and Auto Layout whenever possible.
- Do not detach instances, flatten layers, replace design-system components, or modify shared library assets without explicit authorization.
- Use synthetic data only. Never insert personal, confidential, financial, health, authentication, research, or client data.
- Do not claim production behavior, accessibility compliance, translation quality, or user comprehension from a static Figma test.

## Determine the Mode

- **Audit**: inspect and report risks without changing the canvas.
- **Test**: create labeled test copies and diagnose them. Use this by default for “stress-test”.
- **Repair**: repair confirmed failures only in the authorized selection.
- **Test and repair**: generate cases, diagnose, repair the copies, then re-test.

When edit intent is unclear, default to Audit.

## Follow the Evidence Workflow

### 1. Frame the Test

Determine from visible evidence and the prompt:

1. the selected surface and primary task;
2. the content roles and information needed for that task;
3. whether each value is fixed, user-generated, provided by a service, localized, computed, optional, or external media;
4. known device sizes, locales, writing directions, currencies, formats, and text-size expectations;
5. components, variants, variables, styles, layout rules, and existing test conventions;
6. confirmed limits such as maximum lengths, numeric ranges, and accepted formats;
7. unknowns that must remain assumptions or implementation questions.

Ask one concise question only when the answer materially changes the test. Never invent a product constraint.

### 2. Form Testable Hypotheses

For each meaningful family, write:

> Given [condition], [element] may [observable failure], affecting [task or information]. The test passes if [observable result].

Use each hypothesis to justify the test frames. Do not generate arbitrary strings.

### 3. Inspect the Baseline

- Read complete frames, not isolated text layers.
- Distinguish copy, data, annotations, sample content, tokens, and layer names.
- Identify fixed dimensions, hidden overflow, resizing, max lines, wrapping, Hug contents, Fill container, min/max dimensions, padding, gaps, alignment, and constraints.
- Check current truncation and access to complete values.
- Record baseline defects before introducing stress content.
- Identify decision-critical information and primary actions that must remain available.

### 4. Select a Proportional Profile

| Profile | Use when | Coverage |
| --- | --- | --- |
| **Quick** | First pass or simple component | baseline, plausible minimum, plausible maximum, absent value |
| **Global** | International or localized product | pseudo-expansion, non-Latin writing, RTL, regional formats, font fallback |
| **Accessible** | Dense, mobile, or critical content | text enlargement, increased spacing, narrow reflow, focus reveal, touch |
| **Deep** | Central, highly variable, or fragile component | isolated boundaries, selected interacting pairs, one high-risk compound case |
| **Regression** | After repair | failing case, original content, opposite support, one neighboring case |

Announce the profile and estimated number of frames. Use the smallest set capable of confirming or refuting the hypotheses.

### 5. Build the Case Matrix

Select only relevant families:

| Family | Representative cases |
| --- | --- |
| Length | minimum, long plausible text, multiline, unbroken token |
| Numbers | 0, 1, high value, decimals, sign, unit |
| Presence | absent, partial, unknown, unavailable, redacted |
| State | loading, error, stale or delayed when represented |
| Locale | pseudo-expansion, regional formats, non-Latin script |
| Direction | RTL layout, mixed-direction value, directional icon |
| Unicode | combining marks, emoji sequence, mixed scripts, no-space text |
| Typography | fallback font, missing glyph, taller metrics |
| Media | absent, portrait, landscape, very light, very dark |
| Viewport | narrow supported frame, variable panel width |
| Component | variable heights, dense list, repeated instances |

Test important boundaries separately before combining them. Then choose likely interactions such as long + narrow, RTL + numbers, enlarged text + error, or fallback font + multiline. Add at most one three-factor case unless broader coverage is requested.

## Generate Honest Stress Content

- Use difficult but plausible values, not lorem ipsum or repeated characters.
- Preserve the semantic role of every field and keep related values coherent.
- Label fabricated values as synthetic.
- Test plausible minimums as well as maximums.
- Keep zero, empty, unavailable, unknown, redacted, loading, and error distinct.
- Do not shorten content merely to force a passing result.

For localization tests:

- use visibly delimited, expanded, and accented pseudo-content;
- include a non-Latin sample when the product is international;
- test RTL composition separately from mixed-direction strings containing names, identifiers, URLs, numbers, or extensions;
- inspect punctuation, reading order, alignment, directional icons, font fallback, and grapheme-safe truncation;
- test relevant dates, times, currencies, units, separators, signs, ranges, and plural-sensitive values;
- label pseudo-content as layout test data, never as approved translation.

For variable media, test missing content and fallback behavior first. When relevant, also test portrait, landscape, unusually light, unusually dark, and low-detail media; inspect cropping, focal point, overlay contrast, and readability.

## Apply Content Criticality

- **Decision-critical**: price, fee, consent, consequence, permission, error, recovery, legal or safety information, and action label. Keep fully available.
- **Identity-critical**: person, file, organization, path, reference, account, or identifier. Preserve the distinguishing part and access to the full value.
- **Comparative**: values compared across rows, plans, or options. Preserve comparison and alignment.
- **Explanatory**: descriptions and guidance. Wrapping, controlled clamping, and persistent expansion may be appropriate.
- **Supplementary**: nonessential clarification. A tooltip may be suitable when accessible from pointer and keyboard.

Judge severity by consequence, not by the mere presence of long content.

## Create the Test Area

When editing is authorized, create a section adjacent to the source named:

`Content Test — [selection name] — [profile]`

Within it:

1. retain an unmodified reference copy when useful;
2. group cases by hypothesis;
3. create one duplicate per selected case;
4. preserve source dimensions unless testing a supported viewport;
5. label every frame with family and condition;
6. annotate assumption, synthetic-data status, expected behavior, observation, severity, and result;
7. arrange cases consistently without covering existing work.

Prefer instance overrides and reuse existing properties, variables, modes, components, and test patterns. Do not build new infrastructure for a one-off test.

## Diagnose Each Material Issue

Record:

- **Severity**: Blocker, Major, or Minor;
- **Location**: exact frame, component, or visible layer;
- **Condition**: content, locale, size, direction, or media trigger;
- **Evidence**: the visible failure;
- **Impact**: task, decision, information, or comparison affected;
- **Recommendation**: smallest durable correction;
- **Result**: confirmed, refuted, or inconclusive;
- **Remaining validation**: behavior Figma cannot prove.

Use these severity rules:

- **Blocker**: essential content or action becomes inaccessible, unreadable, misleading, or impossible to complete.
- **Major**: important hierarchy, information, comparison, or interaction clarity degrades materially while the task remains possible.
- **Minor**: visual quality or scanability degrades without obscuring meaning or action.

## Choose a Durable Correction

Compare solutions in this order:

1. **Absorb**: wrapping, Auto height, Hug contents, Fill container, min/max dimensions, flexible tracks.
2. **Reorganize**: stack, reflow, grid, hierarchy, density, adjustable panel, or overflow grouping.
3. **Truncate**: only with an explicit rule, noncritical loss, a preserved distinguishing segment, and reliable full-value access.
4. **Reveal**: persistent expansion, disclosure, popover, menu, detail view, or accessible tooltip.
5. **Annotate**: document intended runtime behavior and unresolved questions.

Never use smaller text, compressed spacing, hidden data, or a shorter fabricated label as the first correction. Never rely on hover alone for required information; provide keyboard and touch access appropriate to the product.

## Map Corrections to Figma

- Use Auto Layout direction, wrapping, gaps, padding, alignment, Hug contents, Fill container, and content-driven growth.
- Use min/max dimensions to define a flexible envelope without inventing product limits.
- Choose text resizing and max lines according to content criticality.
- Test constraints by resizing the actual parent.
- Reuse component properties and variants for meaningful states without detaching instances.
- Reuse variables and modes for locales or test values when the file architecture supports them.
- Create prototype interactions only when they can be checked; otherwise prepare states and annotate the intended connection.

## Simulate Accessibility Stress Carefully

When the Accessible profile applies:

- create a representative text-enlargement case up to 200%;
- simulate increased text spacing where Figma permits meaningful comparison;
- test a narrow frame approximating reflow pressure;
- verify that content does not overlap, disappear, become ambiguous, or require hover alone;
- represent pointer, keyboard focus, and touch alternatives for disclosure patterns.

Report these as design-level tests. Runtime zoom, CSS reflow, semantics, focus order, keyboard behavior, accessible names, screen-reader announcements, and actual target dimensions require implementation testing.

## Repair and Re-test

Repair only when authorized, in generated copies by default. After each correction:

1. reapply the exact failing content;
2. recheck the original content;
3. test the opposite support when relevant, such as desktop versus touch;
4. check related variants if shared structure changed;
5. verify that meaning, hierarchy, actions, and bindings remain intact;
6. keep unresolved cases visible and labeled.

If the same failure appears across instances, prepare a proposed component-level correction in the test area, but do not change a shared component without authorization.

## Add a Content Resilience Contract

For Deep tests, component-level findings, or handoff requests, record:

| Field | Content |
| --- | --- |
| Role and criticality | purpose and cost of information loss |
| Provenance and owner | user, service, localization, computation, content team, or other source |
| Known bounds | confirmed minimum, maximum, formats, and unknown limits |
| Missing or invalid behavior | fallback, unavailable state, masking, delay, or error |
| Layout behavior | wrap, growth, reflow, max lines, overflow, responsive change |
| Full-value access | pointer, keyboard, and touch behavior |
| Locale, direction, and font | supported or priority cases and fallback |
| Remaining validation | engineering, accessibility, localization, content, legal, or product check |

Never turn an assumption into a specification.

## Report Completion

End with a concise summary of the tested selection, mode, profile, hypotheses, cases, issue counts by severity, repairs, results, assumptions, remaining runtime checks, and location of the test section or resilience contract.

If no issue is found, report which cases passed. Say that the selected design passed those cases, not that the product is universally resilient.
