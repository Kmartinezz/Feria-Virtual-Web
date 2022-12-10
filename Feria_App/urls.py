from textwrap import indent
from django.urls import URLPattern, path
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session

#Con este comando se cierran todas las sesiones
Session.objects.all().delete()

urlpatterns = [
    path('', views.index, name = 'index'),
    path('registrar Cliente/', views.FormularioClienteView.index, name = 'registrarCliente'),
    path('guardarCliente/', views.FormularioClienteView.procesar_formulario, name = 'guardarCliente'),
    path('registrar/', views.Registrar, name = 'registrar'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'index.html'), name = 'logout'),

    #Productos y Transporte
    path('ListarProducto',  views.ListarProducto, name = 'listarProducto'),
    path('ListarProductoRegistro',  views.ListarProductoRegistro, name = 'listarProductoRegistro'),
    path('solicitarproducto', views.SolicitarProducto, name = 'solicitarproducto'),
    path('registrarproducto', views.RegistrarProducto, name = 'registrarproducto'),
    path('ListarTransporte',  views.ListarTransporte, name = 'listarTransporte'),

    #Subastas

    #Administrador
    path('Administrador', views.Administrador, name = 'Administrador'),
    path('CrudRegistroProducto', views.CrudRegistroProducto, name = 'CrudRegistroProducto'),
    path('CrudSolicitudProducto', views.CrudSolicitudProducto, name = 'CrudSolicitudProducto'),
    path('CrudTransporte', views.CrudTransporte, name = 'CrudTransporte'),
    path('CrudContrato', views.CrudContrato, name = 'CrudContrato'),

    path('eliminarTransporte/<int:id>', views.EliminarTransporte, name = 'EliminarTransporte'),
    path('eliminarSolicitudProducto/<int:id>', views.EliminarSolicitudProducto, name = 'EliminarSolicitudProducto'),
    path('eliminarRegistroProducto/<int:id>', views.EliminarRegistroProducto, name = 'EliminarRegistroProducto'),
    path('eliminarContrato/<int:id>', views.EliminarContrato, name = 'EliminarContrato'),

    path('editarTransporte/<int:id>', views.EditarTransporte, name = 'EditarTransporte'),
    path('editarSolicitudProducto/<int:id>', views.EditarSolicitudProducto, name = 'EditarSolicitudProducto'),
    path('editarRegistroProducto/<int:id>', views.EditarRegistroProducto, name = 'EditarRegistroProducto'),
    path('editarContrato/<int:id>', views.EditarContrato, name = 'EditarContrato'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)