from django.urls import path
from CartApp import views

app_name = 'cart'

urlpatterns = [
    path('agregar/<int:item_id>/', views.add_item, name="agregar"),
    path('eliminar/<int:item_id>/', views.remove_item, name="eliminar"),
    path('reducir/<int:item_id>/', views.reduce_quantity, name="reducir"),
    path('vaciar/', views.empty_cart, name="vaciar"),
]
