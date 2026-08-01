# Politique de compatibilité

Balise Skills utilise le format ouvert Agent Skills comme frontière de portabilité :

```text
skill-name/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

Seul `SKILL.md` est obligatoire. Les instructions canoniques utilisent des chemins relatifs et ne dépendent pas d’une syntaxe d’invocation, de variables d’environnement, de hooks ou de skills cachés propres à un harness.

## Niveaux de preuve

- `format-valid` : le skill passe le validateur du dépôt et le validateur de référence Agent Skills.
- `install-tested` : le dépôt a été découvert et installé dans une destination isolée pour le harness indiqué.
- `runtime-tested` : le skill installé a été découvert et invoqué dans le harness indiqué.

Le catalogue n’enregistre une preuve d’exécution que lorsqu’une invocation a été observée. Les tests d’installation utilisent des destinations isolées et comparent les répertoires installés à leurs sources canoniques. Consultez les [preuves de vérification](verification.md).

## Stratégie multi-harness

- Claude Code consomme le skill canonique. Un éventuel paquet plugin reste isolé dans un adaptateur dédié.
- Codex/OpenAI consomme le skill canonique et peut recevoir les métadonnées facultatives `agents/openai.yaml` de son adaptateur.
- Cursor consomme le skill canonique sans adaptateur tant qu’aucune exigence propre à Cursor n’est établie.
- Les autres harness compatibles reçoivent le même répertoire canonique au moyen d’un installateur Agent Skills.

## Éditions Figma

Les éditions destinées au Figma Agent et à Figma Make vivent sous `figma-skills/`. Chacune contient un unique fichier `SKILL.md`, sans `references/`, `scripts/` ni `assets/` associés.

Ces éditions conservent le même identifiant Balise, mais leur workflow peut être adapté aux capacités de Figma. Elles ne sont proposées que lorsque l’usage reste autonome et pertinent dans cet environnement.
