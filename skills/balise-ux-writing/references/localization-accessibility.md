# Localization and Accessibility Writing

Use this reference for translation, multilingual products, internationalization, inclusive language, visible accessibility review, and implemented accessibility checks.

## Contents

- Localization workflow
- Translatable structure
- Expansion and layout
- Accessible wording
- Static versus runtime evidence
- High-risk boundaries

## Localization Workflow

Before translating or reviewing localized copy:

- identify source locale and target locale;
- inspect the complete screen, state, and action;
- preserve variables, ICU syntax, markup, and placeholders;
- identify glossary terms, product names, and do-not-translate tokens;
- determine formality, grammatical person, gender, number, and regional convention;
- check whether the target market uses different formats, examples, addresses, or legal wording;
- separate layout pseudo-localization from linguistic validation.

Translate intent and function, not word order. Do not claim native or legal quality without qualified review.

## Translatable Structure

- Avoid concatenating fragments that translators must reorder.
- Give complete sentences or complete functional labels to the localization system.
- Include contextual descriptions for ambiguous keys.
- Support plural and grammatical variants required by the locale.
- Keep variables semantically named and stable.
- Do not embed punctuation or prepositions outside a string when their placement can vary.
- Avoid relying on capitalization to communicate hierarchy; capitalization rules differ by locale.
- Treat names, addresses, dates, times, numbers, currencies, and units as structured data rather than English-shaped strings.

## Expansion and Layout

Check:

- buttons, tabs, navigation, dialogs, tables, cards, and narrow mobile surfaces;
- text wrapping and content-driven height;
- truncation that removes the action or consequence;
- font support and fallback for target scripts;
- RTL order, alignment, and directional icons;
- mixed-direction values such as URLs and identifiers;
- text enlargement and user-controlled spacing.

Do not shorten a translation merely to preserve a fragile layout. Determine whether layout, hierarchy, or content can adapt without losing meaning.

## Accessible Wording

### Labels and Names

- Give controls a meaningful visible label when possible.
- Make link and action wording understandable outside surrounding prose.
- Give icon-only actions an explicit textual name in implementation.
- Keep the visible label and accessible name aligned enough to support voice input.
- Avoid duplicate accessible names when adjacent actions do different things.

### Instructions and Errors

- Do not rely only on color, position, shape, sound, or an icon.
- Refer to a field or action by name rather than only “above”, “red”, or “on the right”.
- Place requirements before input when possible.
- Make correction and recovery specific.
- Keep error text associated with the affected input in implementation.

### Status and Dynamic Feedback

- Use wording that accurately distinguishes progress, completion, failure, and queueing.
- Avoid repeated announcements for routine updates.
- Identify the affected object when context is not obvious.
- Verify live-region behavior in runtime rather than inferring it from visible copy.

### Cognitive Accessibility

- Keep sentences and choices concrete.
- Avoid unnecessary memory demands and unexplained abbreviations.
- Keep recurring labels stable.
- Break complex procedures into meaningful steps.
- Explain irreversible or high-risk consequences before the action.
- Avoid time pressure unless it is real and necessary.

## Static Versus Runtime Evidence

From a static design or screenshot, report visible risks such as:

- missing visible label;
- vague link text;
- information conveyed only by color;
- likely clipping or poor expansion;
- absent visible recovery;
- inconsistent heading or instruction hierarchy.

Do not certify:

- accessible names;
- semantic roles;
- DOM or focus order;
- keyboard behavior;
- live regions;
- screen-reader output;
- language and direction metadata.

When source or runtime is available, inspect and test those properties explicitly.

## High-Risk Boundaries

- Do not simplify away consent scope, price, privacy effect, eligibility, safety, or legal qualification.
- Do not translate legal or regulated content as final without appropriate review.
- Do not turn uncertainty into certainty for clarity.
- Do not use inclusive language to conceal a real product limitation.
- Record where localization, accessibility, legal, policy, or domain expertise remains required.
