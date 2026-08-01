![Balise Skills](assets/balise-skills-banner.webp)

# Balise Skills

Des skills portables pour Claude Code, Codex, Cursor, le Figma Agent, Figma Make et les autres outils compatibles avec le standard Agent Skills.

Installez un skill précis ou une collection prête à l’emploi. Chaque skill utilise [`SKILL.md`](https://agentskills.io/specification) comme format canonique. Les métadonnées propres à chaque outil restent isolées dans des adaptateurs.

## Accès rapide

- [Installer les skills](#installation-guidée)
- [Parcourir les skills disponibles](#skills-disponibles)
- [Utiliser une édition Figma](#utiliser-une-édition-figma)
- [Installer une collection](#collections)
- [Explorer le catalogue](#catalogue)

## Installation guidée

Lancez l’assistant pour choisir les skills, les agents cibles et la portée de l’installation :

```bash
npx skills add mrstev3n/balise-skills
```

Selon votre environnement, le CLI détecte les agents installés ou vous laisse choisir parmi les outils compatibles, dont Claude Code, Codex, Cursor et OpenCode. Il propose ensuite une installation dans le projet ou globale, puis place chaque skill dans le répertoire attendu.

Pour présélectionner tous les skills sans imposer l’agent ni la portée :

```bash
npx skills add mrstev3n/balise-skills --skill '*'
```

Pour consulter le catalogue sans rien installer :

```bash
npx skills add mrstev3n/balise-skills --list
```

## Comprendre les badges

Les badges indiquent les éditions réellement disponibles :

[![Agent Skills](assets/badges/agent-skills.svg)](docs/compatibility.md) [![Figma Agent](assets/badges/figma-agent.svg)](docs/compatibility.md) [![Figma Make](assets/badges/figma-make.svg)](docs/compatibility.md)

---

## Skills disponibles

### `balise-ohada`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-ohada)

Un cadre de travail pour aider une IA à rechercher, analyser et rédiger en droit des affaires OHADA, sans confondre les Actes uniformes avec les règles nationales applicables.

Le skill couvre 15 États membres francophones : Bénin, Burkina Faso, Cameroun, République centrafricaine, Tchad, Comores, Congo, Côte d’Ivoire, République démocratique du Congo (RDC), Gabon, Guinée, Mali, Niger, Sénégal et Togo. Il oriente notamment les recherches relatives aux sociétés commerciales, au RCCM, aux sûretés, au recouvrement et aux procédures collectives.

```bash
npx skills add mrstev3n/balise-skills --skill balise-ohada
```

### `balise-web-legal`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-web-legal)

Le RGPD est souvent le premier réflexe en matière de conformité numérique. Pourtant, un site destiné à un public francophone peut aussi relever de lois nationales sur les données personnelles, les cookies, les transactions électroniques ou la protection des consommateurs.

La valeur distinctive de ce skill est de couvrir les cadres souvent oubliés de l'Afrique francophone. Il aide une IA à déterminer les juridictions applicables avant de rédiger des mentions légales, une politique de confidentialité, une politique de cookies ou des documents de commerce électronique. Il intègre les droits du Bénin, du Burkina Faso, de la Côte d’Ivoire, de la Guinée, du Mali, du Niger, du Sénégal, du Togo, du Cameroun, du Congo, du Gabon, de la République centrafricaine, de la RDC, du Tchad et des Comores. Le RGPD et les règles françaises sont également traités lorsqu'ils s'appliquent, sans effacer les obligations locales.

```bash
npx skills add mrstev3n/balise-skills --skill balise-web-legal
```

### `balise-ux-writing`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-ux-writing) [![Figma Agent](assets/badges/figma-agent.svg)](figma-skills/balise-ux-writing/SKILL.md) [![Figma Make](assets/badges/figma-make.svg)](figma-skills/balise-ux-writing/SKILL.md)

Un skill de content design pour créer, réviser et harmoniser les textes d’interface : navigation, formulaires, erreurs, états vides, onboarding, confirmations, consentement et notifications. Il préserve la terminologie du produit, l’accessibilité, la localisation et les contraintes d’implémentation.

```bash
npx skills add mrstev3n/balise-skills --skill balise-ux-writing
```

### `balise-content-test`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-content-test) [![Figma Agent](assets/badges/figma-agent.svg)](figma-skills/balise-content-test/SKILL.md) [![Figma Make](assets/badges/figma-make.svg)](figma-skills/balise-content-test/SKILL.md)

Un protocole de test pour confronter les interfaces à des contenus réalistes mais difficiles : textes longs, valeurs manquantes, données extrêmes, traduction, écriture RTL, Unicode, agrandissement du texte et espaces étroits.

```bash
npx skills add mrstev3n/balise-skills --skill balise-content-test
```

### `balise-affinity`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-affinity)

Un guide de raisonnement et d’audit pour choisir les bons objets, modes de texte, structures de document et méthodes de production non destructive dans Affinity.

```bash
npx skills add mrstev3n/balise-skills --skill balise-affinity
```

### `balise-affinity-mcp`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-affinity-mcp)

Un workflow d’automatisation pour inspecter et modifier un document Affinity avec le serveur MCP et le SDK JavaScript d’Affinity.

```bash
npx skills add mrstev3n/balise-skills --skill balise-affinity-mcp
```

### `balise-brand-naming`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-brand-naming)

Une méthode structurée pour clarifier les fondations d’une marque, explorer plusieurs territoires de naming, filtrer les candidats et effectuer de premières vérifications numériques, linguistiques, culturelles et juridiques.

```bash
npx skills add mrstev3n/balise-skills --skill balise-brand-naming
```

### `balise-ui-states`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-ui-states) [![Figma Agent](assets/badges/figma-agent.svg)](figma-skills/balise-ui-states/SKILL.md) [![Figma Make](assets/badges/figma-make.svg)](figma-skills/balise-ui-states/SKILL.md)

Un workflow pour identifier, concevoir et vérifier les états nécessaires d’une interface : chargement, vide, partiel, succès, erreur, hors ligne, permission, synchronisation et interactions. Il aide à préserver le contexte, prévoir les transitions et offrir une véritable voie de récupération.

```bash
npx skills add mrstev3n/balise-skills --skill balise-ui-states
```

### `balise-visual-references`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-visual-references) [![Figma Agent](assets/badges/figma-agent.svg)](figma-skills/balise-visual-references/SKILL.md) [![Figma Make](assets/badges/figma-make.svg)](figma-skills/balise-visual-references/SKILL.md)

Une méthode de recherche et de sélection de références visuelles pour une interface, un composant, une marque, une présentation ou une campagne. Le skill transforme les exemples retenus en principes de conception adaptés au projet, sans reproduire leur expression distinctive.

```bash
npx skills add mrstev3n/balise-skills --skill balise-visual-references
```

## Utiliser une édition Figma

Lorsqu’un skill affiche les badges Figma, ouvrez le fichier `SKILL.md` lié, téléchargez-le, puis ajoutez-le depuis **Skills → Add skill** dans le Figma Agent ou Figma Make. L’édition Figma est autonome et peut adapter son workflow aux capacités de cet environnement.

Tous les skills ne possèdent pas nécessairement une édition Figma. Les badges indiquent uniquement les versions réellement disponibles.

## Collections

### Collection `legal`

La collection `legal` installe les deux skills :

```bash
npx skills add mrstev3n/balise-skills \
  --skill balise-ohada \
  --skill balise-web-legal
```

### Collection `content`

```bash
npx skills add mrstev3n/balise-skills \
  --skill balise-ux-writing \
  --skill balise-content-test
```

### Collection `design`

```bash
npx skills add mrstev3n/balise-skills \
  --skill balise-affinity \
  --skill balise-affinity-mcp \
  --skill balise-brand-naming \
  --skill balise-ui-states \
  --skill balise-visual-references
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
