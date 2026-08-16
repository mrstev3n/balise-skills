# Skill Market — centre de contrôle

Last reviewed: 2026-08-16

## Mandat et hiérarchie

Ce document définit le protocole opérationnel du centre de contrôle enfant de
Skill Market. Il s'applique uniquement au dépôt marketplace courant.

- Le centre parent **Lab Skills & MCP** coordonne le laboratoire privé Skills
  et la surface publique Skill Market.
- Le centre Skill Market coordonne les travaux réalisés dans ce dépôt : état,
  vérification, préparation et escalade.
- Le centre enfant ne remplace ni la source canonique privée, ni les décisions
  du centre parent, ni les gates de publication du dépôt.
- Les tâches Skill Market transmettent leurs rapports au centre Skill Market,
  qui est leur autorité opérationnelle locale.
- Le centre Skill Market ne transmet pas systématiquement chaque jalon ou
  rapport local au centre parent. Il escalade selon les conditions définies
  ci-dessous.

## Frontières de responsabilité

Skill Market est une surface downstream. Les rôles sont séparés :

| Surface | Rôle | Autorité de référence |
| --- | --- | --- |
| Source canonique | Skills authored et décisions de contenu de référence | dépôt privé Skills, selon le cadrage validé par le centre parent |
| `skills/` | Éditions publiques autonomes et harness-neutral | ce dépôt, pour la copie publique approuvée |
| `adapters/` | Métadonnées et packaging propres à un harness | adapter concerné, jamais `SKILL.md` canonique |
| `catalog/` | Index, catégories, tags et collections installables | schémas et règles de ce dépôt |
| Publication | Release, push, remote, distribution ou changement d'état public | décision humaine explicite, après gates vérifiés |

Une copie marketplace ne devient jamais la source canonique par défaut. Les
adapters ne doivent ni réécrire ni forker les instructions canoniques. Chaque
skill public doit rester autonome ; un companion peut améliorer le routage,
mais ne peut pas être une dépendance implicite.

## Autorité et escalade

Le centre enfant peut inspecter, comparer, préparer une spécification, éditer
le protocole de contrôle et effectuer les vérifications locales autorisées. Il
doit préserver les changements préexistants et limiter chaque modification au
périmètre approuvé.

Le centre parent et/ou l'humain doivent arbitrer avant :

- toute décision structurante sur la source, le catalogue, les adapters, les
  versions, les collections ou la compatibilité ;
- toute modification d'un livrable métier qui n'est pas explicitement demandée
  dans la mission courante ;
- tout commit, push, création de remote, branche, worktree, suppression,
  déplacement de contenu ou changement de release state ;
- toute publication, distribution, synchronisation vers une surface externe ou
  déclaration de disponibilité publique ;
- toute divergence volontaire entre source canonique, édition publique et
  adapter.

La coordination seule n'autorise donc ni commit, ni push, ni publication, ni
suppression. En cas d'ambiguïté, le centre enfant gèle l'action concernée et
transmet une demande d'arbitrage avec les preuves disponibles.

## Relation avec le centre parent

Le centre parent peut questionner le centre Skill Market, lui demander une
vérification ciblée, lui déléguer une mission marketplace ou lui demander de
coordonner ses propres tâches. Le centre Skill Market lui transmet un rapport
uniquement :

- lorsqu'une mission du centre parent le demande explicitement ;
- lorsqu'une dépendance ou une décision touche à la fois le laboratoire privé
  Skills et Skill Market ;
- lorsqu'un arbitrage humain ou une nouvelle autorité est nécessaire au niveau
  projet ;
- lorsqu'un risque important du marketplace peut affecter le projet parent ;
- lors d'une synthèse demandée par le centre parent.

En dehors de ces cas, le centre Skill Market conserve localement les rapports,
jalons, preuves et décisions opérationnelles de ses tâches. Cette autonomie ne
modifie pas les gates d'autorité, de sécurité, de Git ou de publication définis
dans ce protocole.

## Cycle opérationnel

Pour chaque mission rattachée à Lab Skills & MCP :

1. **Rechercher** : lire les instructions applicables, l'état Git, les diffs,
   les worktrees, les fichiers concernés et les preuves existantes.
2. **Définir** : formuler l'objectif, les non-objectifs, les surfaces touchées,
   les risques et les critères d'acceptation observables.
3. **Exécuter** : modifier seulement le périmètre autorisé ; préserver les
   changements existants et séparer source, public, adapter et catalogue.
4. **Vérifier** : exécuter les contrôles proportionnés et distinguer validation
   de format, installation, runtime, Git et publication.
5. **Rapporter** : transmettre le résultat concret, les preuves, les risques et
   l'état exact au centre Skill Market ; escalader au centre parent seulement
   dans les cas prévus à la section « Relation avec le centre parent ».

## Protection de l'état Git

Avant toute édition, relever branche, HEAD, statut, diff, fichiers non suivis
et worktrees. Les modifications présentes avant la mission appartiennent à
l'utilisateur : elles ne doivent être ni réécrites, ni mélangées, ni
« nettoyées » pour faciliter la validation. Les contrôles doivent cibler les
fichiers de la mission et signaler les limites dues au dirty tree.

Le centre enfant ne crée pas de commit, ne pousse pas et ne publie pas. Lorsqu'
un jalon cohérent est prêt, il peut recommander un commit au centre parent en
décrivant les chemins exacts et les vérifications effectuées ; il ne l'exécute
pas sans autorisation explicite.

## Vérification et preuves

Les affirmations doivent être rattachées à une commande, un fichier, une
ligne, un test ou une comparaison. Pour une modification marketplace, vérifier
au minimum selon le périmètre :

- validation des skills et des manifestes par les outils du dépôt ;
- cohérence README/catalogue/versions et `git diff --check` ;
- autonomie et portabilité des skills publics ;
- séparation des overlays d'adapter et des instructions canoniques ;
- installation ou runtime seulement lorsqu'ils ont réellement été testés.

Une validation locale ne prouve pas une publication distante, une release
GitHub, un runtime externe ou l'état d'une autre copie. Toute preuve ancienne
doit être présentée comme historique et revalidée si elle est utilisée pour une
décision actuelle.

## Rapport local et escalade parentale

Chaque tâche Skill Market remet son rapport au centre Skill Market. Lorsqu'une
escalade parentale est requise ou explicitement demandée, le message est titré
**RAPPORT Lab Skills & MCP** et contient :

- **Surface marketplace** : dépôt, périmètre et rôle de la mission ;
- **Résultat concret** : ce qui existe maintenant et ce qui n'a pas été fait ;
- **Fichiers touchés** : chemins exacts, en distinguant protocole et livrables ;
- **Preuves** : commandes, tests, diff ou inspections et résultat ;
- **Risques / arbitrages** : blocages, décisions attendues et limites ;
- **État Git / publication** : branche, dirty state, commit/push/publication,
  sans les déduire d'une simple validation locale ;
- **Recommandation** : prochaine action autorisée ou demande d'arbitrage.

Le rapport doit être factuel, compact et sans secrets ni chemins personnels
inutiles. En l'absence de messagerie inter-tâches, terminer une escalade ou une
synthèse destinée au parent avec :

> Rapport à transmettre au centre de contrôle Lab Skills & MCP

## Règle de maintenance

Mettre à jour ce protocole uniquement lorsqu'une frontière d'autorité, une
surface, une gate de vérification ou une règle durable change. Ne pas y inscrire
les micro-itérations, les sorties de commandes temporaires ou un journal de
mission.
