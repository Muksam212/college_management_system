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
    photo = models.ImageField(upload_to="parent/photo", null=True, blank=True)
    ph_number = models.PositiveIntegerField("Phone Number")
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Parent"
        verbose_name_plural = "Parents"

    def __str__(self):
        return "{}".format(self.name)

    def delete_at(self):
        self.deleted_at = timezone.now()
        super().save()

class Student(models.Model):
    name = models.CharField("Student Name",max_length=100)
    faculty = models.CharField(max_length=100, choices=FACULTY)
    address = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    ph_number = models.PositiveIntegerField("Phone Number")
    photo = models.ImageField(upload_to="student/photo",null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER)
    date_created = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return "{}".format(self.name)

    def delete(self):
        self.deleted_at = timezone.now()
        super().save()


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="teachers")
    address = models.CharField(max_length=100)
    email = models.EmailField()
    ph_number = models.PositiveIntegerField("Phone Number")
    photo = models.ImageField(upload_to="teacher/photo",null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    faculty = models.CharField(max_length=100, choices=FACULTY)
    gender = models.CharField(max_length=100, choices=GENDER)
    date_created = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return "{}".format(self.name)

    def delete_at(self):
        self.deleted_at = timezone.now()
        super().save()

class Accountant(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name = "accountants")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name = "accountants")
    amount = models.PositiveIntegerField("Salary of teacher and amount to be paid by student")
    ph_number = models.PositiveIntegerField("Phone Number")
    date_created = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Accountant"
        verbose_name_plural = "Accountants"

    def __str__(self):
        return "{}".format(self.name)

    def delete_at(self):
        self.deleted_at = timezone.now()
        super().save()


class Subject(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100, choices=FACULTY)
    student = models.ManyToManyField(Student, related_name="subjects")
    teacher = models.ManyToManyField(Teacher, related_name="subjects")
    date_created = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return "{}".format(self.name)

    def delete(self):
        self.deleted_at = timezone.now()
        super().save()

class Admin(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admins")
    photo = models.ImageField(upload_to="admin/photo",null=True, blank=True)
    ph_number = models.PositiveIntegerField("Phone Number")
    gender = models.CharField(max_length=100, choices=GENDER)
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(default="abc@gmail.com", null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Admins"

    def __str__(self):
        return "{}".format(self.name)

    def delete(self):
        self.deleted_at = timezone.now()
        super().save()


class Driver(models.Model):
    name = models.CharField("Driver Name", max_length=100)
    photo = models.ImageField(upload_to="driver/photo",null=True, blank=True)
    age = models.PositiveIntegerField() 
    ph_number = models.PositiveIntegerField("Phone number of driver who used bus")
    gender = models.CharField(max_length=100, choices=GENDER)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        return "{}".format(self.name)

    def delete_at(self):
        self.deleted_at = timezone.now()
        super().save()