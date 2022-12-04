from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from Feria_App.forms import FormularioCliente
from django.template.loader import get_template
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from Feria_App.forms import RegistrarForm
from Feria_App.models import Productos, Transporte, ProductosVenta, ProductosRegistro


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

    
def ListarProducto(request):
    productos = ProductosVenta.objects.all()
    pregistros = ProductosRegistro.objects.all()
    return render(request, "Productor/ListarProductos.html", {"productos": productos})


def ListarTransporte(request):
    transportes = Transporte.objects.all()
    return render(request, "Transportista/ListarTransporte.html", {"transportes": transportes})
    

def ListarProductoRegistro(request):
    pregistros = ProductosRegistro.objects.all()
    return render(request, "Productor/ListarProductoRegistrado.html", {"pregistros": pregistros})


def SolicitarProducto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre_producto']
        solicitud = request.POST['solicitud']
        cierre_oferta = request.POST['fecha_cierre']
        comuna = request.POST['comuna']
        correo = request.POST['email']
        ProductosVenta(nombre = nombre, solicitud = solicitud, cierre_oferta = cierre_oferta, comuna = comuna, 
        correo = correo).save()
        EnvioCorreoSolicitud(nombre, solicitud, cierre_oferta, comuna, correo)
        return redirect('listarProducto')
    else:
        return render(request, 'Productor/SolicitarProducto.html')

def RegistrarProducto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre_producto']
        comuna = request.POST['comuna']
        correo = request.POST['email']
        calidad = request.POST['calidad']
        cantidad = request.POST['cantidad']
        oferta = request.POST['oferta']
        producto = request.POST['producto']
        ProductosRegistro(nombre = nombre, comuna = comuna, correo = correo, calidad = calidad, 
        cantidad = cantidad, oferta = oferta, producto = producto).save()
        EnvioCorreoRegistro(nombre, comuna, correo, calidad, cantidad, oferta, producto)
        return redirect('listarProductoRegistro')
    else:
        return render(request, 'Productor/RegistrarProducto.html')


def EnvioCorreoRegistro(nombre, comuna, correo, calidad, cantidad, oferta, producto):
    #Con esta linea de abajo podemos llamar los datos que necesitamos, debemos hacer lo mismo para los demas datos
    context = {'correo' : correo, 'comuna' : comuna, 'nombre' : nombre, 'calidad' : calidad, 'cantidad' : cantidad, 'oferta' : oferta, 'producto' : producto}
    template = get_template('Correo/CorreoRegistroProducto.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Correo de Prueba',
        'Feria Virtual',
        settings.EMAIL_HOST_USER,
        [correo]
    )
    email.attach_alternative(content, 'text/html')
    email.send()

def EnvioCorreoSolicitud(nombre, solicitud, cierre_oferta, comuna, correo):
    context = {'nombre' : nombre, 'solicitud' : solicitud, 'cierre_oferta' : cierre_oferta, 'comuna' : comuna, 'correo' : correo}
    template = get_template('Correo/CorreoSolicitudProducto.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Correo de Prueba',
        'Feria Virtual',
        settings.EMAIL_HOST_USER,
        [correo]
    )
    email.attach_alternative(content, 'text/html')
    email.send()