from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

from college_management_app.forms import RegisterForm, LoginForm, StudentForm

#class based views

class LoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            pass
        else:
            return redirect('college_management_app:login-page')
        return super().dispatch(request, *args, **kwargs)
    


class HomePage(TemplateView):
    template_name = "college/index.html"

class DashboardPage(LoginRequiredMixin,TemplateView):
    template_name = "dashboard/base.html"

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
            print(user,'--------------')
            return redirect('college_management_app:dashboard-page')
        else:
            return render(self.request, self.template_name,{'error':'Username or Password is incorrect','form':form})

        return super().form_valid(form)


#Crud Student
class StudentCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    template_name = "student/add.html"
    form_class = StudentForm
    success_url = reverse_lazy('college_management_app:student-create')
    success_message = "Student Register Successful"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return JsonResponse({'error':'Failed to Saved Form'})

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

    def get_initial(self):
        return {'name':'sdfasd'}