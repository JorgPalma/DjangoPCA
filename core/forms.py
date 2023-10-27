from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Persona


class RegistroForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class EditarPefil(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = ["imagen", "primer_nombre", "segundo_nombre", "apellido_pat", "apellido_mate", "rut", "digito_ver", "telefono", "edad"]
