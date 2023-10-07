from django.urls import path
from .views import home, nosotros, contacto, blog, formulario, registro

urlpatterns=[
    path('', home, name="home"),
    path('nosotros/', nosotros, name="nosotros"),
    path('contacto/', contacto, name="contacto"),
    path('blog/', blog, name="blog"),
    path('formulario/', formulario, name="formulario"),
    path('registro/', registro, name="registro")
]