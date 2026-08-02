# Gouvernance et maturité

## Sommaire

- [Objet et routage](#objet-et-routage)
- [Principe directeur](#principe-directeur)
- [Choisir le modèle de gouvernance](#choisir-le-modèle-de-gouvernance)
- [Attribuer les responsabilités](#attribuer-les-responsabilités)
- [Définir les niveaux de maturité](#définir-les-niveaux-de-maturité)
- [Promouvoir une décision](#promouvoir-une-décision)
- [Traiter les contributions](#traiter-les-contributions)
- [Gouverner les exceptions](#gouverner-les-exceptions)
- [Classer les releases](#classer-les-releases)
- [Déprécier et retirer](#déprécier-et-retirer)
- [Organiser le support](#organiser-le-support)
- [Mesurer la santé et la valeur](#mesurer-la-santé-et-la-valeur)
- [Conduire la revue de gouvernance](#conduire-la-revue-de-gouvernance)
- [Livrables et critères d’acceptation](#livrables-et-critères-dacceptation)
- [Limites et anti-patterns](#limites-et-anti-patterns)
- [Router vers les autres références](#router-vers-les-autres-références)

## Objet et routage

Lire cette référence pour :

- définir ownership, arbitrage, contribution et support ;
- choisir une gouvernance centralisée, fédérée ou hybride ;
- gérer le passage du local au canonique ;
- qualifier l’impact d’une release au-delà de SemVer ;
- organiser dépréciation, migration et retrait ;
- mesurer adoption, santé technique, qualité et valeur du système.

Lire `strategy-and-scope.md` avant de créer un modèle d’équipe. La gouvernance doit correspondre au portefeuille et à la capacité réelle, pas à un organigramme idéal.

## Principe directeur

Gouverner les décisions et leur cycle de vie, pas seulement l’accès au dépôt.

Traiter le design system comme un service :

- une mission ;
- un canon ;
- des propriétaires ;
- des consommateurs ;
- une offre de support ;
- des règles de contribution ;
- une politique de changement ;
- une mesure de la santé et de la valeur.

Rendre le processus proportionné au rayon d’impact. Éviter la même procédure pour une correction documentaire et une rupture de contrat multi-plateforme.

## Choisir le modèle de gouvernance

| Modèle | Pouvoir de décision | Contribution | À choisir si | Risque |
|---|---|---|---|---|
| Centralisé | Équipe système | Proposée puis revue | Cohérence critique, équipe dédiée | Goulot et éloignement produit |
| Fédéré | Domaines ou plateformes | Produite localement sous contrat commun | Expertise distribuée | Divergence et dilution de responsabilité |
| Hybride | Canon central, décisions locales bornées | Co-production avec maintainers | Portefeuille complexe | Frontières et arbitrages ambigus |

Définir explicitement :

- ce qui est canonique et commun ;
- ce qui appartient aux domaines ;
- qui tranche un conflit ;
- quels invariants ne peuvent pas être contournés ;
- comment une innovation locale remonte ;
- comment une équipe sort ou entre dans le périmètre.

## Attribuer les responsabilités

Attribuer des personnes ou équipes nommées, pas seulement des rôles abstraits.

| Activité | Responsable principal | Participants requis | Preuve |
|---|---|---|---|
| Priorité et roadmap | Owner produit du système | Design, engineering, consommateurs | Décision et critères publiés |
| Doctrine design | Responsable design | Recherche, marque, accessibilité | Principes et revues |
| Architecture et distribution | Responsable engineering | Maintainers de plateformes | ADR, builds et tests |
| Qualité accessibilité | Owner identifié | Design, engineering, experts | Matrice et vérification humaine |
| Contribution | Maintainer du domaine | Auteur et consommateurs | Décision tracée |
| Release | Release owner | Owners impactés | Checklist et rollback |
| Support | Rotation ou équipe nommée | Maintainers concernés | Canal, délai et escalade |

Ne pas créer une matrice RACI détaillée sans besoin. S’assurer au minimum qu’une personne peut décider, exécuter, revoir et soutenir chaque changement.

## Définir les niveaux de maturité

Utiliser le cycle :

`local → expérimental → candidat → canonique → déprécié → retiré`

### Local

- Servir un contexte limité.
- Autoriser l’apprentissage rapide.
- Ne pas promettre de stabilité transversale.
- Documenter le propriétaire si la solution peut durer.

### Expérimental

- Exposer l’hypothèse et les limites.
- Identifier les premiers consommateurs.
- Autoriser les changements rapides annoncés.
- Collecter les contournements et défauts.

### Candidat

- Démontrer une seconde consommation ou un cas critique justifié.
- Stabiliser le contrat public pressenti.
- Préparer documentation, tests, distribution et ownership.
- Traiter les décisions encore ouvertes.

### Canonique

- Publier une intention et une API stables.
- Fournir versions, tests, documentation et support.
- Interdire les contournements silencieux des invariants.
- Mesurer adoption et qualité.

### Déprécié

- Conserver temporairement la compatibilité annoncée.
- Fournir remplacement, délai et chemin de migration.
- Mesurer les consommateurs restants.

### Retiré

- Supprimer seulement après la fenêtre annoncée ou preuve d’absence d’usage.
- Livrer la rupture selon la politique de version.
- Conserver la trace de décision et de migration.

Si les statuts sont stockés dans DTCG, utiliser une extension documentée pour les maturités non standard. Réserver `$deprecated` à la dépréciation selon le format supporté.

## Promouvoir une décision

Exiger avant promotion :

| Passage | Preuve minimale |
|---|---|
| Local → expérimental | Problème, owner, hypothèse et contexte documentés |
| Expérimental → candidat | Valeur observée, réemploi ou criticité, API révisée |
| Candidat → canonique | Contrat stable, tests, docs, distribution, support et migration |
| Canonique → déprécié | Remplacement, analyse d’impact, fenêtre et communication |
| Déprécié → retiré | Inventaire d’usage, migration achevée, version et rollback définis |

Une obligation d’accessibilité, de sécurité, légale ou de marque peut justifier une promotion ou correction accélérée. Documenter l’exception et la preuve.

Ne pas promouvoir sur la seule base de la popularité, de l’effort investi ou du nombre de demandes.

## Traiter les contributions

Appliquer un processus proportionné :

1. Qualifier le manque : local, systémique ou déjà couvert.
2. Décrire problème, contextes et résultat attendu.
3. Fournir les preuves de répétition ou de criticité.
4. Examiner composition, extension et adaptation avant création.
5. Identifier consumers, owners et rayon d’impact.
6. Proposer contrat, états, accessibilité, contenu et migration.
7. Revoir design et engineering ensemble.
8. Prototyper dans un flow puis un second contexte.
9. Décider statut, version et communication.
10. Fermer avec documentation, tests et responsabilité de maintenance.

Demander une RFC complète pour un changement transversal ou difficilement réversible. Utiliser une issue courte pour une correction bornée et évidente.

## Gouverner les exceptions

Autoriser une exception seulement si elle précise :

- l’invariant contourné ;
- le besoin qui l’exige ;
- les alternatives évaluées ;
- le risque créé ;
- le propriétaire ;
- la durée ou condition de réexamen ;
- la méthode de détection ;
- la stratégie de retour au canon si applicable.

| Type d’exception | Traitement |
|---|---|
| Variation métier durable | Modéliser dans le domaine ou comme extension |
| Contrainte de plateforme | Adapter la sortie, préserver l’intention |
| Dette temporaire | Enregistrer migration et échéance |
| Besoin unique | Garder local, ne pas élargir l’API |
| Invariant critique | Refuser ou escalader vers l’autorité compétente |

## Classer les releases

Utiliser SemVer pour le contrat public, puis ajouter une matrice d’impact.

| Axe | Question | Traitement requis |
|---|---|---|
| API | Nom, type, prop ou sortie cesse-t-il de fonctionner ? | SemVer, compatibilité, guide ou codemod |
| Visuel | Marque, hiérarchie, contraste ou géométrie changent-ils ? | Diffs multi-thèmes, annonce et rollback |
| Comportement | Interaction, focus, état ou layout changent-ils ? | Tests de flows et communication |
| Accessibilité | Usage d’assistance ou préférence utilisateur change-t-il ? | Vérification humaine et migration ciblée |
| Rayon | Combien de produits, thèmes et plateformes ? | Canary, coexistence, cadence et support |

Ne pas considérer automatiquement une valeur de token modifiée comme un patch sans examiner son impact visuel et comportemental.

Pour chaque release, fournir :

- portée et statut ;
- axes d’impact ;
- consommateurs concernés ;
- preuves avant/après ;
- actions requises ;
- fenêtre et owner de migration ;
- rollback ;
- canal de support.

## Déprécier et retirer

1. Inventorier les usages réels.
2. Choisir et documenter le remplacement.
3. Annoncer la dépréciation dans le code, les types et la documentation.
4. Fournir guide, mapping ou codemod quand possible.
5. Définir une fenêtre compatible avec la cadence des consommateurs.
6. Mesurer les versions et usages restants.
7. Accompagner les cas bloqués.
8. Vérifier l’absence d’usage ou accepter explicitement la rupture.
9. Retirer dans la version appropriée.
10. Vérifier build, rendu, comportement et migration.

Ne pas supprimer une API parce qu’elle semble inutilisée dans le seul dépôt inspecté si des consommateurs externes sont possibles.

## Organiser le support

Définir :

- canal d’entrée unique et visible ;
- catégories de demande ;
- niveau de service réaliste ;
- rotation ou propriétaire ;
- règle d’escalade ;
- heures ou zones couvertes ;
- format de reproduction ;
- boucle vers roadmap, documentation ou correctif.

Transformer les demandes répétées en signal d’API, de documentation ou d’onboarding. Ne pas traiter chaque question comme une faute du consommateur.

## Mesurer la santé et la valeur

Combiner métriques quantitatives et retours qualitatifs.

| Dimension | Indicateurs possibles | Limite |
|---|---|---|
| Adoption | Composants canoniques, tokens sémantiques, versions | Usage ne prouve pas satisfaction |
| Divergence | Valeurs brutes, forks, doublons, overrides | Une différence peut être légitime |
| Livraison | Délai de contribution, release et migration | La vitesse seule peut masquer la qualité |
| Qualité | Régressions, défauts a11y, changements cassants | Les tests automatisés restent partiels |
| Service | Temps de réponse, résolution, demandes répétées | Fermer un ticket ne prouve pas l’autonomie |
| Valeur | Temps gagné sur flows témoins, risque évité | Établir un état initial comparable |
| Expérience | Satisfaction, confiance, compréhension | Échantillonner plusieurs rôles |

Aligner les indicateurs sur les objectifs du cadrage. Éviter un tableau de bord exhaustif sans décision associée.

## Conduire la revue de gouvernance

À une cadence adaptée :

1. examiner objectifs et périmètre ;
2. vérifier owners et capacité ;
3. analyser adoption, divergence, qualité et support ;
4. revoir actifs expérimentaux, candidats et dépréciés ;
5. traiter exceptions arrivées à échéance ;
6. prioriser migrations et dette du système ;
7. confronter doctrine et besoins produit émergents ;
8. décider, nommer les responsables et dater la prochaine preuve.

Remplacer les règles devenues fausses. Ne pas empiler les décisions historiques contradictoires.

## Livrables et critères d’acceptation

Livrer au minimum :

- modèle de gouvernance et frontières ;
- responsabilités nommées ;
- politique de maturité ;
- processus de contribution proportionné ;
- politique d’exception ;
- matrice d’impact des releases ;
- politique de dépréciation et retrait ;
- offre de support ;
- objectifs, indicateurs et cadence de revue.

Accepter la gouvernance seulement si :

- chaque décision importante possède une autorité ;
- un contributeur sait quel processus suivre ;
- un consommateur sait où obtenir de l’aide ;
- le statut d’un actif détermine ses garanties ;
- une release expose ses impacts réels ;
- une dépréciation fournit remplacement et fenêtre ;
- les mesures déclenchent des décisions explicites ;
- le modèle reste soutenable par les personnes disponibles.

## Limites et anti-patterns

- Éviter le comité sans pouvoir d’arbitrage.
- Éviter l’équipe centrale comme guichet obligatoire pour toute correction.
- Éviter la fédération sans canon, invariants ou propriétaires.
- Éviter la RFC lourde pour tout changement.
- Éviter la contribution sans responsabilité de maintenance.
- Éviter les exceptions silencieuses et permanentes.
- Éviter le changelog purement technique sans impact consommateur.
- Éviter la suppression sans inventaire des usages.
- Éviter de mesurer seulement le volume du catalogue.
- Éviter de publier ou déployer sans autorisation explicite.

## Router vers les autres références

- Lire `strategy-and-scope.md` pour choisir le modèle selon le portefeuille et les continuums.
- Lire `audits-and-pilots.md` pour produire les preuves de promotion.
- Lire `consumption-and-learning.md` pour onboarding, support et autonomie.
- Lire `implementation-pipelines.md` pour version, distribution, canary et rollback.
- Lire `implementation-pipelines.md` pour définir les preuves de release et de migration.
- Revenir au standard de vérité du `SKILL.md` avant de reprendre une recette de livre ou un outil historique.
