from django.urls import path
from .views import UserAuthentication, user_logout

urlpatterns = [
    path('', UserAuthentication.as_view(), name="Autenticacion"),
    path('cerrar_sesion', user_logout, name="CerrarSesion"),
]
