from django.urls import path
from college_management_app.views import HomePage,RegisterPage, LoginPage, DashboardPage,StudentCreate

app_name = "college_management_app" #Custom url

urlpatterns = [
    path('', HomePage.as_view(), name='home-page'),
    path('dashboard/', DashboardPage.as_view(), name='dashboard-page'),
    path('register/', RegisterPage.as_view(), name='register-page'),
    path('login/', LoginPage.as_view(), name='login-page'),

    #student url
    path('student_create/',StudentCreate.as_view(), name='student-create')
]