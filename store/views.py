from django.shortcuts import render

# Create your views here.
def store(request):
    context={}
    render(request,'store/store.html',context)