from django.shortcuts import render, redirect


# Create your views here.
def create_product(request):
    return render(request, 'products/create_product.html')

def update_product(request):
    return render(request, 'products/update_product.html')

def remove_product(request):
    return render(request, 'products/remove_product.html')