from ast import Or
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
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


def updateitem(request):
    data=json.loads(request.body)
    bookid=data['bookid']
    action=data['action']
    print(action)
    customer=request.user.customer
    book=Book.objects.get(id=bookid)
    order , created=Order.objects.get_or_create(customer=customer,compelte=False)
    orderItem, created=OrderItem.objects.get_or_create(order=order,book=book)

    if action== "add":
        orderItem.quantity=(orderItem.quantity+1)
    elif action =="remove":
        orderItem.quantity=(orderItem.quantity-1)
    orderItem.save()
    if orderItem.quantity <=0 :
        orderItem.delete()
    return JsonResponse('book was added',safe=False)