
# Create your views here.
from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # No need to access 'student' directly from cleaned_data,
            # since the form already handles the foreign key relationship.
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})
