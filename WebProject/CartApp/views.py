from CartApp.cart import Cart
from ShopApp.models import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

def add_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add_product(product)
    return redirect("Tienda")

def remove_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove_product(product)
    return redirect("Tienda")

def reduce_quantity(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.reduce_quantity(product)
    return redirect("Tienda")

def empty_cart(request):
    cart = Cart(request)
    cart.empty_cart()
    return redirect("Tienda")