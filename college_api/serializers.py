from dataclasses import fields
from rest_framework import serializers
from college_management_app.models import *


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class StaffSerializer(serializers.ModelSerializer):
    staffs = serializers.SlugRelatedField(queryset = Staff.objects.all(), slug_field = 'id')
    class Meta:
        model = Staff
        fields = ['name','staffs','salary']


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    #foreign key for nested serializers
    students = serializers.SlugRelatedField(queryset=Course.objects.all(), slug_field = 'id')
    students = serializers.SlugRelatedField(queryset=Parent.objects.all(), slug_field = 'id')
    class Meta:
        model = Student
        fields = ['name','students','students','address','email','age','gender']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"