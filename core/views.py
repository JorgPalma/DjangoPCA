from django.shortcuts import redirect, render, get_object_or_404
from .forms import RegistroForm
from django.contrib.auth import authenticate, login
from .models import User, Persona, Blog, Comentario, Mascota, Contacto
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
    blog = Blog.objects.filter(categoria = "3").order_by('-timestamp')
    
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
    blog = Blog.objects.filter(categoria = "4").order_by('-timestamp')
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
    colors= ['#54d2d2', '#ffcb00', '#f8aa4b', '#ff6150', '#e2e2e2','#465B75', '#FCD949', '#FCAC49', '#ffd49e','#FC5B49', '#49FCFC', '#FC5B49']
    mascotamodel= Mascota.objects.all()
    mascotasexoH = Mascota.objects.filter(sexo = "H").count()
    mascotasexoM = Mascota.objects.filter(sexo = "M").count()

    # Listas para almacenar los datos del archivo CSV
    vacunas = []
    
    comida_tiempo = []
    
    labels = ['H','M']
    sexo = []

    contador_H = 0
    contador_M = 0

    
    for mas in mascotamodel:
        if mas.sexo == 'H':
            contador_H += 1
        elif mas.sexo == 'M':
            contador_M += 1
        
    sexo.append(contador_H)
    sexo.append(contador_M)


    razap = []
    razag = []
    print(mascotamodel)
    for m in mascotamodel:
        print(m)
        if m.raza.animal.nombre_animal == "Perro":
            razap.append(m.raza)
        elif m.raza.animal.nombre_animal == "Gato":
            razag.append(m.raza)

    mestizo=0
    poodle=0
    pastorale=0
    yorkshire=0
    foxterrier=0
    beagle=0
    labradorre=0
    goldenre=0
    pug=0
    bulldog=0
    quiltro=0
    otrop=0
    lblrazaperro= ['Mestizo', 'Poodle o caniche', 'Pastor alemán', 'Yorkshire', 'Fox terrier', 'Beagle', 'Labrador retriever', 'Golden retriever', 'Pug', 'Bulldog', 'Quiltro', 'Otras']

    for ra in razap:
        print(ra)
        if str(ra) == 'Mestizo':
            mestizo += 1
        elif str(ra) == 'Poodle o caniche':
            poodle += 1
        elif str(ra) == 'Pastor alemán':
            pastorale += 1
        elif str(ra) == 'Yorkshire':
            yorkshire += 1
        elif str(ra) == 'Fox terrier':
            foxterrier += 1
        elif str(ra) == 'Beagle':
            beagle += 1
        elif str(ra) == 'Labrador retriever':
            labradorre += 1
        elif str(ra) == 'Golden retriever':
            goldenre += 1
        elif str(ra) == 'Pug':
            pug += 1
        elif str(ra) == 'Bulldog':
            bulldog += 1
        elif str(ra) == 'Quiltro':
            quiltro += 1
        else:
            otrop += 1
    


    trace9= go.Bar(x=lblrazaperro, y=[mestizo, poodle, pastorale, yorkshire, foxterrier, beagle, labradorre, goldenre, pug, bulldog, quiltro, otrop], marker_color='#54d2d2')
    data9= [trace9]
    layout9 = go.Layout(title='Distribución de razas caninas registrada (PetCareAnalytics)', margin=dict(l=0, r=0, b=0, t=30))
    fig9 = go.Figure(data= data9, layout= layout9)
    
    plot_div9 = fig9.to_html(full_html=False)

    siames=0
    maine=0
    esfinge=0
    bengali=0
    expelocorto=0
    british=0
    otrog=0
    lblrazagato=['Siamés', 'Maine Coon', 'Esfinge', 'Bengalí', 'Exótico Pelo Corto', 'British Shorthair', 'Otras']

    for ra in razag:
        print(ra)
        if str(ra) == 'Siamés':
            siames += 1
        elif str(ra) == 'Maine Coon':
            maine += 1
        elif str(ra) == 'Esfinge':
            esfinge += 1
        elif str(ra) == 'Bengalí':
            bengali += 1
        elif str(ra) == 'Exótico Pelo Corto':
            expelocorto += 1
        elif str(ra) == 'British Shorthair':
            british += 1
        else:
            otrog += 1

    trace10 = go.Bar(x=lblrazagato, y=[siames, maine, esfinge, bengali, expelocorto, british, otrog], marker_color='#ffcb00')
    data10 = [trace10]
    layout10 = go.Layout(title='Distribución de razas felinas registrada (PetCareAnalytics)', margin=dict(l=0, r=0, b=0, t=30))  # Ajusta los márgenes según tus preferencias
    fig10 = go.Figure(data=data10, layout=layout10)
    
    plot_div10 = fig10.to_html(full_html=False)

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
    layout = go.Layout(title='Distribución de sexo por Mascota registrada (PetCareAnalytics)', margin=dict(l=0, r=0, b=0, t=30))  # Ajusta los márgenes según tus preferencias
    fig = go.Figure(data=data, layout=layout)
    fig.update_traces(marker=dict(colors=colors))
    plot_div = fig.to_html(full_html=False)

    
    raza_perro = ['Mestizo', 'Poodle', 'Pastor Aleman', 'Yorkshire', 'Dachshund', 'Fox Terrier', 'Beagle', 'Labrador Retriever', 'Golden Retriever', 'Boxer']
    trace2 = go.Bar(x=raza_perro, y=[736648, 174868, 62291, 56997, 37195, 33979, 23178, 21965, 19947, 18573], marker_color='#54d2d2')
    data2 = [trace2]

# Cambia el tamaño del título ajustando la propiedad 'size' dentro de 'font'
    layout2 = go.Layout(title=dict(text='Razas Populares de Perros (Chile 2022)', font=dict(size=18)), margin=dict(l=0, r=0, b=0, t=30))

    fig2 = go.Figure(data=data2, layout=layout2)
    plot_div2 = fig2.to_html(full_html=False)

    raza_gato=['Domestico P. Corto', 'Domestico P. Largo', 'Americano P. Corto', 'Siames', 'Británico P. Corto', 'Persa', 'Europeo', 'Angora Turco', 'Británico P. Largo', 'Curl Americano']
    trace7= go.Bar(x=raza_gato, y=[297316, 98800, 6920, 3175, 2311, 2283, 1893, 1622, 1165, 671], marker_color='#ffcb00')
    data7= [trace7]
    layout7 = go.Layout(title='Razas Populares de Gatos (Chile 2022)', margin=dict(l=0, r=0, b=0, t=30))
    fig7 = go.Figure(data= data7, layout= layout7)
    plot_div7 = fig7.to_html(full_html=False)

    regiones=['Arica y Parinacota', 'Tarapaca', 'Antofagasta', 'Atacama', 'Coquimbo', 'Valparaiso',
              'Metropolitana de Santiago', 'Libertador General Bernardo Ohiggins', 'Maule', 'Ñuble',
              'Biobio', 'La Araucania', 'Los Rios', 'Los Lagos', 'Aysen del general Carlos Ibañez del Campo',
              'Magallanes y de la Antartica chilena']
    fig3 = go.Figure(data=[
        go.Bar(name='Gatos', x=regiones, y=[3188, 6761, 13339, 9860, 13534, 48168, 147606, 23163, 23857, 10701, 32691, 28621, 16272, 31674, 7887, 5198], marker_color='#54d2d2'),
        go.Bar(name='Perros', x=regiones, y=[10659, 31500, 46493, 33017, 49414, 164790, 508302, 106686, 112212, 44433, 113607, 77315, 37735, 75067, 15092, 13250], marker_color='#ff6150')
    ])
    # Change the bar mode
    fig3.update_layout(barmode='group')
    plot_div3 = fig3.to_html(full_html=False)

    animals=['Perro', 'Gato', 'Ambas especies', 'Otras especies']
    
    trace3 = go.Pie(labels=animals, values=[4062, 1956, 1300, 176], hole=.3)
    data3 = [trace3]
    layout3 = go.Layout(title='Viviendas con Mascotas (Chile 2022)', margin=dict(l=0, r=0, b=0, t=30))  # Ajusta los márgenes según tus preferencias
    fig4 = go.Figure(data=data3, layout=layout3)
    fig4.update_traces(marker=dict(colors=colors))
    plot_div4 = fig4.to_html(full_html=False)



    nomb_perro=['Luna', 'Princesa', 'Canela', 'Pelusa', 'Toby', 'Perla', 'Jack', 'Rocky', 'Lucas', 'Max']
    trace5= go.Bar(x=nomb_perro, y=[30079, 14709, 12971, 12146, 10856, 8908, 8538, 8482, 7897, 7850], marker_color='#54d2d2')
    data5= [trace5]
    layout5 = go.Layout(title='Nombres Populares de Perros (Chile 2022)', margin=dict(l=0, r=0, b=0, t=30))
    fig5 = go.Figure(data= data5, layout= layout5)
    plot_div5 = fig5.to_html(full_html=False)

    nomb_gato=['Luna', 'Pelusa', 'Tom', 'Princesa', 'Minina', 'Kitty', 'Mia', 'Niña', 'Michi', 'Negra']
    trace6= go.Bar(x=nomb_gato, y=[8690, 5108, 3217, 2813, 2450, 2213, 2114, 2094, 1940, 1809], marker_color='#ffcb00')
    data6= [trace6]
    layout6 = go.Layout(title='Nombres Populares de Gatos (Chile 2022)', margin=dict(l=0, r=0, b=0, t=30))
    fig6 = go.Figure(data= data6, layout= layout6)
    plot_div6 = fig6.to_html(full_html=False)

    animales=['Gatos', 'Perros', 'Aves Ornamentales', 'Pequeños mamiferos', 'Peces ornamentales', 'Reptiles']
    trace8= go.Bar(x=animales, y=[127161000, 104348000, 53091000, 29317000, 21903000, 11632000], marker_color='#54d2d2')
    data8= [trace8]
    layout8 = go.Layout(title='Animales populares en Europa (2022)', margin=dict(l=0, r=0, b=0, t=30))
    fig8 = go.Figure(data= data8, layout= layout8)
    plot_div8 = fig8.to_html(full_html=False)


    # Pasar el gráfico a la plantilla 'dashboard.html'
    return render(request, 'core/dashboard.html', {'hembra': mascotasexoH,
        'macho': mascotasexoM, 'plot_div': plot_div, 'plot_div2': plot_div2, 'plot_div3': plot_div3, 'plot_div4': plot_div4, 'plot_div5': plot_div5, 'plot_div6': plot_div6, 'plot_div7': plot_div7, 'plot_div8': plot_div8, 'plot_div9': plot_div9, 'plot_div10': plot_div10})
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


def mapavet(request):
    post = Blog.objects.last()

    data = {
        'post': post
    }

    return render(request, 'core/mapavet.html', data)

#Codigo toferxo geolocalizacion
# mi_aplicacion/views.py

# core/views.py

from django.shortcuts import render
from .utils import get_user_location, get_nearby_veterinaries

def veterinaries_nearby(request):
    lat, lon = get_user_location(request)
    nearby_veterinaries = get_nearby_veterinaries(lat, lon)

    print(nearby_veterinaries)  # Agrega esta línea para imprimir los datos en la consola

    return render(request, 'core/mapavet.html', {'nearby_veterinaries': nearby_veterinaries})

def eltest(request):
    post = Blog.objects.last()

    data = {
        'post': post
    }

    return render(request, 'core/eltest.html', data)