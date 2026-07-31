# Catalogue metadata

`catalog/marketplace.json` is the source of truth for discovery metadata. It supports command-line tooling and web catalogue interfaces.

## Category

A category is a primary discovery classification. Each skill has exactly one category. Categories are not installation units and may be active or planned.

## Tag

A tag is a transversal filter. A skill may have several tags, and every used tag must be declared in the catalogue registry.

## Collection

A collection is an ordered, versioned, installable set of skills. A collection may span categories. Its manifest lives under `collections/` and references skills by identifier.

`category:legal` and `collection:legal` are separate entities. Legal is one field within the broader Skill Market catalogue.

## Versioning

Catalogue, collection, and skill versions follow semantic versioning.
