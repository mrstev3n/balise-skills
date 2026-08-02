# Source of truth and change

Use this reference when sources disagree, provenance is unclear, or a previously assessed handoff has changed.

## Contents

1. Domain-specific canon
2. Provenance map
3. Resolving disagreement
4. Change impact
5. Revalidation protocol

## 1. Domain-specific canon

A product rarely has one universal source of truth. Name the canonical source per decision domain.

| Domain | Possible canonical source |
| --- | --- |
| Product intent and scope | approved requirement, decision record, release plan |
| Visual composition | selected Figma revision or design-system guidance |
| Component behavior | published code component, specification, or agreed design contract |
| Tokens | versioned token source or transformation repository |
| Content | CMS, content system, localization source, or approved copy deck |
| Data | API schema, database contract, fixture definition |
| Accessibility behavior | semantic implementation and verified acceptance criteria |
| Assets | source repository, DAM, or licensed original |
| Analytics | tracking plan and implemented event schema |
| Shipped behavior | named runtime environment and release version |

Do not promote the most convenient artifact to canon. Canon should reflect ownership, maintenance, and how downstream work is produced.

## 2. Provenance map

Record:

```text
Domain:
Canonical source:
Version / revision:
Owner:
Derived artifacts:
Transformation / synchronization:
Accepted variance:
Freshness signal:
Change notification:
Last verified:
```

For tokens, include alias resolution and platform transformation. For components, include property mapping and unsupported combinations. For content and assets, include rights and delivery pipeline.

## 3. Resolving disagreement

When Figma, code, documentation, or runtime differ:

1. State the difference factually.
2. Identify the affected domain and consequence.
3. Check versions, branches, release targets, and owners.
4. Determine whether the difference is intended variance, stale derivation, defect, or unresolved decision.
5. Ask the domain owner to choose when evidence cannot resolve intent.
6. Record the decision and update or link affected artifacts after authorization.
7. Revalidate downstream gates.

Do not silently synchronize artifacts. Do not assume newest means correct. Do not use visual similarity to conclude semantic parity.

## 4. Change impact

Classify changes:

- **Cosmetic:** no intended semantic or behavioral effect.
- **Content:** meaning, length, localization, legal text, or data representation changes.
- **Behavioral:** state, interaction, permission, validation, or recovery changes.
- **Structural:** component API, token, layout rule, data schema, or architecture changes.
- **Contractual:** scope, acceptance criterion, owner, deadline, or dependency changes.
- **Critical:** security, privacy, money, identity, destructive action, accessibility completion, or core-flow consequence changes.

A small visual diff can have structural or accessibility impact. A large refactor can preserve product intent. Classify by consequence, not pixel area.

## 5. Revalidation protocol

1. Resolve the changed canonical source and exact revision.
2. List directly and transitively affected artifacts.
3. Invalidate only evidence that depended on the changed decision.
4. Reopen applicable gates and conditions.
5. Compare against the last accepted contract.
6. Notify decision and implementation owners.
7. Replay acceptance criteria at the required evidence level.
8. Update verdict, conditions, and residual risk.

Do not re-audit everything automatically. Do not preserve a Ready verdict when its controlling evidence is stale.
