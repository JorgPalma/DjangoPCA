from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Persona(models.Model):
    nombre_usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user')
    rut = models.IntegerField(default=12345678)
    digito_ver = models.CharField(max_length=1, default=1)
    primer_nombre = models.CharField(max_length=30, default="-")
    segundo_nombre = models.CharField(max_length=30, default=" ", blank=True)
    apellido_pat = models.CharField(max_length=30, default="-")
    apellido_mate = models.CharField(max_length=30, default=" ", blank=True)
    telefono = models.IntegerField(default=123456789)
    edad = models.IntegerField(default=18)
    imagen = models.ImageField(upload_to="perfil", null=True, default='perfil/default.png')
    dinamico = models.CharField(default="", blank=True, max_length=100)

    def __str__(self):
        return f'Perfil de: {self.nombre_usuario}'

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=20, default="Perro")

    def __str__(self):
        return self.nombre_categoria
    
class Blog(models.Model):
    nombre_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')
    titulo = models.CharField(max_length=30)
    informacion = models.CharField(max_length=800)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_post')  
    timestamp = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    is_like = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to="fotos", null=True)

    def __str__(self):
        return f'Post { self.id } de: {self.nombre_usuario}'
    
class Comentario(models.Model):
    nombre_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comentario')
    timestamp = models.DateTimeField(default=timezone.now)
    comentario = models.CharField(max_length=150)
    post = models.ForeignKey(Blog, null=True, on_delete=models.CASCADE, related_name="comentario_post")
    
    def __str__(self):
        return f'Comentrio { self.id } de: {self.nombre_usuario}'
    
class Animal(models.Model):
    nombre_animal = models.CharField(max_length=20, default="Perro")

    def __str__(self):
        return self.nombre_animal
    
class Raza(models.Model):
    nombre_raza = models.CharField(max_length=20, default="Chihuahua")

    def __str__(self):
        return self.nombre_raza
    
class Mascota(models.Model):
    nombre_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_mascota')
    nombre_masc = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1)
    anio_nac = models.IntegerField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='animal_mascota')
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE, related_name='raza_mascota')
    imagen = models.ImageField(upload_to="fotos", null=True)

    def __str__(self):
        return self.nombre_masc
    
class Alergia(models.Model):
    tipo_alergia = models.CharField(max_length=15, default="No")

    def __str__(self):
        return self.tipo_alergia
    
class Formulario(models.Model):
    nombre_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_formulario')
    num_vacunas = models.IntegerField()
    act_fisica = models.CharField(max_length=1)
    comida_tiempo = models.IntegerField()
    sintomas = models.CharField(max_length=30)
    antec_enfermedades = models.CharField(max_length=20)
    operaciones = models.IntegerField()
    peso = models.IntegerField()
    tamanio = models.IntegerField()
    edad = models.IntegerField()
    alergia = models.ForeignKey(Alergia, on_delete=models.CASCADE, related_name='alergia')
    

    def __str__(self):
        return self.nombre_usuario

class Contacto(models.Model):
    nombre_contacto = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=500)

    def __str__(self):
        return self.asunto