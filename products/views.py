from django.shortcuts import render, get_list_or_404
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):

    product = get_list_or_404(Product, id=product_id)

    return render(request, 'products/product_detail.html', {'product': product})

def remove_product(request):
    return render(request, 'products/remove_product.html')