from django.shortcuts import render, HttpResponse

from Shoppingcart.cart import Cart


# Create your views here.

def home(request):
    sh_cart = Cart(request)
    return render(request, 'ProjectWebApp/home.html')







    
# def contact(request):
#     return render(request, 'ProjectWebApp/contact.html')