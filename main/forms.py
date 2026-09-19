from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput, URLInput
from main.models import Experience, Education, Project

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended at"
        ]

        widgets = {
            "title": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Sebutkan titel role internship-mu sebelumnya",
                }
            ),
            "description": Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ceritakan tanggung jawab dan pencapaianmu",
                }
            ),
           "category": Select(
               attrs={"class": "form-control"}),
                "thumbnail": URLInput(attrs={
                "class": "form-control", 
                "placeholder": "https://example.com/image.png (Opsional)"
            }
            ),
            "ended_at": TextInput(
                attrs={
                    "class": "form-control", 
                    "type": "datetime-local"
                }
            ),
        }

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "degree",
            "faculty",
            "location",
            "start_year",
            "end_year"
        ]

        widgets = {
            "institution": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Sebutkan nama tempat institusi pendidikan",
                }
            ),
            "degree": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Bachelor of...(Opsional)",
                }
            ),
            "faculty": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Faculty of...(Opsional)",
                }
            ),
            "location": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Sebutkan lokasi institusi",
                }
            ),
            "start_year": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "2025",
                }
            ),
            "end_year": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "2029",
                }
            ),
            
        }

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://github.com/...",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://drive.google.com/...",
                }
            ),
        }