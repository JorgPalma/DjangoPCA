from django.shortcuts import redirect, render, get_object_or_404
from .forms import RegistroForm
from django.contrib.auth import authenticate, login
from .models import User, Persona, Blog
from .forms import EditarPefil, ContactoForm, AddPostForms
import random
from django.shortcuts import render
import plotly.graph_objs as go
import csv



def home(request):
    return render(request, 'core/home.html')



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
            data["mensaje"] = "contacto guardado"
        else: 
            data["form"] = formulario

    return render(request, 'core/contacto.html', data)

def blog(request):

    blog = Blog.objects.all()

    data = {
        'blog': blog
    }


    return render(request, 'core/blog.html', data)

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
        validacion = True

    data = {
        'user': user,
        'persona': persona,
        'validacion': validacion
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
            return redirect('perfil', username=persona.dinamico,)
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
            post.id = usuario.id
            post.save()
            formulario.save()
            return redirect('blog')
        else:
            data["form"] = formulario
    

def dashboard(request):
    # Datos para el gráfico
    x_data = [1, 2, 3, 4, 5]
    y_data = [10, 11, 12, 13, 14]

    # Crear el gráfico usando Plotly
    trace = go.Scatter(x=x_data, y=y_data, mode='markers+lines')
    data = [trace]
    layout = go.Layout(title='Mi Gráfico Plotly', xaxis=dict(title='Eje X'), yaxis=dict(title='Eje Y'))
    plot_div = go.Figure(data=data, layout=layout).to_html(full_html=False)

    # Pasar el gráfico a la plantilla 'dashboard.html'
    return render(request, 'core/dashboard.html', {'plot_div': plot_div})