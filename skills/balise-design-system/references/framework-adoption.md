# Adapter Tailwind, shadcn ou une base UI existante

## Sommaire

1. [Auditer avant de choisir](#auditer-avant-de-choisir)
2. [Choisir extend, override, wrap ou replace](#choisir-extend-override-wrap-ou-replace)
3. [Relier Tailwind aux tokens](#relier-tailwind-aux-tokens)
4. [Gérer utilitaires et valeurs arbitraires](#gérer-utilitaires-et-valeurs-arbitraires)
5. [Adapter shadcn et les bibliothèques headless](#adapter-shadcn-et-les-bibliothèques-headless)
6. [Préserver l’API du design system](#préserver-lapi-du-design-system)
7. [Migrer sans big bang](#migrer-sans-big-bang)
8. [Vérifier](#vérifier)

## Auditer avant de choisir

Identifier versions, configuration, presets, plugins, variables CSS, utilitaires, composants copiés, dépendances headless, variants, conventions de classes et usages arbitraires.

Mesurer :

- valeurs du framework réellement utilisées ;
- valeurs ajoutées ou écrasées ;
- classes arbitraires répétées ;
- couleurs primitives employées directement ;
- composants locaux et forks ;
- dépendances aux détails internes ;
- compatibilité de version et coût d’upgrade.

Une base populaire n’est pas automatiquement un design system. Elle fournit des capacités, des valeurs par défaut ou du code initial ; l’intention, le contrat, la gouvernance et les preuves restent à construire.

## Choisir extend, override, wrap ou replace

| Stratégie | Utiliser si | Risque |
|---|---|---|
| extend | les défauts sont compatibles et les ajouts sont légitimes | conserver trop de choix inutiles |
| override | l’API convient mais l’expression doit changer | divergences lors des upgrades |
| wrap | il faut une API produit stable au-dessus d’une primitive | wrapper sans valeur ou props dupliquées |
| fork/copier | le code doit être possédé et profondément adapté | maintenance et mises à jour manuelles |
| replace | l’écart structurel ou accessible est trop important | migration coûteuse |

Décider séparément pour fondations, utilitaires, primitives comportementales et composants composés.

## Relier Tailwind aux tokens

Commencer par identifier la version majeure. Dans Tailwind CSS v4, les variables de thème définies dans des namespaces tels que `--color-*`, `--font-*`, `--text-*`, `--spacing-*`, `--radius-*` et `--shadow-*` génèrent des utilitaires correspondants. Dans Tailwind v3, configurer les valeurs via `theme.extend` ou un plugin, de préférence à partir de variables CSS sémantiques générées. Dans les deux cas, Tailwind reste une couche de consommation pratique, pas nécessairement la source portable.

Architecture recommandée pour v4 :

```text
source DTCG ou portable
→ génération de variables CSS sémantiques
→ pont Tailwind @theme inline
→ utilitaires autorisés
→ composants et produits
```

Exemple conceptuel :

```css
:root {
  --ds-color-bg-canvas: oklch(...);
  --ds-color-text-default: oklch(...);
}

.dark {
  --ds-color-bg-canvas: oklch(...);
  --ds-color-text-default: oklch(...);
}

@theme inline {
  --color-canvas: var(--ds-color-bg-canvas);
  --color-content: var(--ds-color-text-default);
}
```

Employer `inline` lorsque les variables de thème référencent d’autres variables afin d’éviter des résolutions CSS inattendues. Revérifier cette recommandation avec la version Tailwind réellement installée.

Pour v3, conserver le même contrat sémantique et mapper les variables dans la configuration :

```js
export default {
  theme: {
    extend: {
      colors: {
        canvas: 'var(--ds-color-bg-canvas)',
        content: 'var(--ds-color-text-default)',
      },
    },
  },
}
```

Ne pas reproduire deux taxonomies différentes entre v3 et v4. Le mapping d’intégration varie ; les rôles publics restent stables.

Ne pas exposer toute la palette par défaut si le produit doit consommer des rôles. Décider si `blue-600` reste un détail interne et si les développeurs doivent utiliser `bg-action-primary`, `text-content-muted` ou une convention équivalente.

## Gérer utilitaires et valeurs arbitraires

Les utilitaires accélèrent la composition ; ils ne dispensent pas de conventions.

Politique recommandée :

- autoriser les utilitaires structurels pour layout et composition ;
- préférer les utilitaires sémantiques pour couleur et rôles partagés ;
- accepter une valeur arbitraire pour exploration ou exception documentée ;
- promouvoir une répétition stable vers un token ou pattern après preuve ;
- linter les couleurs, espaces et z-index arbitraires à risque ;
- ne pas créer un token pour chaque occurrence unique.

Séparer valeur arbitraire légitime (`grid-template` spécifique, mesure liée au contenu) et contournement du système (`text-[#...]` répété).

## Adapter shadcn et les bibliothèques headless

shadcn recommande actuellement des variables CSS sémantiques et mappe celles-ci vers des utilitaires Tailwind. Ses paires surface/foreground fournissent un bon point de départ, mais elles ne couvrent pas automatiquement tous les rôles d’un produit SaaS.

Avant adoption :

- vérifier la version Tailwind/React et la configuration ;
- inventorier les composants réellement copiés ou possédés ;
- mapper `background`, `foreground`, `primary`, `muted`, `border`, `ring`, etc. vers la taxonomie du produit ;
- ajouter états, statuts et contextes manquants sans détourner le sens des tokens existants ;
- vérifier focus, clavier, contenu, RTL, responsive et thèmes ;
- documenter les divergences par rapport à la source amont.

Une primitive headless peut fournir comportement et accessibilité initiale. Le composant du design system doit encore définir contrat, contenu, styling, états, composition et tests en produit.

## Préserver l’API du design system

Éviter que les consommateurs dépendent directement de :

- noms privés du framework ;
- structure DOM accidentelle ;
- sélecteurs internes ;
- palette primitive non gouvernée ;
- détails du package headless ;
- chemins de fichiers copiés.

Exposer une API adaptée au besoin : composants, slots, recipes/variants, tokens sémantiques et utilitaires documentés. Autoriser `className` ou équivalent comme escape hatch sans en faire le chemin nominal pour corriger chaque défaut.

## Migrer sans big bang

1. Geler l’ajout de nouvelles valeurs brutes à risque.
2. Construire le mapping ancien → sémantique.
3. Générer le pont framework depuis la source.
4. Migrer un flow pilote.
5. Comparer rendu, comportement et accessibilité.
6. Ajouter lint, suggestions ou codemods prudents.
7. Maintenir des alias de compatibilité temporaires.
8. Mesurer versions et usages.
9. Retirer seulement après preuve.

Séparer les remplacements mécaniques des choix sémantiques nécessitant une revue humaine.

## Vérifier

- build et déterminisme des variables générées ;
- disponibilité des utilitaires attendus ;
- absence d’exposition involontaire des primitives ;
- thèmes, contrastes et focus ;
- extraction statique des classes selon le framework ;
- taille CSS et régressions ;
- composants dans des flows réels ;
- upgrade de la dépendance sur une branche pilote.

## Sources officielles à revérifier

- [Tailwind CSS — Theme variables](https://tailwindcss.com/docs/theme)
- [Tailwind CSS — Upgrade guide](https://tailwindcss.com/docs/upgrade-guide)
- [shadcn/ui — Theming](https://ui.shadcn.com/docs/theming)

Les APIs et conventions de Tailwind et shadcn évoluent. Inspecter toujours la version installée avant de générer ou migrer une configuration.
