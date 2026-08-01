# Preuves de vérification

Date : 2026-08-01

## Invariants du dépôt

Commande :

```bash
npm run validate
```

Résultat : neuf skills canoniques, quatre éditions Figma autonomes et trois collections découverts. Le frontmatter, les chemins, les liens, les badges, le catalogue, les éditions, les adaptateurs et les collections respectent les invariants du dépôt.

## Schémas JSON

Outil : `check-jsonschema==0.36.2`

Résultat : `catalog/marketplace.json` et les trois manifestes de collection respectent leurs schémas Draft 2020-12.

## Validateur de référence Agent Skills

Source : `agentskills/agentskills`, commit `38a2ff82958afee88dadf4831509e6f7e9d8ef4e`.

Les neuf éditions canoniques et les quatre éditions Figma ont passé le validateur :

```text
skills/balise-affinity
skills/balise-affinity-mcp
skills/balise-brand-naming
skills/balise-content-test
skills/balise-ohada
skills/balise-ui-states
skills/balise-ux-writing
skills/balise-visual-references
skills/balise-web-legal
figma-skills/balise-content-test
figma-skills/balise-ui-states
figma-skills/balise-ux-writing
figma-skills/balise-visual-references
```

## Installation multi-harness

Commande :

```bash
npx --yes skills@1.5.9 add <local-repository> \
  --agent claude-code codex cursor \
  --skill balise-affinity balise-affinity-mcp balise-brand-naming \
          balise-content-test balise-ohada balise-ui-states \
          balise-ux-writing balise-visual-references balise-web-legal \
  --copy --yes
```

Résultat : le CLI a découvert exactement neuf skills et les a installés dans des destinations isolées pour Claude Code, Codex et Cursor. Les comparaisons récursives avec les sources canoniques n’ont révélé aucune différence.

## Invocation observée

Codex CLI `0.145.0` a précédemment découvert et invoqué les sept skills suivants depuis une installation isolée :

- `balise-ohada`
- `balise-web-legal`
- `balise-ux-writing`
- `balise-content-test`
- `balise-affinity`
- `balise-affinity-mcp`
- `balise-brand-naming`

Le catalogue enregistre les preuves d’exécution par skill sans les déduire de la seule validation du format ou de l’installation.
