
from django.urls import path

from . import views
app_name = 'teams'

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.ListTeamView.as_view(), name='list_teams'),
    path('addteam', views.AddTeamView.as_view(), name='add_team'),

]
