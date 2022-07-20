from rest_framework import generics

from college_management_app.models import *
from college_api.serializers import *

from django.http import JsonResponse


class ParentListCreate(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class ParentUpdateDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    lookup_field = 'id'


class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'


class TeacherListCreate(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherUpdateDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'id'