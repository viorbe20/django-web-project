from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

class UserAuthentication(View):
    
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'AuthApp/authentication.html', {'form': form})
