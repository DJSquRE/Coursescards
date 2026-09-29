from django import forms
from django.contrib.auth.models import User
from .models import Course
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm
class UserLoginForm(AuthenticationForm):
    pass

class UserRegisterForm(UserCreationForm):
    pass


class ChangePassword(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)

        PasswordChangeForm.error_messages={
            "password_incorrect":"Doesnt match your Current Password.",
            "password_mismatch":"Doesn't match your New Password."
        }


        print(self.error_messages)
        self.fields['old_password'].widget.attrs.update(
            {
                'class':'form-control',
                'placeholder':'current password'
            }
        )

        self.fields['new_password1'].widget.attrs.update(
                    {
                        'class':'form-control',
                        'placeholder':'new password'
                    }
                )
        self.fields['new_password2'].widget.attrs.update(
                            {
                                'class':'form-control',
                                'placeholder':'confirm password'
                            }
                        )

    def clean(self):
        old_password=self.cleaned_data.get("old_password")
        new_password2=self.cleaned_data.get("new_password2")

        if old_password and new_password2 and new_password2==old_password:
            # raise ValidationError("New password should be different from current password.")
            self.add_error('new_password2',"New password should be different from current password.")

        return new_password2

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=["course_name","subjects","image","status","description"]

        error_messages={
            "subjects":{
                "required":"Select atleast 1 subject"
            }
        }
        widgets={
            "course_name":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter Course Name"
            }),
            "subjects":forms.CheckboxSelectMultiple(attrs={
                            "class":"form-check-label"
                        }),
            "image":forms.FileInput(attrs={
                            "class":"form-control",
                            'accept': 'image/*'
                        }),
            "status":forms.RadioSelect(attrs={
                            "class":"form-check-label"
                        }),
            "description":forms.Textarea(attrs={
                            "class":"form-control",
                            "placeholder":"Add Description*",
                            "required":True
                        }),
            
        }

    def clean_description(self):
        description=self.cleaned_data.get('description')

        if description and len(description)<50:
            raise ValidationError("The description must have atleast 50 characters.")

        return description

    def clean_course_name(self):
        course_name=self.cleaned_data.get('course_name')

        if course_name and len(course_name)<3:
            raise ValidationError("Course Name must be atleast 3 letters long.")

        return course_name

