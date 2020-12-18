from django.shortcuts import render
from projects.models import Project

# Create your views here.
def all_projects(request):
    # query the db to return all projects objects
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request,'all_projects.html',{'projects':projects})


def detail(request,pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, 'detail.html', {'project':project})

