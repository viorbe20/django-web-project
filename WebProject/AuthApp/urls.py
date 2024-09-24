from django.urls import path
from AuthApp import views

urlpatterns = [
    path('', views.authentication, name="Autenticacion"),
]
