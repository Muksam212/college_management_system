from django.shortcuts import render
from rest_framework import generics
from college_api.serializers import *

from college_management_app.models import *

# Create your views here.

#parent serializers
class ParentListCreate(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class =  ParentSerializer

class ParentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    lookup_field = "id"


#course serializer
class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "id"


#department serializer
class DepartmentListCreate(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentUpdateRetrieveDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
