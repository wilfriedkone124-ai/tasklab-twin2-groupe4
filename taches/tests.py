from django.test import TestCase
from django.urls import reverse
from .models import Tache
from .forms import TacheForm

class TacheTests(TestCase):
    def test_creation_modele(self):
        tache = Tache.objects.create(titre="Réviser Django")
        self.assertEqual(str(tache), "Réviser Django")

    def test_liste_accessible(self):
        response = self.client.get(reverse("liste_taches"))
        self.assertEqual(response.status_code, 200)

    def test_creation_affiche_message_de_succes(self):
        response = self.client.post(
            reverse("creer_tache"),
            {"titre": "Nouvelle tâche", "statut": "A_FAIRE", "priorite": 2},
            follow=True,
        )
        self.assertContains(response, "Tâche créée.")

    def test_modification_affiche_message_de_succes(self):
        tache = Tache.objects.create(titre="Ancien titre")
        response = self.client.post(
            reverse("modifier_tache", args=[tache.pk]),
            {"titre": "Nouveau titre", "statut": "A_FAIRE", "priorite": 2},
            follow=True,
        )
        self.assertContains(response, "Tâche modifiée.")
        tache.refresh_from_db()
        self.assertEqual(tache.titre, "Nouveau titre")

    def test_suppression_affiche_message_de_succes(self):
        tache = Tache.objects.create(titre="À supprimer")
        response = self.client.post(
            reverse("supprimer_tache", args=[tache.pk]),
            follow=True,
        )
        self.assertContains(response, "Tâche supprimée.")
        self.assertFalse(Tache.objects.filter(pk=tache.pk).exists())

    # TP 2 : ajouter test de validation, création par formulaire et suppression POST.
