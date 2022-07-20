from django.urls import path

from college_api.views import *



app_name = "college_api" #custom  url

urlpatterns = [
    #parent api
    path('api/parent/list', ParentListCreate.as_view(), name='parent-create'),
    path('api/parent/update/delete/<int:id>/',ParentUpdateDetails.as_view(), name='parent-update'),

    #student api
    path('api/student/list', StudentListCreate.as_view(), name='student-create'),
    path('api/student/update/delete/<int:id>/', StudentUpdateDetails.as_view(), name='student-update'),

    #teacher api
    path('api/teacher/list', TeacherListCreate.as_view(), name='teacher-list'),
    path('api/teacher/update/delete/<int:id>/', TeacherUpdateDetails.as_view(), name='teacher-update')

]
