# Catalog taxonomy

Use facets as intersecting filters. Do not assign a source to one exclusive category.

## Selection model

Translate a request into this sequence:

1. **Deliverable** — what is being designed.
2. **Pattern** — what visual or interaction problem needs references.
3. **Granularity** — whether the useful evidence is a project, system, page, section, screen, component, interaction, or asset.
4. **Format** — whether the source provides screenshots, video, animation, live sites, cases, analyses, flows, or templates.
5. **Context and region** — which market, industry, tone, or cultural frame matters.
6. **Access** — whether browser access is public, partial, account-gated, or subscription-gated and whether an MCP is advertised.

Rank sources by the number and importance of matching facets. Choose complementary sources when one supplies the pattern and another supplies the target medium or strategic context.

## Controlled facets

### Deliverables

- `brand-identity`
- `website`
- `mobile-app`
- `desktop-app`
- `deck`
- `advertising`
- `email`
- `dashboard`
- `ecommerce`
- `game-interface`
- `automotive-interface`
- `film-video`
- `social-content`
- `app-store`

### Granularity

- `project`
- `collection`
- `system`
- `deck`
- `page`
- `section`
- `screen`
- `flow`
- `component`
- `interaction`
- `asset`

### Content formats

- `screenshot`
- `video`
- `animation`
- `live-site`
- `case-study`
- `editorial-analysis`
- `annotated-example`
- `full-flow`
- `template`

### Contexts

- `b2b`
- `saas`
- `ecommerce`
- `corporate`
- `editorial`
- `cultural`
- `luxury`
- `experimental`
- `gaming`
- `automotive`
- `startup`
- `consumer`
- `entertainment`
- `sustainability`
- `regional`
- `international`

### Browser access

- `public` — useful examples can be inspected without an account.
- `partial` — public preview exists, but meaningful depth requires an account.
- `account-required` — the useful library requires sign-in.
- `subscription` — meaningful access requires a paid plan.
- `unstable` — direct browsing may be unreliable or incomplete.

### MCP status

- `none` — no MCP was observed.
- `advertised` — the platform advertises an MCP; current tool availability is not implied.

## Pattern tags

Pattern tags are controlled by the `vocabulary.patterns` array in `source-catalog.json`. Prefer an existing tag. Add a new one only when it expresses a reusable research need that cannot be represented by the current vocabulary.

## Example: cross-medium selection

For “a modular layout for presenting brand applications in a deck,” match:

- deliverables: `brand-identity`, `deck`;
- patterns: `modular-grid`, `brand-application`, `information-design`;
- granularity: `system`, `section`;
- formats: `screenshot`, `case-study`.

This can surface BentoGrids for modular composition, Rebrand for brand applications, and Deck Gallery for presentation adaptation.
