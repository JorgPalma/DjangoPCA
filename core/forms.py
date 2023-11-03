from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Persona, Contacto, Blog


class RegistroForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class EditarPefil(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = ["imagen", "primer_nombre", "segundo_nombre", "apellido_pat", "apellido_mate", "rut", "digito_ver", "telefono", "edad"]


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ["nombre_contacto", "email", "asunto", "mensaje"]

class AddPostForms(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ["titulo", "informacion", "categoria", "imagen"]
