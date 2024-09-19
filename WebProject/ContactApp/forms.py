from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100, required=True)
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(label='Mensaje', widget=forms.Textarea) # With widget message field will appear as a multi-line text area instead of a single-line text input