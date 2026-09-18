from django.shortcuts import render,redirect
from .models import Course,Subject
from .forms import CourseForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
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
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            user=form.get_user()

            login(request,user)

            return redirect("courseview")

    else:
        form=AuthenticationForm()


    return render(request,"registration/login.html",{"form":form})




#testing_view
def testview(request):
    subjects=Subject.objects.prefetch_related("subjects")

    return render(request,"testing.html",{"subjects":subjects})