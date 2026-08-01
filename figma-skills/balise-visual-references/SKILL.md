---
name: balise-visual-references
description: Recommends visual-reference sources and precise search routes, guides users to collect screenshots or links, and analyzes the returned material into original design principles for Figma work. Use for inspiration, benchmarking, art direction, interface patterns, components, flows, websites, mobile products, brands, decks, and visual systems when the user needs references before or during design.
---

# Visual References for Figma

Guide the user from a design question to a useful reference set, then translate the selected examples into original design decisions. Work entirely from this file and from material the user supplies. Do not assume access to a browser, external connector, MCP, API, or private reference library.

## Operating rule

Separate the workflow into two phases:

1. **Recommend and collect**: propose sources, search terms, and capture instructions; ask the user to visit the sources and attach selected screenshots or links.
2. **Analyze and apply**: inspect only the material supplied in the conversation or available in the Figma file, then derive principles for the current design.

Do not describe a source or reference as inspected until its visual content is actually available. A URL alone may identify provenance but does not prove the current visual state of the page.

## Frame the request

Identify:

- the deliverable: website, mobile app, desktop product, dashboard, brand system, deck, campaign, email, or another surface;
- the target pattern: app bar, navigation, hero, cards, table, form, onboarding, pricing, search, settings, empty state, motion, typography, or another reusable problem;
- the desired granularity: system, page, section, screen, component, flow, interaction, or asset;
- the project context: audience, market, industry, tone, device, content density, accessibility, and technical constraints;
- the decision the references should clarify.

If essential context is missing, ask at most one concise question before recommending sources.

## Recommend a focused route

Choose three to five complementary sources. Favor specialist libraries over general inspiration feeds. For each recommendation, include:

| Source | Why it fits | Starting URL | Search terms or route | What to capture |
| --- | --- | --- | --- | --- |

Use precise queries that combine the product, component, state, and context. Examples:

- `mobile banking bottom navigation active state`
- `B2B SaaS data table bulk actions`
- `editorial mobile app bar scroll behavior`
- `onboarding permission request before after`
- `pricing comparison enterprise SaaS`
- `empty state no results filters dashboard`

Ask for screenshots that retain enough surrounding context to explain the component's role. For motion or flows, request a short recording or a sequence of key states. Three to eight selected references are usually sufficient.

## Source guide

Use this concise directory to shape recommendations. Access and catalog contents can change; present each URL as a starting point, not a guarantee of current availability.

### Interface patterns and flows

- **Mobbin** — https://mobbin.com — mobile and web product screens and flows. Useful for onboarding, navigation, search, checkout, settings, permissions, and state sequences. Search by product category, platform, flow, or UI element.
- **Page Flows** — https://pageflows.com — recorded user flows across web and mobile products. Useful for interaction sequences, onboarding, authentication, checkout, and feature discovery.
- **Interface Index** — https://interface-index.com — B2B, SaaS, and desktop UI patterns. Useful for tables, filters, search, settings, navigation, and dense product interfaces.
- **Chamjo** — https://chamjo.design — regional mobile-product flows. Useful when local-market conventions, payments, delivery, or region-specific product behavior matter.
- **Interface In Game** — https://interfaceingame.com — game UI screenshots and videos. Useful for HUDs, menus, inventories, maps, settings, and gamified systems.
- **Auto Interfaces** — https://www.autointerfaces.com — automotive screens and interaction flows. Useful for dashboards, navigation, vehicle controls, and constrained attention contexts.

### Websites, sections, and conversion patterns

- **Land-book** — https://land-book.com — curated websites and landing pages. Useful for broad web direction, composition, typography, and sector comparison.
- **A1 Gallery** — https://www.a1.gallery — websites, pages, sections, profiles, and fonts. Useful for hero, navigation, layout, typography, and section-level research.
- **SaaS Pages** — https://saaspages.xyz — SaaS landing pages and conversion blocks. Useful for heroes, pricing, social proof, CTAs, and page architecture.
- **BentoGrids** — https://bentogrids.com — modular grid examples across product, web, graphic design, and motion. Useful for card systems, feature presentation, information hierarchy, and brand applications.
- **HOVERSTAT.ES** — https://www.hoverstat.es/archive/ — experimental websites, interaction, typography, and content. Useful when the brief needs less conventional web patterns.
- **Lowww** — https://www.lowww.directory — lightweight websites with low-impact design signals. Useful for restrained visual systems and performance-conscious web direction.

### Brand, editorial, and communication

- **Behance** — https://www.behance.net — broad project-based portfolios. Useful for identity systems, campaigns, packaging, editorial systems, and complete case presentations. Narrow searches by deliverable, sector, region, and year.
- **Rebrand Gallery** — https://www.rebrand.gallery — identity systems, applications, launch stories, and reveal motion. Useful for brand-system breadth and presentation structure.
- **BP&O** — https://bpando.org — editorial analysis of branding and packaging. Useful for understanding rationale and system decisions, not only collecting images.
- **Fonts In Use** — https://fontsinuse.com — real typographic applications. Useful for type pairing, hierarchy, editorial tone, and medium-specific typography.
- **Email Love** — https://emaillove.com — email designs and customer journeys. Useful for lifecycle communication, ecommerce, transactional messages, and dark-mode comparison.

### Motion and speculative interfaces

- **Motionographer** — https://motionographer.com — motion design and animation projects. Useful for title sequences, transitions, brand motion, and audiovisual direction.
- **HUDS+GUIS** — https://www.hudsandguis.com — fictional interfaces from film, television, and product design. Useful for experimental dashboards and speculative art direction; do not treat cinematic UI as production-usability evidence.

## Pattern-specific routes

Choose sources based on the question:

- **App bar or navigation**: Mobbin, Interface Index, Page Flows. Search platform + navigation type + state, then capture default, scrolled, active, overflow, and narrow states.
- **Forms or onboarding**: Mobbin, Page Flows, Chamjo. Capture the complete sequence, validation, permissions, progress, error, and recovery—not one polished screen.
- **Tables, filters, and dashboards**: Interface Index, Mobbin, A1 Gallery. Capture content density, selection, bulk actions, loading, empty, error, and responsive behavior when available.
- **Hero, pricing, or conversion block**: SaaS Pages, A1 Gallery, Land-book. Capture the target section plus adjacent content so hierarchy and narrative remain visible.
- **Cards or modular systems**: BentoGrids, A1 Gallery, Behance. Capture the complete grid and several cards to reveal sizing, repetition, exceptions, and content stress.
- **Brand system**: Rebrand Gallery, Behance, BP&O, Fonts In Use. Capture the system overview, identity rules, applications, typography, and motion rather than isolated logo marks.
- **Motion or interaction**: Page Flows, Motionographer, HOVERSTAT.ES. Request a recording or key-frame sequence with trigger, transition, duration impression, feedback, and end state.

## Request the evidence

End the recommendation phase with a direct handoff:

> Visit the suggested sources, select the references that feel most relevant, then attach three to eight screenshots or links here. Keep the surrounding interface visible; for motion or flows, include a short recording or successive states. I will compare them and translate the strongest ideas into principles for this Figma design.

Do not proceed as if the research were complete when the user has not supplied visual evidence.

## Analyze the returned material

For each supplied reference, report:

1. **Observation** — the visible composition, hierarchy, typography, color, imagery, copy, motion, or interaction.
2. **Principle** — why that choice works in its original context.
3. **Application** — how the principle can serve the current frame, component, flow, or system.
4. **Boundary** — what should not be copied literally and what depends on another audience, brand, content model, platform, or technical context.

Across the full set:

- identify recurring patterns and meaningful disagreements;
- distinguish structural principles from surface style;
- note missing states and evidence;
- rank ideas by relevance to the brief rather than popularity;
- recommend one direction or a small set of genuinely distinct directions.

Static screenshots cannot prove interaction quality, responsiveness, accessibility, implementation behavior, or performance. State these limits when they affect the recommendation.

## Translate insights into Figma work

Convert the analysis into an actionable design brief:

- layout and hierarchy rules;
- component anatomy and variants;
- spacing, density, and alignment principles;
- typography and color roles;
- content and image behavior;
- interaction or state requirements;
- responsive and accessibility questions to resolve;
- originality boundaries.

When asked to design or revise a Figma artifact, apply the approved principles to the selected scope. Preserve the project's components, variables, styles, naming, constraints, and existing visual language. Do not publish or alter shared assets beyond the authorized scope.

Use references as evidence and inspiration, never as templates to reproduce distinctive protected expression, brand assets, copy, or proprietary screens.
