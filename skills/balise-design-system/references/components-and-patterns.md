# Composants et patterns

## Sommaire

1. [Taxonomie contractuelle](#taxonomie-contractuelle)
2. [Contrat de composant](#contrat-de-composant)
3. [Matrice d’états](#matrice-détats)
4. [Contrat de pattern](#contrat-de-pattern)
5. [Décider de la généralisation](#décider-de-la-généralisation)
6. [Prévenir la variant soup](#prévenir-la-variant-soup)
7. [Documenter un anti-pattern](#documenter-un-anti-pattern)
8. [Vérifier](#vérifier)

## Taxonomie contractuelle

Préférer :

```text
tokens → primitives UI → composants → compositions → patterns → templates/parcours
```

Utiliser Atomic Design comme lentille de décomposition si l’équipe le comprend. Ne pas l’imposer lorsque atome/molécule/organisme reste ambigu.

| Niveau | Responsabilité | Exemples |
|---|---|---|
| primitive technique | comportement accessible bas niveau | Slot, Portal, FocusTrap |
| primitive layout | relation spatiale | Stack, Inline, Grid |
| composant | unité avec API et états | Button, Field, Dialog |
| composition | assemblage récurrent | FieldGroup, Toolbar |
| pattern | solution à un problème contextualisé | recherche, upload, validation |
| template/parcours | structure avec données et flow | settings, checkout |

## Contrat de composant

Documenter :

- problème, finalité et non-usages ;
- anatomie, DOM, slots et composition ;
- props, types, valeurs par défaut et événements ;
- variants justifiés et combinaisons interdites ;
- contenu, microcopy et localisation ;
- clavier, focus, annonces et technologies d’assistance ;
- responsive, zoom, RTL, thèmes et modes ;
- tokens consommés et dépendances ;
- exemples avec données réalistes ;
- lineage, consommateurs, statut, version et migration.

## Matrice d’états

Sélectionner les états pertinents, puis justifier les exclusions :

- default, hover, focus-visible, active/pressed ;
- selected, disabled, read-only ;
- loading, skeleton, empty, partial ;
- success, warning, error ;
- offline, permission denied, expired ;
- contenu long, média manquant, zéro/un/beaucoup d’items ;
- clavier, tactile, reduced motion, high contrast, RTL et zoom.

Ne pas décrire uniquement le happy path.

## Contrat de pattern

Refuser une recommandation sans :

1. tâche utilisateur ;
2. problème ;
3. contexte ;
4. contraintes ;
5. solutions candidates ;
6. preuves ;
7. compromis et risques ;
8. décision et hypothèses ;
9. test ;
10. critère de succès.

Documenter quand utiliser, quand éviter, alternative, impact accessibilité, états requis et preuve à collecter.

## Décider de la généralisation

Conserver localement une occurrence unique. Déclencher une revue lorsque plusieurs usages convergent ou lorsqu’une exigence transverse le justifie.

Évaluer :

- finalité commune ;
- structure de contenu compatible ;
- comportement commun ;
- variation intentionnelle ;
- coût de l’abstraction ;
- capacité de maintenance ;
- second contexte indépendant.

Une exigence légale, de sécurité, d’accessibilité ou de marque peut justifier une correction et une revue accélérées. Maintenir néanmoins les preuves de contrat, qualité, ownership et consommation avant le statut canonique.

## Prévenir la variant soup

- Préférer composition aux props combinatoires.
- Nommer les variants par intention ou comportement.
- Écarter les variantes à usage unique.
- Séparer état, variante et contexte.
- Créer un pattern lorsque la logique dépasse le composant.
- Maintenir un registre d’exceptions légitimes.

## Documenter un anti-pattern

Consigner nom, symptômes, attrait local, contexte manquant, conséquences, prévention, récupération et alternatives. Chercher les causes organisationnelles et techniques avant de corriger l’apparence.

## Vérifier

Tester contrat public et invariants, pas seulement l’implémentation interne :

- unit et interaction ;
- HTML natif et accessibilité automatique ;
- clavier, focus et revue manuelle ciblée ;
- régression visuelle variant × état × thème × viewport ;
- contenu réel et extrême ;
- intégration dans un flow consommateur ;
- performance et poids si significatifs.
