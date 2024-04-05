from django import forms
from .models import Match,Team

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['team_dom', 'team_ext', 'date', 'resultat_team_dom', 'resultat_team_ext', 'idTournament']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['nom']
        labels = {
            'nom': 'Nom de l\'équipe',
        }