from django.shortcuts import render, redirect
import poplib
import threading
import time
from .models import Ticket  # Importa el modelo Ticket
from email import parser


def process_email(msg_content):
    email_message = parser.Parser().parsestr(msg_content)
    
    # Extract the subject and body
    subject = email_message['subject']
    body = email_message.get_payload()
    
    # Create a new ticket with the email content
    Ticket.objects.create(
        title=subject,
        description=body,
    )
    print("Nuevo ticket creado a partir del correo:")
    print(f"Título: {subject}")
    print(f"Descripción: {body}")
    # Aquí puedes procesar el contenido del correo electrónico
    # Por ejemplo, extraer el remitente, el asunto, el cuerpo, etc.
    print("Nuevo correo electrónico recibido:")
    print(msg_content)

def obtener_correos(pop_server, port, username, password):
    while True:
        try:
            # Conectarse al servidor POP3
            mail = poplib.POP3(pop_server, port)
            mail.user(username)
            mail.pass_(password)

            # Obtener el número total de mensajes en la bandeja de entrada
            num_messages = len(mail.list()[1])
            print(f'Número total de mensajes en la bandeja de entrada: {num_messages}')

            # Leer los nuevos mensajes uno por uno
            for i in range(1, num_messages + 1):
                # Obtener el contenido del mensaje
                response, msg_bytes, octets = mail.retr(i)
                msg_content = b'\n'.join(msg_bytes).decode('utf-8')

                # Procesar el correo electrónico
                process_email(msg_content)

                # Marcar el mensaje como eliminado (opcional)
                mail.dele(i)

            # Cerrar la conexión
            mail.quit()

        except Exception as e:
            print(f'Error al procesar correos electrónicos: {e}')

        # Esperar un tiempo antes de la siguiente verificación (por ejemplo, 30 segundos)
        time.sleep(30)

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
