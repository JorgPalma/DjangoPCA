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


    
class Blog(models.Model):
    nombre_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')
    titulo = models.CharField(max_length=30)
    informacion = models.CharField(max_length=800)
    class Categoria_Choices(models.TextChoices):
        PER = "1", "Perro"
        GAT = "2", "Gato"
        ALI = "3", "Alimentación"
        ADO = "4", "Adopción"
    categoria = models.CharField(max_length=2,
                                choices=Categoria_Choices.choices,
                                default=Categoria_Choices.PER)
    timestamp = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    like = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to="fotos", null=True)

    def __str__(self):
        return f'Post { self.id } de: {self.nombre_usuario}'
    
class Comentario(models.Model):
    nombre_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comentario')
    timestamp = models.DateTimeField(default=timezone.now)
    comentario = models.CharField(max_length=150)
    likes = models.IntegerField(default=0)
    like = models.BooleanField(default=False)
    post = models.ForeignKey(Blog, null=True, on_delete=models.CASCADE, related_name="comentario_post")
    
    def __str__(self):
        return f'Comentrio { self.id } de: {self.nombre_usuario}'

    
class Mascota(models.Model):
    nombre_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_mascota')
    nombre_masc = models.CharField(max_length=30)
    class Especie_Choices(models.TextChoices):
        PER = "1", "Perro"
        GAT = "2", "Gato"
    especie = models.CharField(max_length=2,
                            choices=Especie_Choices.choices,
                            default=Especie_Choices.PER)
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