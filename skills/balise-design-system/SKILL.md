---
name: balise-design-system
description: "Architecturer, auditer, construire, intégrer et faire évoluer un design system robuste de Figma au code. Utiliser pour cadrer un système partagé, structurer style guides et variables, design tokens primitifs/sémantiques/composants, aliases, thèmes et modes, rampes de couleur, échelles typographiques, composants et patterns; organiser Figma-to-code, DTCG, Style Dictionary, packages multi-plateformes, Tailwind ou shadcn; auditer ou consolider l’architecture UI partagée d’un SaaS, dashboard, produit multi-tenant ou base existante; guider consommation, documentation, gouvernance, versionnage et migration. Déclencheurs : design system, design tokens, style guide, Figma variables, component library, UI kit, theming, dark mode, multi-marque, multi-tenant design system, SaaS design system, Tailwind theme architecture, semantic tokens, DTCG, Style Dictionary, design-to-code."
---

# Design System

Concevoir le système comme un produit partagé : décisions, composants, documentation, distribution et gouvernance. Ne jamais réduire la réponse à une palette, un fichier de variables ou une bibliothèque isolée.

## Choisir le workflow

Qualifier la demande avant d’agir :

| Demande | Point de départ | Sortie principale |
|---|---|---|
| Définir une approche | contexte, finalité, consommateurs | brief, options, architecture, pilote |
| Auditer l’existant | code, design, docs, usages | inventaire, divergences, dette, priorités |
| Créer ou migrer des tokens | produits, modes, plateformes | taxonomie, source, mappings, pipeline |
| Construire les fondations | usages et contraintes réels | rampes, rôles, échelles, validations |
| Structurer Figma et relier au code | styles, variables, collections, composants | mapping, autorités, preuves de synchronisation |
| Consolider un SaaS | navigation, données, formulaires, tenants | fondations, patterns, états, densité, thèmes |
| Adapter Tailwind ou une base UI | version, conventions, dette, API existante | stratégie extend/override/replace, pont sémantique |
| Spécifier un composant/pattern | problème, contexte, états | contrat, API, comportement, preuves |
| Guider la consommation | rôles et points de friction | golden path, extension, contribution, upgrade |
| Organiser la gouvernance | équipe, capacité, risques | ownership, maturité, release, métriques |

Lire seulement les références nécessaires :

- Stratégie, périmètre et modèle d’organisation : [references/strategy-and-scope.md](references/strategy-and-scope.md)
- Audits, inventaires et sélection du pilote : [references/audits-and-pilots.md](references/audits-and-pilots.md)
- Architecture DTCG, couches, alias, thèmes et modes : [references/token-architecture.md](references/token-architecture.md)
- Nommage et autorités design/code/docs : [references/naming-and-source-authority.md](references/naming-and-source-authority.md)
- Couleur, typographie, espace et autres fondations : [references/color-and-typography.md](references/color-and-typography.md)
- Primitives UI, composants, patterns et états : [references/components-and-patterns.md](references/components-and-patterns.md)
- Parcours consommateur, onboarding et documentation : [references/consumption-and-learning.md](references/consumption-and-learning.md)
- Gouvernance, maturité, contribution et mesure : [references/governance-and-maturity.md](references/governance-and-maturity.md)
- Transformations, packages, tests, releases et migrations : [references/implementation-pipelines.md](references/implementation-pipelines.md)
- Style Dictionary, cycle de compilation et critères d’adoption : [references/style-dictionary.md](references/style-dictionary.md)
- Variables, styles, bibliothèques et passage Figma → code : [references/figma-to-code.md](references/figma-to-code.md)
- Fondations et patterns structurels pour produits SaaS : [references/saas-structures.md](references/saas-structures.md)
- Adoption de Tailwind, shadcn et autres bases UI : [references/framework-adoption.md](references/framework-adoption.md)
- Fiches, matrices et contrats de livraison : [references/deliverable-templates.md](references/deliverable-templates.md)

## Workflow cœur

### 1. Inspecter le réel

Inspecter avant de recommander :

- produits, surfaces, marques, thèmes, modes, langues et plateformes ;
- équipes productrices, mainteneurs, consommateurs et sponsors ;
- styles, variables, tokens, composants, patterns et documentation existants ;
- frameworks, build, packages, versions, compatibilité et contraintes de sécurité ;
- accessibilité, performance, legacy, white-label, natif et calendrier ;
- répétitions, forks, valeurs brutes, divergences et contournements.

Utiliser les scripts fournis lorsqu’ils correspondent au format réel :

```bash
python3 <skill-dir>/scripts/validate_dtcg.py path/to/tokens.json
python3 <skill-dir>/scripts/audit_token_usage.py src --manifest path/to/generated-tokens.css
```

Résoudre `<skill-dir>` depuis le chemin absolu du `SKILL.md` sélectionné, jamais depuis le cwd du projet consommateur. Ne pas présenter ces contrôles ciblés comme une validation complète du schéma DTCG, ni comme une preuve visuelle, comportementale ou d’accessibilité.

### 2. Cadrer le résultat

Énoncer : contexte, objectif, non-objectifs, publics, périmètre, principes, contraintes, workstreams et critères d’acceptation observables.

Situer le système sur trois axes :

- strict ↔ souple ;
- modulaire ↔ intégré ;
- centralisé ↔ distribué.

Pouvoir conclure qu’un système complet n’est pas justifié. Préférer alors des conventions légères, quelques fondations ou un kit local maintenable.

### 3. Modéliser les décisions

Choisir uniquement les couches utiles :

1. valeurs sources ou mesures ;
2. primitives/références/options ;
3. sémantiques/décisions ;
4. composants/patterns si une décision doit varier indépendamment ;
5. contextes produit seulement s’ils expriment une responsabilité légitime.

Traiter marque, thème clair/sombre, contraste, densité, plateforme et RTL comme des axes de variation possibles, pas automatiquement comme des couches.

Définir une autorité par artefact :

- décisions agnostiques : source portable versionnée, DTCG lorsque supporté et pertinent ;
- contrat composant : types, schéma ou manifeste ;
- comportement et accessibilité : implémentation testée ;
- intention et règles : documentation liée à la version ;
- authoring design : miroir synchronisé selon une gouvernance explicite.

### 4. Prototyper une tranche réelle

Choisir un flow pilote visible et borné. Tester suffisamment de fondations et environ 3 à 7 composants pour révéler les défauts d’architecture, sans transformer ce nombre en règle.

Évaluer le pilote par valeur, répétition, champion, faisabilité, indépendance, délai d’apprentissage et visibilité du résultat.

Extraire après usage réel : produit → extraction → abstraction → seconde consommation → correction. Ne pas canoniser une ressemblance visuelle non éprouvée.

### 5. Implémenter et distribuer

Préférer une chaîne reproductible :

```text
portable token source (DTCG when supported)
→ schema et lint
→ résolution des alias
→ transformations de plateforme
→ artefacts générés
→ tests packages/visuels/a11y
→ release versionnée
→ PR ou upgrade consommateur
→ télémétrie d’adoption
```

Ne pas choisir Style Dictionary, Tokens Studio, Figma, Storybook ou un framework par réflexe. Comparer leurs capacités avec le workflow, la portabilité, la sécurité et la maintenance attendus. Lorsque Style Dictionary est retenu, le traiter comme un compilateur remplaçable entre la source portable et les artefacts consommés, pas comme la stratégie de tokens ni comme la source de vérité du design system.

### 6. Vérifier proportionnellement

Associer chaque changement à une preuve :

- source : schéma, types, noms, alias, cycles, références et sorties ;
- couleur : gamut et couples foreground/background par état et mode ;
- typographie : fonte réelle, zoom, reflow, langues, fallbacks et contenu extrême ;
- composant : API, clavier, focus, annonces, contenu, responsive, thèmes, RTL et états ;
- pipeline : build, snapshots, package size, provenance et smoke tests consommateurs ;
- migration : dry-run, mapping, coexistence, dépréciation, adoption et rollback.

Distinguer explicitement preuve statique, preuve rendue, preuve avec technologie d’assistance et preuve en produit consommateur.

### 7. Transmettre et faire adopter

Concevoir le parcours : découvrir → évaluer → installer → composer → adapter → contribuer → mettre à jour.

Fournir le chemin recommandé le plus court pour les cas fréquents, puis révéler les détails internes à la demande. Documenter les degrés de liberté et les escape hatches légitimes.

## Garde-fous obligatoires

- Ne pas imposer une taxonomie universelle ou Atomic Design comme architecture canonique.
- Ne pas exposer les primitives comme API de consommation par défaut.
- Ne pas créer un token de composant qui duplique un rôle sémantique sans raison.
- Ne pas construire une rampe avant d’identifier ses usages et couples de contraste.
- Ne pas générer une échelle typographique à partir d’un ratio magique seul.
- Ne pas traiter le dark mode comme une inversion ou un simple remapping automatique.
- Ne pas considérer les variables Figma comme la preuve du runtime.
- Ne pas considérer la palette ou l’échelle Tailwind par défaut comme la sémantique du produit.
- Ne pas conserver une valeur arbitraire répétée sous prétexte que le framework l’autorise.
- Ne pas considérer SemVer seul comme une mesure d’impact visuel, comportemental ou accessibilité.
- Ne pas ajouter une prop à chaque exception locale ; préférer composition, pattern ou maintien local explicite.
- Ne pas viser automatiquement 100 % de couverture ou d’adoption.
- Ne pas publier, déployer, renommer, supprimer ou migrer sans autorisation adaptée.

## Contrats de sortie

Adapter la profondeur au besoin, mais inclure au minimum :

### Approche ou architecture

- contexte et hypothèses ;
- options comparées et décision ;
- non-objectifs et risques ;
- couches, axes de variation et autorités ;
- pilote et critères d’acceptation.

### Tokens ou fondations

- rôles et usages ;
- taxonomie et conventions ;
- source canonique et alias ;
- thèmes/modes et sorties ;
- tests, migrations et limites.

### Composant ou pattern

- problème, contexte et non-usages ;
- anatomie, API, slots et composition ;
- variants et matrice d’états ;
- contenu, accessibilité, responsive et thèmes ;
- tests, lineage, statut et migration.

### Audit ou migration

- preuves inspectées ;
- divergences intentionnelles vs accidentelles ;
- mapping et priorités ;
- étapes réversibles ;
- métriques d’avancement et risques non vérifiés.

### Figma vers code

- inventaire styles, variables, collections, modes et composants ;
- mapping explicite design ↔ source portable ↔ runtime ;
- autorité d’édition et sens de synchronisation ;
- divergences, pertes de type et limites d’outil ;
- preuve rendue dans un consommateur réel.

### SaaS ou base existante

- shell, navigation, densité, responsive et contraintes multi-tenant ;
- fondations, patterns de données, formulaires et matrice d’états ;
- stratégie extend/override/replace du framework ;
- frontière entre tokens publics, variables d’intégration et détails privés ;
- pilote, migration progressive et critères d’adoption.

## Standard de vérité

Distinguer toujours :

- standard d’échange actuel ;
- convention d’équipe ;
- heuristique issue d’un corpus ;
- décision locale de produit.

Revérifier les capacités d’outil, versions, normes et recommandations d’accessibilité lorsqu’elles peuvent avoir évolué. Ne pas recopier les recettes historiques des ouvrages sans actualisation.
