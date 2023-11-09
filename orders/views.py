from email import message
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderDetail
from Shoppingcart.cart import Cart
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


# Create your views here.
@login_required(login_url = '/auth/login')
def process_order(request):
    order = Order.objects.create(customer = request.user)
    cart = Cart(request)
    orders = list()
    for key,value in cart.carrito.items():
        orders.append(OrderDetail(
            product_id = key,
            quantity = value['product_quantity'],
            customer = request.user,
            order = order


        ))
    #similar to several insert into sql
    OrderDetail.objects.bulk_create(orders)
    send_order(
        order=order,
        order_detail=orders, 
        username = request.user.username, 
        user_email= request.user.email
        )
    messages.success(request, 'El pedido se ha hecho correctamente')
    return redirect('../store')

def send_order(**kwargs):
    subject = 'Gracias por tu compra'
    message = render_to_string('emails/order.html',{
        'order': kwargs.get('order'),
        'order_detail': kwargs.get('order_detail'),
        'username': kwargs.get('username'),
    })

    message_text = strip_tags(message)
    from_email = 'tupaginafav@tetete.com'
    #to_email = kwargs.get('user_email')
    to_email = 'onesold8@gmail.com'

    send_mail(subject, message_text, from_email, [to_email], html_message = message)