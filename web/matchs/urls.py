
from django.urls import path
from .views import list_matchs, add_match, add_team
from django.urls import path

urlpatterns = [ 
    path('', list_matchs, name='list_matchs'), 
    path('<int:id>', list_matchs, name="list_matchs"),
    path('ajouter-match/<int:id>', add_match, name='add_match'),
    path('ajouter-equipe/', add_team, name='add_team'),
]