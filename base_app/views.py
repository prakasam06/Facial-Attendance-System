from django.shortcuts import render,redirect
from django.contrib.auth import logout
# Create your views here.
from .decorators import group_required

def home(request):
    return render(request,'home.html')

def logout_view(request):
    logout(request)
    # Optionally, you can redirect the user to another page after logout.
       
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        print(request.POST) 
    return render(request,'home.html')

