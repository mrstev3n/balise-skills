# Structurer Figma et relier le design au code

## Sommaire

1. [Définir les autorités](#définir-les-autorités)
2. [Auditer le fichier](#auditer-le-fichier)
3. [Choisir variables ou styles](#choisir-variables-ou-styles)
4. [Structurer collections, groupes et modes](#structurer-collections-groupes-et-modes)
5. [Mapper Figma vers les tokens](#mapper-figma-vers-les-tokens)
6. [Aligner composants design et code](#aligner-composants-design-et-code)
7. [Organiser le passage au front-end](#organiser-le-passage-au-front-end)
8. [Vérifier la synchronisation](#vérifier-la-synchronisation)

## Définir les autorités

Ne jamais commencer par synchroniser automatiquement. Définir quelle représentation fait autorité pour chaque vérité :

| Vérité | Autorité possible | Miroir |
|---|---|---|
| intention et usage | documentation versionnée | descriptions Figma et portail |
| valeur agnostique et alias | source portable versionnée | variables Figma |
| composition visuelle | composant Figma gouverné | story et composant code |
| API et comportement | implémentation typée et testée | propriétés de composant Figma |
| rendu final | produit exécuté | preview Figma |

Choisir un sens de synchronisation par artefact : code → Figma, Figma → code, ou proposition bidirectionnelle avec arbitrage. Éviter toute double écriture silencieuse.

## Auditer le fichier

Inventorier :

- fichiers, pages, bibliothèques publiées et dépendances ;
- styles couleur, texte, effet et grille ;
- variables, types, collections, groupes, modes et scopes ;
- alias et valeurs détachées ;
- composants, variants, propriétés, slots et instances détachées ;
- auto layout, contraintes, grilles et comportements responsive ;
- descriptions, statuts, propriétaires et usages ;
- doublons, anciennes versions et éléments locaux non publiés.

Mesurer au minimum : valeurs uniques, usages par valeur, taux d’application des variables, nombre de styles proches, alias directs vers primitives, instances détachées, variants combinatoires et divergences design/code.

Classer chaque élément : canonique, candidat, legacy, local justifié, doublon ou inconnu.

## Choisir variables ou styles

Les variables Figma représentent des valeurs contextuelles et peuvent s’aliaser entre variables de même type. Les modes font varier leurs valeurs selon un contexte. Les styles restent adaptés à des compositions réutilisables que les variables ne représentent pas seules.

| Besoin | Préférer |
|---|---|
| couleur, nombre, chaîne, booléen, timing ou easing contextuel | variable |
| alias primitive → sémantique | variable |
| thème clair/sombre, marque, densité ou contexte | mode si la modélisation reste lisible |
| typographie composée | style texte alimenté par variables lorsque possible |
| gradient, effet ou composition non tokenisable proprement | style documenté |
| comportement, accessibilité ou responsive | composant et code, pas variable seule |

Ne pas convertir tous les styles en variables par dogme. Ne pas conserver un style simple seulement par habitude si une variable améliore modes, alias et inspection.

## Structurer collections, groupes et modes

Une collection exprime un ensemble qui partage des modes et un cycle de publication. Un groupe organise la découverte à l’intérieur d’une collection ; il n’ajoute pas un axe de variation.

Axes possibles : marque, schéma de couleur, contraste, densité, plateforme, viewport, langue. Ne pas mettre automatiquement chaque axe en mode : le produit cartésien devient vite impossible à maintenir.

Choisir la structure en répondant à :

1. Quelles variables changent ensemble ?
2. Qui possède cette variation ?
3. Quels modes doivent être prévisualisés ensemble ?
4. Quelles limites de plan ou d’outil s’appliquent ?
5. Le runtime représente-t-il réellement ce même axe ?

Séparer généralement primitives et sémantiques si cela clarifie l’authoring et limite l’exposition. Garder les primitives privées quand les consommateurs doivent choisir un rôle.

## Mapper Figma vers les tokens

Produire un manifeste de correspondance :

| Champ | Exemple |
|---|---|
| identifiant stable design | variable Figma ou clé contrôlée |
| nom design | `Color/Semantic/Text/Default` |
| token portable | `color.semantic.text.default` |
| variable runtime | `--ds-color-text-default` |
| type | color |
| modes | light, dark |
| statut | canonical |
| propriétaire | foundations |
| preuve | story et page produit |

Ne pas supposer qu’un slash Figma, un chemin DTCG et un identifiant CSS doivent être identiques. Préserver une correspondance déterministe et documentée tout en respectant chaque environnement.

Détecter : alias cassés, types incompatibles, valeurs non représentables, arrondis, espaces colorimétriques, unités implicites et métadonnées perdues.

## Aligner composants design et code

Comparer le contrat, pas seulement le nom :

- anatomie et slots ;
- variants et propriétés ;
- états interactifs et asynchrones ;
- contenu et localisation ;
- densité et responsive ;
- thème, contraste et RTL ;
- clavier, focus, rôles et annonces ;
- composition et escape hatches.

Une propriété booléenne Figma n’implique pas automatiquement une prop publique. Un variant visuel peut être un état géré par le composant. Une possibilité technique du code n’a pas besoin d’être exposée à tous les designers.

Maintenir une matrice de lineage : composant Figma, composant code, version, statut, propriétaire, couverture de stories et divergences intentionnelles.

## Organiser le passage au front-end

Parcours recommandé :

```text
inventaire Figma et code
→ modèle de responsabilités
→ mapping des fondations
→ pilote sur un flow produit réel
→ génération ou adaptation des tokens
→ implémentation de quelques composants
→ comparaison rendue
→ correction du contrat
→ seconde consommation
→ publication progressive
```

Pour le handoff, fournir noms inspectables, usage attendu, états, contenu extrême, tailles, contraintes, responsive, modes et lien vers la source/version. Ne pas remplacer ce contrat par une simple mesure de pixels dans Dev Mode.

## Vérifier la synchronisation

Exiger :

- export ou lecture déterministe de la source autorisée ;
- diff des valeurs, types, alias, modes et statuts ;
- vérification des tokens appliqués à des instances réelles ;
- comparaison visuelle sur thèmes, viewports et contenus ;
- test du package dans le front-end ;
- revue des divergences intentionnelles ;
- rollback et historique versionné.

Distinguer quatre preuves : parité structurelle, parité de valeurs, parité rendue et équivalence d’usage. Aucune ne remplace les autres.

## Source officielle à revérifier

- [Figma — variables, collections et modes](https://help.figma.com/hc/en-us/articles/14506821864087-Overview-of-variables-collections-and-modes)

Les capacités, types, limites de modes et plans Figma évoluent : les revérifier avant toute architecture ou automatisation.
