from django.urls import path
from college_management_app.views import (HomePage,RegisterPage, LoginPage, DashboardPage,StudentCreate, 
                                        LogoutPage, StudentList, StudentEdit, StudentDelete)

app_name = "college_management_app" #Custom url

urlpatterns = [
    path('', HomePage.as_view(), name='home-page'),
    path('dashboard/', DashboardPage.as_view(), name='dashboard-page'),
    path('register/', RegisterPage.as_view(), name='register-page'),
    path('login/', LoginPage.as_view(), name='login-page'),
    path('logout/', LogoutPage.as_view(), name='logout-page'),
    
    #student url
    path('student_create/',StudentCreate.as_view(), name='student-create'),
    path('student_list/', StudentList.as_view(), name='student-list'),
    path('student/<int:id>/update/', StudentEdit.as_view(), name='student-update'),
    path('student/<int:id>/delete/', StudentDelete.as_view(), name='student-delete')
]