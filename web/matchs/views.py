from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import Match, Team, Tournament
from .forms import MatchForm, TeamForm

# Create your views here.
def list_matchs(request, id):
    tournament = get_object_or_404(Tournament, pk=id)
    matchs = Match.objects.filter(idTournament=id)
    context = {
        'tournament': tournament,
        'matchs': matchs,
        'title': tournament.nom,
    }
    return render(request, 'list_matchs.html', context)

def add_match(request, id):
    teams = Team.objects.all()
    tournament = get_object_or_404(Tournament,pk=id)
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('list_matchs', args=[id]))
    else:
        form = MatchForm()
    context = {
        'form': form,
        'teams': teams,
        'tournament': tournament,
        'title': 'Ajout Match',
    }
    return render(request, 'add_match.html', context)

def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_match', args=[request.POST['idTournament']]))  # Redirection vers 'add_match' avec l'identifiant du tournoi
    else:
        form = TeamForm()
    return render(request, 'add_team_modal.html', {'form': form})