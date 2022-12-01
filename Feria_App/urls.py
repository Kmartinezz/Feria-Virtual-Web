from textwrap import indent
from django.urls import URLPattern, path
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name = 'index'),
    path('registrar Cliente/', views.FormularioClienteView.index, name='registrarCliente'),
    path('guardarCliente/', views.FormularioClienteView.procesar_formulario, name='guardarCliente'),
    path('registrar/', views.Registrar, name='registrar'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('ListarProducto',  views.ListarProducto, name='listarProducto'),
    path('ListarProductoRegistro',  views.ListarProductoRegistro, name='listarProductoRegistro'),
    path('solicitarproducto', views.SolicitarProducto, name='solicitarproducto'),
    path('registrarproducto', views.RegistrarProducto, name='registrarproducto'),
    path('ListarTransporte',  views.ListarTransporte, name='listarTransporte'),
    
]