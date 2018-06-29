from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Child

class SignUpForm(UserCreationForm):
    First_Name = forms.CharField(max_length=50, required=True)
    Last_Name = forms.CharField(max_length=50, required=True)
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=50, required=True)
    field_order = ['username','password1','password2','First_Name','Last_Name','email']
    class Meta:
        model = User
        fields = {'First_Name', 'Last_Name','username','email'}

class Upload_Form(forms.ModelForm):
    field_order = ['name', 'age', 'details','image']
    class Meta:
        model = Child
        fields = {'name','age','details','image'}
