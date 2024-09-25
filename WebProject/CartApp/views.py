from CartApp.cart import Cart
from ShopApp.models import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

def add_item(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.add_item(item)
    return redirect("Tienda")

def remove_item(request, item_id):
    cart = Cart(request)
    item = Item.objects.get(id=item_id)
    cart.remove_item(item)
    return redirect("Tienda")

def reduce_quantity(request, item_id):
    cart = Cart(request)
    item = Item.objects.get(id=item_id)
    cart.reduce_quantity(item)
    return redirect("Tienda")

def empty_cart(request):
    cart = Cart(request)
    cart.empty_cart()
    return redirect("Tienda")