from django.shortcuts import redirect, render, get_object_or_404
from .forms import RegistroForm
from django.contrib.auth import authenticate, login
from .models import User, Persona, Blog, Comentario, Mascota
from .forms import EditarPefil, ContactoForm, AddPostForms, ComentarioForm, AddMascotaForms
import random
from django.shortcuts import render
import plotly.graph_objs as go
import csv
from django.contrib import messages


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
    blog = Blog.objects.all().order_by('-timestamp')
    data = {
        'blog': blog
    }
    return render(request, 'core/blog.html', data)

def blogperro(request):
    blog = Blog.objects.filter(categoria = "1").order_by('-timestamp')
    data = {
        'blog': blog
    }
    return render(request, 'core/blogperro.html', data)

def bloggato(request):
    blog = Blog.objects.filter(categoria = "2").order_by('-timestamp')
    data = {
        'blog': blog
    }
    return render(request, 'core/bloggato.html', data)

def blogalimentacion(request):
    blog = Blog.objects.filter(categoria = "3").order_by('-timestamp')
    data = {
        'blog': blog
    }
    return render(request, 'core/blogalimentacion.html', data)

def blogadopcion(request):
    blog = Blog.objects.filter(categoria = "4").order_by('-timestamp')
    data = {
        'blog': blog
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
    
import csv
import plotly.graph_objs as go
from django.shortcuts import render

def convertir_a_entero(valor, valor_por_defecto=0):
    try:
        return int(valor)
    except (ValueError, TypeError):
        return valor_por_defecto

def dashboard(request):
    # Ruta al archivo CSV
    csv_file_path = 'core/templates/CSV/csv.csv'

    # Listas para almacenar los datos del archivo CSV
    vacunas = []
    ac_fisica = []
    comida_tiempo = []
    tiene_sintomas = []
    sintomas = []
    tiene_enfermedad = []
    enferme_ante = []
    tiene_alergias = []
    alergias = []
    tiene_operaciones = []
    operaciones = []

    # Leer datos desde el archivo CSV y manejar valores no numéricos
    with open(csv_file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            vacunas.append(convertir_a_entero(row['vacunas']))
            ac_fisica.append(row['ac_fisica'])
            comida_tiempo.append(convertir_a_entero(row['comida_tiempo'], valor_por_defecto=0))
            tiene_sintomas.append(row['tiene_sintomas'])
            sintomas.append(row['sintomas'])
            tiene_enfermedad.append(row['tiene_enfermedad'])
            enferme_ante.append(row['enferme_ante'])
            tiene_alergias.append(row['tiene_alergias'])
            alergias.append(row['alergias'])
            tiene_operaciones.append(row['tiene_operaciones'])
            operaciones.append(row['operaciones'])

    # Crear el gráfico usando Plotly
    trace = go.Scatter(x=comida_tiempo, y=vacunas, mode='markers+lines')
    data = [trace]
    layout = go.Layout(title='Mi Gráfico Plotly', xaxis=dict(title='Comida a Tiempo'), yaxis=dict(title='Vacunas'))
    plot_div = go.Figure(data=data, layout=layout).to_html(full_html=False)

    # Pasar el gráfico a la plantilla 'dashboard.html'
    return render(request, 'core/dashboard.html', {'plot_div': plot_div})

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