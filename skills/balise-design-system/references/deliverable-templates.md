# Fiches et contrats de livraison

Utiliser ces structures comme minimum adaptable. Remplir avec des preuves du projet ; ne jamais inventer une décision manquante.

## Sommaire

1. [Fiche de cadrage](#fiche-de-cadrage)
2. [Fiche de fondation ou token](#fiche-de-fondation-ou-token)
3. [Fiche de composant](#fiche-de-composant)
4. [Matrice d’états](#matrice-détats)
5. [Manifeste Figma vers code](#manifeste-figma--code)
6. [ADR d’outillage](#adr-doutillage)
7. [Plan de migration](#plan-de-migration)
8. [Preuve de consommation](#preuve-de-consommation)
9. [Checklist de livraison](#checklist-de-livraison)

## Fiche de cadrage

```markdown
# Design system — cadrage
Contexte :
Objectif :
Non-objectifs :
Produits et plateformes :
Marques, thèmes et modes :
Consommateurs :
Contraintes :
État actuel et preuves :
Axes strict/souple, modulaire/intégré, centralisé/distribué :
Option retenue et alternatives :
Pilote :
Risques :
Critères d’acceptation :
```

## Fiche de fondation ou token

```markdown
Nom public :
Intention :
Type :
Couche : primitive | semantic | component
Usages :
Non-usages :
Valeur ou alias par mode :
Source canonique :
Sorties de plateforme :
Compatibilité et fallback :
Accessibilité :
Statut et propriétaire :
Dépréciation/remplacement :
Preuves :
```

## Fiche de composant

```markdown
# Composant
Problème résolu :
Contextes :
Alternatives et non-usages :
Anatomie et slots :
API publique :
Variants :
États :
Contenu et localisation :
Clavier, focus, rôles et annonces :
Responsive, densité, thèmes et RTL :
Tokens consommés :
Composition et escape hatches :
Tests :
Lineage Figma/code :
Statut, owner et version :
Migration :
```

## Matrice d’états

| Axe | Cas à décider |
|---|---|
| données | initial, loading, success, empty, partial, stale, error |
| interaction | rest, hover, focus, active, selected, disabled |
| validation | pristine, valid, invalid, warning |
| permission | allowed, read-only, hidden, denied |
| réseau | online, slow, offline, retrying |
| traitement | queued, running, canceling, complete, failed |
| thème | light, dark, contraste, marque/tenant si inclus dans le périmètre |
| contenu | court, long, localisé, manquant, extrême |

Documenter uniquement les combinaisons pertinentes, mais prouver que les axes ont été considérés.

## Manifeste Figma → code

| Design | Portable | Runtime | Type | Modes | Owner | Statut | Preuve |
|---|---|---|---|---|---|---|---|
| variable/style/component | token ou manifeste | CSS/Swift/Android/composant | type | contextes | équipe | maturité | test/story/flow |

Ajouter identifiants stables, version, date de synchronisation et divergence intentionnelle lorsque disponibles.

## ADR d’outillage

```markdown
# ADR — décision d’outillage
Contexte et capacités nécessaires :
Options évaluées :
Critères pondérés :
Décision :
Pourquoi maintenant :
Conséquences positives :
Risques et coût de sortie :
Sécurité et provenance :
Version/capacités vérifiées :
Pilote et résultats :
Conditions de révision :
```

## Plan de migration

```markdown
Périmètre et inventaire :
Mapping ancien → nouveau :
Exceptions intentionnelles :
Pilote :
Coexistence :
Automatisation et revue humaine :
Tests et comparaison :
Dépréciation :
Communication :
Métriques d’adoption :
Rollback :
Condition de retrait :
```

## Preuve de consommation

Pour chaque sortie, consigner :

- package et version ;
- produit et flow consommateur ;
- installation/build ;
- tokens ou composants utilisés ;
- thèmes et plateformes testés ;
- preuves statiques, rendues, accessibilité et produit ;
- divergences et contournements ;
- temps d’intégration et feedback ;
- décision : corriger, canoniser, maintenir local ou retirer.

## Checklist de livraison

- [ ] Contexte, objectif et non-objectifs explicites
- [ ] Sources de vérité attribuées
- [ ] Taxonomie et axes de variation justifiés
- [ ] Fondations calibrées sur les usages
- [ ] Contrats composants et états complets
- [ ] Mapping Figma/code vérifié
- [ ] Builds et artefacts déterministes
- [ ] Preuves accessibilité et responsive
- [ ] Thèmes, marques ou tenants vérifiés lorsqu’ils sont inclus dans le périmètre
- [ ] Deuxième consommation ou limite déclarée
- [ ] Version, provenance et migration
- [ ] Documentation du chemin recommandé
- [ ] Risques non vérifiés clairement signalés
