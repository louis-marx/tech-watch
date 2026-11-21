# tech-watch : règles de développement

## Ponytail

Le plugin `ponytail@ponytail` est activé pour ce projet en mode **ultra** (`.claude/settings.json`).

- **Écrire du code** : applique le skill `/ponytail:ponytail` au niveau ultra. Lis d'abord le code touché, puis descends l'échelle : est-ce nécessaire, déjà dans le dépôt, dans la bibliothèque standard, dans une dépendance installée, en une ligne, sinon le minimum qui marche.
- **Jamais sacrifié** : validation aux frontières, gestion d'erreur qui évite une perte de données, sécurité, et tout ce que j'ai demandé explicitement.
- **Un test par logique non triviale** : le plus petit test qui échoue si la logique casse. Pas de suite par fonction.
- **Raccourci assumé** : un commentaire `# ponytail: <plafond>, <quand y revenir>`. Sans déclencheur, le raccourci pourrit. `/ponytail:ponytail-debt` en dresse la liste.
- **Avant chaque commit qui touche `src/` ou `tests/`** : lance `/ponytail:ponytail-review` sur le diff indexé et applique ses points jusqu'à « Lean already. Ship. ».
- **Conflit avec une règle validée** (ruff, ty, hooks, une de mes décisions) : le point est signalé, pas appliqué. Tu n'assouplis aucune règle sans mon accord.
- **Portée de la review** : la complexité seulement. Bugs, sécurité et performance passent par une review normale.
