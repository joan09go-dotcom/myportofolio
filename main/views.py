from django.shortcuts import render
from django.utils import timezone  # 1. Import timezone di atas
from main.models import Experience, Education


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