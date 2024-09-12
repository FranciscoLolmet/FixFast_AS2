from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
#parte del formulario 
from django.contrib.auth.forms import UserModel
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm 
from django.contrib.auth import login, authenticate
#librerias para servidor smtp y exchange
from datetime import datetime, timedelta

#renderizacion de todas las paginas
def home(request):
    return render(request, 'core/home.html')

def creaciondeticket(request):
    return render(request, 'core/creaciondeticket.html')

def configuracion(request):
    return render(request, 'core/configuracion.html')

def creaciondeticket(request):
    return render(request, 'core/creaciondeticket.html')

def ticketscerrados(request):
    return render(request, 'core/ticketscerrados.html')

def configuraciondecorreo(request):     
    return render(request, 'core/configuraciondecorreo.html')

def lista_tickets(request):     
    return render(request, 'core/listaticket.html')

def lista_tickets(request):     
    return render(request, 'core/editarticket.html') 

def lista_usuarios(request):     
    return render(request, 'core/lista_usuarios.html')

def editaruser(request):     
    return render(request, 'core/editaruser.html')

def editaruser(request):     
    return render(request, 'core/agregaruser.html')

def editaruser(request):     
    return render(request, 'core/eliminaruser.html')

@login_required
def products(request):
    return render(request, 'core/products.html')

#parte del formulario 
def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Cambia 'home' por la URL de la página a la que deseas redirigir al usuario después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

##################CAMBIAR CONTRASEÑA

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['new_password1'])
            user.save()
            
            # Autenticar nuevamente al usuario
            username = request.user.username
            password = form.cleaned_data['new_password1']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)  # Iniciar sesión de nuevo con la nueva contraseña
                messages.success(request, 'Your password has been successfully changed!')
                return redirect('/accounts/login/')  # Redirigir a la página de perfil o a donde prefieras
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'change_password.html', {'form': form})


#para devolver error si ingresa mal usuario y contraseña 
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationError(data=request.POST)
        if form.is_valid():
            # Lógica para el inicio de sesión exitoso
            return redirect('home')
    else:
        form = AuthenticationForm() # type: ignore

    return render(request, 'login.html', {'form': form})
#esta parte es la logica para que guarde datos en la bd de django
from django.shortcuts import render, redirect
from .forms import TicketForm

def creaciondeticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio o donde desees después de guardar el ticket
    else:
        form = TicketForm()
    return render(request, 'core/creaciondeticket.html', {'form': form})


from .models import Ticket

def alltickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'core/alltickets.html', {'tickets': tickets})





# logica para cerrar el Ticket

from django.shortcuts import get_object_or_404, redirect
from .models import Ticket

def cerrar_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket.closed = True
    ticket.save()
    return redirect('home')

def all_closed_tickets(request):
    closed_tickets = Ticket.objects.filter(closed=True)
    return render(request, 'ticketscerrados.html', {'closed_tickets': closed_tickets})

from django.shortcuts import get_object_or_404, redirect
from .models import Ticket

def listatickets(request):
    tickets = Ticket.objects.all()  # Obtén todos los objetos de la tabla ticket
    return render(request, 'listaticket.html', {'tickets': tickets})




#editar tickets
from django.shortcuts import get_object_or_404, redirect
from .models import Ticket

def editarticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == 'POST':
        ticket.id = request.POST['id']
        ticket.title = request.POST['title']
        ticket.description = request.POST['description']
        ticket.save()
        return redirect('listatickets')
    return render(request, 'editarticket.html', {'ticket': Ticket})

# core/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Ticket  # Asegúrate de importar tu modelo

def eliminarticket(request, ticket_id):
    # Obtener el producto o devolver un 404 si no existe
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Eliminar el producto
    ticket.delete()

    # Enviar un mensaje de éxito (opcional)
    messages.success(request, f'El ticket "{ticket.title}" ha sido eliminado con éxito.')

    # Redirigir a la lista de productos
    return redirect('listatickets')  # Asegúrate de que este nombre coincida con tu URL para la lista de productos



#-----------------------
#-------------------

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User

def lista_usuarios(request):
    usuarios = User.objects.all()  # Captura todos los usuarios de la base de datos
    return render(request, 'core/lista_usuarios.html', {'usuarios': usuarios})

########################################################PERFIL
def perfil(request):
    usuarios = User.objects.all()  # Captura todos los usuarios de la base de datos
    return render(request, 'core/perfil.html', {'usuarios': usuarios})


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from .forms import User




from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
 # Asegúrate de importar tu modelo

def eliminaruser(request, user_id):
    # Obtener el producto o devolver un 404 si no existe
    usuarios = get_object_or_404(User, id=user_id)

    # Eliminar el producto
    usuarios.delete()

    # Enviar un mensaje de éxito (opcional)
    messages.success(request, f'El usuario "{usuarios.username}" ha sido eliminado con éxito.')

    # Redirigir a la lista de productos
    return redirect('listauser')  # Asegúrate de que este nombre coincida con tu URL para la lista de productos



def editaruser(request, user_id):
    usuarios = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        usuarios.username = request.POST['username']
        usuarios.last_name = request.POST['last_name']
        usuarios.email = request.POST['email']
        usuarios.save()
        return redirect('listauser')
    return render(request, 'editaruser.html', {'usuarios': usuarios})

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def agregaruser(request, user_id):
    usuarios = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        usuarios.username = request.POST['username']
        usuarios.last_name = request.POST['last_name']
        usuarios.email = request.POST['email']
        usuarios.save()
        return redirect('listauser')
    return render(request, 'agregaruser.html', {'usuarios': usuarios})
#-----------------------

#logica de la vista para procesar los correos
from django.shortcuts import render, redirect
from .logicadecorreo import obtener_correos
import threading

def configurar_correo(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        pop_server = request.POST.get('pop_server')
        port = int(request.POST.get('port'))
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Crear un hilo para ejecutar la función de obtener correos
        correo_thread = threading.Thread(target=obtener_correos, args=(pop_server, port, username, password))
        correo_thread.start()

        # Redirigir al usuario a la página de inicio después de iniciar el hilo
        return redirect('home')

    # Renderizar el formulario HTML
    return render(request, 'configuracion_correo.html')
