from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    customers = Customer.objects.all()
    orders = Orders.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='pending').count()
    context = {'customers' : customers, 'orders' : orders, 'total_orders' : total_orders, 'delivered' : delivered, 'pending' : pending}
    return render(request, 'accounts/dashboard.html', context)

def customer(request):
    return render(request, 'accounts/customer.html')

def products(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'accounts/products.html', context)
