from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import signup_form
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.




    
    
def register_page(request):
    form = signup_form()
    
    
    if request.method =="POST":
         form = signup_form(request.POST)
         if form.is_valid():
             form.save()
             user = form.cleaned_data.get('username')
              #  sends a pop up  messgae of a successfully created acoount
             messages.success(request, 'Account created successfully for' + user) 
             
             return redirect('login')
             
        
    context = {'form':form }
    return render(request, 'accounts/registration.html' ,context)

def login_page(request):
    
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
          # using the auth method
        user = authenticate(request , username = username,password=password)
        
        #  checking if user is the one,and redirect to the homepage
        if user is not None:
            login(request ,user)
            return redirect('index')
        else:
            messages.info(request,'The Username/Password entered is incorrect..')
            
        
    context = { }
    return render(request, 'accounts/login.html',context)

def logout_user(request):
    logout(request)
    return render(request , 'accounts/login.html')


def index(request):
    context = { }
    return render(request, 'index.html' ,context)