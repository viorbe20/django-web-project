from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        
        if contact_form.is_valid():
            name = request.POST.get('Nombre')
            email = request.POST.get('Email')
            message = request.POST.get('Mensaje')
            
            # Redirect to contact
            
            return redirect("/contacto/?valido")
            
    return render(request, 'ContactApp/contact.html', {'contact_form': contact_form})