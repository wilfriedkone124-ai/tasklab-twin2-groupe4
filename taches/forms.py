from django import forms
from .models import Tache

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ["titre", "description", "statut", "priorite"]

    def clean_priorite(self):
        priorite = self.cleaned_data["priorite"]
        if not 1 <= priorite <= 3:
            raise forms.ValidationError("La priorité doit être entre 1 et 3.")
        return priorite
