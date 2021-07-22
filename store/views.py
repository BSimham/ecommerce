from store.models import Product
from django.shortcuts import render
from .models import *
# Create your views here.


def store(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'store/store.html',context)

def cart(request):

    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer,complete=False) #creating an object or quering one
        items=order.orderitem_set.all() # it will get all the orderitems that have this order as parent
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0}

    context={'items':items, 'order':order}
    return render(request,'store/cart.html',context)

def checkout(request):
    context={}
    return render(request,'store/checkout.html',context)