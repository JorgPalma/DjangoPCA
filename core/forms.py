from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Persona, Contacto, Blog, Formulario


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
        exclude = ()
        labels = {
            'nombre_contacto': ('Nombre'),
            'email': ('E-mail'),
            'asunto': ('Asunto'),
            'mensaje': ('Mensaje'),
        }
        widgets = {
            "nombre_contacto":forms.TextInput(attrs={'placeholder':'Nombre Apellido','name':'nombre','id':'nombre','class':'input-class_name'}),
            "email":forms.EmailInput(attrs={'placeholder':'E-mail','name':'email','id':'email','class':'input-class_name'}),
            "asunto":forms.TextInput(attrs={'placeholder':'Asunto','name':'asunto','id':'asunto','class':'input-class_name'}),
            "mensaje":forms.Textarea(attrs={'placeholder':'¿Cómo podemos ayudarte?','name':'mensaje','id':'mensaje','class':'input-class_name'}),
                }

class AddPostForms(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ["titulo", "informacion", "categoria", "imagen"]


class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ["vacunas","ac_fisica","comida_tiempo","tiene_sintomas","sintomas","tiene_enfermedad","enferme_ante","tiene_alergias","alergias","tiene_operaciones","operaciones"]



