from django.shortcuts import render, redirect
from .models import *
from .forms import OrdersForm


def home(request):
    customers = Customer.objects.all()
    orders = Orders.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='pending').count()
    context = {'customers': customers, 'orders': orders, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending}
    return render(request, 'accounts/dashboard.html', context)


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.orders_set.all()
    order_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customer.html', context)


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'accounts/products.html', context)


def createOrder(request):
    form = OrdersForm()
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):

    orders = Orders.objects.get(id=pk)
    form = OrdersForm(instance=orders)

    if request.method == 'POST':
        form = OrdersForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


# def deleteOrders(request, pk):
#     orders = Orders.objects.get(id=pk)
#     context = {'item': orders}
#     return render(request, 'accounts/delete.html', context)

def deleteOrders(request, pk_test2):
    orders2 = Customer.objects.get(id=pk_test2)
    if request.method == 'POST':
        orders2.delete()
        return redirect('/')
    context = {'item': orders2}
    return render(request, 'accounts/delete.html', context)


