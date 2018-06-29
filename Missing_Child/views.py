from django.shortcuts import render,redirect
from django.contrib.auth import login as login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .forms import Upload_Form
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import  Child

def home(request):
    child = Child.objects.all()
    return render(request, 'home.html',{'child':child})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})

def upload(request):
    if request.method == 'POST':
        form = Upload_Form(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=Upload_Form()
    return render(request,'upload.html',{'form':form })
