from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Student,Teacher,Accountant,Admin,Subject,Parent,Driver])