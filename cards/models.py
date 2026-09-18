from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
# course name ( unique vlaidation) 
# subject
#  created at 
# updated at 
# status  
# desciption (min 50)


class Subject(models.Model):

    subject=models.CharField(max_length=50)
    # Course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name="subjects")
    def __str__(self):
        return f"{self.subject}"
    
class Course(models.Model):
    
    statuschoices=[
         ("active","ACTIVE"),
         ("inactive","INACTIVE")
    ]
    course_name=models.CharField(max_length=50,unique=True)

    subjects=models.ManyToManyField(Subject,related_name="courses")
    
    # class Meta:
    #      constraints=[
    #           models.UniqueConstraint(
    #                fields=['course_name','subjects'],
    #                name="primary"
    #           )
    #      ]
    image=models.ImageField(upload_to="course/")

    status=models.CharField(
         choices=statuschoices,
         default="active"
    )

    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    description=models.TextField()

    def clean(self):
    
            if len(self.description)<50:
                raise ValidationError("The description must have atleast 50 characters.")

    
    def __str__(self):
            return f"{self.course_name}"



