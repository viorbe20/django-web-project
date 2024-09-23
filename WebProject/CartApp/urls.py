from django.urls import path
from CartApp import views

app_name = 'cart'

urlpatterns = [
    path('agregar/<int:product_id>/', views.add_product, name="agregar"),
    path('eliminar/<int:product_id>/', views.remove_product, name="eliminar"),
    path('reducir/<int:product_id>/', views.reduce_quantity, name="reducir"),
    path('vaciar/', views.empty_cart, name="vaciar"),
]
