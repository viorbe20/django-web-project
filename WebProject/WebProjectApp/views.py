from django.shortcuts import render, HttpResponse
from ServicesApp.models import Service

def home(request):
    return render(request, 'WebProjectApp/home.html')

def services(request):
    all_services = Service.objects.all() # Get all services created
    return render(request, 'WebProjectApp/services.html', {'all_services': all_services})

def shop(request):
    return render(request, 'WebProjectApp/shop.html')

def blog(request):
    return render(request, 'WebProjectApp/blog.html')

def contact(request):
    return render(request, 'WebProjectApp/contact.html')