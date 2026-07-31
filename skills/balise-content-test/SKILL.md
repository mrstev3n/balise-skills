---
name: balise-content-test
description: Stress-tests UI content resilience across design files, screenshots, prototypes, source code, and rendered interfaces. Use when auditing, generating, repairing, or regression-testing difficult but realistic content and data cases involving length, missing values, numeric extremes, localization, RTL, Unicode, font fallback, text enlargement, variable media, narrow layouts, wrapping, truncation, disclosure, or content-driven component behavior. Preserves source artifacts and product meaning, distinguishes static evidence from runtime proof, and can produce content resilience contracts for design and engineering handoff.
---

# Content Stress Test

Test how an interface behaves when ideal placeholder content is replaced by difficult but plausible content and data. Start from a risk, isolate important variables, observe the effect, repair only when authorized, and re-test with evidence appropriate to the artifact.

Treat content as any variable data rendered by the interface: text, names, identifiers, numbers, dates, currencies, units, status values, missing or partial values, user-generated input, localized strings, and externally supplied media.

## Protect Scope and Evidence

- Treat the user’s selected files, frames, components, routes, pages, screenshots, or URLs as the working boundary.
- Inspect surrounding context when required to understand behavior, but do not edit outside the authorized scope.
- When the user asks to review, audit, explain, or diagnose, make no product or design changes.
- When testing a design artifact, preserve the source and create labeled duplicates when editing is available.
- When testing code, preserve existing architecture, component contracts, design-system conventions, localization bindings, and unrelated user changes.
- Do not modify shared components, published libraries, production systems, data, or deployments without explicit authorization.
- Use synthetic values. Never introduce real personal, confidential, medical, financial, authentication, research, or client data.
- State the evidence level for conclusions. Do not infer runtime, accessibility, localization, or user-understanding proof from a static artifact.
- Do not invent product limits, supported locales, fallback behavior, policies, or implementation guarantees.

## Load the Relevant References

Read only the references needed for the request:

- Read [test-library.md](references/test-library.md) when choosing profiles, cases, data sources, or compound scenarios.
- Read [localization-unicode.md](references/localization-unicode.md) for pseudo-localization, plurals, regional formats, RTL, mixed-direction content, Unicode, or font fallback.
- Read [accessibility-runtime.md](references/accessibility-runtime.md) for the Accessible profile, browser verification, zoom, reflow, focus, keyboard, hover, touch, or accessibility claims.
- Read [remediation-patterns.md](references/remediation-patterns.md) before repairing or recommending overflow, disclosure, responsive, or component patterns.
- Read [resilience-contract.md](references/resilience-contract.md) for Deep tests, handoff, repeated component failures, or persistent reporting.

When the user requests a saved report, use [content-resilience-report-template.md](assets/content-resilience-report-template.md). Do not create a report file when a concise conversational result is sufficient.

## Determine the Mode

Infer the requested mode:

- **Audit**: inspect and report risks or visible failures without changing artifacts.
- **Test**: create or run representative stress cases and diagnose the results.
- **Repair**: correct confirmed issues in the authorized artifact.
- **Test and repair**: test, diagnose, repair, and regression-test.

Default to Audit when edit intent is unclear. Testing may produce temporary local artifacts only when they are necessary, safely scoped, and within the request.

## Identify the Evidence Surface

Classify what is actually available:

| Surface | Inspect | Valid conclusions |
| --- | --- | --- |
| Static design or screenshot | geometry, hierarchy, visible states, annotations | visible failure or design-level risk |
| Editable design | components, properties, variables, Auto Layout, test copies | static behavior and intended interaction |
| Source code | layout rules, formatter use, semantics, fixtures, breakpoints | implementation structure and likely behavior |
| Rendered interface | actual content, viewports, zoom, focus, hover, keyboard, disclosure | observed runtime behavior in tested conditions |
| Specialist evaluation | assistive technology, translation, legal or domain review | only the specialist’s verified scope |

Use the highest evidence level safely available and relevant to the request. Do not require a live application when the user only wants a design audit.

## Follow the Workflow

### 1. Establish Context

Determine:

1. the primary user task and decision points;
2. variable content roles and their provenance;
3. known device sizes, breakpoints, locales, direction, currencies, date formats, and text-size expectations;
4. component, design-system, localization, and data conventions;
5. confirmed bounds and valid missing, loading, error, or redacted states;
6. the artifacts and tools available for verification;
7. unknowns that must remain assumptions or questions.

Inspect visible or repository evidence before asking. Ask one concise question only when the answer would materially change scope, validity, or safety.

### 2. Form Hypotheses

For each meaningful risk, define:

> Given [source or condition], [element] may [observable failure], affecting [task or information]. The test passes if [observable result].

Do not generate cases without a reason. A long string is a condition, not a finding.

### 3. Inspect the Baseline

Before introducing stress:

- read complete screens or components rather than isolated strings;
- distinguish product copy, dynamic data, sample values, annotations, and source tokens;
- identify fixed dimensions, clipping, hidden overflow, line clamps, flex or grid behavior, constraints, and content-driven sizing;
- locate component properties, variants, variables, translation keys, formatters, and existing fixtures;
- identify current truncation and the path to the full value;
- record baseline defects so they are not attributed to the stress case;
- identify decision-critical information and primary actions.

### 4. Choose a Profile and Budget

Choose `Quick`, `Global`, `Accessible`, `Deep`, or `Regression` using `test-library.md`.

Before generating substantial artifacts, state:

- selected profile;
- hypotheses;
- approximate case or frame count;
- evidence surface;
- explicit non-goals.

Do not run every profile by default.

### 5. Generate Representative Cases

- Use difficult but plausible synthetic values.
- Preserve semantic type and internal coherence.
- Include plausible minimum and maximum boundaries.
- Keep empty, absent, unknown, unavailable, redacted, loading, invalid, and error distinct.
- Test important factors separately before selecting compound scenarios.
- Label pseudo-localized content as structural test data, not translation.
- Never shorten valid content merely to force a pass.
- Avoid exhaustive permutations. Select interactions whose factors can plausibly amplify one another.

### 6. Execute According to the Artifact

#### Static or Editable Design

- Preserve source frames and use labeled test copies.
- Reuse existing components, properties, variables, modes, styles, and layout conventions.
- Group cases by hypothesis and annotate assumptions, expected behavior, observed behavior, severity, and result.
- Do not create a new variable architecture for a one-off test unless requested.
- When interaction cannot be verified, prepare states and annotate the intended connection rather than claiming it works.

#### Source Code

- Find existing fixtures, stories, visual tests, locale setup, and component tests before creating new infrastructure.
- Prefer the project’s established testing surface, such as component stories, test routes, local fixtures, or browser tests.
- Make test data easy to remove or clearly separate from production data.
- Do not weaken validation, types, translations, or semantics to inject a case.
- In Audit mode, inspect and report without editing source.

#### Rendered Interface

- Establish a reproducible baseline before interaction.
- Test only authorized local, preview, or safe environments.
- Exercise relevant viewport, zoom, text-spacing, focus, pointer, keyboard, touch, locale, and data conditions.
- Capture exact reproduction steps, screenshots, computed behavior, or test output proportional to the risk.
- Do not mutate real user data, submit consequential forms, or publish changes without authorization.

### 7. Diagnose Observable Effects

Record material findings with:

- **Severity**: Blocker, Major, or Minor;
- **Location**: exact artifact, frame, component, file, route, or layer;
- **Condition**: triggering value, locale, direction, viewport, state, or media;
- **Evidence**: what was visibly or technically observed;
- **Impact**: task, decision, comparison, or information affected;
- **Recommendation**: smallest durable correction;
- **Result**: hypothesis confirmed, refuted, or inconclusive;
- **Evidence level**: static, source, runtime, or specialist;
- **Remaining validation**: checks not yet proven.

Severity rules:

- **Blocker**: essential content or action becomes inaccessible, unreadable, misleading, or impossible to complete.
- **Major**: important information, hierarchy, comparison, or interaction clarity degrades materially while the task remains possible.
- **Minor**: visual quality or scanability degrades without obscuring meaning or action.

Do not inflate severity and do not report length alone as a defect.

### 8. Repair Only When Authorized

Read `remediation-patterns.md` before choosing a correction.

Prefer:

1. existing component, design-system, or localization behavior;
2. wrapping and content-driven sizing;
3. reflow, hierarchy, or structured overflow;
4. explicit truncation with a reliable path to the complete value;
5. a component-level proposal when the defect repeats.

Avoid smaller typography, compressed spacing, hidden data, fabricated shorter copy, detached components, or unrelated redesign.

If a repair affects a shared component, published asset, public API, data model, or broad product behavior, explain the impact and obtain authorization before applying it.

### 9. Re-test

After repair:

- rerun the exact failing case;
- recheck original or typical content;
- test the opposite support when relevant;
- check related variants or call sites affected by shared structure;
- verify essential content, actions, semantics, bindings, and hierarchy;
- run proportional existing tests, type checks, builds, or browser checks;
- preserve unresolved cases and report unverified risk.

### 10. Create a Resilience Contract When Valuable

Use `resilience-contract.md` when:

- the user requests handoff documentation;
- the same component is reused broadly;
- a Deep test exposes product constraints;
- a repeated defect requires a design-system decision;
- design and engineering need a shared overflow or fallback rule.

Record content role, provenance, known bounds, missing behavior, layout behavior, full-value access, localization/font requirements, acceptance criteria, and remaining validation. Mark inferred and unknown facts explicitly.

## Respect High-Risk Content

- Preserve the visibility and meaning of prices, fees, consent, privacy, security, permissions, deletion, medical information, legal terms, and recovery instructions.
- Do not truncate, visually demote, or transiently reveal information required for an informed decision.
- Do not fabricate legal requirements, product policies, accessibility claims, supported locales, or engineering guarantees.
- Escalate substantive content changes to the appropriate product, content, localization, accessibility, legal, security, or engineering owner.

## Report Completion

End with:

1. scope, mode, profile, and evidence level;
2. cases created, inspected, or executed;
3. issue counts by severity;
4. repairs and files or frames changed, if any;
5. regression checks performed;
6. hypotheses confirmed, refuted, or inconclusive;
7. assumptions and remaining validation;
8. location of generated artifacts or the resilience contract.

If no material issue is found, report the cases that passed. Say the tested artifact passed those conditions, not that the product is universally resilient.

## Example Requests

- “Audit this React table for content resilience using its existing Storybook stories; do not change code.”
- “Run a Global stress profile on the selected Figma components with pseudo-localization, RTL, regional formats, and font fallback.”
- “Test this local checkout at 200% zoom and narrow widths, then repair confirmed Blocker and Major issues.”
- “Generate synthetic fixtures for long names, missing metadata, numeric extremes, and mixed-direction identifiers.”
- “Regression-test the repaired component and produce a content resilience contract for handoff.”
