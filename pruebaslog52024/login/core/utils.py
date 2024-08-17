# utils.py
from .models import Ticket

def create_ticket_from_email(sender, subject, body):
    ticket = Ticket(
        sender=sender,
        title=subject,
        description=body,
    )
    ticket.save()
