from django.urls import path
from BlogApp import views

urlpatterns = [
    path('', views.blog, name="Blog"),
]