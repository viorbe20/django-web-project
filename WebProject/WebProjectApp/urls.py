from django.urls import path
from WebProjectApp import views

urlpatterns = [
    path('', views.home, name="Inicio"),
    path('servicios', views.services, name="Servicios"),
    path('tienda', views.shop, name="Tienda"),
    path('blog', views.blog, name="Blog"),
    path('contacto', views.contact, name="Contacto"),
]
