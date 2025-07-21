from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('place_order/', views.place_order, name='place_order'),
    path('cancel/<int:order_id>/cancel/', views.cancel_order, name='cancel_order'),
    path('make_payment/', views.make_payment, name='make_payment'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
]