from django import forms
from matchs.models import Tournament

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['nom', 'sport']
