from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order, OrderDetail
from Shoppingcart.cart import Cart


# Create your views here.
@login_required(login_url = '/auth/login')
def proccess_order(request):
    order = Order.objects.create(user = request.user)
    cart = Cart(request)
    orders = list()
    for key,value in cart.objects.items():
        orders.append(OrderDetail(
            product_id = key,
            quantity = value ['quantity'],
            user = request.user,
            order = order


        ))