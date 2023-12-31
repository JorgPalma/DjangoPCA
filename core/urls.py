from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import home, nosotros, contacto, detallepost, eliminarPost, verPosts, eliminarMensaje, verMensaje, mensajes, eliminarMascota, editarMascota, addMascota, likepost ,blog, blogperro, bloggato, blogalimentacion, blogadopcion, addPost, registro, consulta, perfil, editarPerfil, noticias, bienvenido, enviado, dashboard, mapavet, eltest

urlpatterns=[
    path('', home, name="home"),
    path('nosotros/', nosotros, name="nosotros"),
    path('contacto/', contacto, name="contacto"),
    path('post/<id>', detallepost, name="detallepost"),
    path('blog/', blog, name="blog"),
    path('blog/perros/', blogperro, name="blogperro"),
    path('blog/gatos/', bloggato, name="bloggato"),
    path('blog/alimentacion/', blogalimentacion, name="blogalimentacion"),
    path('blog/adopcion/', blogadopcion, name="blogadopcion"),
    path('registro/', registro, name="registro"),
    path('consulta/', consulta, name="consulta"),
    path('perfil/<str:username>/', login_required (perfil), name="perfil"),
    path('editarPerfil/<str:dinamico>/', login_required (editarPerfil), name="editarPerfil"),
    path('noticias/', noticias, name="noticias"),
    path('bienvenido/<dinamico>/', bienvenido, name="bienvenido"),
    path('addPost/', addPost, name="addPost"),
    path('dashboard/', dashboard, name="dashboard"),
    path('enviado/', enviado, name="enviado"),
    path('likepost/<id>', likepost, name="likepost"),
    path('addMascota/', addMascota, name="addMascota"),
    path('mapavet/', mapavet, name="mapavet"),
    path('eltest/', eltest, name="eltest"),
    path('editarMascota/<id>', editarMascota, name="editarMascota"),
    path('eliminarMascota/<id>', eliminarMascota, name="eliminarMascota"),
    path('mensajes/', mensajes, name="mensajes"),
    path('verMensaje/<id>', verMensaje, name="verMensaje"),
    path('eliminarMensaje/<id>', eliminarMensaje, name="eliminarMensaje"),
    path('verPosts/', verPosts, name="verPosts"),
    path('eliminarPost/<id>', eliminarPost, name="eliminarPost"),
]
