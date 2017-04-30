from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from .forms import ProjectForm
from django.shortcuts import redirect


def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})


def add_new_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            p = Project.objects.create(title=title, description=description)

            if p.pk > 0:
                return redirect('index')
    return render(request, 'project/add.html', {'form': form})
