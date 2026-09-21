from django.urls import path
from . import views

urlpatterns=[
    path('courses/',views.courseview,name="courseview"),
    path('courses/<int:pk>/',views.coursedetail,name="coursedetail"),
    path('login/',views.login_view,name='login'),
    path('register',views.register_view,name='register'),
    path('testing/',views.testview),
    path("logout/",views.logout_view, name="logout"),
] 

