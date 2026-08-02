# Nommage et autorités du système

## Nommage

Faire du nom un outil de choix, pas seulement de recherche.

### Tokens sémantiques

Employer la grammaire candidate :

```text
[namespace].[catégorie].[propriété].[rôle].[emphase].[état].[échelle]
```

Exemple : `core.color.background.danger.bold.hovered`.

### Tokens de composants

Employer une grammaire distincte :

```text
[namespace].[objet].[élément].[propriété].[variante].[état].[échelle]
```

Exemple : `core.button.container.background.primary.hovered`.

Omettre les segments sans pouvoir discriminant. Fixer l’ordre, le singulier/pluriel, les termes réservés et les valeurs par défaut dans un lexique versionné.

| Segment | Question | Piège |
|---|---|---|
| namespace | qui possède la décision ? | répéter le package |
| catégorie | quel type ? | confondre type et CSS |
| objet/élément | quelle anatomie ? | tokeniser trop tôt |
| propriété | où s’applique-t-il ? | oublier le contrat de contraste |
| rôle | quelle intention ? | nommer par apparence |
| emphase | quel poids relatif ? | nombres opaques |
| variante | quelle option fonctionnelle ? | confondre état et rôle |
| état | quelle condition ? | dupliquer le variant |
| échelle | quel rang ? | tailles quasi identiques |

Tester le vocabulaire avec designers, développeurs, contenu et consommateurs. Rechercher les synonymes et faux amis. Aligner conversation, fichiers de design, code et documentation.

## Autorité par type d’artefact

Ne pas chercher un fichier unique qui contiendrait toute la vérité. Définir une autorité par décision :

| Décision | Autorité | Miroirs | Preuve |
|---|---|---|---|
| tokens agnostiques | DTCG versionné | variables design, sorties plateforme | validation et diff |
| contrat composant | types/schéma/manifeste | docs API, bindings design | tests de conformité |
| comportement/a11y | implémentation testée | previews, kits | tests runtime |
| intention/usage | documentation versionnée | aide contextuelle | revue de release |
| ressources visuelles | bibliothèque design gouvernée | exports | version et provenance |

Définir pour chaque frontière : propriétaire, sens de synchronisation, fréquence, gestion de conflit, version et rollback.

## Décisions structurelles

Consigner un ADR lorsque le choix affecte plusieurs équipes ou reste coûteux à inverser :

- format canonique ;
- modèle de thèmes ;
- grammaire de noms ;
- pipeline de transformation ;
- canaux de distribution ;
- politique de version ;
- source d’édition ;
- compatibilité de plateforme.

Inclure contexte, options, décision, conséquences, date et critères de révision.

## Garde-fous

- Ne pas faire de Figma une autorité implicite du runtime.
- Ne pas faire du code une autorité de l’intention éditoriale.
- Ne pas promettre une synchronisation bidirectionnelle sans arbitrage de conflit.
- Ne pas donner un nom humoristique à une API structurante si sa traduction ou sa maintenance devient ambiguë.
- Ne pas renommer publiquement sans mapping, dépréciation et migration.
