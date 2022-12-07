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

#
#
#
#
#FALTA REALIZAR EL UPDATE DE DATOS EN LOS CRUD
#
#
#

# Create your views here.
def index(request):
    return render(request, 'index.html')

#-------------------------------------------ADMINISTRADOR VIEWS-------------------------------------------

def Administrador(request):
    return render(request, 'Administrador/Administrador.html')


#-------------------------------------------RegistroProducto VIEWS-------------------------------------------

def CrudRegistroProducto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre_producto']
        nombre_persona = request.POST['nombre_persona']
        rut = request.POST['rut']
        telefono = request.POST['telefono']
        comuna = request.POST['comuna']
        correo = request.POST['email']
        producto = request.POST['producto']
        calidad = request.POST['calidad']
        cantidad = request.POST['cantidad']
        oferta = request.POST['oferta']

        ProductosRegistro(nombre = nombre, nombre_persona = nombre_persona, rut = rut, telefono = telefono, 
        comuna = comuna, correo = correo, calidad = calidad, cantidad = cantidad, oferta = oferta, producto = producto).save()
        return redirect('CrudRegistroProducto')
    else:
        #READ
        pregistros = ProductosRegistro.objects.all()
        return render(request, "Administrador/Crud-RegistroProducto.html", {"pregistros": pregistros})

    #UPDATE
    #-----Update here-----

def EliminarRegistroProducto(request, id):
    pregistros = ProductosRegistro.objects.get(id = id)
    pregistros.delete()
    return redirect('CrudSolicitudProducto')


#-------------------------------------------SolicitudProducto VIEWS-------------------------------------------    

def CrudSolicitudProducto(request):
    #CREATE
    if request.method == 'POST':
        nombre = request.POST['nombre_producto']
        nombre_persona = request.POST['nombre_persona']
        rut = request.POST['rut']
        telefono = request.POST['telefono']
        solicitud = request.POST['solicitud']
        cierre_oferta = request.POST['fecha_cierre']
        comuna = request.POST['comuna']
        correo = request.POST['email']

        ProductosVenta(nombre = nombre, nombre_persona = nombre_persona, rut = rut, telefono = telefono, 
        solicitud = solicitud, cierre_oferta = cierre_oferta, comuna = comuna, correo = correo).save()
        #EnvioCorreoSolicitud(nombre, solicitud, cierre_oferta, comuna, correo)
        return redirect('CrudRegistroProducto')
    else:
        #READ
        productos = ProductosVenta.objects.all()
        return render(request, "Administrador/Crud-SolicitudProducto.html", {"productos": productos})

    #UPDATE
    #-----Update here-----

def EliminarSolicitudProducto(request, id):
    productos = ProductosVenta.objects.get(id = id)
    productos.delete()
    return redirect('CrudSolicitudProducto')


#-------------------------------------------Trasnporte VIEWS-------------------------------------------    

def CrudTransporte(request):

    #CREATE
    if request.method == 'POST':
        nombre = request.POST['nombre_transporte']
        nombre_persona = request.POST['nombre_persona']
        rut = request.POST['rut']
        telefono = request.POST['telefono']
        t_transporte = request.POST['t_transporte']
        patente = request.POST['patente']
        correo = request.POST['email']
        comuna = request.POST['comuna']

        Transporte(nombre = nombre, nombre_persona = nombre_persona, rut = rut, telefono = telefono,
        t_transporte = t_transporte, patente = patente, correo = correo, comuna = comuna).save()
        return redirect('CrudTransporte')

    #UPDATE
    #-----Update here-----

    #READ
    elif request.method != 'POST':
        transportes = Transporte.objects.all()
        return render(request, "Administrador/Crud-Transporte.html", {"transportes": transportes})
    
def EliminarTransporte(request, id):
    transporte = Transporte.objects.get(id = id)
    transporte.delete()
    return redirect('CrudTransporte')


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


#-------------------------------------------Correo VIEWS-------------------------------------------    

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