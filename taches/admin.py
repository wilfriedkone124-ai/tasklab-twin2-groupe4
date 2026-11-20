from django.contrib import admin
from .models import Tache

@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
    list_display = ("titre", "statut", "priorite", "date_creation")
    list_filter = ("statut", "priorite")
    search_fields = ("titre",)
