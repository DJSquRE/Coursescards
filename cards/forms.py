from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=["course_name","subjects","image","status","description"]

        widgets={
            "course_name":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter Course Name"
            }),
            "subjects":forms.SelectMultiple(attrs={
                            "class":"form-control",
                            "placeholder":"Select Subject"
                        }),
            "image":forms.FileInput(attrs={
                            "class":"form-control",
                            'accept': 'image/*'
                        }),
            "status":forms.Select(attrs={
                            "class":"form-control"
                        }),
            "description":forms.Textarea(attrs={
                            "class":"form-control",
                            "placeholder":"Add Description*",
                            "required":True
                        }),
            
        }

