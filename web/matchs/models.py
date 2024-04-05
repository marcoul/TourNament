from django.db import models
from django.utils import timezone

class Team(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nom


class Tournament(models.Model):
    nom = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nom

class Match(models.Model):
    team_dom = models.ForeignKey(Team, related_name='matchs_domicile', on_delete=models.CASCADE)
    team_ext = models.ForeignKey(Team, related_name='matchs_exterieur', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    resultat_team_dom = models.IntegerField(default=0)
    resultat_team_ext = models.IntegerField(default=0)
    idTournament = models.ForeignKey(Tournament, default=None, blank=None, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.team_dom.nom} vs {self.team_ext.nom} - {self.idTournament.nom}"
