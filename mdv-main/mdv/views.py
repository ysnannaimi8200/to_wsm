from urllib import request
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CreateUserForm
from .decorators import unauthenticated_user
# Create your views here.



def home_screen_view(request):
    print(request.headers)
    return render(request, "mdv/home.html",{})


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username , password= password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password are incorrect')
    context={}
    return render(request, 'mdv/login.html')

def logoutuser (request):
    logout(request)
    return redirect('login')


def registerpage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() 
            user = form.cleaned_data.get('username')
            messages.success(request,'Account successfully created for  ' + user)    

    context = {'form':form}
    return render(request, "mdv/register.html",context)

