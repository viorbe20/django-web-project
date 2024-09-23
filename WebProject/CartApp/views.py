from CartApp import Cart
from ShopApp.models import *
from django.shortcuts import redirect

def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add_product(product)
    return redirect("tienda")

def remove_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove_product(product)
    return redirect("tienda")

def reduce_quantity(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.reduce_quantity(product)
    return redirect("tienda")

def empty_cart(request):
    cart = Cart(request)
    cart.empty_cart()
    return redirect("tienda")