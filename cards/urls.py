from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns=[
    path('courses/',views.courseview,name="courseview"),
    path('courses/<int:pk>/',views.coursedetail,name="coursedetail"),
    path('login/',views.login_view,name='login'),
    path('testing/',views.testview)
] 

