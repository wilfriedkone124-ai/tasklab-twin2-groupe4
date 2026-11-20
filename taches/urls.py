from django.urls import path
from . import views
urlpatterns = [
    path("", views.liste_taches, name="liste_taches"),
    path("nouvelle/", views.creer_tache, name="creer_tache"),
    path("<int:pk>/modifier/", views.modifier_tache, name="modifier_tache"),
    path("<int:pk>/supprimer/", views.supprimer_tache, name="supprimer_tache"),
]
