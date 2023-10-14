from django.shortcuts import redirect, render
from .forms import RegistroForm
from django.contrib.auth import authenticate, login

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
            return redirect(to="home")
            

    return render(request, 'registration/registro.html', data)

def consulta(request):
    return render(request, 'core/consulta.html')