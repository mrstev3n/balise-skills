# Content Resilience Contract

Use this reference for Deep tests, component handoff, repeated failures, or requests for persistent documentation.

## Purpose

A content resilience contract records how a component is expected to behave when real data reaches its boundaries. It is a compact specification, not a test log or a substitute for product requirements.

## Contract Fields

### Identity

- component or surface name;
- tested artifact and version when known;
- owner or team when confirmed;
- primary task.

### Role and Criticality

Record:

- the role of each variable content field;
- whether it is decision-critical, identity-critical, comparative, explanatory, or supplementary;
- what the user loses if the value is hidden, ambiguous, or unavailable.

### Provenance

Record whether the value is:

- fixed product copy;
- user-generated;
- server-provided;
- computed;
- localized;
- optional;
- external media.

Name the owner only when confirmed.

### Bounds and Formats

Record:

- known minimum and maximum;
- typical value when useful;
- supported formats, locales, scripts, or units;
- whether a bound is confirmed, inferred, or unknown.

Never convert a test fixture into a business rule.

### Missing, Delayed, and Invalid Data

Specify separately:

- empty but valid;
- absent;
- unknown;
- unavailable;
- loading or delayed;
- invalid;
- redacted;
- error.

Record the visible fallback and whether the user can recover.

### Layout Behavior

Record:

- wrapping and content-driven growth;
- min/max width or height;
- max lines and truncation position;
- reflow or responsive substitution;
- overflow menu, scrolling, disclosure, or detail behavior;
- media crop and fallback when relevant.

### Full-Value Access

Record the behavior for:

- pointer;
- keyboard;
- touch;
- assistive technology when verified.

Do not write “tooltip” as a complete rule. State the trigger, persistence, dismissal, and fallback.

### Localization and Typography

Record:

- priority locales and direction;
- pseudo-localization status;
- regional formatting rules;
- font coverage and fallback;
- expert review still required.

### Acceptance and Remaining Validation

Record:

- observable pass criteria;
- artifacts actually tested;
- confirmed, refuted, or inconclusive hypotheses;
- runtime, accessibility, localization, product, content, engineering, legal, or design-system checks still open.

## Compact Contract Example

```markdown
### Content resilience contract — Transaction row

- Task: identify and compare a transaction before opening details.
- Criticality: merchant is identity-critical; amount and status are comparative.
- Sources: merchant from API; amount computed; status localized.
- Bounds: merchant maximum unknown; amount supports negative values and two decimals.
- Missing behavior: absent merchant becomes “Merchant unavailable”; amount is never replaced by zero.
- Layout: merchant uses one line with end ellipsis; amount never truncates; row grows for enlarged text.
- Full value: merchant revealed on focus/hover; the existing detail view reveals it on touch.
- Locale: test French expansion, Arabic RTL, localized currency, and font fallback.
- Pass: amount and status remain fully visible; merchant stays identifiable; row action remains reachable.
- Remaining: API bound, screen-reader naming, and production bidi isolation.
```

## Finding Record

Use this structure for each material issue:

```markdown
### [Severity] Short finding title

- Location:
- Condition:
- Hypothesis:
- Evidence:
- User impact:
- Recommendation:
- Result: confirmed | refuted | inconclusive
- Evidence level: static | source | runtime | specialist
- Remaining validation:
```

## Persistent Report

When the user requests a saved report, use `assets/content-resilience-report-template.md` as the starting structure. Omit empty sections instead of filling them with speculation.
