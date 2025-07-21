from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request, 'orders/home.html')


def place_order(request):
    return render(request, 'place_order.html')

def cancel_order(request, order_id):
    return render(request, 'cancel_order.html')


def make_payment(request):
    return render(request, 'make_payment.html')
