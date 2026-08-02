# Audits et pilotes

## Sommaire

- [Objet et routage](#objet-et-routage)
- [Principe directeur](#principe-directeur)
- [Préparer l’audit](#préparer-laudit)
- [Conduire l’audit à quatre vues](#conduire-laudit-à-quatre-vues)
- [Inventorier par finalité](#inventorier-par-finalité)
- [Qualifier les écarts](#qualifier-les-écarts)
- [Synthétiser les preuves](#synthétiser-les-preuves)
- [Choisir un pilote](#choisir-un-pilote)
- [Définir le contrat du pilote](#définir-le-contrat-du-pilote)
- [Exécuter la boucle pilote](#exécuter-la-boucle-pilote)
- [Évaluer la seconde consommation](#évaluer-la-seconde-consommation)
- [Décider après le pilote](#décider-après-le-pilote)
- [Livrables et critères d’acceptation](#livrables-et-critères-dacceptation)
- [Limites et anti-patterns](#limites-et-anti-patterns)
- [Router vers les autres références](#router-vers-les-autres-références)

## Objet et routage

Lire cette référence pour :

- auditer un système existant ou les actifs qui pourraient le devenir ;
- identifier répétitions, divergences, dettes et variations légitimes ;
- comparer design, code, produit et documentation ;
- sélectionner une tranche pilote ;
- prouver qu’une abstraction fonctionne au-delà de son contexte d’origine ;
- décider de conserver localement, corriger, promouvoir ou abandonner une solution.

Lire d’abord `strategy-and-scope.md` si le problème, les produits ou les responsabilités ne sont pas cadrés.

## Principe directeur

Observer avant de normaliser. Auditer les décisions et les usages, pas seulement les fichiers ou les composants nommés.

Rechercher les causes de variation :

- intention produit ;
- besoin de marque ;
- contrainte de plateforme ;
- dette ou accident historique ;
- absence de règle ;
- incompatibilité technique ;
- contournement d’une API insuffisante.

Ne pas déduire qu’une différence est une erreur avant d’avoir établi sa fonction.

## Préparer l’audit

Définir avant la collecte :

- question à résoudre ;
- périmètre et exclusions ;
- période ou version observée ;
- produits et parcours témoins ;
- sources accessibles ;
- responsables à interroger ;
- méthode de comptage ;
- format de preuve ;
- critères d’arrêt.

Conserver la provenance de chaque observation : fichier, composant, écran, URL, version, capture, commande ou entretien.

Échantillonner si le corpus est vaste. Décrire la méthode d’échantillonnage et ne pas généraliser au-delà de sa couverture.

## Conduire l’audit à quatre vues

### Vue marque

Inventorier :

- couleurs, typographies, iconographie, illustration et mouvement ;
- voix, ton, terminologie et formats éditoriaux ;
- signatures perceptives et règles de composition ;
- marques, sous-marques et expressions par canal ;
- invariants et adaptations autorisées.

Produire : une matrice **attribut → expression → contexte → propriétaire → source**.

### Vue produit

Inventorier :

- tâches, parcours, patterns fonctionnels et états ;
- contenu réel, erreurs, chargement, vide, permissions et succès ;
- responsive, densité, zoom, localisation et RTL ;
- comportements critiques et exigences d’accessibilité ;
- exceptions métier.

Produire : une carte **tâche → pattern → variantes → résultat attendu → risque**.

### Vue design

Inventorier :

- bibliothèques, variables, styles, composants et variants ;
- doublons, détachements, overrides et actifs locaux ;
- écarts de nommage, de structure et de maturité ;
- modes, thèmes et composants non publiés ;
- correspondance entre documentation et fichiers.

Produire : un inventaire **actif → usages → variations → autorité → statut**.

### Vue code

Inventorier :

- dépendances, packages, versions et frameworks ;
- valeurs brutes et déclarations dupliquées ;
- tokens, alias, thèmes et transformations ;
- composants partagés, forks et wrappers ;
- sélecteurs internes, overrides et contournements ;
- tests, stories, documentation et pipelines ;
- usages réels et versions en circulation.

Produire : une carte **déclaration → consommateurs → duplication → risque → chemin de migration**.

## Inventorier par finalité

Regrouper d’abord par problème ou résultat utilisateur, puis comparer les implémentations.

Préférer :

- « confirmer une action risquée » à « modales » ;
- « choisir une valeur unique » à « radios » ;
- « signaler un échec récupérable » à « alertes rouges » ;
- « structurer une page dense » à « cartes ».

Utiliser la décomposition atomique uniquement comme lentille secondaire pour étudier les relations partie–ensemble.

Pour chaque motif, relever :

| Champ | Question |
|---|---|
| Problème | Quel besoin résout-il ? |
| Contextes | Où apparaît-il ? |
| Anatomie | Quelles parties sont réellement invariantes ? |
| Variations | Lesquelles sont intentionnelles ? |
| États | Quels états et transitions existent ? |
| Contenu | Quelles données et longueurs supporte-t-il ? |
| Qualité | Quelles preuves d’accessibilité et de comportement ? |
| Usage | Combien de consommateurs et quelles versions ? |
| Ownership | Qui peut expliquer et maintenir la décision ? |

## Qualifier les écarts

Classer chaque différence avant toute fusion :

| Classe | Signification | Action probable |
|---|---|---|
| Invariant | Doit rester identique | Protéger dans le canon |
| Variation légitime | Répond à un contexte explicite | Modéliser comme axe ou extension |
| Dette | Différence sans valeur actuelle | Migrer progressivement |
| Expérience locale | Besoin encore peu prouvé | Garder local et observer |
| Conflit de doctrine | Deux règles incompatibles | Arbitrer avec owners et preuves |
| Inconnu | Cause non établie | Investiguer, ne pas normaliser |

Ne pas fusionner deux solutions seulement parce qu’elles se ressemblent. Ne pas séparer deux solutions seulement parce que leur code diffère.

## Synthétiser les preuves

Produire une synthèse qui sépare :

- fréquence observée ;
- impact utilisateur ou métier ;
- coût de divergence ;
- risque de migration ;
- capacité de maintenance ;
- qualité de la preuve ;
- décision proposée.

Utiliser une matrice compacte :

| Candidat | Répétition | Impact | Divergence | Faisabilité | Confiance | Décision |
|---|---:|---:|---:|---:|---:|---|
| Exemple | 3/5 | 5/5 | 4/5 | 4/5 | Moyenne | Tester en pilote |

Expliquer chaque note. Ne pas laisser un score masquer une incertitude importante.

## Choisir un pilote

Évaluer plusieurs candidats avec la même scorecard.

| Critère | Question | Bon signal |
|---|---|---|
| Valeur | Le résultat compte-t-il pour un utilisateur ou le métier ? | Effet observable sur un flow |
| Répétition | Contient-il des décisions récurrentes ? | Patterns partagés identifiables |
| Champion | Une équipe veut-elle réellement l’adopter ? | Owner et temps confirmés |
| Faisabilité | Peut-on livrer et vérifier rapidement ? | Dépendances maîtrisées |
| Indépendance | Peut-on isoler la tranche ? | Faible rayon de régression |
| Apprentissage | Teste-t-il les hypothèses d’architecture ? | Plusieurs couches ou contextes utiles |
| Visibilité | Le résultat peut-il démontrer la valeur ? | Comparaison compréhensible |
| Réemploi | Un second contexte est-il accessible ? | Consommateur distinct identifié |

Ne pas choisir le flow le plus simple s’il ne teste aucune hypothèse importante. Ne pas choisir le plus stratégique s’il rend l’apprentissage impossible dans un délai raisonnable.

## Définir le contrat du pilote

Écrire avant l’implémentation :

1. problème et résultat attendu ;
2. produit, flow et équipes concernés ;
3. hypothèses à tester ;
4. non-objectifs ;
5. périmètre des fondations, tokens et composants ;
6. contextes, thèmes et plateformes couverts ;
7. état initial et métriques ;
8. responsabilités ;
9. preuves à produire ;
10. règle de décision finale ;
11. plan de rollback ou coexistence ;
12. candidat à la seconde consommation.

Utiliser environ 3 à 7 composants comme heuristique d’apprentissage uniquement si ce volume couvre réellement le flow. Ne pas transformer ce nombre en quota.

## Exécuter la boucle pilote

1. Construire la solution dans le contexte source.
2. Extraire les décisions répétables.
3. Nommer et typer les contrats.
4. Documenter intention, limites et états.
5. Vérifier le flow source avec contenu réel.
6. Consommer dans un second contexte sans copier les détails locaux.
7. Observer les contournements, demandes et incompatibilités.
8. Corriger l’abstraction ou réduire son périmètre.
9. Mesurer le résultat par rapport à l’état initial.
10. Décider du statut et de la suite.

Produire documentation, tests et migration en même temps que l’implémentation. Ne pas les différer à la fin du pilote.

## Évaluer la seconde consommation

Considérer l’abstraction comme transférable seulement si le second contexte :

- importe le même contrat public ;
- n’exige pas de sélecteur interne fragile ;
- n’ajoute pas une prop opportuniste pour un cas unique ;
- conserve les invariants d’accessibilité et de comportement ;
- peut exprimer ses différences par composition, thème ou extension documentée ;
- produit un résultat vérifié dans son environnement réel.

Si la seconde consommation échoue, choisir explicitement :

- corriger l’API ;
- scinder le pattern ;
- conserver une variante locale ;
- reporter la canonisation ;
- abandonner l’abstraction.

## Décider après le pilote

| Décision | Conditions observables |
|---|---|
| Promouvoir candidat | Réemploi démontré, owners et preuves de qualité présents |
| Canoniser | Contrat stable, documentation, tests, distribution et support prêts |
| Itérer | Valeur confirmée mais architecture ou API encore instable |
| Garder local | Besoin réel mais non transversal ou fortement contextuel |
| Abandonner | Valeur insuffisante, coût ou risque supérieur au bénéfice |

Ne pas canoniser pour récompenser l’effort déjà investi.

## Livrables et critères d’acceptation

Livrer :

- périmètre et méthode de l’audit ;
- inventaires avec provenance ;
- carte des invariants, variations et dettes ;
- analyse des opportunités ;
- scorecard comparée des pilotes ;
- contrat du pilote retenu ;
- résultat avant/après ;
- preuves du contexte source et de la seconde consommation ;
- décision de maturité et prochaines actions.

Accepter le travail seulement si :

- chaque conclusion importante cite une preuve ;
- les inconnues restent visibles ;
- la variation intentionnelle est séparée de la dette ;
- le pilote teste une hypothèse d’architecture ;
- les états critiques et contextes annoncés sont vérifiés ;
- la décision finale découle de critères annoncés à l’avance.

## Limites et anti-patterns

- Éviter l’inventaire de captures sans analyse de finalité.
- Éviter les comptages non reproductibles ou sans périmètre.
- Éviter la palette avant l’inventaire des usages.
- Éviter le pilote vitrine déconnecté d’un produit réel.
- Éviter le happy path sans erreurs, chargement, vide ou contenu extrême.
- Éviter la promotion après une seule implémentation.
- Éviter le score composite non expliqué.
- Éviter le big bang proposé uniquement pour « repartir proprement ».
- Éviter de modifier des produits ou publier des packages sans autorisation explicite.

## Router vers les autres références

- Lire `strategy-and-scope.md` pour interpréter les preuves et fixer les frontières.
- Lire `color-and-typography.md` pour auditer les fondations visuelles.
- Lire `token-architecture.md` pour analyser valeurs, alias, types et dépendances.
- Lire `components-and-patterns.md` pour évaluer anatomie, états et réemploi.
- Lire `governance-and-maturity.md` pour décider du statut après pilote.
- Lire `implementation-pipelines.md` et `components-and-patterns.md` pour construire les preuves techniques et rendues.
- Lire `implementation-pipelines.md` pour industrialiser seulement après validation du pilote.
