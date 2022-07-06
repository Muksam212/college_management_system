from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

#making global variable for choices
GENDER = (
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHER','OTHER'),
)

FACULTY = (
    ('SCIENCE','SCIENCE'),
    ('MANAGEMENT','MANAGEMENT'),
    ('OTHER','OTHER')
)

class Parent(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER)
    photo = models.ImageField(upload_to="parent/photo")
    ph_number = models.PositiveIntegerField("Phone Number")

    class Meta:
        verbose_name = "Parent"
        verbose_name_plural = "Parents"

    def __str__(self):
        return "{}".format(self.name)

class Student(models.Model):
    name = models.CharField("Student Name",max_length=100)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name="students")
    faculty = models.CharField(max_length=100, choices=FACULTY)
    address = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    ph_number = models.PositiveIntegerField("Phone Number")
    photo = models.ImageField(upload_to="student/photo")
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER)
    date_created = models.DateTimeField(auto_now_add=True)
    delete_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return "{}".format(self.name)

    def delete(self):
        self.delete_at = timezone.now()
        super().save()


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    ph_number = models.PositiveIntegerField("Phone Number")
    photo = models.ImageField(upload_to="teacher/photo")
    age = models.PositiveIntegerField(null=True, blank=True)
    faculty = models.CharField(max_length=100, choices=FACULTY)
    gender = models.CharField(max_length=100, choices=GENDER)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return "{}".format(self.name)


class Accountant(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name = "accountants")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name = "accountants")
    ph_number = models.PositiveIntegerField("Phone Number")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Accountant"
        verbose_name_plural = "Accountants"

    def __str__(self):
        return "{}".format(self.name)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100, choices=FACULTY)
    student = models.ManyToManyField(Student, related_name="subjects")
    teacher = models.ManyToManyField(Teacher, related_name="subjects")
    date_created = models.DateTimeField(auto_now_add=True)
    delete_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return "{}".format(self.name)

    def delete(self):
        self.delete_at = timezone.now()
        super().save()

class Admin(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admins")
    photo = models.ImageField(upload_to="admin/photo")
    ph_number = models.PositiveIntegerField("Phone Number")
    gender = models.CharField(max_length=100, choices=GENDER)
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(default="abc@gmail.com", null=True, blank=True)
    delete_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"

    def __str__(self):
        return "{}".format(self.name)

    def delete(self):
        self.delete_at = timezone.now()
        super().save()


class Driver(models.Model):
    name = models.CharField("Driver Name", max_length=100)
    photo = models.ImageField(upload_to="driver/photo")
    age = models.PositiveIntegerField()
    ph_number = models.PositiveIntegerField("Phone number of driver who used bus")
    gender = models.CharField(max_length=100, choices=GENDER)

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        return "{}".format(self.name)