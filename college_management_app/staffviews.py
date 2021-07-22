from django.shortcuts import render
from college_management_app.models import Subjects

def staff_home(request):
    return render(request,'staff/staff_home_template.html')

def staff_take_attendance(request):
    subject=Subjects.objects.filter(staff_id=request.user.id)
    return render(request,'staff/staff_take_attendance.html',{"subject":subject})
