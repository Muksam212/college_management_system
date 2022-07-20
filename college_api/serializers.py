from rest_framework import serializers
from college_management_app.models import *

class TeacherSerializer(serializers.ModelSerializer):
    #using foreign key 
    class Meta:
        model = Teacher
        fields = ['id','name','address','email','ph_number','photo','age','faculty','gender','date_created']

        
class StudentSerializer(serializers.ModelSerializer):
    #nested serializers
    teachers = TeacherSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ['id','name','faculty','address','email','ph_number','photo','age','gender','teachers','date_created']
        depth = 1

class ParentSerializer(serializers.ModelSerializer):
    
    #nested serializers
    students = StudentSerializer(many=True, read_only=True)
    class Meta:
        model = Parent
        fields = ['id','name','gender','photo','ph_number','students']
        depth = 1


