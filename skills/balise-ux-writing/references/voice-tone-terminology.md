# Voice, Tone, Terminology, and Governance

Use this reference for voice systems, tone decisions, terminology audits, harmonization, style guidance, and content ownership.

## Contents

- Voice and tone
- Terminology decisions
- Plain and inclusive language
- Content hierarchy
- Governance and source of truth
- Decision records

## Voice and Tone

Treat voice as the product’s stable character and tone as its adjustment to context and stakes.

Use evidence in this order:

1. approved voice and style guidance;
2. established high-quality product patterns;
3. terminology and tone already used consistently in the flow;
4. a conservative neutral default when no system exists.

Do not invent a new brand personality during a scoped rewrite.

Typical tone calibration:

- low-stakes onboarding or success: warm and encouraging;
- routine action or settings: neutral and concise;
- waiting or uncertainty: informative and measured;
- user-correctable error: calm, direct, and actionable;
- system failure: accountable without false promises;
- privacy, security, payment, deletion, or data loss: serious and explicit.

Avoid humor, idioms, slang, exclamation, or anthropomorphism when they could obscure risk, translate poorly, or blame the person.

## Terminology Decisions

Before harmonizing:

- identify the underlying object, action, state, and destination;
- distinguish genuine product differences from accidental synonyms;
- locate the authoritative term in requirements, design system, domain model, API, or content guidance;
- inspect where each competing term appears;
- determine whether changing it affects training, support, legal text, URLs, analytics, or external documentation.

Prefer:

- one stable noun per product object;
- one verb per recurring action;
- one progression vocabulary per flow;
- distinct words for distinct consequences;
- user language over internal architecture when accuracy is preserved.

Do not force uniformity when terms represent different operations, permissions, states, or scopes.

## Plain and Inclusive Language

- Prefer familiar, concrete words and active constructions.
- Put the most useful information early.
- Use one instruction or decision at a time.
- Keep parallel choices grammatically parallel.
- Address the person directly when helpful.
- Avoid using “we” to obscure who acts or who is responsible.
- Avoid assumptions about gender, family, ability, culture, location, literacy, device, or motivation.
- Avoid idioms and metaphors that lose meaning across cultures.
- Use domain terms when the audience needs precision; explain them when unfamiliarity is plausible.
- Preserve respectful self-identification and user-provided names.

Plain language does not mean removing necessary detail or legal precision.

## Content Hierarchy

For each screen or component, establish:

1. orientation: where the person is;
2. purpose: why this moment exists;
3. decision or input: what is required;
4. action: what can happen next;
5. feedback and recovery: what happened and how to continue;
6. supporting detail: what can be deferred.

Remove duplication only when the remaining hierarchy still communicates the task, consequence, and recovery.

## Governance and Source of Truth

When work crosses several surfaces:

- identify canonical copy, translation key, glossary, content schema, or design-system pattern;
- separate source strings from generated bundles and snapshots;
- record ownership when known;
- preserve identifiers even when visible wording changes;
- avoid bulk replacements without reviewing context-sensitive uses;
- note content debt that cannot be fixed safely in the current scope;
- distinguish a proposed standard from an approved standard.

Use a terminology decision record for systemic changes:

```markdown
### Terminology decision

- Concept:
- Preferred term:
- Rejected alternatives:
- Functional distinction:
- Evidence:
- Affected surfaces:
- Exceptions:
- Owner or approval needed:
```

## Decision Quality

A useful content decision states:

- the user task and moment;
- the wording or pattern selected;
- why it is more accurate or usable;
- what tradeoff it accepts;
- which evidence supports it;
- what remains to validate.

Do not present personal preference as a design rule.
