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

    # TP 2 : ajouter test de validation, création par formulaire et suppression POST.
