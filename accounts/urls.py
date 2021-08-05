from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'dashboard'),
    path('customer/<pk_test>/', views.customer, name ='customer'),
    path('products/', views.products, name = 'products'),
    path('create_order/', views.createOrder, name = 'createOrder'),
]