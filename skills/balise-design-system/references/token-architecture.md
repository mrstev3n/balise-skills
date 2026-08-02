# Architecture des design tokens

## Sommaire

1. [Décider si les tokens sont nécessaires](#décider-si-les-tokens-sont-nécessaires)
2. [Modéliser les couches](#modéliser-les-couches)
3. [Définir les alias](#définir-les-alias)
4. [Traiter thèmes et modes](#traiter-thèmes-et-modes)
5. [Employer DTCG](#employer-dtcg)
6. [Contrôler la qualité](#contrôler-la-qualité)
7. [Éviter les anti-patterns](#éviter-les-anti-patterns)

## Décider si les tokens sont nécessaires

Tokeniser une décision lorsqu’au moins un besoin est démontré :

- réemploi dans plusieurs contextes ;
- propagation coordonnée d’un changement ;
- variation par marque, thème, mode ou plateforme ;
- synchronisation entre design et code ;
- contrôle, lint, migration ou mesure ;
- protection des consommateurs contre une valeur interne.

Conserver localement une valeur unique, stable et non variable. Ne pas créer une API publique pour chaque pixel.

Inventorier avant de modéliser :

- produits et packages consommateurs ;
- valeurs et variables existantes ;
- thèmes, modes, marques et plateformes ;
- propriétés qui changent ensemble ;
- valeurs identiques par accident ou intention ;
- propriétaires et fréquence de changement.

## Modéliser les couches

### Valeurs sources

Conserver les mesures ou données qui nourrissent le système : ancres de marque, métriques de fonte, courbes, unités et contraintes. Ne pas les exposer automatiquement.

### Primitives ou références

Nommer ce qu’est la valeur :

- `color.blue.600`
- `dimension.200`
- `font.weight.semibold`
- `duration.rapid`

Réserver ces tokens à l’aliasage, aux générateurs et aux cas expressément documentés.

### Sémantiques ou décisions

Nommer le rôle stable :

- `color.background.brand.bold`
- `color.text.danger`
- `color.border.focused`
- `space.stack.field`

Faire consommer cette couche par défaut. Porter les thèmes et modes par réassignation de ces rôles.

### Composants ou patterns

Créer une couche locale uniquement si elle :

- coordonne plusieurs propriétés propres au composant ;
- doit évoluer indépendamment du rôle global ;
- exprime une variabilité ou un contrat public réel ;
- réduit une ambiguïté répétée.

Éviter `button.primary.background.default` s’il ne fait qu’aliaser durablement `color.background.brand.bold` sans décision supplémentaire.

### Contextes produit

Ajouter un scope produit lorsque landing, dashboard, dataviz ou white-label possède une responsabilité et un propriétaire distincts. Ne pas l’utiliser pour cacher une sémantique globale mal conçue.

## Définir les alias

Employer un alias pour séparer option et décision :

```json
{
  "color": {
    "primitive": {
      "blue": {
        "600": {
          "$type": "color",
          "$value": {
            "colorSpace": "srgb",
            "components": [0.08, 0.32, 0.78],
            "alpha": 1
          }
        }
      }
    },
    "semantic": {
      "background": {
        "brand": {
          "bold": {
            "$type": "color",
            "$value": "{color.primitive.blue.600}",
            "$description": "Fond des actions de marque à forte emphase"
          }
        }
      }
    }
  }
}
```

Contrôler :

- cible existante ;
- type compatible ;
- absence de cycle ;
- profondeur justifiée ;
- résolution identique dans chaque sortie ;
- description du rôle ;
- remplacement d’un token déprécié.

Limiter la profondeur par compréhension et performance de l’outillage, non par chiffre universel. Signaler une chaîne qui n’ajoute aucune responsabilité.

## Traiter thèmes et modes

Définir un thème comme une API de personnalisation contrôlée. Définir un mode comme un contexte, une préférence ou une condition lorsque cette distinction sert l’outil et l’organisation.

Axes fréquents :

| Axe | Exemples | Risque principal |
|---|---|---|
| Marque | marque A, marque B | fork de composants |
| Apparence | clair, sombre | inversion naïve |
| Contraste | standard, élevé | couverture incomplète |
| Densité | compacte, confortable | cibles trop petites |
| Plateforme | web, iOS, Android | vocabulaire CSS imposé au natif |
| Direction | LTR, RTL | icônes et layouts non adaptés |

Maintenir un contrat sémantique stable. Réassigner les valeurs par axe sans obliger les composants à connaître les primitives.

Pour le sombre :

- recalibrer surfaces, texte, chroma et élévation ;
- tester chaque état interactif ;
- traiter images, illustrations, dataviz et ombres ;
- préserver focus, liens visités et contenus inverses ;
- vérifier les préférences système et le flash au chargement.

## Employer DTCG

Utiliser le format stable DTCG 2025.10 lorsque l’outillage cible le comprend réellement.

Employer :

- `$value` pour la valeur ou la référence ;
- `$type` au niveau pertinent ;
- `$description` pour le contexte ;
- groupes pour l’organisation ;
- `$deprecated` pour signaler une dépréciation ;
- `$extensions` pour une maturité, provenance ou donnée propre à l’organisation.

Ne pas présenter `experimental`, `candidate` ou `canonical` comme champs natifs DTCG. Les documenter comme extension versionnée.

Vérifier les types composites, unités et espaces colorimétriques supportés par la version de chaque transformeur. Une source conforme peut dépasser les capacités de l’outil.

## Contrôler la qualité

Exiger au minimum :

- JSON valide ;
- tokens typés ;
- conventions de nommage ;
- références résolues ;
- absence de cycles ;
- alias inter-types valides ;
- thèmes et modes complets ;
- valeurs générées reproductibles ;
- descriptions des rôles publics ;
- dépréciations avec remplacement ;
- diff des artefacts et provenance de build.

Ajouter selon le contexte :

- lint contre valeurs brutes ;
- détection de doublons ;
- graphe des alias ;
- tests de couples de couleurs ;
- taille des packages ;
- smoke tests consommateurs ;
- télémétrie d’adoption.

## Éviter les anti-patterns

- Ne pas exposer les primitives comme choix par défaut.
- Ne pas nommer un token sémantique par sa valeur actuelle.
- Ne pas créer une couche qui renomme sans protéger.
- Ne pas mélanger thème et fork de composant.
- Ne pas stocker la même décision manuellement dans Figma et le code.
- Ne pas promettre l’accessibilité parce qu’un mode est tokenisé.
- Ne pas traiter un changement de valeur comme un patch sans évaluer son impact visuel et comportemental.
- Ne pas supprimer un token avant preuve d’absence d’usage et fenêtre de migration.
