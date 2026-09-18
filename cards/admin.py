from django.contrib import admin
from .models import Course,Subject

from django.core.exceptions import ValidationError

class CourseAdmin(admin.ModelAdmin):
    list_display=['course_name',"created_at","updated_at","status"]

class SubjectAdmin(admin.ModelAdmin):
    list_display=['id',"subject"]


admin.site.register(Course,CourseAdmin)

admin.site.register(Subject,SubjectAdmin)






    

   