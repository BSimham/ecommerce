from django.shortcuts import render

# Create your views here.
def store(request):
    context={}
    render(request,'store/store.html',context)
def cart(request):
    context={}
    render(request,'store/cart.html',context)
def checkout(request):
    context={}
    render(request,'store/checkout.html',context)