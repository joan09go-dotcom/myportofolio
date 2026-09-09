from django.shortcuts import render

from main.models import Experience


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
    context = {
        "name": "Jordan Manaksak Hutahaean",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)