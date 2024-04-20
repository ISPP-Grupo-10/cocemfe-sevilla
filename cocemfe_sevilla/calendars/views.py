from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Events
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from .forms import EventForm
from professionals.views import is_admin
from documents.models import Document
from django.db import IntegrityError

def create_event(title, description, datetime, document, creator, type):
    try:
        event = Events.objects.create(
            creator=creator, 
            title=title,
            description=description,
            datetime=datetime,
            document=document,
            type=type
        )
        return event  
    except  Exception as e:
        print(f"Error al crear el evento: {e}")
        return None

@user_passes_test(is_admin)
def new_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False) 
            event.creator = request.user 
            try:
                event.save() 
                return redirect('/calendars')
            except IntegrityError as e:
                # Manejar la excepción de violación de restricción de integridad
                error_message = "Error al crear el evento: {}".format(e)
                return render(request, 'create_event.html', {'form': form, 'error_message': error_message})
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

@user_passes_test(is_admin)
def delete_event(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    event.delete()
    return redirect('/calendars')  

@login_required
def calendar(request):
    return render(request, 'eventos.html') 

@login_required
def devolver_eventos(request):
    if request.user.is_superuser:
        all_events = Events.objects.all()
    else:
        documentos = Document.objects.filter(professionals=request.user).all()
        all_events = [Events.objects.filter(document=documento).all() for documento in documentos]
    eventos_data = [{
        'id': evento.id,
        'title': evento.title,
        'start': evento.datetime,
        'description': evento.description,
        'participantes': [{'first_name': profesional.first_name, 'last_name': profesional.last_name} for profesional in evento.document.professionals.all()],
        'color': 'red' if evento.type == 'aportaciones' else ('green' if evento.type ==  'votaciones' else ('blue' if evento.type ==  'reunion' else ('yellow' if evento.type ==  'revision' else 'orange'))),
        
    } for evento in all_events]
    return JsonResponse(eventos_data, safe=False)

##############
# Create your views here.
@login_required
def index(request):
    all_events = Events.objects.filter(user=request.user).all()
    return render(request,'eventos.html',{'events':all_events})

@login_required
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end, user=request.user)
    event.save()
    data = {}
    return JsonResponse(data)

@login_required
def update_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def enviar_correo_evento():
    # Obtener la fecha actual
    fecha_actual = timezone.now().date()

    # Obtener todos los eventos que ocurren hoy
    eventos_hoy = Events.objects.filter(start__date=fecha_actual)

    # Iterar sobre los eventos y enviar correos electrónicos a los usuarios
    for evento in eventos_hoy:
        usuario = evento.user
        send_mail(
        "Eventos de hoy",
        "Hola {6}, recuerda que hoy tienes los siguientes eventos: {0} ".format(evento, usuario.name),
        "cuidame09@gmail.com",
        usuario.email,
        fail_silently=True
        )