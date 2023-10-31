from django.shortcuts import render
from .cart import Cart
from Store.models import Product
from django.shortcuts import redirect
# Create your views here.

def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add_product(product)
    return redirect('store')

def substract_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.substract_product(product)
    return redirect('store')

def delete_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.delete_product(product)
    return redirect('store')

def clean_products(request, product_id):
    cart = Cart(request)
    cart.clean_cart()
    return redirect('store')

