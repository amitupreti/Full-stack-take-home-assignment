
from django.urls import path

from . import views
app_name = 'teams'

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.ListTeamView.as_view(), name='list_teams'),
    path('addteam', views.AddTeamView.as_view(), name='add_team'),
    path('updateteam/<int:pk>', views.UpdateTeamView.as_view(), name='update_team'),
    path('deleteteam/<int:pk>', views.DeleteTeamView.as_view(), name='delete_team'),

]
