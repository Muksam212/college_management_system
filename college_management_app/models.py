from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GENDER = (
    ('MALE','MALE'),
    ('FEMALE','FEMALE')
)

class Admin(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "admins")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"

    def __str__(self):
        return "{}".format(self.name)

class Parent(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="parent/profile")
    ph_number = models.PositiveIntegerField("Phone Number")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Parent"
        verbose_name_plural = "Parents"
    
    def __str__(self):
        return "{}".format(self.name)

class Course(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return "{}".format(self.name)



class Department(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name="departments")
    total_staff = models.PositiveIntegerField()
    total_student = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return "{}".format(self.name)


    
class Staff(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name = "staffs")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name ='staffs')
    salary = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staffs"

    def __str__(self):
        return "{}".format(self.name)


class Class(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="departments")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Classes"

    def __str__(self):
        return "{}".format(self.name)


class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ManyToManyField(Course)
    parent = models.ManyToManyField(Parent)
    temporary_address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=100, choices=GENDER)
    profile_pic = models.ImageField(upload_to="student/profile")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return "{}".format(self.name)

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    profile_pic = models.ImageField("Profile Picture", upload_to="teacher/profile")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return "{}".format(self.name)