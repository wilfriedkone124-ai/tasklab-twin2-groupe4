# TaskLab - Groupe 4

Application Django de gestion de tâches (projet fil rouge Génie Logiciel TWIN2).

## Installation

1. `git clone https://github.com/wilfriedkone124-ai/tasklab-twin2-groupe4.git` puis `cd tasklab-twin2-groupe4`
2. `python3 -m venv .venv`, puis l'activer (Windows : `.venv\Scripts\Activate.ps1`, Linux/macOS : `source .venv/bin/activate`)
3. `pip install -r requirements.txt`
4. (Facultatif) copier `.env.example` en `.env`
5. `python manage.py migrate`
6. `python manage.py runserver` puis ouvrir `http://127.0.0.1:8000/`

## Variables de configuration

| Variable | Rôle | Exemple |
| :--- | :--- | :--- |
| `SECRET_KEY` | Clé secrète Django | `replace-me-with-a-long-random-secret` |
| `DEBUG` | Mode debug | `True` |
| `ALLOWED_HOSTS` | Hôtes autorisés | `127.0.0.1,localhost` |

## Tests et Qualité

Commande pour lancer les tests : `python manage.py test`

| Test | Résultat attendu |
| :--- | :--- |
| Création valide | La tâche existe en base, compteur = 1 |
| GET de la liste | Code 200, le titre apparaît |
| POST de création | Redirection 302 vers la liste, 1 tâche de plus |
| POST de suppression | Redirection 302, la tâche n'existe plus |
| GET sur la suppression | Code 405 (la vue exige POST) |
| Titre vide | Page réaffichée (200), rien créé |
| Priorité 9 | Page réaffichée (200), rien créé |
| Après sabotage du formulaire | Le test « priorité 9 » échoue (302 au lieu de 200) |

## Fonctionnalités

* Filtre par statut : `/?statut=EN_COURS` (valeurs : `A_FAIRE`, `EN_COURS`, `TERMINEE` ; valeur inconnue → liste complète)
* Variante du Groupe 4 : compteur de tâches par statut

## Choix de configuration

* **`.env` non versionné :** Sécurité — contient des secrets (clé secrète) qui ne doivent pas apparaître sur un dépôt public ni dans l'historique Git, et varie selon les machines.
* **`.venv/` non versionné :** Reproductibilité et poids — contient des milliers de fichiers liés au système d'exploitation et se recrée facilement via `pip install -r requirements.txt`.
* **`db.sqlite3` non versionné :** Données locales — fichier binaire modifié à chaque utilisation (source de conflits impossibles à résoudre) qui se recrée via `python manage.py migrate`.

## Suivi de projet

Tableau Trello : *(à compléter avec le lien du groupe)*

## Versions

* `v1.0.0` : version stable initiale
* `v1.1.0` : correctif de validation + filtre par statut + variante