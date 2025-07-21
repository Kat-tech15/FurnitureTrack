from django.urls import path
from . import views

urlpatterns = [
    path('create_product/', views.create_product, name='create_product'),
    path( 'product/<int:product_id>/update', views.update_product, name='update_product'),
    path('product<int:product_id>/remove', views.remove_product, name='remove_product'),
]