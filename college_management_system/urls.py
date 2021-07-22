"""college_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from college_management_system import settings
from college_management_app import views, studentviews, staffviews

urlpatterns = [
    path('admin_home', views.admin_home, name='admin_home'),
    path('admin/', admin.site.urls),
    path('', views.login),
    path('doLogin', views.doLogin, name='login'),
    path('logout_user', views.logout_user, name="logout"),
    path('add_staff', views.add_staff, name='add_staff'),
    path('add_staff_save', views.add_staff_save, name='add_staff_save'),
    path('add_course', views.add_course, name='add_course'),
    path('add_course_save', views.add_course_save, name='add_course_save'),
    path('add_student', views.add_student, name='add_student'),
    path('add_student_save', views.add_student_save, name='add_student_save'),
    path('add_subject', views.add_subject, name='add_subject'),
    path('add_subject_save', views.add_subject_save, name='add_subject_save'),
    path('manage_staff', views.manage_staff, name='manage_staff'),
    path('manage_student', views.manage_student, name='manage_student'),
    path('manage_course', views.manage_course, name='manage_course'),
    path('manage_subject', views.manage_subject, name='manage_subject'),
    path('edit_staff/<str:staff_id>', views.edit_staff, name='edit_staff'),
    path('edit_staff_save', views.edit_staff_save, name='edit_staff_save'),
    path('delete_staff/<str:delete_id>',views.delete_staff, name='delete_staff'),
    
    path('edit_student/<str:student_id>', views.edit_student, name='edit_student'),
    path('edit_student_save', views.edit_student_save, name='edit_student_save'),
    path('delete_student/<str:delete_id>', views.delete_student,name='delete_student'),
    
    path('edit_course/<str:course_id>', views.edit_course, name='edit_course'),
    path('edit_course_save', views.edit_course_save, name='edit_course_save'),
    path('delete_course/<str:delete_id>', views.delete_course, name='delete_course'),

    path('edit_subject/<str:subject_id>', views.edit_subject, name='edit_subject'),
    path('edit_subject_save', views.edit_subject_save, name='edit_subject_save'),
    path('delete_subject/<str:delete_id>', views.delete_subject, name='delete_subject'),


    path('student_home', studentviews.student_home, name='student_home'),
    path('staff_home', staffviews.staff_home, name='staff_home'),
    path('staff_take_attendance', staffviews.staff_take_attendance, name='staff_take_attendance'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

