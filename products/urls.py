from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path( 'product/<int:product_id>/detail', views.product_detail, name='product_detail'),
    path('product<int:product_id>/remove', views.remove_product, name='remove_product'),
]