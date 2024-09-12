from django.urls import path, include
from .views import home, products, exit, creaciondeticket, alltickets, configuracion, ticketscerrados, configuraciondecorreo, change_password
from django.conf import settings
from django.conf.urls.static import static
#formulario 
from .views import register, products, listatickets, editarticket, lista_usuarios,eliminaruser,editaruser, agregaruser, eliminarticket,perfil
#reestablecimiento de contraseña
from django.contrib.auth import views as auth_views
from . import views




#todas las urls a las que se puede acceder desde el proyecto
urlpatterns = [
   path('', home, name='home'),#nos devuelve al inicio de la pagina
   path('products/', products, name='products_login'), #nos redirecciona al dashboard
   path('products/', products, name='products'),
   path('logout/', exit, name='exit'),#nos permite salir de nuestra cuenta
   path('register/', register, name='register'),
   path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),#nos manda para resetear las password
   path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),#nos muestra el mensaje de listo 
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   path('creaciondeticket/', creaciondeticket, name='creaciondeticket'), #nos manda a la creacion de tickets
   path('alltickets/', alltickets, name='alltickets' ),#nos manda a la donde estan los tickets
   path('creaciondeticket/', creaciondeticket, name='creaciondeticketdirecto'),
   path('cerrar-ticket/<int:ticket_id>/', views.cerrar_ticket, name = 'cerrar_ticket'),
   path('configuracion/', configuracion, name='configuracion'),
   path('ticketscerrados/', ticketscerrados, name='ticketcerrados'),
   path('listaticket/', listatickets, name='listatickets'),
   path('editarticket/<int:ticket_id>/', editarticket, name='editarticket'),
   path('eliminarticket/<int:ticket_id>/', eliminarticket, name='eliminarticket'),
   path('eliminaruser/<int:user_id>/', eliminaruser, name='eliminaruser'),
   path('editaruser/<int:user_id>/', editaruser, name='editaruser'),
   path('agregaruser/<int:user_id>/', agregaruser, name='agregaruser'),
   path('listauser/', lista_usuarios, name='listauser'),
   path('change_password/', change_password, name='change_password'),
   path('perfil/', perfil, name='perfil'),
   path('configuraciondecorreo/', configuraciondecorreo, name='configuraciondecorreo'),#pagina para configurar correo pop3
   path('configuracion-correo/', views.configurar_correo, name='configuracion_correo')
   
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    

