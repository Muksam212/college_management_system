from django.urls import path
from college_management_app.views import HomePage,RegisterPage, LoginPage
app_name = "college_management_app"

urlpatterns = [
    path('', HomePage.as_view(), name='home-page'),
    path('register/', RegisterPage.as_view(), name='register-page'),
    path('login/', LoginPage.as_view(), name='login-page')
]