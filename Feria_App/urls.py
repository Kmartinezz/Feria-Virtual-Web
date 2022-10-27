from textwrap import indent
from django.urls import URLPattern, path
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name = 'index'),
    path('registrarCliente/', views.FormularioClienteView.index, name='registrarCliente'),
    path('guardarCliente/', views.FormularioClienteView.procesar_formulario, name='guardarCliente'),
    path('registrarProducto/', views.FormularioProductorView.index, name='registrarProducto'),
    path('guardarProducto/', views.FormularioProductorView.procesar_formulario, name='guardarProducto'),
    path('registrar/', views.Registrar, name='registrar'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('producto', views.FormularioProductorView.listarProductos, name='producto'),
    path('productos_venta', login_required(views.listarProductos_venta), name='productos_venta'),
    path('index2/', views.index2, name = 'index2'),
    path('ListarProducto',  views.listar_productos, name='listarProducto'),
    path('solicitarproducto', views.SolicitarProducto, name='solicitarproducto'),
    path('registrarproducto', views.RegistrarProducto, name='registrarproducto'),
    
]