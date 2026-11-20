# TaskLab TWIN2 — Projet fil rouge
Projet pédagogique Django pour les chapitres VIII à XII du Génie Logiciel.

## Installation
```bash
python -m venv .venv
# Windows PowerShell : .venv\\Scripts\\Activate.ps1
# Linux/macOS : source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations taches
python manage.py migrate
python manage.py runserver
```
Accès : http://127.0.0.1:8000/ ; admin : /admin/ (créer un superuser si besoin).

## Tests
`python manage.py test`

## Travail à réaliser
Voir le document TP associé. Ce starter est volontairement incomplet :
pas de filtre de statut, peu de tests, pas de version de livraison.
Ne jamais publier une clé SECRET_KEY de production ; DEBUG=False en production.
