# Stratégie et périmètre

## Sommaire

- [Objet et routage](#objet-et-routage)
- [Principe directeur](#principe-directeur)
- [Entrées à réunir](#entrées-à-réunir)
- [Séquence de cadrage](#séquence-de-cadrage)
- [Définir la finalité](#définir-la-finalité)
- [Tracer le périmètre](#tracer-le-périmètre)
- [Diagnostiquer les trois continuums](#diagnostiquer-les-trois-continuums)
- [Choisir une stratégie de transformation](#choisir-une-stratégie-de-transformation)
- [Choisir une architecture proportionnée](#choisir-une-architecture-proportionnée)
- [Formuler les principes](#formuler-les-principes)
- [Définir la valeur et les critères de succès](#définir-la-valeur-et-les-critères-de-succès)
- [Produire le contrat de cadrage](#produire-le-contrat-de-cadrage)
- [Limites et garde-fous](#limites-et-garde-fous)
- [Router vers les autres références](#router-vers-les-autres-références)

## Objet et routage

Lire cette référence pour :

- créer ou recadrer un design system ;
- décider si un besoin justifie un système partagé ;
- délimiter produits, marques, plateformes, équipes et contraintes ;
- choisir un modèle strict ou souple, modulaire ou intégré, centralisé ou distribué ;
- arbitrer entre migration incrémentale, nouveau socle et refonte globale ;
- rédiger une stratégie, une charte ou une spécification de design system.

Ne pas utiliser cette référence seule pour définir les tokens, les composants ou le pipeline. Router vers les références spécialisées après cadrage.

## Principe directeur

Traiter le design system comme un produit partagé et une pratique de décision, pas comme une collection de composants.

Partir des produits, usages, plateformes et équipes réels. Ne pas commencer par une taxonomie, un outil ou une bibliothèque à reproduire.

Séparer quatre catégories de décisions :

| Catégorie | Question | Autorité probable |
|---|---|---|
| Norme d’échange | Quel format portable utiliser ? | Spécification officielle actuelle |
| Convention d’équipe | Comment nommer et contribuer ? | Accord documenté de l’organisation |
| Décision produit | Quels rôles et comportements servir ? | Recherche, contraintes et preuves produit |
| Expression de marque | Quelles valeurs et signatures appliquer ? | Direction de marque validée |

Ne pas présenter une convention locale comme une norme universelle.

## Entrées à réunir

Inspecter avant de recommander :

- produits, surfaces et parcours concernés ;
- marques, sous-marques, thèmes et modes ;
- plateformes, technologies, navigateurs et versions ;
- langues, scripts, formats de données et besoins RTL ;
- équipes productrices, mainteneuses et consommatrices ;
- composants, styles, tokens, fichiers de design et documentations existants ;
- contraintes d’accessibilité, performance, sécurité, légales et de marque ;
- dette, incohérences, lenteurs et incidents observés ;
- horizon du travail : prototype, produit, portefeuille ou plateforme ;
- capacité réelle de maintenance, support, migration et arbitrage.

Signaler explicitement toute entrée inconnue. Ne pas inventer la structure organisationnelle ou le portefeuille.

## Séquence de cadrage

1. Inspecter le réel et citer les preuves disponibles.
2. Formuler le problème sans supposer sa solution.
3. Définir la finalité partagée et les bénéficiaires.
4. Établir inclusions, exclusions et frontières.
5. Diagnostiquer les trois continuums organisationnels.
6. Choisir la stratégie de transformation.
7. Choisir l’architecture minimale capable de servir le périmètre.
8. Formuler des principes arbitrables.
9. Définir résultats attendus, indicateurs et preuves.
10. Faire valider le contrat de cadrage avant l’industrialisation.

Si le besoin est encore exploratoire, produire des hypothèses réversibles plutôt qu’une architecture définitive.

## Définir la finalité

Formuler la finalité sous la forme :

> Aider **[publics]** à **[résultat]** sur **[périmètre]**, en réduisant **[problèmes observés]**, sous **[contraintes]**.

Vérifier que la finalité :

- décrit un résultat produit ou organisationnel ;
- relie design, code, documentation, distribution et service ;
- permet d’arbitrer une demande de contribution ;
- ne se réduit pas à « harmoniser l’interface » ;
- reste compatible avec les variations légitimes.

Rejeter une finalité qui ne peut pas expliquer pourquoi une décision doit être partagée.

## Tracer le périmètre

Documenter chaque axe avec les valeurs **inclus**, **hors périmètre**, **à confirmer** ou **phase ultérieure**.

| Axe | Questions obligatoires | Décision observable |
|---|---|---|
| Produits | Quels produits et parcours ? | Liste nommée et propriétaire identifié |
| Surfaces | Marketing, application, back-office, mobile, embarqué ? | Frontière explicite par surface |
| Marques | Une ou plusieurs identités ? | Invariants et variations décrits |
| Contextes | Clair, sombre, contraste renforcé, densité ? | Axes de variation indépendants |
| Plateformes | Web, iOS, Android ou autres ? | Cibles et versions supportées |
| Contenu | Langues, scripts, texte long, données ? | Jeux d’essai et contraintes listés |
| Actifs | Tokens, composants, patterns, docs, outils ? | Livrables inclus et non-objectifs |
| Organisation | Qui décide, produit, maintient, consomme ? | Responsabilités et capacité confirmées |

Ne pas confondre thème, mode, marque, plateforme et produit. Modéliser ces axes séparément avant de les combiner.

## Diagnostiquer les trois continuums

Ne pas choisir une extrémité par préférence. Positionner chaque axe avec justification.

### Strict ↔ souple

Renforcer la conformité lorsque l’invariant protège :

- accessibilité ou sécurité ;
- marque réglementée ou engagement contractuel ;
- comportement critique ;
- interopérabilité multi-produit ;
- coût élevé de divergence.

Autoriser une dérogation documentée lorsque le domaine, le contexte ou l’apprentissage local apporte une valeur supérieure au coût de divergence.

### Modulaire ↔ intégré

Favoriser la modularité si les équipes composent des parcours variés à partir de primitives stables.

Favoriser des solutions intégrées si la valeur dépend d’un comportement métier, d’une orchestration ou d’un contexte fortement dirigé.

Ne pas exposer toutes les parties internes comme API publique.

### Centralisé ↔ distribué

Choisir selon l’emplacement réel de l’expertise et de la capacité d’arbitrage.

| Modèle | À privilégier si | Risque à contrôler |
|---|---|---|
| Centralisé | Peu de produits, équipe dédiée, cohérence critique | Goulot, éloignement du terrain |
| Fédéré | Expertise répartie, domaines autonomes | Divergence, responsabilité diffuse |
| Hybride | Canon commun et expertise locale | Processus trop lourd ou ambigu |

## Choisir une stratégie de transformation

| Stratégie | Choisir si | Premier mouvement | Risque principal |
|---|---|---|---|
| Incrémentale | Produit vivant, dette diffuse, faible tolérance au risque | Auditer puis piloter un flow réel | Coexistence prolongée |
| Nouveau socle | Nouveau produit ou rupture technologique assumée | Construire une tranche complète | Sur-conception sans consommation |
| Wholesale | Refonte financée, fenêtre de migration et ownership forts | Cartographier toutes les dépendances | Big bang, résistance, régression |
| Hybride | Certaines fondations doivent basculer ensemble | Fixer invariants globaux puis migrer par domaines | Frontière de migration floue |

Préférer l’incrémental en l’absence de preuve qu’une bascule globale est finançable, testable et réversible.

## Choisir une architecture proportionnée

| Situation | Architecture probable | Première preuve attendue |
|---|---|---|
| Produit unique jeune | Primitives, sémantiques et composants essentiels | Noyau consommé sur un flow |
| Produit existant incohérent | Couche de compatibilité et migration incrémentale | Carte des doublons et pilote sans régression |
| Portefeuille multi-produit | Sémantiques partagées, contextes par domaine | Matrice invariants/variations/owners |
| Multi-marque | Contrats sémantiques stables, valeurs par marque | Deux marques sur les mêmes composants |
| Multi-plateforme | Source portable, transformations par cible | Sorties générées et testées par plateforme |

N’ajouter une couche que si elle :

- exprime une décision distincte ;
- réduit une répétition ou protège un invariant ;
- possède une autorité et un cycle de vie ;
- peut être expliquée aux consommateurs ;
- est testable dans le pipeline ou le produit.

## Formuler les principes

Écrire trois à cinq principes spécifiques, mémorisables et actionnables.

Pour chaque principe, fournir :

- l’intention ;
- la décision qu’il permet d’arbitrer ;
- un exemple conforme ;
- un contre-exemple ;
- une limite ou exception légitime.

Éviter les slogans impossibles à contredire, comme « simple », « cohérent » ou « centré utilisateur », sans règle de décision associée.

## Définir la valeur et les critères de succès

Relier chaque objectif à un état initial, une cible, une méthode de mesure et un propriétaire.

| Angle | Exemple de signal | Preuve acceptable |
|---|---|---|
| Produit | Cohérence d’un flow, défauts évités | Comparaison rendue et tests |
| Engineering | Temps d’intégration, doublons, valeurs brutes | Mesure sur flow témoin et audit de code |
| Design | Temps de composition, variantes parallèles | Inventaire design avant/après |
| Accessibilité | Régressions et défauts critiques | Tests automatiques et vérification humaine |
| Adoption | Usage du canon, versions en circulation | Télémétrie ou inventaire reproductible |
| Service | Délai de support et contribution | Historique des demandes et décisions |

Ne pas utiliser le nombre de composants comme mesure principale de valeur.

## Produire le contrat de cadrage

Livrer au minimum :

1. contexte et preuves ;
2. problème ;
3. objectif ;
4. non-objectifs ;
5. publics et bénéficiaires ;
6. produits, marques, plateformes et contextes inclus ;
7. principes ;
8. continuums et modèle organisationnel ;
9. stratégie de transformation ;
10. architecture probable et hypothèses ;
11. workstreams ;
12. risques, dépendances et décisions ouvertes ;
13. critères d’acceptation observables ;
14. prochain pilote proposé.

Qualifier chaque affirmation comme **constat**, **décision**, **hypothèse** ou **question ouverte**.

## Limites et garde-fous

- Ne pas copier la granularité d’Atlassian, Primer, Carbon ou Material sans besoin démontré.
- Ne pas choisir un outil avant d’avoir défini les décisions à transporter.
- Ne pas promettre une source unique absolue ; définir une autorité par type de vérité.
- Ne pas imposer Atomic Design comme taxonomie canonique.
- Ne pas uniformiser une variation métier légitime.
- Ne pas industrialiser un modèle qu’aucune équipe ne peut maintenir.
- Ne pas présenter les exemples historiques des livres comme l’état actuel des systèmes cités.
- Revérifier formats, accessibilité et capacités d’outil dans leurs sources officielles actuelles.

## Router vers les autres références

- Lire `audits-and-pilots.md` pour inventorier le réel, prioriser et sélectionner un pilote.
- Lire `token-architecture.md` pour décider des couches, alias et types de tokens.
- Lire `components-and-patterns.md` pour définir primitives UI, composants et patterns.
- Lire `consumption-and-learning.md` pour concevoir l’installation, le golden path et l’onboarding.
- Lire `governance-and-maturity.md` pour ownership, contribution, canonisation, release et mesure.
- Lire `implementation-pipelines.md` pour source, transformations, distribution et protection.
- Lire `implementation-pipelines.md` et `components-and-patterns.md` pour transformer les critères en preuves exécutables.
