from django.shortcuts import render
from ShopApp.models import *

# Create your views here.
def shop(request):
    all_items = Item.objects.all()
    return render(request, 'ShopApp/shop.html', {'all_items': all_items})