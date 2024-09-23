from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage 

def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name'] 
            email = contact_form.cleaned_data['email'] 
            message = contact_form.cleaned_data['message']  
            
            email_message = EmailMessage(
                "Mensaje de contacto",
                f"De: {name}\n\nE-mail: {email}\n\nMensaje:\n\n{message}",
                'source@example.com', # Source email 
                ["target@example.com"], # Target email 
                reply_to=[email]
            )

            try:
                email_message.send()

                return redirect("/contacto/?valido")
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
                return redirect("/contacto/?novalido")
        
        else:
            return redirect("/contacto/?novalido")
    
    return render(request, 'ContactApp/contact.html', {'contact_form': contact_form})
