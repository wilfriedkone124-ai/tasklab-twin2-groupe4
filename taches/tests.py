from django.test import TestCase
from django.urls import reverse
from .models import Tache
from .forms import TacheForm


class TacheTests(TestCase):
    # ---- Tests déjà fournis ----
    def test_creation_modele(self):
        tache = Tache.objects.create(titre="Réviser Django")
        self.assertEqual(str(tache), "Réviser Django")

    def test_liste_accessible(self):
        response = self.client.get(reverse("liste_taches"))
        self.assertEqual(response.status_code, 200)

    # ---- TP 2 : tests à ajouter ----
    def test_creation_valide(self):
        """Un formulaire avec des données correctes est valide."""
        form = TacheForm(data={
            "titre": "Écrire les tests",
            "description": "TP2",
            "statut": "A_FAIRE",
            "priorite": 2,
        })
        self.assertTrue(form.is_valid())

    def test_priorite_invalide_refusee(self):
        """Une priorité hors de [1, 3] doit être rejetée par le formulaire."""
        for mauvaise_priorite in (0, 4):
            with self.subTest(priorite=mauvaise_priorite):
                form = TacheForm(data={
                    "titre": "Tâche invalide",
                    "statut": "A_FAIRE",
                    "priorite": mauvaise_priorite,
                })
                self.assertFalse(form.is_valid())
                self.assertIn("priorite", form.errors)

    def test_liste_affiche_les_taches(self):
        """GET sur la liste : la page contient les tâches existantes."""
        Tache.objects.create(titre="Tâche visible")
        response = self.client.get(reverse("liste_taches"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tâche visible")

    def test_creation_via_post(self):
        """POST valide sur /nouvelle/ : redirection et tâche enregistrée."""
        response = self.client.post(reverse("creer_tache"), {
            "titre": "Créée par POST",
            "description": "",
            "statut": "EN_COURS",
            "priorite": 1,
        })
        self.assertRedirects(response, reverse("liste_taches"))
        self.assertEqual(Tache.objects.count(), 1)
        self.assertEqual(Tache.objects.first().titre, "Créée par POST")

    def test_creation_post_invalide_ne_cree_rien(self):
        """POST avec priorité invalide : pas de redirection, rien en base."""
        response = self.client.post(reverse("creer_tache"), {
            "titre": "Mauvaise priorité",
            "statut": "A_FAIRE",
            "priorite": 9,
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Tache.objects.count(), 0)

    def test_suppression_via_post(self):
        """POST sur /<pk>/supprimer/ : la tâche disparaît."""
        tache = Tache.objects.create(titre="À supprimer")
        response = self.client.post(reverse("supprimer_tache", args=[tache.pk]))
        self.assertRedirects(response, reverse("liste_taches"))
        self.assertFalse(Tache.objects.filter(pk=tache.pk).exists())

    def test_suppression_refuse_get(self):
        """GET sur la suppression est interdit (405) et ne supprime rien."""
        tache = Tache.objects.create(titre="Toujours là")
        response = self.client.get(reverse("supprimer_tache", args=[tache.pk]))
        self.assertEqual(response.status_code, 405)
        self.assertTrue(Tache.objects.filter(pk=tache.pk).exists())
