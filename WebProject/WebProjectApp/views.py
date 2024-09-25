from django.shortcuts import render
from CartApp.cart import Cart

def home(request):
    cart = Cart(request)
    return render(request, 'WebProjectApp/home.html')