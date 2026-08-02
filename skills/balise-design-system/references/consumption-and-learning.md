# Consommation, documentation et apprentissage

## Parcours consommateur

Concevoir :

| Étape | Question | Réponse du système | Preuve |
|---|---|---|---|
| découvrir | existe-t-il une solution ? | recherche, taxonomie, statut, owner | trouvable rapidement |
| évaluer | convient-elle ? | usages, non-usages, limites | décision sans lire la source |
| installer | comment démarrer ? | package, prérequis, exemple | écran témoin fonctionnel |
| composer | comment réaliser un flow ? | patterns, données, états | golden path complet |
| adapter | que puis-je changer ? | slots, thèmes, escape hatches | pas de sélecteur fragile |
| contribuer | local ou systémique ? | arbre de décision, RFC, revue | ownership et tests clairs |
| mettre à jour | quel impact ? | release, migration, codemod | effort estimable et vérifiable |

## Golden path

Fournir le chemin recommandé le plus court pour les cas fréquents. Révéler les détails et alternatives à la demande. Ne pas confondre exhaustivité et utilisabilité.

Inclure un exemple exécutable avec données, chargement, vide, erreur et succès lorsque le flow les comporte.

## Parcours par rôle

### Concevoir

Privilégier rôles sémantiques, composants, patterns, contenu et contraintes. Masquer les primitives autant que possible.

### Développer

Fournir packages, API, imports, types, exemples exécutables, tests, compatibilité et migration.

### Contribuer

Fournir critères d’entrée, preuve de réemploi, RFC/ADR, matrice d’états, reviewers et politique de release.

### Piloter

Fournir scope, statut, adoption, risques, roadmap et résultats produit/humains.

## Apprentissage progressif

Niveau 1 — réussir le premier usage : mission, installation, premier flow, erreurs fréquentes, support.

Niveau 2 — décider seul : recherche par tâche, quand utiliser/éviter, composition, limites, manque local ou systémique.

Niveau 3 — contribuer : principes, architecture, proposition, tests, migration, mentorat et autonomie.

## Documentation minimale à la publication

- finalité et statut ;
- quand utiliser et éviter ;
- exemple ou API ;
- états et contenu ;
- accessibilité ;
- propriétaire ;
- version et migration.

Approfondir selon risque, complexité, fréquence et rayon d’impact. Tester la findability par recherche ou card sorting lorsque le portail grandit.

## Support et feedback

Choisir des canaux soutenables : issues, canal de discussion, office hours, pairing, ateliers, enquêtes ou interviews. Énoncer les attentes de réponse.

Utiliser les questions récurrentes comme signal de documentation, d’API ou de vocabulaire défaillant.

## Mesurer le parcours

Observer :

- temps jusqu’au premier usage ;
- taux de réussite du golden path ;
- recherches sans résultat ;
- contournements et forks ;
- délai de contribution ;
- versions en circulation ;
- satisfaction et confiance ;
- incidents de migration.

Ne pas mesurer uniquement les visites du portail ou le nombre de composants.
