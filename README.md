![Skill Market](assets/skill-market-banner.webp)

# Skill Market

Des skills portables pour Claude Code, Codex, Cursor et les autres outils compatibles avec le standard Agent Skills.

Installez un skill précis ou une collection prête à l’emploi. Chaque skill utilise [`SKILL.md`](https://agentskills.io/specification) comme format canonique. Les métadonnées propres à chaque outil restent isolées dans des adaptateurs.

## Skills disponibles

### `ohada-legal-practice`

Recherche et rédaction en droit des affaires OHADA et dans les droits nationaux de 15 États membres francophones.

```bash
npx skills add mrstev3n/Skill-Market --skill ohada-legal-practice
```

### `website-legal-compliance`

Audit et rédaction de mentions légales, politiques de confidentialité, règles relatives aux cookies et documents de commerce électronique pour plusieurs juridictions.

```bash
npx skills add mrstev3n/Skill-Market --skill website-legal-compliance
```

## Installer la collection `legal`

La collection `legal` installe les deux skills :

```bash
npx skills add mrstev3n/Skill-Market \
  --skill ohada-legal-practice \
  --skill website-legal-compliance
```

Pour afficher tous les skills disponibles avant l’installation :

```bash
npx skills add mrstev3n/Skill-Market --list
```

## Catalogue

Skill Market propose trois niveaux de découverte :

- Les **catégories** regroupent les skills par domaine principal.
- Les **tags** relient les skills selon leurs sujets et leurs usages.
- Les **collections** réunissent plusieurs skills dans un ensemble installable.

La collection `legal` inaugure un catalogue conçu pour couvrir plusieurs domaines.

Les métadonnées exploitables par des outils se trouvent dans [`catalog/marketplace.json`](catalog/marketplace.json). Consultez le [modèle de métadonnées](docs/metadata.md) et la [politique de compatibilité](docs/compatibility.md) pour en savoir plus.

## Valider le catalogue

```bash
npm run validate
```

Cette commande vérifie les schémas du catalogue, la structure des skills, les liens, les adaptateurs et l’intégrité des collections.

## Licence

Licence Apache 2.0. Consultez le fichier [`LICENSE`](LICENSE).
