from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import signup_form

# Create your views here.

def home(request):
    context = { }
    return render(request, 'index.html' ,context)

    
    
def register_page(request):
    form = signup_form()
    
    
    if request.method =="POST":
         form = signup_form(request.POST)
         if form.is_valid():
             form.save()
             
        
    context = {'form':form }
    return render(request, 'accounts/registration.html' ,context)

def login_page(request):
    context = { }
    return render(request, 'accounts/login.html',context)