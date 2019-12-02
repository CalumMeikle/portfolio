from django.shortcuts import render
from projects.models import Project

# Create your views here.

def project_index(request):
    projects = Project.objects.all() #Query all objects in a database
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk) #Another database query but this time for objects with a primarykey pk
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)