# Couleur, typographie et fondations

## Sommaire

1. [Construire un système de couleur](#construire-un-système-de-couleur)
2. [Créer une rampe](#créer-une-rampe)
3. [Mapper les rôles](#mapper-les-rôles)
4. [Construire la typographie](#construire-la-typographie)
5. [Traiter espace et autres fondations](#traiter-espace-et-autres-fondations)
6. [Vérifier](#vérifier)

## Construire un système de couleur

Commencer par les usages :

- surfaces neutres, élevées, inverses et sélectionnées ;
- texte primaire, secondaire, discret, désactivé et inverse ;
- bordures, séparateurs et focus ;
- actions brand, danger et neutres avec leurs états ;
- feedback success, warning, danger et information ;
- dataviz, illustrations et marque si nécessaires.

Définir les couples foreground/background et leurs états avant de fixer le nombre de tons.

## Créer une rampe

1. Choisir ancres de marque, neutres et contraintes de sortie.
2. Travailler en OkLCh ou autre espace perceptuel adapté.
3. Définir des pas par fonction : surface subtile, bordure, action, texte.
4. Ajuster lightness, chroma et parfois hue; ne pas interpoler aveuglément.
5. Contrôler le gamut sRGB ou Display P3 cible et fournir les fallbacks nécessaires.
6. Tester les couples sémantiques en contexte.
7. Corriger manuellement lorsque perception, marque ou accessibilité l’exige.

Ne pas imposer 9 ou 12 pas. Conserver le nombre minimal qui couvre les décisions et états réels.

Ne pas utiliser HSL `lighten`/`darken` comme méthode principale de production. HSL reste un format historique ou pédagogique, pas une garantie de régularité perceptuelle.

## Mapper les rôles

Séparer :

- primitives de palette ;
- tokens sémantiques ;
- tokens de composants justifiés ;
- valeurs propres aux thèmes/modes.

Exiger une matrice :

| Rôle | Clair | Sombre | Contraste élevé | États | Paire attendue |
|---|---|---|---|---|---|
| background.brand.bold | … | … | … | hover/pressed | text.inverse |
| text.danger | … | … | … | disabled | background.default |
| border.focused | … | … | … | focus-visible | surfaces cibles |

Vérifier WCAG 2.2 selon les définitions exactes. Si APCA est exploré, le traiter comme stratégie séparée et explicitement non interchangeable.

Prévoir un second signal pour erreur, succès, sélection et autres informations. Tester forced colors, daltonismes, préférences de contraste et contenus adjacents.

## Construire la typographie

Partir des rôles et contenus :

- body, label, caption, code ;
- heading et display ;
- nombres, données tabulaires et interfaces denses ;
- marketing expressif si le périmètre le demande.

Définir chaque rôle comme style composite :

- famille et fallbacks ;
- taille ;
- hauteur de ligne ;
- poids ou axe variable ;
- letter-spacing ;
- optical sizing ou largeur lorsque pertinent.

Employer un ratio modulaire comme exploration, jamais comme vérité finale. Une échelle artisanale limitée peut mieux servir l’UI.

Séparer niveau HTML et style visuel. Ne pas lier automatiquement `heading-1` à `h1`.

Choisir `rem`, unités relatives ou `px` selon propriété, plateforme et comportement attendu. Préserver réglages utilisateur, zoom et reflow.

Tester :

- fonte réellement chargée et fallback ;
- scripts non latins, accents, RTL et langues longues ;
- zoom 200–400 % selon le contexte ;
- longueurs de ligne ;
- wrap, truncation et contenu extrême ;
- chiffres, tableaux et alignement de baseline ;
- modes de densité et viewports.

## Traiter espace et autres fondations

### Espace

Construire une rampe limitée et non nécessairement linéaire. Ajouter des rôles comme `space.inline.control`, `space.stack.field` et `space.section` lorsque cela réduit les choix.

Appliquer la proximité : espace inter-groupe supérieur à l’espace intra-groupe. Ne pas forcer chaque élément à remplir son conteneur.

### Layout

Définir grille, gutters, marges, max-width et conteneurs. Déclencher les adaptations au point de rupture du contenu; employer les container queries lorsque la dépendance est locale au parent.

### Densité

Coordonner espace, taille et parfois type. Ne pas réduire cibles ou lisibilité pour obtenir une interface compacte.

### Forme

Limiter rayons, bordures et épaisseurs. Relier les rôles à la marque et au comportement plutôt qu’à une collection décorative.

### Élévation

Distinguer élévation visuelle et z-index. Définir surface, ombre, overlay et interaction par rôle : base, raised, overlay, modal, drag.

### Mouvement

Définir durée, easing et distance par intention. Prévoir reduced motion et distinguer feedback, transition et orchestration.

### Iconographie et images

Définir grille, tailles optiques, stroke, fill, RTL, labels et actifs de marque. Prévoir focal point, ratios, responsive images, contenus manquants et texte alternatif.

## Vérifier

Ne pas conclure qu’une fondation fonctionne parce que ses tokens valident.

Exiger :

- rendu avec contenus et fontes réels ;
- thèmes et modes ;
- états interactifs ;
- contraste texte et non-texte ;
- zoom, reflow et localisation ;
- gamut et fallbacks ;
- responsive et densité ;
- tests avec préférences utilisateur pertinentes.
