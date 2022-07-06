from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from college_management_app.forms import RegisterForm, LoginForm

class HomePage(TemplateView):
    template_name = "college/base.html"

class RegisterPage(SuccessMessageMixin,FormView):
    template_name = "registration/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('college_management_app:register-page')
    success_message = "Register Successfully"

    def form_valid(self, form):
        uname = form.cleaned_data['username']
        email = form.cleaned_data['email']
        pwd = form.cleaned_data['password']
        cf_pwd = form.cleaned_data['confirm_password']

        User.objects.create_user(username=uname, email=email, password=pwd)
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

class LoginPage(FormView):
    template_name = "registration/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('college_management_app:login-page')

    def form_valid(self, form):
        uname = form.cleaned_data['username']
        pword = form.cleaned_data['password']

        user = authenticate(username=uname, password=pword)

        if user is not None:
            login(self.request, user)
        else:
            return render(self.request, self.template_name,{'error':'Username or Password is incorrect','form':form})

        return super().form_valid(form)
        
