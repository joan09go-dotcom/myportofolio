from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Experience, Education, Project
from main.forms import ExperienceForm, EducationForm, ProjectForm

# Main
def show_main(request):
    context = {
        "name": "Jordan Manaksak Hutahaean",
        "npm": "2506532580",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student at the University of Indonesia with a strong interest in building intelligent and reliable software systems. I enjoy working on projects that combine problem-solving, software development, and emerging AI technologies. "
            "Driven by curiosity and hands-on experience, I continuously develop my technical skills and look for opportunities to turn ideas into practical solutions."
        ),
    }
    return render(request, "index.html", context)


# Experience
def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Jordan Manaksak Hutahaean",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def update_experience(request, id):
    experience = get_object_or_404(Experience, id=id)
    
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('main:show_experience')
    else:
        form = ExperienceForm(instance=experience)
    
    context = {
        'form': form,
        'experience': experience,  
        'name': 'Jordan Manaksak Hutahaean',
    }
    return render(request, "update_experience.html", context)

def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def show_experience(request):
    json_response = get_experience_json(request)
    experiences = serializers.deserialize(
        "json", json_response.content.decode("utf-8")
    )
    experiences = [exp.object for exp in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Jordan Manaksak Hutahaean",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experiences)
    return HttpResponse(experience_json, content_type="application/json")


# Education
def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Edukasi baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Jordan Manaksak Hutahaean",
        "form": form,
    }
    return render(request, "education_form.html", context)
def update_education(request, id):
    education = get_object_or_404(Education, pk=id)
    form = EducationForm(request.POST or None, instance=education)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Edukasi berhasil diperbarui!")
        return redirect("main:show_education")

    context = {
        "name": "Jordan Manaksak Hutahaean", 
        "form": form,
        "education": education,  
    }
    return render(request, "update_education.html", context)

def delete_education(request, id):
    education = get_object_or_404(Education, pk=id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Edukasi berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def show_education(request):
    json_response = get_education_json(request)
    educations = serializers.deserialize(
        "json", json_response.content.decode("utf-8")
    )
    educations = [edu.object for edu in educations]
    institution_query = request.GET.get("institution", "").strip()

    context = {
        "name": "Jordan Manaksak Hutahaean",
        "education_list": educations,
        "institution_query": institution_query,
    }
    return render(request, "education.html", context)

def get_education_json(request):
    institution_query = request.GET.get("institution", "").strip()
    educations = Education.objects.all()

    if institution_query:
        educations = educations.filter(institution__icontains=institution_query)

    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")


# Project
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

def update_project(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project berhasil diperbarui!")
        return redirect("main:show_projects")

    context = {
        "name": "Jordan Manaksak Hutahaean", 
        "form": form,
        "project": project, 
    }
    return render(request, "update_projects.html", context)

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