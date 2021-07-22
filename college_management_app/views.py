from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import auth
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from college_management_app.models import CustomUser, Staffs, Courses, Subjects, Students
# Create your views here.
def admin_home(request):
    return render(request,'admin/admindashboard.html')

def login(request):
    return render(request,'admin/login.html')

def doLogin(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            
             auth.login(request, user)

             if user.user_type=='1':

                  return HttpResponseRedirect('/admin_home')

             elif user.user_type=='2':
                  return HttpResponseRedirect('/staff_home')
             else:
                  return HttpResponseRedirect('/student_home')
        else:
            messages.info(request,'Wrong username and password')
            return HttpResponse('invalid')

    else:
        return HttpResponse('invalid')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

def add_staff(request):
    return render(request,'admin/add_staff.html')

def add_staff_save(request):
    if request.method!='POST':
        return HttpResponse("<h1> Method not allowed </h1>")

    else:
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        address=request.POST.get('address')
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.staffs.address=address
            user.save()
            messages.success(request,'successfully added staff')
            return HttpResponseRedirect('/add_staff')
        except:
            return HttpResponseRedirect('/add_staff')


def add_course(request):
    return render(request,'admin/add_course.html')
def add_course_save(request):
    if request.method!='POST':
        return HttpResponseRedirect("Method not allowed")
    else:
        course=request.POST.get("course")
        try:
            course_model=Courses(course_name=course)
            course_model.save()
            messages.success(request,'successfully added course')
            return HttpResponseRedirect('/add_course')
        except:
            messages.error(request,'failed to added course')
            return HttpResponseRedirect('/add_course')

def add_student(request):
    courses=Courses.objects.all()
    return render(request,'admin/add_student.html',{'courses':courses})

def add_student_save(request):
    if request.method!='POST':
        return HttpResponse("<h1> Method not allowed </h1>")

    else:
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        address=request.POST.get('address')
        course_id=request.POST.get('course')
        sex=request.POST.get('sex')
        
        profile_pic=request.FILES['profile_pic']
        fs=FileSystemStorage()
        filename=fs.save(profile_pic.name,profile_pic)
        profile_pic_url=fs.url(filename)
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
            user.students.address=address
            course_obj=Courses.objects.get(id=course_id)
            user.students.gender=sex
            user.students.profile_pic=profile_pic_url
            user.save()
            messages.success(request,'successfully added student')
            return HttpResponseRedirect('/add_student')
        except:
            messages.error(request,'failed to added student')
            return HttpResponseRedirect('/add_student')


def add_subject(request):
    courses=Courses.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request,'admin/add_subject.html',{'staffs':staffs, 'courses':courses})

def add_subject_save(request):
    if request.method!='POST':
        return HttpResponse('Method not allowed')
    else:
        subject_name=request.POST.get('subject_name')
        course_id=request.POST.get('course')
        course=Courses.objects.get(id=course_id)
        staff_id=request.POST.get('staff')
        staff=CustomUser.objects.get(id=staff_id)

        try:
            subject=Subjects(subject_name=subject_name, course_id=course, staff_id=staff)
            subject.save()
            messages.success(request,'successfully added subject')
            return HttpResponseRedirect('/add_subject')
        except:
            messages.error(request,'failed to added subject')
            return HttpResponseRedirect('/add_subject')
    
def manage_staff(request):
    staffs=Staffs.objects.all()
    return render(request,'admin/manage_staff.html',{'staffs':staffs})

def manage_student(request):
    students=Students.objects.all()
    return render(request,'admin/manage_student.html',{'students':students})

def manage_course(request):
    courses=Courses.objects.all()
    return render(request,'admin/manage_course.html',{'courses':courses})

def manage_subject(request):
    subjects=Subjects.objects.all()
    return render(request,'admin/manage_subject.html',{'subjects':subjects})

def edit_staff(request, staff_id):
    staff=Staffs.objects.get(admin=staff_id)
    return render(request,'admin/edit_staff.html',{'staff':staff})

def edit_staff_save(request):
    if request.method!="POST":
        return HttpResponse("<h1> Method Not Allowed</h1>")
    else:
        staff_id=request.POST.get("staff_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        address=request.POST.get("address")
        try:
            user=CustomUser.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            staff_model=Staffs.objects.get(admin=staff_id)
            staff_model.address=address
            staff_model.save()
            messages.success(request,'Successfully edited staff')
            return HttpResponseRedirect('/edit_staff/'+staff_id)
        except:
            messages.error(request,'Failed to edited staff')
            return HttpResponseRedirect('/edit_staff'+staff_id)

def delete_staff(request, delete_id):
    staff=Staffs.objects.get(admin=delete_id)
    staff.delete()
    return redirect('manage_staff')


def edit_student(request, student_id):
    courses=Courses.objects.all()
    student=Students.objects.get(admin=student_id)
    return render(request,'admin/edit_student.html',{"courses":courses,"student":student})

def edit_student_save(request):
    if request.method!="POST":
        return HttpResponse("<h2> Method not allowed</h2>")
    else:
        student_id=request.POST.get("student_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        address=request.POST.get("address")
        course_id=request.POST.get("course")
        sex=request.POST.get("sex")
 
        if request.FILES["profile_pic"]:
            profile_pic=request.FILES["profile_pic"]
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name, profile_pic)
            profile_pic_url=fs.url(filename)
        else:
            profile_pic_url=None
        try:
            user=CustomUser.objects.get(id=student_id)
            user.first_name=first_name
            user.last_name=last_name
            user.username=username
            user.email=email
            user.save()

            student=Students.objects.get(admin=student_id)
            student.address=address
            student.gender=sex
            course=Courses.objects.get(id=course_id)
            student.course_id=course
            if profile_pic_url!=None:
                student.profile_pic=profile_pic_url
            student.save()
            messages.success(request,"Successfully edited student")
            return HttpResponseRedirect("/edit_student/"+student_id)
        except:
            messages.error(request,"Failed to edited student")
            return HttpResponseRedirect("/edit_student/"+student_id)

def delete_student(request,delete_id):
    student=Students.objects.get(admin=delete_id)
    student.delete()
    return redirect('manage_student')


def edit_course(request,course_id):
    course=Courses.objects.get(id=course_id)
    return render(request,'admin/edit_course.html',{"course":course})

def edit_course_save(request):
    if request.method!="POST":
        return HttpResponse("<h1> Method not allowed </h2>")
    else:
        course_id=request.POST.get("course_id")
        course_name=request.POST.get("course")

        try:
            course=Courses.objects.get(id=course_id)
            course.course_name=course_name
            course.save()
            messages.success(request,"Successfully edited course")
            return HttpResponseRedirect("/edit_course/"+course_id)
        except:
            messages.error(request,"Failed to edited course")
            return HttpResponseRedirect("/edit_course/"+course_id)

def delete_course(request,delete_id):
    courses=Courses.objects.get(id=delete_id)
    courses.delete()
    return redirect('manage_course')

def edit_subject(request, subject_id):
    subject=Subjects.objects.get(id=subject_id)
    courses=Courses.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request,'admin/edit_subject.html',{'subject':subject,'staffs':staffs,'courses':courses})

def edit_subject_save(request):
    if request.method!="POST":
        return HttpResponse("<H1> Method not allowed </H2>")
    else:
        subject_id=request.POST.get("subject_id")
        subject_name=request.POST.get("subject_name")
        staff_id=request.POST.get("staff")
        course_id=request.POST.get("course")

        try:
            subject=Subjects.objects.get(id=subject_id)
            subject.subject_name=subject_name
            staff=CustomUser.objects.get(id=staff_id)
            subject.staff_id=staff
            course=Courses.objects.get(id=course_id)
            subject.course_id=course
            subject.save()

            messages.success(request,'Successfully edited subject')
            return HttpResponseRedirect('/edit_subject/'+subject_id)
        except:
            messages.error(request,'Failed to edited subject')
            return HttpResponseRedirect('/edit_subject/'+subject_id)

def delete_subject(request, delete_id):
    subject=Subjects.objects.get(id=delete_id)
    subject.delete()
    return redirect('manage_subject')