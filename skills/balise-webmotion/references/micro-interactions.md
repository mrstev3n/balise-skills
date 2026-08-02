# Micro-interaction catalog

Load this file when designing the micro-interaction stratum of a choreography plan, or when a build needs its small moments systematized.

Think like a curator of micro-interactions: know the patterns, know when each is appropriate — and above all know when to animate nothing. **Restraint is part of quality: everything that moves without reason devalues what moves with reason.**

## Catalog

| Pattern | Effect | When to use | When to abstain |
| --- | --- | --- | --- |
| Magnetic button | Button attracts the pointer within a short radius | Hero CTA, single conversion moment | Dense forms, frequently used interfaces |
| Link underline reveal | Line draws itself under the link on hover | Navigation, editorial body | Almost never contraindicated — nearly always profitable |
| Image reveal mask | Image unveils via animated clip-path | Hero, portfolio, case studies | Repeated purely decorative images |
| Text scramble | Characters scramble then resolve | Tech accents, short state transitions | Body copy, long-read content, untreated accessibility |
| Custom cursor | Pointer replaced or augmented (dot, contextual label) | Immersive experiences, portfolios | Utility products, forms, anywhere native pointer precision matters |
| Preloader as brand moment | Choreographed waiting sequence | Genuinely long loads (3D, video) | Fast sites — a preloader without real need is an anti-pattern |
| Hover distortion | Image reacts (inner scale, material shift) | Portfolio cards, teasers | Long lists, touch-majority usage |
| Toast/notification choreography | Orchestrated entry, stacking, exit | Any product with system feedback | Never let a toast mask critical content |
| Form feedback | Micro-animations for validation, error, success | Every form | Never contraindicated if discreet and fast (< 300 ms) |
| Menu/burger morph | Icon transforms, menu deploys with spatial continuity | Mobile navigation and overlays | Very high-frequency menus — prioritize speed |
| Badge/cart pop | Physical confirmation of an addition | E-commerce, accumulation actions | Destructive actions — never "celebrate" a deletion |

## Application principles

- **A system, not a collection.** All micro-interactions in one project share easing, durations, and feedback logic. Impose consistency, not variety.
- **Frequency decides intensity.** The more frequent an interaction, the faster and more discreet its response (100–300 ms). Spectacular effects are reserved for rare moments.
- **Every micro-interaction ships with its reduced-motion and touch state**, defined in the motion map from the start — not as post-processing.
- **One signature per viewport.** Secondary and ambient layers support it; nothing competes with it.
