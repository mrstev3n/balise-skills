# Harness adapters

Canonical skills live under `skills/`. An adapter may add harness-specific metadata or packaging, but it must not fork or rewrite the canonical instructions.

Each adapter must document:

- the harness and supported packaging surface;
- the files it overlays or generates;
- the verification performed;
- any runtime version actually tested.

An adapter directory is added only when it contains a real, validated integration.
