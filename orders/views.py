from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request, 'orders/home.html')


def place_order(request):
    return render(request, 'orders/place_order.html')

def cancel_order(request, order_id):
    return render(request, 'orders/cancel_order.html')


def make_payment(request):
    return render(request, 'orders/make_payment.html')

def submit_feedback(request):
    return render(request, 'orders/submit_feedback.html')