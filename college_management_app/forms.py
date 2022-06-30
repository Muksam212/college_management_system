from college_management_app.models import *
from django.contrib.auth.models import User
from django import forms

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class':'form-control'
        })
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })