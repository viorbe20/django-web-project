from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from OrdersApp.models import Order, OrderItems
from CartApp.cart import Cart

@login_required(login_url="/autenticacion/iniciar_sesion")
def place_order(request):
    order = Order.objects.create(user=request.user)
    cart = Cart(request)
    order_items = list()
    
    for key, value in cart.cart.items():
        
        order_items.append(OrderItems(
            item_id = key,
            quantity = value["quantity"],
            user = request.user,
            order = order
        ))
    
    OrderItems.objects.bulk_create(order_items)
    
    send_email (
        order = order,
        order_items = order_items,
        username = request.user.username,
        user_email = request.user.email
    )
    
    messages.success(request, "El pedido se ha realizado correctamente")

    return redirect('Tienda')

def send_email(**kwargs):
    subject = "Gracias por realizar el pedido"
    message = render_to_string("emails/order.html", {
        "order": kwargs.get("order"),
        "order_items": kwargs.get("order_items"),
        "username": kwargs.get("username")
    })
    
    message_text = strip_tags(message)
    from_email = "noreply@example.com"
    #to = kwargs.get("user_email")
    to = 'to@example.com'
    
    send_mail(subject, message_text, from_email, [to], html_message=message)