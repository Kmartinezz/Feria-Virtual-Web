from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from Feria_App.forms import FormularioCliente

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from Feria_App.forms import RegistrarForm
from Feria_App.models import Productos, Transporte, ProductosVenta


# Create your views here.
def index (request):
    return render(request, 'index.html')

class FormularioClienteView(HttpRequest):

    def index(request):
        cliente = FormularioCliente()
        return render(request,"Cliente/ClienteIndex.html",{"form":cliente})
    
    def procesar_formulario(request):
        cliente = FormularioCliente(request.POST)
        if cliente.is_valid():
            cliente.save()
            cliente = FormularioCliente()
        return render(request, "Cliente/ClienteIndex.html", {"form":cliente, "mensaje": 'ok'})

def Registrar(request):
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = RegistrarForm()
    return render(request, 'registrar.html', {'form': form})

""" def SolicitarProducto(request):
    return render(request, 'Productor/SolicitarProducto.html') """

def RegistrarProducto(request):
    return render(request, 'Productor/RegistrarProducto.html')
    
def ListarProducto(request):
    productos = ProductosVenta.objects.all()
    return render(request, "Productor/ListarProductos.html", {"productos": productos})

def ListarTransporte(request):
    transportes = Transporte.objects.all()
    return render(request, "Transportista/ListarTransporte.html", {"transportes": transportes})

def SolicitarProducto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre_producto']
        solicitud = request.POST['solicitud']
        cierre_oferta = request.POST['fecha_cierre']
        comuna = request.POST['comuna']
        correo = request.POST['email']
        ProductosVenta(nombre = nombre, solicitud = solicitud, cierre_oferta = cierre_oferta, comuna = comuna, correo = correo).save()
        return redirect('listarProducto')
        #return render(request, 'Productor/SolicitarProducto.html')
    else:
        return render(request, 'Productor/SolicitarProducto.html')
