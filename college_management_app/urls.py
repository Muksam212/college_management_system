from django.urls import path
from college_management_app.views import HomePage
app_name = "college_management_app"

urlpatterns = [
    path('', HomePage.as_view(), name='home-page')
]