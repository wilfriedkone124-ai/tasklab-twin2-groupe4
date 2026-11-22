from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from .forms import TacheForm
from .models import Tache



class TacheTests(TestCase):
    def setUp(self):
        self.tache = Tache.objects.create(
            titre="Écrire le rapport", statut="A_FAIRE", priorite=1
        )

    # -- Tests de départ (conservés) --
    def test_creation_modele(self):
        tache = Tache.objects.create(titre="Réviser Django")
        self.assertEqual(str(tache), "Réviser Django")

    def test_liste_accessible(self):
        response = self.client.get(reverse("liste_taches"))
        self.assertEqual(response.status_code, 200)

    # -- Demandés par le sujet --
    def test_creation_valide(self):
        self.assertEqual(Tache.objects.count(), 1)
        self.assertEqual(self.tache.statut, "A_FAIRE")

    def test_get_liste_affiche_la_tache(self):
        reponse = self.client.get(reverse("liste_taches"))
        self.assertEqual(reponse.status_code, 200)
        self.assertContains(reponse, "Écrire le rapport")

    def test_creation_via_post(self):
        reponse = self.client.post(
            reverse("creer_tache"),
            {
                "titre": "Nouvelle tâche",
                "description": "",
                "statut": "A_FAIRE",
                "priorite": 2,
            },
        )
        self.assertRedirects(reponse, reverse("liste_taches"))
        self.assertEqual(Tache.objects.count(), 2)

    def test_suppression_via_post(self):
        reponse = self.client.post(
            reverse("supprimer_tache", args=[self.tache.pk])
        )
        self.assertRedirects(reponse, reverse("liste_taches"))
        self.assertFalse(Tache.objects.filter(pk=self.tache.pk).exists())

    # -- Cas d'erreur --
    def test_suppression_en_get_refusee(self):
        reponse = self.client.get(
            reverse("supprimer_tache", args=[self.tache.pk])
        )
        self.assertEqual(reponse.status_code, 405)
        self.assertTrue(Tache.objects.filter(pk=self.tache.pk).exists())

    def test_titre_vide_refuse(self):
        reponse = self.client.post(
            reverse("creer_tache"),
            {"titre": "", "statut": "A_FAIRE", "priorite": 1},
        )
        self.assertEqual(reponse.status_code, 200)
        self.assertEqual(Tache.objects.count(), 1)

    def test_priorite_hors_limites_refusee(self):
        reponse = self.client.post(
            reverse("creer_tache"),
            {"titre": "Tâche absurde", "statut": "A_FAIRE", "priorite": 9},
        )
        self.assertEqual(reponse.status_code, 200)
        self.assertEqual(Tache.objects.count(), 1)

    def test_formulaire_valide(self):
        form = TacheForm(
            data={
                "titre": "Réviser",
                "description": "",
                "statut": "EN_COURS",
                "priorite": 3,
            }
        )
        self.assertTrue(form.is_valid())
