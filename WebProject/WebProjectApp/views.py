from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'WebProjectApp/home.html')

def services(request):
    return render(request, 'WebProjectApp/services.html')

def shop(request):
    return render(request, 'WebProjectApp/shop.html')

def blog(request):
    return render(request, 'WebProjectApp/blog.html')

def contact(request):
    return render(request, 'WebProjectApp/contact.html')


