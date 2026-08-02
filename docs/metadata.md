# Métadonnées du catalogue

`catalog/marketplace.json` est la source de vérité des métadonnées de découverte. Il peut alimenter des outils en ligne de commande et une future interface web.

## Catégorie

Une catégorie est le classement principal d’un skill. Chaque skill possède exactement une catégorie. Une catégorie n’est pas installable et peut être active ou planifiée.

## Tag

Un tag est un filtre transversal. Un skill peut posséder plusieurs tags, tous déclarés dans le registre du catalogue.

## Collection

Une collection est un ensemble ordonné, versionné et installable de skills. Elle peut couvrir plusieurs catégories. Son manifeste se trouve sous `collections/` et référence les skills par leur identifiant.

`category:legal` et `collection:legal` sont deux entités distinctes. Legal constitue un domaine du catalogue multidomaine Balise Skills.

## Édition

Une édition désigne le conditionnement d’un même skill pour un environnement donné :

- `agent-skills` contient le répertoire canonique installable dans Claude Code, Codex, Cursor et les outils compatibles ;
- `figma` contient un fichier `SKILL.md` autonome pour le Figma Agent et Figma Make.

Une édition Figma est déclarée uniquement lorsque le workflow peut fonctionner utilement dans cet environnement. Les badges du README reflètent les cibles déclarées dans le catalogue.

## Versionnement

Le catalogue, les collections et les skills suivent le versionnement sémantique. Le champ `updatedAt`, au format `AAAA-MM-JJ`, indique la date de publication de la version déclarée.

Toutes les éditions d’un même skill partagent une seule version. Une modification de l’édition canonique, de l’édition Figma ou d’un adaptateur impose donc d’incrémenter `version` et d’actualiser `updatedAt` dans `catalog/marketplace.json`.

Une collection change de version lorsque sa composition ou son contrat évolue. Sa date correspond à la publication de cette version du manifeste.

Le README reprend automatiquement les versions et dates des skills depuis le catalogue :

```bash
npm run sync:readme
```

La validation refuse un README désynchronisé et détecte les modifications de contenu qui ne sont pas accompagnées d’une nouvelle version.
