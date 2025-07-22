from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order
from products.models import Product


# Create your views here.
def home(request):
    return render(request, 'orders/home.html')

@login_required
def place_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        quantity = request.POST.get('quantity', 1)
        Order.objects.create(
            customer=request.user,
            product=product,
            quntity=quantity,
        )
        return redirect('my_orders')
    
    return render(request, 'orders/place_order.html', {'product': product})

def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    if order.status == 'pending':
        order.status = 'cancelled'
        order.save()
        return redirect('my_orders')
    return render(request, 'orders/cancel_order.html')

def my_orders(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'orders/my_orders.html', {'orders': orders})

def make_payment(request):
    return render(request, 'orders/make_payment.html')

def submit_feedback(request):
    return render(request, 'orders/submit_feedback.html')