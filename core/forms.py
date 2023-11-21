from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Persona, Contacto, Blog, Formulario, Comentario, Mascota


class RegistroForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class EditarPefil(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = ["primer_nombre", "segundo_nombre", "apellido_pat", "apellido_mate", "rut", "digito_ver", "telefono", "edad", "imagen" ]
        labels = {
            'primer_nombre': ('Primer nombre'),
            'segundo_nombre': ('Segundo nombre'),
            'apellido_pat': ('Apellido paterno'),
            'apellido_mate': ('Apellido materno'),
            'rut': ('Rut (sin puntos)'),
            'digito_ver': ('Dígito verificador'),
            'telefono': ('Número de contacto'),
            'edad': ('Edad'),
        }

        widgets = {
            "primer_nombre":forms.TextInput(attrs={'placeholder':'Primer Nombre','name':'p_nombre','id':'p_nombre','class':'input-class_name'}),
            "segundo_nombre":forms.TextInput(attrs={'placeholder':'Segundo Nombre','name':'s_nombre','id':'s_nombre','class':'input-class_name'}),
            "apellido_pat":forms.TextInput(attrs={'placeholder':'Apellido Paterno','name':'p_apellido','id':'p_apellido','class':'input-class_name'}),
            "apellido_mate":forms.TextInput(attrs={'placeholder':'Apellido Materno','name':'m_apellido','id':'m_apellido','class':'input-class_name'}),
            "rut":forms.NumberInput(attrs={'placeholder':'11111111','name':'rut','id':'rut','class':'input-class_name'}),
            "digito_ver":forms.TextInput(attrs={'placeholder':'1','name':'dv','id':'dv','class':'input-class_name'}),
            "telefono":forms.NumberInput(attrs={'placeholder':'964782354','name':'telefono','id':'telefono','class':'input-class_name'}),
            "edad":forms.NumberInput(attrs={'placeholder':'18','name':'edad','id':'edad','class':'input-class_name'}),
            }

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

        widgets = {
            "titulo":forms.TextInput(attrs={'placeholder':'Título de la publicación','name':'titulo','id':'titulo','class':'input-class_name'}),
            "informacion":forms.Textarea(attrs={'placeholder':'¿Qué quieres comentar con la comunidad?','name':'informacion','id':'informacion','class':'input-class_name'}),
                }


class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ["vacunas","ac_fisica","comida_tiempo","tiene_sintomas","sintomas","tiene_enfermedad","enferme_ante","tiene_alergias","alergias","tiene_operaciones","operaciones"]



class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["comentario"]
        widgets = {
            "comentario":forms.TextInput(attrs={'placeholder':'Añadir un comentario'}),
                }
        
class AddMascotaForms(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = ["nombre_masc", "sexo", "anio_nac", "animal", "imagen"]

        labels = {
            'nombre_masc': ('Nombre de tu masctoa'),
            'sexo': ('M (macho) o H (hembra)'),
            'anio_nac': ('Año de nacimiento'),
        }

        widgets = {
            "nombre_masc":forms.TextInput(attrs={'placeholder':'Nombre','name':'nombre','id':'nombre','class':'input-class_name'}),
            "sexo":forms.TextInput(attrs={'placeholder':'H','name':'sexo','id':'sexo','class':'input-class_name'}),
            "anio_nac":forms.NumberInput(attrs={'placeholder':'2010','name':'anio_nac','id':'anio_nac','class':'input-class_name'}),
                }
