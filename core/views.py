from django.shortcuts import redirect, render, get_object_or_404
from .forms import RegistroForm
from django.contrib.auth import authenticate, login
from .models import User, Persona, Blog, Comentario, Mascota, Formulario, Contacto
from .forms import EditarPefil, ContactoForm, AddPostForms, ComentarioForm, AddMascotaForms
import random
from django.shortcuts import render
import plotly.graph_objs as go
import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q


def home(request):
    post = Blog.objects.last()

    data = {
        'post': post
    }

    return render(request, 'core/home.html', data)



def nosotros(request):
    return render(request, 'core/nosotros.html')

def contacto(request):

    data = {
        'form': ContactoForm() 
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('enviado')
        else: 
            data["form"] = formulario

    return render(request, 'core/contacto.html', data)

def blog(request):

    search_query = request.GET.get('search', '')

    if search_query:
        blog = Blog.objects.filter(Q(informacion__icontains=search_query) | Q(titulo__icontains=search_query)).order_by('-timestamp')
    else:
        blog = Blog.objects.all().order_by('-timestamp')

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(blog, 10)
        blog = paginator.page(page)
    except:
        raise Http404

    data = {
        'blog': blog,
        'paginator': paginator
    }
    return render(request, 'core/blog.html', data)

def blogperro(request):
    blog = Blog.objects.filter(categoria = "1").order_by('-timestamp')

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(blog, 10)
        blog = paginator.page(page)
    except:
        raise Http404

    data = {
        'blog': blog,
        'paginator': paginator
    }
    return render(request, 'core/blogperro.html', data)

def bloggato(request):
    blog = Blog.objects.filter(categoria = "2").order_by('-timestamp')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(blog, 10)
        blog = paginator.page(page)
    except:
        raise Http404

    data = {
        'blog': blog,
        'paginator': paginator
    }
    return render(request, 'core/bloggato.html', data)

def blogalimentacion(request):
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(blog, 10)
        blog = paginator.page(page)
    except:
        raise Http404

    data = {
        'blog': blog,
        'paginator': paginator
    }
    return render(request, 'core/blogalimentacion.html', data)

def blogadopcion(request):
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(blog, 10)
        blog = paginator.page(page)
    except:
        raise Http404

    data = {
        'blog': blog,
        'paginator': paginator
    }
    return render(request, 'core/blogadopcion.html', data)

def formulario(request):
    return render(request, 'core/formulario.html')

def registro(request):

    dinamico = ''

    for i in range (1,100):
        rando = chr(random.randint(48,122))
        dinamico = dinamico + rando
    
    print(dinamico)

    data = {
        'form': RegistroForm
    }

    if request.method == "POST":
        formulario = RegistroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login (request, user)
            usuario = get_object_or_404(User, pk=request.user.pk)
            persona = Persona()
            persona.nombre_usuario = usuario
            persona.dinamico = dinamico
            persona.save()
            return redirect('bienvenido', dinamico=persona.dinamico,)
            

    return render(request, 'registration/registro.html', data)

def consulta(request):
    return render(request, 'core/consulta.html')

def perfil(request, username = None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        persona = Persona.objects.get(nombre_usuario = user)
        validacion = False
    else:
        user = current_user
        persona = Persona.objects.get(nombre_usuario = user)
        mascota = Mascota.objects.filter(nombre_usuario = user)
        validacion = True
    

    data = {
        'user': user,
        'persona': persona,
        'validacion': validacion,
        'mascota': mascota
    }

    return render(request, 'core/perfil.html', data)

def editarPerfil(request, dinamico):

    persona = get_object_or_404(Persona, dinamico = dinamico)
    
    data = {
        'form': EditarPefil(instance = persona),
        'persona': persona,
    }

    if request.method == 'POST':
        formulario = EditarPefil(data=request.POST, files=request.FILES, instance=persona)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Bien, lo hiciste excelente!")
            return redirect('perfil', username=persona.nombre_usuario)
            
        else:
            data["form"] = formulario

    return render(request, 'core/editarperfil.html', data)

def noticias(request):
    return render(request, 'core/noticias.html')

def bienvenido(request, dinamico):
    persona = get_object_or_404(Persona, dinamico = dinamico)
    
    if dinamico != persona.dinamico:
        validacion = False
    else:
        validacion = True
        
    data = {
        'persona': persona,
        'validacion': validacion,
    }
    return render(request, 'core/bienvenido.html', data)

def handler404(request, exception):
    context = {}
    response = render(request, "core/404.html", context=context)
    response.status_code = 404
    return response


def handler500(request):
    context = {}
    response = render(request, "core/404.html", context=context)
    response.status_code = 500
    return response

def addPost(request):

    data = {
        'form': AddPostForms(),
    }

    if request.method == "POST":
        formulario = AddPostForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            usuario = get_object_or_404(User, pk=request.user.pk)
            post.nombre_usuario = usuario
            post.save()
            formulario.save()
            messages.success(request, "Post creado con exito!")
            return redirect('blog')
        else:
            data["form"] = formulario

    return render(request, 'core/addpost.html', data)
    


def convertir_a_entero(valor, valor_por_defecto=0):
    try:
        return int(valor)
    except (ValueError, TypeError):
        return valor_por_defecto

def dashboard(request):
    # Ruta al archivo CSV
    # csv_file_path = 'core/templates/CSV/csv.csv'

    # # Cargar datos geoespaciales de Chile desde el archivo GeoJSON
    # with open('core/templates/CSV/map.geojson') as geojson_file:
    #     geojson_data = geojson_file.read()

    # # Crear un gráfico de dispersión en el mapa de Chile con Plotly Go
    # fig8 = go.Figure(go.Scattergeo(
    #     geojson=geojson_data,
    #     featureidkey= 'properties.Region',
    #     locations=["Región de Arica y Parinacota", "Región de Tarapacá", "Región de Antofagasta", "Región de Magallanes y Antártica Chilena", "Región de Aysén del Gral.Ibañez del Campo", "Región de Atacama", "Región de Coquimbo", "Región de Valparaíso", "Región Metropolitana de Santiago", "Región de Los Lagos", "Región de Los Ríos", "Región de La Araucanía", "Región del Bío-Bío", "Región de Ñuble", "Región del Maule", "Región del Libertador Bernardo O'Higgins"],
    #     mode='markers',
    #     marker=dict(
    #         size=10,
    #         color='red',
    #         opacity=0.8,
    #     ),
    #     text=[],
    # ))

    
    
    # fig8.update_geos(fitbounds="locations", visible=False, showcountries=True, showcoastlines=True)

    # # Convierte el gráfico a HTML
    # graph_html = fig8.to_html(full_html=False)



    formulariomodel= Formulario.objects.all()
    mascotamodel= Mascota.objects.all()
    # Listas para almacenar los datos del archivo CSV
    vacunas = []
    
    comida_tiempo = []
    
    labels = ['H','M']
    sexo = []
    
    lblanimal = ['Perro' , 'Gato']
    contador= [95, 28]

    contador_H = 0
    contador_M = 0

    for c in formulariomodel:
        comida_tiempo.append(convertir_a_entero(c.comida_tiempo))
        vacunas.append(c.id)
    
    for mas in mascotamodel:
        if mas.sexo == 'H':
            contador_H += 1
        elif mas.sexo == 'M':
            contador_M += 1
        
    sexo.append(contador_H)
    sexo.append(contador_M)
    # Leer datos desde el archivo CSV y manejar valores no numéricos
    # with open(csv_file_path, 'r') as csvfile:
    #     csvreader = csv.DictReader(csvfile)
    #     for row in csvreader:
    #         vacunas.append(convertir_a_entero(row['vacunas']))
    #         ac_fisica.append(row['ac_fisica'])
    #         comida_tiempo.append(convertir_a_entero(row['comida_tiempo'], valor_por_defecto=0))
    #         tiene_sintomas.append(row['tiene_sintomas'])
    #         sintomas.append(row['sintomas'])
    #         tiene_enfermedad.append(row['tiene_enfermedad'])
    #         enferme_ante.append(row['enferme_ante'])
    #         tiene_alergias.append(row['tiene_alergias'])
    #         alergias.append(row['alergias'])
    #         tiene_operaciones.append(row['tiene_operaciones'])
    #         operaciones.append(row['operaciones'])

 # Crear el pie chart con Plotly
    trace = go.Pie(labels=labels, values=sexo, hole=.3)
    data = [trace]
    layout = go.Layout(title='Distribución de sexo por Mascota registrada', margin=dict(l=0, r=0, b=0, t=30))  # Ajusta los márgenes según tus preferencias
    fig = go.Figure(data=data, layout=layout)
    plot_div = fig.to_html(full_html=False)


    trace2 = go.Pie(labels=lblanimal, values=contador, hole=.3, textinfo='label+percent')
    data2 = [trace2]
    layout2 = go.Layout(title='Distribución', margin=dict(l=0, r=0, b=0, t=30))  # Ajusta los márgenes según tus preferencias
    fig2 = go.Figure(data=data2, layout=layout2)
    plot_div2 = fig2.to_html(full_html=False)


    animals=['giraffes', 'orangutans', 'monkeys']
    fig3 = go.Figure(data=[
        go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
        go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
    ])
    # Change the bar mode
    fig3.update_layout(barmode='group')
    plot_div3 = fig3.to_html(full_html=False)

    animals=['Perro', 'Gato', 'Ambas especies', 'Otras especies']
    trace3= go.Bar(x=animals, y=[4062, 1956, 1300, 176])
    data3= [trace3]
    layout3 = go.Layout(title='Viviendas con Mascotas', margin=dict(l=0, r=0, b=0, t=30))
    fig4 = go.Figure(data= data3, layout= layout3)
    plot_div4 = fig4.to_html(full_html=False)


    # Pasar el gráfico a la plantilla 'dashboard.html'
    return render(request, 'core/dashboard.html', {'plot_div': plot_div, 'plot_div2': plot_div2, 'plot_div3': plot_div3, 'plot_div4': plot_div4})
    fig.write_html('pie_chart.html')


def enviado (request):
    return render(request, 'core/enviado.html')

def detallepost(request, id):
    post = get_object_or_404(Blog, id = id)
    usuario = get_object_or_404(Persona, nombre_usuario = post.nombre_usuario)
    comentario = Comentario.objects.filter(post = post)

    data = {
        'comentario': comentario,
        'post': post,
        'usuario': usuario,
        'form': ComentarioForm(),
    }

    if request.method == "POST":
        formulario = ComentarioForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            usuario = get_object_or_404(User, pk=request.user.pk)
            comentario.nombre_usuario = usuario
            comentario.post = post
            post.save()
            formulario.save()
            return redirect('detallepost', post.id)
        else:
            data["form"] = formulario

    return render(request, 'core/detallepost.html', data)


def likepost (request, id):
    post = get_object_or_404(Blog, id = id)

    if post.is_like == False:
        current_likes = post.likes
        post.likes = current_likes + 1
        post.is_like = True
        post.save()
    elif post.is_like == True:
        current_likes = post.likes
        post.likes = current_likes - 1
        post.is_like = False
        post.save()

    return detallepost(request, id)

def addMascota(request):

    data = {
        'form': AddMascotaForms(),
    }

    if request.method == "POST":
        formulario = AddMascotaForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            usuario = get_object_or_404(User, pk=request.user.pk)
            post.nombre_usuario = usuario
            post.save()
            formulario.save()
            messages.success(request, "¡Mascota agregada con éxito!")
            return redirect('home')
        else:
            data["form"] = formulario

    return render(request, 'core/addMascota.html', data)


def test(request):
    post = Blog.objects.last()

    data = {
        'post': post
    }

    return render(request, 'core/test.html', data)

def editarMascota(request, id):

    mascota = get_object_or_404(Mascota, id = id)
    
    data = {
        'form': AddMascotaForms(instance = mascota),
        'mascota': mascota,
    }

    if request.method == 'POST':
        formulario = AddMascotaForms(data=request.POST, files=request.FILES, instance=mascota)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Los datos de tu mascota se han actualizado")
            return redirect('home')
            
        else:
            data["form"] = formulario

    return render(request, 'core/editarmascota.html', data)

def eliminarMascota(request, id):

    mascota = get_object_or_404(Mascota, id = id)
    mascota.delete()
    messages.success(request, "Realizado")

    return redirect(to="home")

@permission_required("core.view_contacto")
def mensajes(request):

    blog = Contacto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(blog, 10)
        blog = paginator.page(page)
    except:
        raise Http404

    data = {
        'blog': blog,
        'paginator': paginator
    }

    return render(request, 'core/mensajes.html', data)

@permission_required("core.change_contacto")
def verMensaje(request, id):
    mensaje = get_object_or_404(Contacto, id = id)

    data = {
        'mensaje': mensaje,
    }

    return render(request, 'core/verMensaje.html', data)

@permission_required("core.delete_contacto")
def eliminarMensaje(request, id):

    mensaje = get_object_or_404(Contacto, id = id)
    mensaje.delete()

    return redirect(to="mensajes")

@permission_required("core.view_blog")
def verPosts(request):
    blog = Blog.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(blog, 10)
        blog = paginator.page(page)
    except:
        raise Http404

    data = {
        'blog': blog,
        'paginator': paginator
    }

    return render(request, 'core/verPosts.html', data)

@permission_required("core.delete_blog")
def eliminarPost(request, id):

    blog = get_object_or_404(Blog, id = id)
    blog.delete()

    return redirect(to="verPosts")


def test(request):
    post = Blog.objects.last()

    data = {
        'post': post
    }

    return render(request, 'core/test.html', data)

#Codigo toferxo geolocalizacion
# mi_aplicacion/views.py

# core/views.py

from django.shortcuts import render
from .utils import get_user_location, get_nearby_veterinaries

def veterinaries_nearby(request):
    lat, lon = get_user_location(request)
    nearby_veterinaries = get_nearby_veterinaries(lat, lon)

    print(nearby_veterinaries)  # Agrega esta línea para imprimir los datos en la consola

    return render(request, 'core/test.html', {'nearby_veterinaries': nearby_veterinaries})
