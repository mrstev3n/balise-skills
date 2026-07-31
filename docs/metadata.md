# Catalogue metadata

`catalog/marketplace.json` is the source of truth for discovery metadata. It is designed for command-line tooling and a future web catalogue.

## Category

A category is a primary discovery classification. Each skill has exactly one category. Categories are not installation units and may be active or planned.

## Tag

A tag is a transversal filter. A skill may have several tags, and every used tag must be declared in the catalogue registry.

## Collection

A collection is an ordered, versioned, installable set of skills. A collection may span categories. Its manifest lives under `collections/` and references skills by identifier.

`category:legal` and `collection:legal` are separate entities. Legal is the first collection in Skill Market, not the total scope of the marketplace.

## Versioning

The initial release uses a single `0.1.0` version across the catalogue, collection, and skills. Independent skill versioning may be introduced only with a documented migration and release policy.
