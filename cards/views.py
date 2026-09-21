from django.shortcuts import render,redirect
from .models import Course,Subject
from .forms import CourseForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.http import JsonResponse
from django.core.paginator import Paginator
# Create your views here.
@login_required(login_url='/login/')
def courseview(request):

    search_query=request.GET.get('q','')
    if request.user.is_superuser:
        courses=Course.objects.prefetch_related("subjects").all()      
    else:
        courses=Course.objects.prefetch_related("subjects").exclude(status="inactive")

    if search_query:
        courses=courses.filter(course_name__startswith=search_query)
    
    paginator=Paginator(courses,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if request.method =="POST":
        form=CourseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    else:
        form=CourseForm()

    context={
        "courses":page_obj,
        "form":form,
        "query":search_query
    }
    return render(request,"course.html",context) 

def coursedetail(request,pk):
    if not request.user.is_authenticated:
         return redirect("login")

    course=Course.objects.get(pk=pk)
    form=CourseForm

    if request.method=='POST':
        form=CourseForm(request.POST,request.FILES,instance=course)

        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
        
    else:
        form=CourseForm(instance=course)

    context={
        "course":course,
        "form":form
    }
    return render(request,"course_detail.html",context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect("courseview")
    
    if request.method=="POST":
        user_name=request.POST.get("loguser")
        pass_word=request.POST.get("logpass")

        user=authenticate(request,username=user_name ,password=pass_word)

        if user is not None:
            login(request,user)
            return redirect("courseview")

        else:
            return render(request,"registration/login.html",{"error":"Invalid Username or Password"})


    return render(request,"registration/login.html")

def register_view(request):
    if request.method=="POST":
       user_name=request.POST.get("username")
       pass_word=request.POST.get("password")

       if User.objects.filter(username=user_name).exists():
           messages.error(request, "Username is already taken.")
           return redirect("register")

       user = User.objects.create_user(username=user_name, password=pass_word)
       user.save()
       messages.success(request, "Registration successful! Now Log in : ")
       
    
    return render(request,"registration/register.html")


def logout_view(request):
    logout(request)
    return redirect("login")


#testing_view_for_courses_and_subjects
def testview(request):
    subjects=Subject.objects.prefetch_related("subjects")

    return render(request,"testing.html",{"subjects":subjects})