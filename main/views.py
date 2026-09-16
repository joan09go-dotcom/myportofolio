from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Education, Project

from main.forms import ProjectForm



def show_main(request):
    context = {
        "name": "Jordan Manaksak Hutahaean",
        "npm": "2506532580",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student at the University of Indonesia with a strong interest in building intelligent and reliable software systems. I enjoy working on projects that combine problem-solving, software development, and emerging AI technologies."
            "Driven by curiosity and hands-on experience, I continuously develop my technical skills and look for opportunities to turn ideas into practical solutions."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    experiences = Experience.objects.all()
    now = timezone.now()
    
    for exp in experiences:
        if exp.ended_at and exp.ended_at > now:
            exp.status_text = "Sedang Berlangsung"
        else:
            exp.status_text = "Selesai"

    context = {
        "name": "Jordan Manaksak Hutahaean",
        "experience_list": experiences,
    }
    return render(request, "experience.html", context)


def show_education(request):
    context = {
        "name": "Jordan Manaksak Hutahaean", 
        "education_list": Education.objects.all().order_by('-start_year'),
    }
    return render(request, "education.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Jordan Manaksak Hutahaean",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Jordan Manaksak Hutahaean",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")