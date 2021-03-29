from django.forms import ModelForm
from projects.models import ProjectsModel

class ProjectForm(ModelForm):
    class Meta:
        model = ProjectsModel
        fields = ['title', 'description']
