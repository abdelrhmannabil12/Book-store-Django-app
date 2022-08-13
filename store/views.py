from ast import Or
from unicodedata import name
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.core.paginator import Paginator

def store(request):
    books = Book.objects.all()

    pagination=Paginator(books,3)
    page=request.GET.get('page')
    booksperpage=pagination.get_page(page)
    return render(request, 'store/store.html', {'books': books,
    'booksperpage':booksperpage})


def profile(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, compelte=False)
        items = order.orderitem_set.all()

    else:
        items = []
    return render(request, 'store/profile.html', {'items': items, 'order': order})


def logout(request):
    return render(request, 'store/logout.html')


def login(request):

    return render(request, 'store/login.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            customer, created = Customer.objects.get_or_create(email=email
                                                               )
            customer.user = form.save()
            customer.name = username
            customer.save()

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'store/register.html', {'form': form})


def updateitem(request):
    data = json.loads(request.body)
    bookid = data['bookid']
    action = data['action']
    print(action)
    customer = request.user.customer
    book = Book.objects.get(id=bookid)
    order, created = Order.objects.get_or_create(
        customer=customer, compelte=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, book=book)

    if action == "add":
        orderItem.quantity = (orderItem.quantity+1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity-1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('book was added', safe=False)
