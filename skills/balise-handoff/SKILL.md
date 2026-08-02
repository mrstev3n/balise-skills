---
name: balise-handoff
description: Audits and prepares designs, specifications, prototypes, design-system artifacts, and implemented interfaces for developer handoff using explicit scope, source-of-truth mapping, evidence levels, risk-based gates, open-decision ownership, and acceptance criteria. Use to assess whether a Figma selection or product surface is ready for implementation, improve developer handoff, review Ready for dev claims, assemble a handoff contract, trace design-to-code provenance, or revalidate a design after changes.
---

# Handoff Readiness

Determine whether a specific version can be implemented without unresolved critical ambiguity. Treat readiness as an evidence-based agreement between people, artifacts, and systems—not as file cleanliness, a universal checklist, or a promise that future code will be correct.

## Operating contract

- Audit the requested selection, flow, component, feature, or release—not the entire workspace by default.
- Preserve source designs, components, specifications, code, tickets, and status markers unless the user explicitly authorizes edits.
- Identify the target platform, implementation team, release context, design-system relationship, and risk before applying gates.
- Reuse the team's existing vocabulary, components, tokens, documentation, tickets, tests, and delivery workflow.
- Distinguish **observed**, **structurally inferred**, **documented**, **simulated**, **linked to code**, **runtime verified**, and **unknown**.
- Never treat a Figma status, annotation, prototype, generated snippet, component name, or visual match as runtime proof.
- Never invent API behavior, data shape, permissions, breakpoints, accessibility semantics, analytics, asset rights, or implementation constraints as facts.
- Do not require every dimension mechanically. Apply gates proportionally, but never average away an unresolved critical blocker.
- Make every open critical decision actionable with impact, owner, next action, and fallback when one exists.
- Do not turn handoff into a final ceremony. Prefer evidence produced and maintained throughout product work.

## Choose the mode

Infer the mode from the request. Default to **Audit** when edit intent is absent.

| Mode | Action |
| --- | --- |
| **Audit** | Inspect evidence, apply gates, and issue a readiness verdict without editing. |
| **Prepare** | Add or repair handoff structure, annotations, mappings, links, and decision records after explicit edit intent. |
| **Verify** | Reinspect affected gates after corrections, implementation, or design-system changes. |
| **Contract** | Produce a durable handoff summary from available evidence without changing the source. |
| **Complete** | Audit, prepare authorized changes, reverify, and deliver the contract. |

Audit and Verify are read-only. In a design tool, Prepare should use a labeled handoff area or copy by default. Edit source frames, shared components, status markers, or production code only when the user explicitly requests that mutation.

## Load only the needed references

- Read [readiness-model.md](references/readiness-model.md) when selecting gates, classifying severity, assigning evidence, or deciding the verdict.
- Read [figma-execution.md](references/figma-execution.md) when the source or output includes Figma frames, components, variables, prototypes, annotations, Dev Mode, Code Connect, or MCP context.
- Read [source-of-truth-and-change.md](references/source-of-truth-and-change.md) when design and code disagree, sources are distributed, dependencies changed after handoff, or provenance is unclear.
- Read [implementation-evidence.md](references/implementation-evidence.md) when inspecting code, Storybook, tests, runtime behavior, accessibility, assets, data contracts, or acceptance proof.
- Use [handoff-readiness-contract-template.md](assets/handoff-readiness-contract-template.md) when the user requests a durable readiness report or implementation package.

## Workflow

### 1. Frame the handoff candidate

Establish:

- selected surface and stable artifact link or path;
- exact version, branch, revision, status, or review date;
- included and excluded flows, states, platforms, and viewports;
- intended release, implementation audience, and decision owner;
- user and product goal;
- known design-system, codebase, data, asset, and policy dependencies;
- risk profile and requested outcome.

If scope or version cannot be identified, do not inspect arbitrary nearby work and call it the target. Mark the candidate **Not assessable** until the missing boundary can be resolved.

### 2. Choose a proportional profile

Use the lightest profile that still controls the real risk:

- **Quick:** small, reversible change; colocated team; known implementation; low consequence.
- **Standard:** ordinary feature or component handoff; inspect every dimension and activate applicable gates.
- **Deep:** external or distant team, new platform, wide reuse, migration, money, identity, permissions, sensitive data, safety, security, localization, or consequential accessibility risk.

State the profile and why. A Deep profile changes evidence requirements; it does not justify auditing unrelated surfaces.

### 3. Inspect the real delivery ecosystem

Inspect the selected artifact and relevant adjacent evidence:

- parent flow, alternate branches, states, prototypes, and annotations;
- components, instances, properties, overrides, libraries, variables, modes, styles, tokens, and layout rules;
- product requirements, decisions, tickets, API or data contracts, content sources, asset sources, and analytics requirements;
- canonical code components, routes, state owners, tests, Storybook stories, Code Connect mappings, and release history;
- status, version history, change notes, owners, and communication channel.

Presence is not freshness. A linked ticket may be stale; a matching name may represent a different concept; a clean frame may omit behavior. Record access limitations instead of inferring their contents.

### 4. Map sources of truth

For each critical domain, record:

1. canonical source;
2. version or revision;
3. owner;
4. derived artifacts;
5. transformation or synchronization mechanism;
6. accepted variance;
7. change-notification path.

Domains can include intent, visual composition, component API, tokens, content, data, behavior, accessibility, assets, analytics, and acceptance tests. Do not assume Figma is canonical for every domain, and do not assume runtime behavior defines intended behavior.

### 5. Build the readiness matrix

Evaluate these dimensions proportionally:

1. **Scope, version, and ownership**
2. **Component architecture and design-to-code mapping**
3. **Variables, styles, tokens, themes, and modes**
4. **Layout, responsiveness, reflow, and content-driven sizing**
5. **States, interactions, data, permissions, and recovery**
6. **Content, semantics, accessibility intent, and localization**
7. **Assets, provenance, licensing, export, and production pipeline**
8. **Design decisions, constraints, alternatives, and acceptance criteria**
9. **Links to tickets, specifications, code, documentation, and support**
10. **Change detection, revalidation, and implementation proof**

Mark each applicable gate **Pass**, **Conditional**, **Blocked**, or **Unknown**. Use **Not applicable** only with a short reason. Do not reward quantity of annotations; require the smallest evidence that resolves the implementation decision.

### 6. Assign evidence precisely

Use the scale below per material assertion:

- **E0 — Unknown:** absent, inaccessible, contradictory, or not assessed.
- **E1 — Visible:** shown in a static artifact or representative example.
- **E2 — Structured:** encoded in inspectable properties, variables, layout, schema, or source structure.
- **E3 — Documented:** intent, rule, exception, decision, or criterion is explicit and attributable.
- **E4 — Simulated:** exercised in a prototype or controlled scenario.
- **E5 — Linked:** mapped to a versioned implementation, token source, story, or canonical system artifact.
- **E6 — Runtime verified:** executed and checked in a named environment against a stated criterion.

Higher is not automatically required or universally better. Match the evidence to the claim. Visual hierarchy may be sufficiently evidenced in the design; keyboard behavior generally requires runtime verification.

### 7. Classify findings by consequence

- **Critical blocker:** guessing could create irreversible action, data loss, security or privacy exposure, inaccessible completion, financial error, broken core flow, incompatible architecture, or release-scope failure.
- **Major condition:** implementation can begin only with an explicit owner, deadline, rule, or fallback.
- **Minor improvement:** clarification reduces rework but does not block safe implementation.
- **Observation:** useful context with no required change.

For every blocker or condition, state:

- observed evidence and missing evidence;
- implementation consequence;
- affected surface and dependency;
- proposed owner;
- smallest next action;
- acceptable fallback, if one exists;
- gate to reverify.

### 8. Decide the verdict

Issue one verdict:

- **Ready:** no unresolved critical blocker; required gates have adequate evidence; residual unknowns fit normal implementation collaboration.
- **Ready with conditions:** implementation can begin because each material open issue has an explicit condition, owner, timing, and safe fallback or bounded impact.
- **Not ready:** a critical decision would need to be guessed or an essential dependency is unresolved.
- **Not assessable:** scope, version, context, or access is insufficient for an honest audit.

Do not calculate readiness as a universal percentage. Counts by severity may support prioritization, but the highest unresolved applicable risk controls the verdict.

### 9. Prepare authorized improvements

When edit intent is explicit:

- encode relationships structurally before adding explanatory text;
- reuse existing components, properties, tokens, modes, layout rules, and documentation conventions;
- add annotations only for intent, behavior, exception, accessibility, or dependency that structure cannot express;
- link canonical tickets, specifications, stories, code, assets, and decisions;
- remove obsolete or distracting handoff artifacts only when their status is verified and deletion is authorized;
- preserve before/after evidence and avoid detaching instances or creating a parallel design system;
- record decisions during the work, not only at the end.

After preparation, reinspect affected gates. A created annotation is not a pass until it resolves the ambiguity and is consistent with the artifact.

### 10. Revalidate changes

When the design, library, variables, styles, code, data contract, or requirements change:

1. identify the changed source and dependent artifacts;
2. classify the impact as cosmetic, content, behavioral, structural, contractual, or critical;
3. invalidate only affected evidence;
4. notify or identify the relevant owners;
5. replay affected gates and acceptance criteria;
6. update the contract and residual risks.

Do not rely on a single design-tool status to detect dependency changes.

### 11. Deliver the handoff contract

Return a concise decision surface containing:

1. scope, version, profile, and mode;
2. verdict and short rationale;
3. source-of-truth map;
4. passed gates and their strongest relevant evidence;
5. blockers, conditions, unknowns, owners, and actions;
6. implementation notes and accepted variance;
7. acceptance criteria and verification environment;
8. change and revalidation protocol;
9. residual risk and explicit non-claims.

Link directly to artifacts and tests. Separate what is ready for implementation from what remains a proposal.

## Decision rules

### Structure before annotation

Use native properties, layout rules, variables, schemas, and component APIs to express repeatable behavior. Use annotations for rationale, exceptions, cross-system mappings, and behavior outside the artifact. Do not annotate every pixel.

### Intent before literal translation

Clarify non-negotiables, acceptable variance, and user outcome. Generated snippets and visual dimensions are inputs, not production architecture. Prefer existing code components and conventions over recreating the design literally.

### Representative use before isolated polish

Inspect components in product context, with representative content and meaningful variations. An isolated perfect component does not prove page-level composition, data resilience, or flow completeness.

### Accessibility claims require the right surface

Static artifacts can express intended reading order, labels, focus sequence, contrast, and behavior. They cannot prove semantics, keyboard operation, announcements, zoom, reflow, or assistive-technology behavior in production.

### Source disagreement is a decision, not a cleanup task

When design, code, and documentation differ, identify the domain owner and intended canon. Do not silently force one artifact to match another or call the newest timestamp correct.

## Boundaries with adjacent skills

- Use `complete-ui-states` to model missing states and recovery paths. Handoff Readiness records whether required state evidence exists.
- Use `content-stress-test` for systematic content variability, overflow, localization, and truncation resilience.
- Use `ux-writing` for comprehensive interface copy, voice, terminology, and content-system work.
- Route autonomy, material disclosure, consent, reversibility, or deceptive-pattern risks to a dedicated trustworthy-flow review.
- Use accessibility, security, or legal specialists when the verdict depends on their domain. Do not claim certification from this skill.

## Completion standard

Finish only when:

- scope, version, platform, profile, and intended audience are explicit;
- applicable gates are justified and evidence levels are honest;
- canonical sources and material divergences are mapped;
- no critical ambiguity is hidden by a score, status, or tidy file;
- each blocker and condition has a consequence and next action;
- mutation stayed within authorization and source artifacts were preserved;
- acceptance proof is observable and proportional to the claim;
- the verdict distinguishes design intent, linked implementation, and runtime verification;
- change and residual risk remain visible after the handoff.
