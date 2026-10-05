from django.urls import path
from main.views import (
    show_main,
    show_experience, create_experience, create_experience_ajax, update_experience, delete_experience, get_experience_json,
    show_education, create_education, create_education_ajax, update_education, delete_education, get_education_json,
    show_projects, create_project, create_project_ajax, update_project, delete_project, get_projects_json,
    register, login_user, logout_user, 
    toggle_star_for_projects, toggle_star_for_experience, toggle_star_for_education
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    
    # Experience
    path("experience/", show_experience, name="show_experience"),
    path("experience/create/", create_experience, name="create_experience"),
    path("experience/update/<uuid:id>/", update_experience, name="update_experience"),
    path("experience/delete/<uuid:id>/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),

    # Education
    path("education/", show_education, name="show_education"),
    path("education/create/", create_education, name="create_education"),
    path("education/update/<uuid:id>/", update_education, name="update_education"),
    path("education/delete/<uuid:id>/", delete_education, name="delete_education"),
    path("api/education/", get_education_json, name="get_education_json"),

    # Project
    path("projects/", show_projects, name="show_projects"),
    path("projects/create/", create_project, name="create_project"),
    path("projects/update/<uuid:id>/", update_project, name="update_projects"),
    path("projects/delete/<uuid:project_id>/", delete_project, name="delete_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),

    # Authentication
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),

    # Fitur star
    path("projects/<uuid:project_id>/star/", toggle_star_for_projects, name="toggle_star_for_projects",),
    path("experience/<uuid:experience_id>/star/", toggle_star_for_experience, name="toggle_star_for_experience",),
    path("education/<uuid:education_id>/star/", toggle_star_for_education, name="toggle_star_for_education",),

    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("educations/add-ajax/", create_education_ajax, name="create_education_ajax"),
    path("experiences/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
]