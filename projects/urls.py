from django.urls import path
from projects.views import create_project,my_project,all_project

app_name = 'project'

urlpatterns = [

   path('my_project/', my_project,name='my_projects'),
   path('create/', create_project,name='create_project'),
   path('all_projects/', all_project,name='all_projects'),


]
