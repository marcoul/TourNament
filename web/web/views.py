from django.shortcuts import render, redirect
from .forms import TournamentForm
from matchs.models import Tournament


def index(request):
    context = {}
    context['tournaments'] = Tournament.objects.all()
    context['title'] = 'Home'
    return render(request, 'web/templates/index.html', context)

def add_tournament(request):
    context = {}
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('..')
    else:
        form = TournamentForm()
    context['form'] = form
    context['title']= 'Ajout Tournoi'
    return render(request, 'add_tournament.html', context)