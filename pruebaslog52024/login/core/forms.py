from django import forms
from .models import Ticket
# nos permite realizar el modelo para nuestra bd de tickets
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'asignar', 'categorias']
        
        
