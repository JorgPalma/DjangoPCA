from django.shortcuts import redirect, render, get_object_or_404
from .forms import RegistroForm
from django.contrib.auth import authenticate, login
from .models import User, Persona
from .forms import EditarPefil

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def blog(request):
    return render(request, 'core/blog.html')

def formulario(request):
    return render(request, 'core/formulario.html')

def registro(request):

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
            persona.save()
            return redirect(to="home")
            

    return render(request, 'registration/registro.html', data)

def consulta(request):
    return render(request, 'core/consulta.html')

def perfil(request, username):

    user = get_object_or_404(User, username = username)
    persona = Persona.objects.get(nombre_usuario = user)


    data = {
        'user': user,
        'persona': persona,
        'comparacion1': persona.nombre_usuario,
        'comparacion2': user.username
    }

    return render(request, 'core/perfil.html', data)

def editarPerfil(request, id):

    persona = get_object_or_404(Persona, id = id)
    
    data = {
        'form': EditarPefil(instance = persona),
        'persona': persona
    }

    if request.method == 'POST':
        formulario = EditarPefil(data=request.POST, files=request.FILES, instance=persona)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="home")
        else:
            data["form"] = formulario

    return render(request, 'core/editarperfil.html', data)

def noticias(request):
    return render(request, 'core/noticias.html')