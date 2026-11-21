# Walking skeleton — tech-watch

Objectif : mettre en place toutes les briques de l'[architecture](architecture.md) et les relier de bout en bout, chacune sous sa forme la plus simple. Ici, on ne cherche pas encore la valeur.

## Pour qui

- **Le premier utilisateur seul.** Installation, paramétrage et lancement peuvent rester rudimentaires.
- **Rien de personnel dans le moteur** : le paramétrage du premier utilisateur est un exemple, rangé à part.

## Les briques

- **Paramétrage** : sources RSS, taille de l'épisode.
- **① Collecter** : récupérer les articles des sources.
- **② Choisir** : retenir de quoi remplir l'épisode, sans reprendre ce qui a déjà été raconté.
- **③ Raconter** : produire l'épisode, avec le moins de dépendances possible.
- **Mémoire** : garder la trace de ce qui a été raconté.

## Terminé quand

- Un lancement produit un épisode à partir de vraies sources, en passant par chaque brique.
- Un deuxième lancement ne reprend rien de ce qui a déjà été raconté.
- Un lancement qui échoue ne modifie pas la mémoire.

## Hors walking skeleton

- Profil, centres d'intérêt, dosage court / long terme
- Texte complet des articles, regroupement, suivi des sujets
- Régularité automatique, diffusion de l'épisode
- Installation par d'autres personnes

## À définir plus tard

- Forme de l'épisode, techniques, cadence, diffusion.
- Étape suivante : un MVP qui teste la valeur.
