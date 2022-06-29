from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "admintemplate/base.html"
