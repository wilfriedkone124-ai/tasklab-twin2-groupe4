from django.db import models

class Tache(models.Model):
    STATUTS = [
        ("A_FAIRE", "À faire"),
        ("EN_COURS", "En cours"),
        ("TERMINEE", "Terminée"),
    ]
    titre = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    statut = models.CharField(max_length=12, choices=STATUTS, default="A_FAIRE")
    priorite = models.PositiveSmallIntegerField(default=2)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
