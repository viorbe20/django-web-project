from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth import authenticate

class UserAuthentication(View):
    
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'Auth/authentication.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Inicio')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                
            return render(request, 'Auth/authentication.html', {'form': form})
    
def user_logout(request):
    logout(request)
    return redirect('Inicio')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user_name = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=user_name, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('Inicio')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")
    
    form = AuthenticationForm()
    return render(request, 'Login/login.html', {'form': form})