from django.shortcuts import render,redirect

# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/reqister.html')

def logout(request):
    return render(request, 'accounts/logout.html')