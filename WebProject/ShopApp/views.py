from django.shortcuts import render
from ShopApp.models import *

# Create your views here.
def shop(request):
    all_products = Product.objects.all()
    return render(request, 'ShopApp/shop.html', {'all_products': all_products})