from django.shortcuts import render,redirect, get_object_or_404
from projects.forms import ProjectForm
from django.contrib.auth.decorators import login_required
from projects.models import ProjectsModel

@login_required
def create_project(request):
    context = {}

    if request.method == 'POST':
        try:
            form = ProjectForm(request.POST)
            new_project = form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            return redirect('project:my_projects')
        except ValueError:
            context["form"] = ProjectForm()
            context['error'] = 'bad data try again'


    else:
        context['form'] = ProjectForm()



    return render(request,'projects/create.html',context)

@login_required
def my_project(request):
    context = {}
    projects_list = ProjectsModel.objects.filter(user=request.user).order_by('-created')
    context['projects'] = projects_list
    return render(request,'projects/project.html',context)

@login_required
def all_project(request):
    context = {}
    projects_list = ProjectsModel.objects.all
    context['projects'] = projects_list
    return render(request,'projects/all_projects.html',context)
