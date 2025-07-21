from django.shortcuts import render,redirect

# Create your views here.

def login_view(request):
    return render(request, 'accounts/login.html')

def register_view(request):
    return render(request, 'accounts/reqister.html')

def logout_view(request):
    return render(request, 'accounts/logout.html')