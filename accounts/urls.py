from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'dashboard'),
    path('customer/<pk_test>/', views.customer, name ='customer'),
    path('products/', views.products, name = 'products'),
    path('create_order/', views.createOrder, name = 'createOrder'),
    path('update_order/<str:pk>/', views.updateOrder, name='updateOrder'),
    # path('delete_order/<str:pk>/', views.deleteOrders, name='deleteOrders'),
    path('deleteOrders/<str:pk>/', views.deleteOrders, name= 'deleteOrders'),

]