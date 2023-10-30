from django.urls import path
from .views import home, nosotros, contacto, blog, formulario, registro, consulta, perfil, editarPerfil, noticias

urlpatterns=[
    path('', home, name="home"),
    path('nosotros/', nosotros, name="nosotros"),
    path('contacto/', contacto, name="contacto"),
    path('blog/', blog, name="blog"),
    path('formulario/', formulario, name="formulario"),
    path('registro/', registro, name="registro"),
    path('consulta/', consulta, name="consulta"),
    path('perfil/', perfil, name="perfil"),
    path('editarPerfil/<id>/', editarPerfil, name="editarPerfil"),
    path('noticias/', noticias, name="noticias")
]
