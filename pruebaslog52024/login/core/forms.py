from django import forms
from .models import Ticket
from django.contrib.auth.models import User
# nos permite realizar el modelo para nuestra bd de tickets
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'asignar', 'categorias']

# nos permite realizar el modelo para nuestra bd de tickets
class UsuarioForm(forms.ModelForm):
    class Meta2:
        model = User
        fields = ['username','last_name','email']
        
