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
            "subjects":forms.CheckboxSelectMultiple(attrs={
                            "class":"form-check"
                        }),
            "image":forms.FileInput(attrs={
                            "class":"form-control",
                            'accept': 'image/*'
                        }),
            "status":forms.RadioSelect(attrs={
                            "class":"form-check"
                        }),
            "description":forms.Textarea(attrs={
                            "class":"form-control",
                            "placeholder":"Add Description*",
                            "required":True
                        }),
            
        }

