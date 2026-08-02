# Structures de design system pour produits SaaS

## Sommaire

1. [Commencer par le produit](#commencer-par-le-produit)
2. [Modéliser le shell](#modéliser-le-shell)
3. [Fondations adaptées au SaaS](#fondations-adaptées-au-saas)
4. [Patterns de données](#patterns-de-données)
5. [Formulaires et workflows](#formulaires-et-workflows)
6. [États complets](#états-complets)
7. [Multi-tenant et personnalisation](#multi-tenant-et-personnalisation)
8. [Responsive, densité et accessibilité](#responsive-densité-et-accessibilité)
9. [Piloter et mesurer](#piloter-et-mesurer)

## Commencer par le produit

Un SaaS n’a pas seulement besoin de beaux composants. Il exige une structure cohérente pour naviguer, lire des données, agir, attendre, corriger une erreur et comprendre les permissions.

Inventorier :

- personas, rôles, permissions et plans ;
- domaines, objets métier et actions fréquentes ;
- navigation globale, locale et contextuelle ;
- densité des données et fréquence d’usage ;
- workflows longs, asynchrones ou destructifs ;
- desktop, mobile, tablette et environnements embarqués ;
- tenants, marques, préférences et contraintes réglementaires ;
- frameworks, composants et dette existants.

Prioriser les flows à forte répétition et fort risque : onboarding, recherche, gestion de données, création/édition, paramètres, facturation, permissions et support.

## Modéliser le shell

Spécifier les régions et leurs responsabilités :

- app frame et largeur utile ;
- navigation principale et réduction ;
- contexte de workspace/tenant ;
- header, commandes globales et recherche ;
- breadcrumb ou navigation locale ;
- titre, actions de page et métadonnées ;
- contenu, panneaux secondaires et inspector ;
- notifications, toasts et surfaces modales.

Ne pas figer un shell unique si les domaines exigent des structures différentes. Définir invariants, variantes autorisées et règles de composition.

Tester clavier, zoom, petits viewports, longues traductions, navigation profonde, permissions partielles et contenu vide.

## Fondations adaptées au SaaS

Construire les tokens à partir des usages :

- surfaces : canvas, section, card, overlay, selected, disabled ;
- contenus : default, muted, subtle, inverse, link, status ;
- bordures : default, strong, interactive, focus, critical ;
- actions : primary, secondary, quiet, destructive ;
- statuts : informative, success, warning, danger, neutral ;
- espace : contrôle, groupe, section, page ;
- densité : compact, comfortable si elle répond à de vrais usages ;
- type : labels, corps, données tabulaires, titres, code ;
- mouvement : feedback, entrée/sortie, progression, réduction du mouvement ;
- élévation : seulement lorsque la superposition ou la hiérarchie l’exige.

Prévoir valeurs tabulaires, chiffres alignés, troncature inspectable, unités, monnaies, dates et nombres localisés.

## Patterns de données

### Tableaux

Documenter : colonnes, alignement, largeur, tri, filtre, sélection, actions, pagination/virtualisation, édition, cellules complexes, responsive, vide, chargement et erreur.

Ne pas rendre toutes les tables configurables par défaut. Distinguer table de consultation, table d’action, grille éditable et comparaison.

### Recherche et filtres

Définir portée, délai, soumission, tokens actifs, effacement, sauvegarde de vues, résultats nuls, erreurs et partage d’URL. Préserver l’état lorsque l’utilisateur ouvre un résultat puis revient.

### Visualisation

Tokeniser rôles et séquences utiles, pas des couleurs de série arbitraires. Tester distinction sans couleur, légendes, valeurs manquantes, petits espaces, thèmes et export.

## Formulaires et workflows

Spécifier :

- label persistant, aide, requis/optionnel et format ;
- validation au bon moment ;
- erreur liée au champ et résumé si nécessaire ;
- disabled versus read-only ;
- sauvegarde, autosave, brouillon et changements non enregistrés ;
- étapes, reprise, annulation et sortie ;
- actions destructives proportionnées au risque ;
- succès, échec partiel et traitement asynchrone.

Pour chaque champ, documenter type de donnée, contraintes, exemple réaliste, clavier/mobile, autofill, localisation et technologie d’assistance.

## États complets

Chaque surface reliée à des données doit considérer :

```text
initial → loading → success
                 ↘ empty
                 ↘ partial
                 ↘ stale
                 ↘ permission denied
                 ↘ recoverable error
                 ↘ terminal error
```

Ajouter selon le contexte : offline, rate-limited, maintenance, synchronisation, conflit, traitement en file, plan insuffisant et ressource supprimée.

Ne pas utiliser un spinner unique pour tous les délais. Choisir skeleton, progression déterminée, optimistic UI ou tâche en arrière-plan selon la durée et la certitude.

## Multi-tenant et personnalisation

Séparer :

- invariants d’expérience et d’accessibilité ;
- sémantiques du produit ;
- expression de marque ;
- configuration du tenant ;
- préférence utilisateur ;
- exception locale contrôlée.

Limiter les entrées de thème à un contrat testé. Une couleur de marque fournie par un tenant ne doit pas devenir automatiquement couleur de texte, focus ou statut.

Prévoir fallbacks, validation de contraste, gamut, logo, favicon, emails, graphiques, export PDF et surfaces externes. Tester deux tenants très différents sur les mêmes composants avant de déclarer le modèle robuste.

## Responsive, densité et accessibilité

Responsive signifie prioriser et recomposer, pas seulement réduire. Pour chaque pattern, définir :

- invariant ;
- éléments reflowés, masqués ou déplacés ;
- alternative aux interactions hover ;
- comportement des tableaux et graphiques ;
- ordre de lecture et focus ;
- seuil fondé sur le contenu ou le conteneur.

La densité ne doit pas réduire les cibles, le focus ou la lisibilité sous les exigences retenues. Tester zoom, text spacing, reflow, clavier, lecteur d’écran, contraste et préférences de mouvement.

## Piloter et mesurer

Construire un pilote autour d’un flow réel et borné. Utiliser navigation, formulaire, tableau ou liste, feedback asynchrone, permissions et thèmes comme grille de sélection ; inclure seulement les dimensions critiques pour le produit. Tester plusieurs thèmes uniquement lorsqu’ils appartiennent au périmètre du système.

Preuves :

- temps de construction et cohérence ;
- nombre de valeurs brutes ou exceptions ;
- couverture d’états ;
- accessibilité et responsive ;
- seconde consommation par une autre équipe/surface ;
- effort d’upgrade ;
- satisfaction et demandes de contournement.

Ne pas viser un catalogue exhaustif avant que le shell, les fondations et quelques patterns centraux aient été éprouvés en produit.
