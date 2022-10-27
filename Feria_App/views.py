from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from Feria_App.forms import FormularioCliente, FormularioProductor

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from Feria_App.forms import RegistrarForm
from Feria_App.models import Productos, Transporte, productor, ProductosVenta


# Create your views here.
def index (request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')

def SolicitarProducto(request):
    return render(request, 'SolicitarProducto.html')

def RegistrarProducto(request):
    return render(request, 'RegistrarProducto.html')

class FormularioClienteView(HttpRequest):

    def index(request):
        cliente = FormularioCliente()
        return render(request,"ClienteIndex.html",{"form":cliente})
    
    def procesar_formulario(request):
        cliente = FormularioCliente(request.POST)
        if cliente.is_valid():
            cliente.save()
            cliente = FormularioCliente()
        return render(request, "ClienteIndex.html", {"form":cliente, "mensaje": 'ok'})


def listarProductos_venta(request):
    producto = Productos.objects.all()
    return render(request, 'productos_venta.html',{'producto':producto})


class FormularioProductorView(HttpRequest):
    def index(request):
        productor = FormularioProductor()
        return render(request,"productor.html",{"form":productor})
    
    def procesar_formulario(request):
        productor = FormularioProductor(request.POST)
        if productor.is_valid():
            productor.save()
            productor = FormularioProductor()
        return render(request, "productor.html", {"form":productor, "mensaje": 'ok'})
    
    def listarProductos(request):
        producto = productor.objects.all()
        return render(request, 'Productos.html',{'producto':producto})

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
    
def listar_productos(request):
    productos = ProductosVenta.objects.all()
    return render(request, "ListarProductos.html", {"productos": productos})

def listar_transporte(request):
    transportes = Transporte.objects.all()
    return render(request, "ListarTransporte.html", {"transportes": transportes})
