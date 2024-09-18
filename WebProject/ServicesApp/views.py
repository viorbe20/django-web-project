from django.shortcuts import render
from ServicesApp.models import Service

# Create your views here.
def services(request):
    all_services = Service.objects.all()
    return render(request, 'ServicesApp/services.html', {'all_services': all_services})