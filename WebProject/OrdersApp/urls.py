from django.urls import path
from OrdersApp import views

urlpatterns = [
    path('', views.place_order, name="procesar_pedido"),
]