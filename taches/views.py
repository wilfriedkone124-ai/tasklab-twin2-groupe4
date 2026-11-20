from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Tache
from .forms import TacheForm

def liste_taches(request):
    taches = Tache.objects.all().order_by("-date_creation")
    return render(request, "taches/liste.html", {"taches": taches})

def creer_tache(request):
    form = TacheForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("liste_taches")
    return render(request, "taches/form.html", {"form": form, "titre": "Nouvelle tâche"})

def modifier_tache(request, pk):
    tache = get_object_or_404(Tache, pk=pk)
    form = TacheForm(request.POST or None, instance=tache)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("liste_taches")
    return render(request, "taches/form.html", {"form": form, "titre": "Modifier la tâche"})

@require_POST
def supprimer_tache(request, pk):
    tache = get_object_or_404(Tache, pk=pk)
    tache.delete()
    return redirect("liste_taches")
