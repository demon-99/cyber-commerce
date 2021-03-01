from django.shortcuts import render
from . models import *
# Create your views here.
def store(request):
    if request.user.is_authenticated:
        Customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=Customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items=[]
    products = Product.objects.all()
    context={'items':items,'order':order,'products':products}
    return render(request,'store/store.html',context)

def cart(request):
    if request.user.is_authenticated:
        Customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=Customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items=[]
    context={'items':items,'order':order}
    return render(request,'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        Customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=Customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items=[]
    context={'items':items,'order':order}
    return render(request,'store/checkout.html',context)

def about(request):
    if request.user.is_authenticated:
        Customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=Customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items=[]
    context={'items':items,'order':order}
    return render(request,'store/about.html',context)

def contact(request):
    if request.user.is_authenticated:
        Customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=Customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items=[]
    context={'items':items,'order':order}
    return render(request,'store/contact.html',context)