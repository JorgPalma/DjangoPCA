from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import home, nosotros, contacto, blog, formulario, registro, consulta, perfil, editarPerfil, noticias

urlpatterns=[
    path('', home, name="home"),
    path('nosotros/', nosotros, name="nosotros"),
    path('contacto/', contacto, name="contacto"),
    path('blog/', blog, name="blog"),
    path('formulario/', formulario, name="formulario"),
    path('registro/', registro, name="registro"),
    path('consulta/', consulta, name="consulta"),
    path('perfil/', login_required (perfil), name="perfil"),
    path('editarPerfil/<id>/', login_required (editarPerfil), name="editarPerfil"),
    path('noticias/', noticias, name="noticias")
]
