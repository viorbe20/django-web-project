from django.shortcuts import render
# from ShopApp.models import Shop

# Create your views here.
def shop(request):
    return render(request, 'ShopApp/shop.html')