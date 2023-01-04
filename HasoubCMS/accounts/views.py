from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
#from django.contrib.auth.views import login, logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.http import HttpResponse
import datetime 
from django.contrib.auth.decorators import login_required


#from custom_functions import get_error_message
def get_error_message(request):
    password1=request.POST['password1']
    password2=request.POST['password2']
    email=request.POST['email']
    username=request.POST['username']
    if AppUser.objects.filter(username=username).exists():
        return "Username already exists"
    if password1!=password2:
        return "The Passwords didn't match"
    if AppUser.objects.filter(email=email).exists():
        return "Email already exists"


# Create your views here.

from .forms import *

@login_required(login_url='/login')    
def register_request(request):
    if request.user.is_superuser or request.user.is_staff:
        if request.method=="POST":
            form=NewUserForm(request.POST)
            if form.is_valid():
                user=form.save()
                login(request,user)
                print("register successful")
                messages.success(request,"Register successful")
                return redirect('homepage')
            print("unsucessful")
            messages.error(request,get_error_message(request))
            return render(request=request,template_name='register.html',context={'register_form':form})
            #return HttpResponse("Invalid")
        else:
            form=NewUserForm()
            return render(request=request,template_name='register.html',context={'register_form':form})
        # now = datetime.datetime.now()
        # html = "<html><body>It is now %s.</body></html>" % now
        # return HttpResponse(html)
    else:
        return HttpResponse("Not super user")
def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                print('loggged')
                messages.info(request,f"You are logged as {username}")
                return redirect('homepage')
            else:
                print("Invalid username and password!")
                messages.error(request,"invalid username and password")
        else:
            print("not valid form")
            messages.error(request,"not valid form")

    form=AuthenticationForm()
    return render(request=request,template_name='login.html',context={'login_form':form})
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
def logout_request(request):
    logout(request)
    messages.info(request,"You have sucessfully logged out")
    return redirect("login")
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)

def home_page(request):
    return render(request,'sara.html')