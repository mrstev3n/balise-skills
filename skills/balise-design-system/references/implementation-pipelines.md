# Pipeline, distribution, tests et migration

## Sommaire

1. [Cartographier la chaîne](#cartographier-la-chaîne)
2. [Transformer](#transformer)
3. [Distribuer](#distribuer)
4. [Tester](#tester)
5. [Versionner](#versionner)
6. [Migrer](#migrer)
7. [Comparer les outils](#comparer-les-outils)

Pour une décision ou une implémentation fondée sur Style Dictionary, lire aussi [style-dictionary.md](style-dictionary.md).

## Cartographier la chaîne

Documenter :

- auteurs et outils d’édition ;
- format canonique ;
- validation ;
- transformations ;
- artefacts et plateformes ;
- packages et registries ;
- documentation ;
- consommateurs ;
- releases, mises à jour et télémétrie.

Employer un ADR pour les décisions structurelles.

## Transformer

Pipeline recommandé :

```text
parse → merge → preprocess → validate → resolve aliases
→ transform → filter → format → package → test
```

Préserver :

- types et unités ;
- alias ou provenance lorsque possible ;
- descriptions et dépréciations ;
- ordre déterministe ;
- métadonnées utiles ;
- compatibilité par plateforme.

Ne pas forcer un vocabulaire CSS sur iOS ou Android. Construire des adaptateurs au-dessus d’un noyau agnostique.

## Distribuer

Comparer :

| Canal | Utile si | Risque |
|---|---|---|
| package versionné | consommation logicielle régulière | upgrades différés |
| API | besoins dynamiques contrôlés | disponibilité et sécurité |
| CLI | génération locale explicite | versions divergentes |
| PR automatisée | nombreux dépôts | bruit et conflits |
| copie manuelle | prototype ponctuel | dérive immédiate |

Préférer packages, lockfiles, provenance, changelog et PR de mise à jour à la copie silencieuse.

Publier séparément tokens, icônes, composants ou thèmes lorsque leurs consommateurs et cadences diffèrent réellement.

## Tester

### Source

- schéma officiel et JSON avec un validateur compatible avec la version DTCG ciblée ;
- types et noms ;
- références, cycles et alias inter-types ;
- modes complets ;
- dépréciations et remplacements ;
- snapshots de sorties.

Utiliser `validate_dtcg.py` comme contrôle local ciblé des types courants, alias, cycles, références, unités et dépréciations. Le compléter par le schéma officiel et les tests du transformeur; le script ne prétend pas implémenter toute la spécification DTCG ni toutes les extensions d’outil.

### Packages

- build reproductible ;
- exports publics ;
- types ;
- compatibilité ;
- poids et performance ;
- provenance.

### Composants

- unit et interaction ;
- accessibilité automatique et manuelle ciblée ;
- régression visuelle ;
- thèmes, modes, états et viewports ;
- smoke tests dans plusieurs consommateurs.

### Migration

- dry-run ;
- mapping ;
- codemod/lint autofix ;
- coexistence ;
- rollback ;
- mesure d’adoption.

## Versionner

Employer SemVer pour le contrat structurel, puis qualifier séparément :

| Axe | Question |
|---|---|
| API | un consommateur cesse-t-il de compiler/fonctionner ? |
| visuel | marque, géométrie ou contraste changent-ils fortement ? |
| comportement | interaction, focus ou layout changent-ils ? |
| accessibilité | une technologie d’assistance ou préférence est-elle affectée ? |
| migration | quel rayon, effort et rollback ? |

Ne pas appliquer « valeur modifiée = patch » automatiquement.

Prévoir canary/bêta, release notes orientées impact et matrice de compatibilité lorsque le rayon est large.

## Migrer

1. Inventorier usages et versions.
2. Définir mapping ancien → nouveau.
3. Séparer migration mécanique et revue sémantique.
4. Fournir alias de compatibilité si utile.
5. Ajouter warnings, lint autofix et codemods.
6. Prévoir coexistence et date de retrait.
7. Tester diff et flows critiques.
8. Mesurer adoption et incidents.
9. Retirer seulement après preuve.

Pour les codemods, présenter les suggestions puis demander une revue humaine lorsque le contexte d’usage détermine le bon token.

## Comparer les outils

Évaluer capacités, pas notoriété :

- support DTCG réel ;
- types composites et espaces couleur ;
- alias, modes et thèmes ;
- transformations de plateforme ;
- extensibilité et portabilité ;
- source d’édition et conflits ;
- sécurité et hébergement ;
- CI, releases et provenance ;
- maintenance et communauté ;
- coût de sortie.

Vérifier les versions actuelles avant toute prescription. Les stacks Grunt, Bower, Hologram, anciennes APIs Style Dictionary ou copies inter-dépôts des ouvrages servent seulement d’histoire des capacités.
