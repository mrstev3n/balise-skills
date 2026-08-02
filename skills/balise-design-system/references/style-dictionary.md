# Style Dictionary comme compilateur de tokens

## Sommaire

1. [Le situer correctement](#le-situer-correctement)
2. [Décider s’il est utile](#décider-sil-est-utile)
3. [Modéliser le cycle de build](#modéliser-le-cycle-de-build)
4. [Structurer source, configuration et sorties](#structurer-source-configuration-et-sorties)
5. [Préserver sémantique et alias](#préserver-sémantique-et-alias)
6. [Construire pour plusieurs plateformes](#construire-pour-plusieurs-plateformes)
7. [Tester et publier](#tester-et-publier)
8. [Éviter les pièges](#éviter-les-pièges)

## Le situer correctement

Style Dictionary est un système de build pour parser des tokens, les combiner, les transformer puis produire des artefacts adaptés à plusieurs plateformes. Il est utile comme couche de compilation, pas comme doctrine de design.

Séparer les responsabilités :

| Couche | Responsabilité | Exemple |
|---|---|---|
| stratégie | décider quelles décisions doivent être partagées | primitives privées, rôles sémantiques publics |
| contrat portable | représenter types, valeurs, alias et métadonnées | fichiers DTCG versionnés |
| compilation | adapter sans réécrire l’intention | Style Dictionary ou transformeur équivalent |
| distribution | exposer une API stable par plateforme | CSS, TypeScript, Swift, Android XML/Compose |
| consommation | appliquer les décisions dans un produit réel | composants et applications |

Style Dictionary ne décide pas :

- du bon périmètre du système ;
- de la taxonomie primitive/sémantique/composant ;
- du sens d’un token ;
- de la qualité d’une rampe ou d’une échelle typographique ;
- de l’accessibilité du rendu ;
- de la gouvernance et du parcours consommateur.

## Décider s’il est utile

Le considérer sérieusement lorsque plusieurs de ces conditions existent :

- plusieurs plateformes ou formats de sortie ;
- conversions de noms, unités, couleurs ou valeurs composites ;
- besoin de packages reproductibles et versionnés ;
- alias partagés entre plusieurs fichiers ;
- marques, thèmes ou produits qui combinent un noyau et des surcharges ;
- besoin de formats, filtres ou transforms spécialisés ;
- volonté de tester la même source contre plusieurs consommateurs.

Un script plus petit peut suffire lorsque la source est minuscule, la sortie unique et la transformation triviale. Comparer coût d’adoption, surface de configuration, dépendance Node, maintenance des hooks, compatibilité DTCG et coût de sortie.

Décision attendue : `adopter`, `piloter`, `différer` ou `écarter`, accompagnée des capacités nécessaires et d’une preuve sur un échantillon réel.

## Modéliser le cycle de build

Le cycle documenté par Style Dictionary est :

```text
configuration
→ découverte des sources
→ parsing des fichiers
→ fusion profonde
→ préprocesseurs globaux ou plateforme
→ expansion éventuelle des composites
→ transforms ordonnés par plateforme
↔ résolution des références et transforms transitifs
→ filtres par fichier
→ formats et en-têtes
→ actions post-build
→ artefacts consommables
```

Ne pas simplifier ce cycle en « JSON vers CSS ». Chaque frontière peut modifier le contrat ou perdre de l’information.

Employer le mécanisme le moins puissant qui suffit :

| Extension | Portée | Usage légitime |
|---|---|---|
| parser | un fichier source | lire un format non pris en charge |
| preprocessor | dictionnaire fusionné | opération globale impossible token par token |
| transform | un token | adapter nom, attribut ou valeur à une plateforme |
| transform group | suite ordonnée | rendre une politique de plateforme réutilisable |
| filter | sortie d’un fichier | sélectionner l’API publique ou un sous-ensemble |
| format | fichier produit | sérialiser dans le langage cible |
| action | après génération | copier un actif ou réaliser une opération adjacente bornée |

Les préprocesseurs ont un rayon d’action large. Les réserver aux opérations qui exigent réellement la vue complète du dictionnaire.

## Structurer source, configuration et sorties

Préférer cette séparation :

```text
tokens/                 # source portable, lisible et versionnée
  primitive/
  semantic/
  component/            # seulement si justifié
config/                 # plateformes, thèmes et politiques de sortie
transforms/             # extensions testées et nommées par intention
formats/                # sérialisation propre aux consommateurs
dist/                   # artefacts générés, jamais édités à la main
tests/                  # fixtures, snapshots et smoke tests consommateurs
```

La séparation des fichiers d’entrée est une ergonomie d’auteur : Style Dictionary réalise une fusion profonde. Elle ne doit pas déterminer accidentellement la taxonomie publique. Détecter les collisions, surcharges silencieuses et dépendances à l’ordre des sources.

Garder la configuration déterministe : version épinglée, globs explicites, ordre des transforms documenté, chemins de sortie stables et absence de données dépendantes de la machine.

## Préserver sémantique et alias

Style Dictionary prend en charge le format DTCG depuis la version 4, mais sa documentation actuelle avertit que le format DTCG 2025.10 n’est pas encore intégralement supporté. Tester les fonctionnalités réellement utilisées, notamment types composites, couleurs, extensions, groupes et références.

Règles :

- ne pas mélanger syntaxe historique `value/type/comment` et syntaxe DTCG `$value/$type/$description` dans une même instance ;
- garder les alias dans la source canonique ;
- décider par sortie s’il faut résoudre les alias ou conserver des références avec `outputReferences` ;
- tester les chaînes d’alias et les transforms transitifs ;
- ne pas utiliser CTI comme taxonomie par défaut seulement parce qu’un ancien helper l’encourage ;
- ne pas convertir automatiquement un ancien corpus vers DTCG sans revoir les types et la sémantique : le convertisseur officiel ne corrige pas toutes les anciennes valeurs de type.

Préserver une référence en CSS peut maintenir la relation entre variables sémantiques et primitives. La résoudre en Swift ou Android peut être nécessaire selon le runtime. Ce choix appartient au contrat de sortie, pas à une règle universelle.

## Construire pour plusieurs plateformes

Chaque plateforme doit repartir de la même source avant ses transformations propres. Les transforms sont ordonnés et non destructifs entre plateformes ; leur ordre fait donc partie du contrat technique.

Pour chaque plateforme, préciser :

- consommateurs et version minimale ;
- convention de nommage publique ;
- unités et conversions autorisées ;
- traitement des couleurs et du gamut ;
- expansion ou conservation des composites ;
- conservation ou résolution des références ;
- fichiers, modules et exports publics ;
- stratégie de thème/marque/mode ;
- tests d’intégration attendus.

Ne pas forcer les termes CSS dans les APIs Swift ou Android. Les noms sémantiques peuvent rester cohérents tandis que leur syntaxe et leur représentation suivent les conventions natives.

## Tester et publier

Une preuve minimale comprend :

1. validation du format source contre la version DTCG ciblée ;
2. détection des collisions, références manquantes et cycles ;
3. build propre de chaque plateforme ;
4. snapshot ou diff lisible des artefacts ;
5. second build identique pour prouver le déterminisme ;
6. tests unitaires des transforms, filtres et formats personnalisés ;
7. smoke test dans au moins un consommateur réel par famille de sortie ;
8. vérification de l’API publique et des primitives privées ;
9. provenance, version du transformeur et changelog dans la release ;
10. rollback ou régénération depuis la source.

Ne pas accepter « le build passe » comme seule preuve. Un transform peut produire une valeur syntaxiquement valide mais sémantiquement incorrecte, inaccessible ou incompatible avec un runtime.

## Éviter les pièges

- Ne pas faire de la configuration Style Dictionary la source de stratégie ou d’intention.
- Ne pas éditer `dist/` ni recopier manuellement ses fichiers dans les produits.
- Ne pas dépendre implicitement de l’ancien format ou des anciennes APIs vues dans un ouvrage.
- Ne pas multiplier les transforms personnalisés avant d’évaluer les capacités natives.
- Ne pas effectuer dans une `action` une publication ou une mutation externe non explicitement autorisée.
- Ne pas exposer toutes les primitives parce qu’un format sait les sérialiser.
- Ne pas confondre fusion de fichiers, héritage de thèmes et alias sémantique.
- Ne pas supposer la compatibilité complète avec la dernière spécification DTCG.

## Sources officielles à revérifier

- [Architecture](https://styledictionary.com/info/architecture/)
- [Design Tokens et compatibilité DTCG](https://styledictionary.com/info/tokens/)
- [État du support DTCG](https://styledictionary.com/info/dtcg/)
- [Configuration](https://styledictionary.com/reference/config/)
- [Transforms](https://styledictionary.com/reference/hooks/transforms/)
- [Exemples multi-plateformes et multi-marques](https://styledictionary.com/getting-started/examples/)

Revérifier ces pages avant de prescrire une version, une API ou une capacité : l’outil et son support DTCG évoluent.
