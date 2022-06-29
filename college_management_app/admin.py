from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Admin,Parent,Course,Department,Staff,Class,Student,Teacher])
