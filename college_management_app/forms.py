from college_management_app.models import *
from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        uname = self.cleaned_data['username']
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError('Username Already exists')
        return uname
    
    def clean_mail(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email Already exists')
        return email

    def clean_confirm_password(self):
        pwd = self.cleaned_data['password']
        cf_pwd = self.cleaned_data['confirm_password']

        if pwd != cf_pwd:
            raise forms.ValidationError("Password didn't match")
        return cf_pwd


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','faculty','address','ph_number','photo','age']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Enter your Name'
        })
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control',
            })
        self.fields['photo'].widget.attrs.update({
            'class':'form-control',
            'onchange':'loadFile(event)',
        })