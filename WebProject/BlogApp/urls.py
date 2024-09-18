from django.urls import path
from BlogApp import views

urlpatterns = [
    path('', views.blog, name="Blog"),
    path('categoria/<int:category_id>/', views.category, name="Categoria"),
]
