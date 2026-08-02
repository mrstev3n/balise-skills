![Balise Skills](assets/balise-skills-banner.webp)

# Balise Skills

Des skills portables pour Claude Code, Codex, Cursor, le Figma Agent, Figma Make et les autres outils compatibles avec le standard Agent Skills.

Installez un skill précis ou une collection prête à l’emploi. Chaque skill utilise [`SKILL.md`](https://agentskills.io/specification) comme format canonique. Les métadonnées propres à chaque outil restent isolées dans des adaptateurs.

## Accès rapide

- [Installer les skills](#installation-guidée)
- [Mettre les skills à jour](#mettre-à-jour-les-skills)
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

## Mettre à jour les skills

Le CLI compare les skills installés avec leur source et applique les nouvelles versions disponibles :

```bash
npx skills update
```

Vous pouvez limiter la mise à jour à un skill, choisir les skills de manière interactive, viser les installations globales ou accepter toutes les mises à jour sans confirmation :

```bash
npx skills update balise-webmotion
npx skills update -p
npx skills update -g
npx skills update -y
```

`npx` lance le CLI d’installation : Balise Skills n’a pas besoin d’être publié comme paquet npm. La version et la date affichées sous chaque skill correspondent à son édition la plus récente dans le catalogue.

## Comprendre les badges

Les badges indiquent les éditions réellement disponibles :

[![Agent Skills](assets/badges/agent-skills.svg)](docs/compatibility.md) [![Figma Agent](assets/badges/figma-agent.svg)](docs/compatibility.md) [![Figma Make](assets/badges/figma-make.svg)](docs/compatibility.md)

---

## Skills disponibles

### `balise-ohada`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-ohada)

<sub>Version 0.2.0 · Mise à jour le 31 juillet 2026</sub>

Un cadre de travail pour aider une IA à rechercher, analyser et rédiger en droit des affaires OHADA, sans confondre les Actes uniformes avec les règles nationales applicables.

Le skill couvre 15 États membres francophones : Bénin, Burkina Faso, Cameroun, République centrafricaine, Tchad, Comores, Congo, Côte d’Ivoire, République démocratique du Congo (RDC), Gabon, Guinée, Mali, Niger, Sénégal et Togo. Il oriente notamment les recherches relatives aux sociétés commerciales, au RCCM, aux sûretés, au recouvrement et aux procédures collectives.

```bash
npx skills add mrstev3n/balise-skills --skill balise-ohada
```

### `balise-web-legal`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-web-legal)

<sub>Version 0.2.0 · Mise à jour le 31 juillet 2026</sub>

Le RGPD est souvent le premier réflexe en matière de conformité numérique. Pourtant, un site destiné à un public francophone peut aussi relever de lois nationales sur les données personnelles, les cookies, les transactions électroniques ou la protection des consommateurs.

La valeur distinctive de ce skill est de couvrir les cadres souvent oubliés de l'Afrique francophone. Il aide une IA à déterminer les juridictions applicables avant de rédiger des mentions légales, une politique de confidentialité, une politique de cookies ou des documents de commerce électronique. Il intègre les droits du Bénin, du Burkina Faso, de la Côte d’Ivoire, de la Guinée, du Mali, du Niger, du Sénégal, du Togo, du Cameroun, du Congo, du Gabon, de la République centrafricaine, de la RDC, du Tchad et des Comores. Le RGPD et les règles françaises sont également traités lorsqu'ils s'appliquent, sans effacer les obligations locales.

```bash
npx skills add mrstev3n/balise-skills --skill balise-web-legal
```

### `balise-ux-writing`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-ux-writing) [![Figma Agent](assets/badges/figma-agent.svg)](figma-skills/balise-ux-writing/SKILL.md) [![Figma Make](assets/badges/figma-make.svg)](figma-skills/balise-ux-writing/SKILL.md)

<sub>Version 0.1.0 · Mise à jour le 1 août 2026</sub>

Un skill de content design pour créer, réviser et harmoniser les textes d’interface : navigation, formulaires, erreurs, états vides, onboarding, confirmations, consentement et notifications. Il préserve la terminologie du produit, l’accessibilité, la localisation et les contraintes d’implémentation.

```bash
npx skills add mrstev3n/balise-skills --skill balise-ux-writing
```

### `balise-content-test`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-content-test) [![Figma Agent](assets/badges/figma-agent.svg)](figma-skills/balise-content-test/SKILL.md) [![Figma Make](assets/badges/figma-make.svg)](figma-skills/balise-content-test/SKILL.md)

<sub>Version 0.1.0 · Mise à jour le 1 août 2026</sub>

Un protocole de test pour confronter les interfaces à des contenus réalistes mais difficiles : textes longs, valeurs manquantes, données extrêmes, traduction, écriture RTL, Unicode, agrandissement du texte et espaces étroits.

```bash
npx skills add mrstev3n/balise-skills --skill balise-content-test
```

### `balise-affinity`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-affinity)

<sub>Version 0.1.0 · Mise à jour le 1 août 2026</sub>

Un guide de raisonnement et d’audit pour choisir les bons objets, modes de texte, structures de document et méthodes de production non destructive dans Affinity.

```bash
npx skills add mrstev3n/balise-skills --skill balise-affinity
```

### `balise-affinity-mcp`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-affinity-mcp)

<sub>Version 0.1.0 · Mise à jour le 1 août 2026</sub>

Un workflow d’automatisation pour inspecter et modifier un document Affinity avec le serveur MCP et le SDK JavaScript d’Affinity.

```bash
npx skills add mrstev3n/balise-skills --skill balise-affinity-mcp
```

### `balise-brand-naming`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-brand-naming)

<sub>Version 0.1.0 · Mise à jour le 1 août 2026</sub>

Une méthode structurée pour clarifier les fondations d’une marque, explorer plusieurs territoires de naming, filtrer les candidats et effectuer de premières vérifications numériques, linguistiques, culturelles et juridiques.

```bash
npx skills add mrstev3n/balise-skills --skill balise-brand-naming
```

### `balise-ui-states`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-ui-states) [![Figma Agent](assets/badges/figma-agent.svg)](figma-skills/balise-ui-states/SKILL.md) [![Figma Make](assets/badges/figma-make.svg)](figma-skills/balise-ui-states/SKILL.md)

<sub>Version 0.1.0 · Mise à jour le 1 août 2026</sub>

Un workflow pour identifier, concevoir et vérifier les états nécessaires d’une interface : chargement, vide, partiel, succès, erreur, hors ligne, permission, synchronisation et interactions. Il aide à préserver le contexte, prévoir les transitions et offrir une véritable voie de récupération.

```bash
npx skills add mrstev3n/balise-skills --skill balise-ui-states
```

### `balise-visual-references`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-visual-references) [![Figma Agent](assets/badges/figma-agent.svg)](figma-skills/balise-visual-references/SKILL.md) [![Figma Make](assets/badges/figma-make.svg)](figma-skills/balise-visual-references/SKILL.md)

<sub>Version 0.1.0 · Mise à jour le 1 août 2026</sub>

Une méthode de recherche et de sélection de références visuelles pour une interface, un composant, une marque, une présentation ou une campagne. Le skill transforme les exemples retenus en principes de conception adaptés au projet, sans reproduire leur expression distinctive.

```bash
npx skills add mrstev3n/balise-skills --skill balise-visual-references
```

### `balise-trustworthy-flows`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-trustworthy-flows) [![Figma Agent](assets/badges/figma-agent.svg)](figma-skills/balise-trustworthy-flows/SKILL.md) [![Figma Make](assets/badges/figma-make.svg)](figma-skills/balise-trustworthy-flows/SKILL.md)

<sub>Version 0.1.0 · Mise à jour le 2 août 2026</sub>

Un workflow pour auditer, concevoir et réparer les parcours où une décision engage réellement la personne : consentement, permissions, tarification, abonnement, résiliation, suppression ou partage de données. Il aide à rendre les conséquences lisibles, les choix équilibrés et les sorties accessibles, sans prétendre déduire l’intention du produit ni sa conformité juridique depuis une interface.

```bash
npx skills add mrstev3n/balise-skills --skill balise-trustworthy-flows
```

### `balise-handoff`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-handoff) [![Figma Agent](assets/badges/figma-agent.svg)](figma-skills/balise-handoff/SKILL.md) [![Figma Make](assets/badges/figma-make.svg)](figma-skills/balise-handoff/SKILL.md)

<sub>Version 0.1.0 · Mise à jour le 2 août 2026</sub>

Un cadre pour déterminer si une conception est réellement prête à être implémentée. Il relie les maquettes, composants, prototypes, spécifications et preuves techniques, puis rend explicites les décisions ouvertes, leurs responsables, les risques et les critères d’acceptation.

```bash
npx skills add mrstev3n/balise-skills --skill balise-handoff
```

### `balise-design-system`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-design-system)

<sub>Version 0.1.0 · Mise à jour le 2 août 2026</sub>

Une méthode complète pour architecturer, auditer et faire évoluer un design system de Figma au code : fondations, variables, tokens sémantiques, composants, thèmes, DTCG, Style Dictionary, documentation, distribution et gouvernance. Le skill aide aussi à organiser l’adoption, les migrations et les architectures multi-marques ou multi-plateformes.

```bash
npx skills add mrstev3n/balise-skills --skill balise-design-system
```

### `balise-webmotion`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-webmotion)

<sub>Version 0.1.0 · Mise à jour le 2 août 2026</sub>

Un workflow de recherche, de direction et de production pour créer des mouvements web ambitieux : transitions de page, narration au scroll, micro-interactions, gestes, effets 3D, animations vectorielles et prototypes rapides. Le skill choisit une approche adaptée au projet, construit le moment signature, puis vérifie les performances, les interactions et la réduction des mouvements.

```bash
npx skills add mrstev3n/balise-skills --skill balise-webmotion
```

### `balise-motion-graphic`

[![Agent Skills](assets/badges/agent-skills.svg)](skills/balise-motion-graphic)

<sub>Version 0.1.0 · Mise à jour le 2 août 2026</sub>

Un workflow de direction et de production pour les contenus animés rendus : teasers, vidéos sociales, génériques, kinetic typography, explainers, boucles et animations de marque. Il couvre le brief, les références, les assets, le rythme, le son, le choix du moteur, le rendu et la validation du fichier exporté.

```bash
npx skills add mrstev3n/balise-skills --skill balise-motion-graphic
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
  --skill balise-design-system \
  --skill balise-handoff \
  --skill balise-motion-graphic \
  --skill balise-trustworthy-flows \
  --skill balise-ui-states \
  --skill balise-visual-references \
  --skill balise-webmotion
```

### Collection `motion`

```bash
npx skills add mrstev3n/balise-skills \
  --skill balise-webmotion \
  --skill balise-motion-graphic
```

## Catalogue

Balise Skills propose trois niveaux de découverte :

- Les **catégories** regroupent les skills par domaine principal.
- Les **tags** relient les skills selon leurs sujets et leurs usages.
- Les **collections** réunissent plusieurs skills dans un ensemble installable.

Les collections `legal`, `content`, `design` et `motion` composent un catalogue conçu pour couvrir plusieurs domaines.

Les métadonnées exploitables par des outils se trouvent dans [`catalog/marketplace.json`](catalog/marketplace.json). Consultez le [modèle de métadonnées](docs/metadata.md) et la [politique de compatibilité](docs/compatibility.md) pour en savoir plus.

## Valider le catalogue

```bash
npm run validate
```

Cette commande vérifie la structure des skills, les liens, les adaptateurs et l’intégrité du catalogue et des collections. La CI valide également les manifestes contre leurs schémas JSON.

## Licence

Licence Apache 2.0. Consultez le fichier [`LICENSE`](LICENSE).
