from ast import Or
from django.shortcuts import render
from .models import *
# Create your views here.
def store(request):
    books=Book.objects.all()
    return render(request,'store/store.html',{'books':books})
def profile(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order , created=Order.objects.get_or_create(customer=customer,compelte=False)
        items=order.orderitem_set.all()

    else:
        items=[]
    return render(request,'store/profile.html',{'items':items,'order':order})
def logout(request):
    return render(request,'store/logout.html')
