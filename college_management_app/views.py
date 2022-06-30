from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User

from college_management_app.forms import RegisterForm

class LoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            pass
        else:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)


class HomePage(TemplateView):
    template_name = "college/base.html"

class RegisterPage(SuccessMessageMixin,FormView):
    template_name = "registration/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('college_management_app:register-app')
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
