from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Persona(models.Model):
    nombre_usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user')
    rut = models.IntegerField()
    digito_ver = models.CharField(max_length=1)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30)
    apellido_pat = models.CharField(max_length=30)
    apellido_mate = models.CharField(max_length=30)
    telefono = models.IntegerField()
    edad = models.IntegerField()

    def __str__(self):
        return self.primer_nombre

    
class Blog(models.Model):
    nombre_usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_post')
    titulo = models.CharField(max_length=30)
    informacion = models.CharField(max_length=800)
    categoria = models.CharField(max_length=30)
    timestamp = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to="fotos", null=True)

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    nombre_usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_comentario')
    timestamp = models.DateTimeField(default=timezone.now)
    comentario = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nombre_usuario
    
class Mascota(models.Model):
    nombre_usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_mascota')
    nombre_masc = models.CharField(max_length=30)
    especie = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    edad = models.IntegerField()
    tamanio = models.IntegerField()
    peso = models.IntegerField()
    genero = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre_masc
    
class Formulario(models.Model):
    nombre_usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_formulario')
    vacunas = models.IntegerField()
    ac_fisica = models.CharField(max_length=1)
    comida_tiempo = models.IntegerField()
    tiene_sintomas = models.CharField(max_length=1)
    sintomas = models.CharField(max_length=20)
    tiene_enfermedad = models.CharField(max_length=1)
    enferme_ante = models.CharField(max_length=20)
    tiene_alergias = models.CharField(max_length=1)
    alergias = models.CharField(max_length=15)
    tiene_operaciones = models.CharField(max_length=1)
    operaciones = models.CharField(max_length=2)

    def __str__(self):
        return self.nombre_usuario

class Contacto(models.Model):
    nombre_contacto = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=500)

    def __str__(self):
        return self.asunto