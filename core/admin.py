from django.contrib import admin
from .models import Persona, Blog, Comentario, Contacto, Mascota, Formulario

# Register your models here.

admin.site.register(Persona)
admin.site.register(Blog)
admin.site.register(Comentario)
admin.site.register(Contacto)
admin.site.register(Mascota)
admin.site.register(Formulario)