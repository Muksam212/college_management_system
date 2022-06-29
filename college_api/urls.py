from django.urls import path
from college_api.views import (ParentListCreate, ParentRetrieveUpdateDestroy, 
                                CourseListCreate, CourseRetrieveUpdateDestroy, DepartmentListCreate,
                                 DepartmentUpdateRetrieveDestroy)

app_name = "college_api"

urlpatterns = [
    #parent url
    path('api/parent/list/create/',ParentListCreate.as_view(), name='parent-create'),
    path('api/parent/update/delete/<int:id>/', ParentRetrieveUpdateDestroy.as_view(), name="parent-update-delete"),

    #course url
    path('api/course/list/create/', CourseListCreate.as_view(), name="course-create"),
    path('api/course/update/delete/<int:id>/', CourseRetrieveUpdateDestroy.as_view(), name="course-delete"),

    #department url
    path('api/department/list/create/', DepartmentListCreate.as_view(), name="department-create"),
    path('api/department/update/delete/<int:id>/', DepartmentUpdateRetrieveDestroy.as_view(), name="department-delete")

]
