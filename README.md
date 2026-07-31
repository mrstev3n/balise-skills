![Balise Skills](assets/balise-skills-banner.webp)

# Balise Skills

Des skills portables pour Claude Code, Codex, Cursor et les autres outils compatibles avec le standard Agent Skills.

Installez un skill précis ou une collection prête à l’emploi. Chaque skill utilise [`SKILL.md`](https://agentskills.io/specification) comme format canonique. Les métadonnées propres à chaque outil restent isolées dans des adaptateurs.

## Skills disponibles

### `balise-ohada`

Un cadre de travail pour aider une IA à rechercher, analyser et rédiger en droit des affaires OHADA, sans confondre les Actes uniformes avec les règles nationales applicables.

Le skill couvre 15 États membres francophones : Bénin, Burkina Faso, Cameroun, République centrafricaine, Tchad, Comores, Congo, Côte d’Ivoire, République démocratique du Congo (RDC), Gabon, Guinée, Mali, Niger, Sénégal et Togo. Il oriente notamment les recherches relatives aux sociétés commerciales, au RCCM, aux sûretés, au recouvrement et aux procédures collectives.

```bash
npx skills add mrstev3n/balise-skills --skill balise-ohada
```

### `balise-web-legal`

Le RGPD est souvent le premier réflexe en matière de conformité numérique. Pourtant, un site destiné à un public francophone peut aussi relever de lois nationales sur les données personnelles, les cookies, les transactions électroniques ou la protection des consommateurs.

La valeur distinctive de ce skill est de couvrir les cadres souvent oubliés de l'Afrique francophone. Il aide une IA à déterminer les juridictions applicables avant de rédiger des mentions légales, une politique de confidentialité, une politique de cookies ou des documents de commerce électronique. Il intègre les droits du Bénin, du Burkina Faso, de la Côte d’Ivoire, de la Guinée, du Mali, du Niger, du Sénégal, du Togo, du Cameroun, du Congo, du Gabon, de la République centrafricaine, de la RDC, du Tchad et des Comores. Le RGPD et les règles françaises sont également traités lorsqu'ils s'appliquent, sans effacer les obligations locales.

```bash
npx skills add mrstev3n/balise-skills --skill balise-web-legal
```

### `balise-ux-writing`

Un skill de content design pour créer, réviser et harmoniser les textes d’interface : navigation, formulaires, erreurs, états vides, onboarding, confirmations, consentement et notifications. Il préserve la terminologie du produit, l’accessibilité, la localisation et les contraintes d’implémentation.

```bash
npx skills add mrstev3n/balise-skills --skill balise-ux-writing
```

### `balise-content-test`

Un protocole de test pour confronter les interfaces à des contenus réalistes mais difficiles : textes longs, valeurs manquantes, données extrêmes, traduction, écriture RTL, Unicode, agrandissement du texte et espaces étroits.

```bash
npx skills add mrstev3n/balise-skills --skill balise-content-test
```

### `balise-affinity`

Un guide de raisonnement et d’audit pour choisir les bons objets, modes de texte, structures de document et méthodes de production non destructive dans Affinity.

```bash
npx skills add mrstev3n/balise-skills --skill balise-affinity
```

### `balise-affinity-mcp`

Un workflow d’automatisation pour inspecter et modifier un document Affinity avec le serveur MCP et le SDK JavaScript d’Affinity.

```bash
npx skills add mrstev3n/balise-skills --skill balise-affinity-mcp
```

### `balise-brand-naming`

Une méthode structurée pour clarifier les fondations d’une marque, explorer plusieurs territoires de naming, filtrer les candidats et effectuer de premières vérifications numériques, linguistiques, culturelles et juridiques.

```bash
npx skills add mrstev3n/balise-skills --skill balise-brand-naming
```

## Installer la collection `legal`

La collection `legal` installe les deux skills :

```bash
npx skills add mrstev3n/balise-skills \
  --skill balise-ohada \
  --skill balise-web-legal
```

## Installer la collection `content`

```bash
npx skills add mrstev3n/balise-skills \
  --skill balise-ux-writing \
  --skill balise-content-test
```

## Installer la collection `design`

```bash
npx skills add mrstev3n/balise-skills \
  --skill balise-affinity \
  --skill balise-affinity-mcp \
  --skill balise-brand-naming
```

Pour afficher tous les skills disponibles avant l’installation :

```bash
npx skills add mrstev3n/balise-skills --list
```

## Catalogue

Balise Skills propose trois niveaux de découverte :

- Les **catégories** regroupent les skills par domaine principal.
- Les **tags** relient les skills selon leurs sujets et leurs usages.
- Les **collections** réunissent plusieurs skills dans un ensemble installable.

Les collections `legal`, `content` et `design` composent un catalogue conçu pour couvrir plusieurs domaines.

Les métadonnées exploitables par des outils se trouvent dans [`catalog/marketplace.json`](catalog/marketplace.json). Consultez le [modèle de métadonnées](docs/metadata.md) et la [politique de compatibilité](docs/compatibility.md) pour en savoir plus.

## Valider le catalogue

```bash
npm run validate
```

Cette commande vérifie la structure des skills, les liens, les adaptateurs et l’intégrité du catalogue et des collections. La CI valide également les manifestes contre leurs schémas JSON.

## Licence

Licence Apache 2.0. Consultez le fichier [`LICENSE`](LICENSE).
