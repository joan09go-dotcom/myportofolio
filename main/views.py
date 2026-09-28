from django.contrib.auth.decorators import login_required, permission_required   
from django.core.exceptions import PermissionDenied        
from django.contrib import messages 
from django.core import serializers 
from django.http import HttpResponse 
from django.shortcuts import get_object_or_404, redirect, render 
from main.models import Experience, Education, Project 
from main.forms import ExperienceForm, EducationForm, ProjectForm 
from django.contrib.auth import login, logout 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.shortcuts import redirect, render 
import datetime 

# Register 
def register(request): 
    form = UserCreationForm(request.POST or None) 
 
    if request.method == "POST" and form.is_valid(): 
        form.save() 
        messages.success(request, "Akun berhasil dibuat. Silahkan login.") 
        return redirect("main:login") 
 
    context = { 
        "name" : "Jordan Manaksak Hutahaean", 
        "form" : form, 
    } 
 
    return render(request, "register.html", context) 
 
# Login  
def login_user(request): 
    form = AuthenticationForm(request, data=request.POST or None) 
 
    if request.method == "POST" and form.is_valid(): 
        user = form.get_user() 
        login(request, user) 
        response = redirect("main:show_main") 
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) 
        return response 
 
    context = { 
        "name": "Jordan Manaksak Hutahaean", 
        "form": form, 
    } 
    return render(request, "login.html", context) 
 
# Logout 
def logout_user(request): 
    logout(request) 
    response = redirect("main:show_main") 
    response.delete_cookie('last_login') 
    return response
 
# Main 
def show_main(request): 
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan') 
    context = { 
        "name": "Jordan Manaksak Hutahaean", 
        "npm": "2506532580", 
        "study_program": "S1 Ilmu Komputer", 
        "bio": ( 
            "Computer Science student at the University of Indonesia with a strong interest in building intelligent and reliable software systems. I enjoy working on projects that combine problem-solving, software development, and emerging AI technologies. " 
            "Driven by curiosity and hands-on experience, I continuously develop my technical skills and look for opportunities to turn ideas into practical solutions." 
        ), 
        "last_login" : last_login, 
    } 
    return render(request, "index.html", context) 
 
# Experience 
@login_required(login_url="/login/") 
def create_experience(request): 
   
    if not request.user.is_superuser: 
        raise PermissionDenied 

    # 1. Menyiapkan form sebagai medium penyimpanan data 
    form = ExperienceForm(request.POST or None) 
 
    # 2. Cek validasi jika form disubmit 
    if request.method == "POST" and form.is_valid(): 
        # 3. Simpan ke database jika benar 
        form.save() 
        # 4. Tampilkan success message 
        messages.success(request, "Pengalaman baru berhasil ditambahkan!") 
        # 5. Balikkan tampilan ke experience.html 
        return redirect("main:show_experience") 
 
    # 6. Bungkus data data yang diperlukan  
    context = { 
        "name": "Jordan Manaksak Hutahaean", 
        "form": form, 
    } 
 
    # Render file 
    return render(request, "experience_form.html", context) 

@permission_required("main.change_experience", raise_exception=True)
@login_required(login_url="/login/") 
def update_experience(request, id): 
     
    # 1. Menyiapkan tempat untuk data khusus yang dituju dengan modal navigasi paramter Models Class name dan id-nya 
    experience = get_object_or_404(Experience, id=id) 
 
    # 2. Buat logic yang sama dengan create tapi formnya di specify dengan instance 
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

@login_required(login_url="/login/") 
def delete_experience(request, id): 

    if not request.user.is_superuser: 
        raise PermissionDenied 
    
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
        "is_editor": is_editor(request.user),
    } 
    return render(request, "experience.html", context) 
 
def get_experience_json(request): 
    title_query = request.GET.get("title", "").strip() 
    experiences = Experience.objects.all() 
 
    if title_query: 
        experiences = experiences.filter(title__icontains=title_query) 
 
    experience_json = serializers.serialize("json", experiences,use_natural_foreign_keys=True) 
        
    return HttpResponse(experience_json, content_type="application/json") 

# Fitur star experience untuk user biasa
@login_required(login_url="/login/")
def toggle_star_for_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)


    return redirect("main:show_experience")
 
 
# Education 
@login_required(login_url="/login/") 
def create_education(request): 

    if not request.user.is_superuser: 
        raise PermissionDenied 
     
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

@permission_required("main.change_education", raise_exception=True)
@login_required(login_url="/login/") 
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

@login_required(login_url="/login/") 
def delete_education(request, id):

    if not request.user.is_superuser: 
        raise PermissionDenied 
     
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
 
    educations_json = serializers.serialize("json", educations, use_natural_foreign_keys=True) 
    
    return HttpResponse(educations_json, content_type="application/json") 

# Fitur star education untuk user biasa
@login_required(login_url="/login/")
def toggle_star_for_education(request, education_id):
    educations = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in educations.starred_by.all():
            educations.starred_by.remove(request.user)
        else:
            educations.starred_by.add(request.user)

    return redirect("main:show_education")
 
 
# Project 
@login_required(login_url="/login/")  
def create_project(request): 
 
    if not request.user.is_superuser: 
        raise PermissionDenied 
     
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

@login_required(login_url="/login/")  
@permission_required("main.change_project", raise_exception=True)
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
 
@login_required(login_url="/login/")  
def delete_project(request, project_id): 
    if not request.user.is_superuser: 
        raise PermissionDenied 
      
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
        "is_editor": is_editor(request.user),
    } 
    return render(request, "project.html", context) 
 
def get_projects_json(request): 
    title_query = request.GET.get("title", "").strip() 
    projects = Project.objects.all() 
 
    if title_query: 
        projects = projects.filter(title__icontains=title_query) 
 
    projects_json = serializers.serialize("json", projects, use_natural_foreign_keys=True)

    return HttpResponse(projects_json, content_type="application/json") 

# Fitur star project untuk user biasa
@login_required(login_url="/login/")
def toggle_star_for_projects(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

def is_editor(user):
    return user.is_authenticated and user.groups.filter(name="Editor").exists()