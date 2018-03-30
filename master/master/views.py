from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import UserForm
# Create your views here.


# Homepage view
def home(request):
    return render(request, 'pages/index.html',{'page':'home'})


# Mentions legal view
def mentions(request):
    return render(request, 'pages/mentions_legal.html')


# Contact view
def contact(request):
    return render(request, 'pages/contact.html')


