from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Events
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from .forms import EventForm
from professionals.views import is_admin
from documents.models import Document

def create_event(title, description, datetime, document, creator):
    try:
        
        event = Events.objects.create(
            creator=creator, 
            title=title,
            description=description,
            datetime=datetime,
            document=document
        )
        return event  
    except:
        return None  

@user_passes_test(is_admin)
def new_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form}) 

@user_passes_test(is_admin)
def delete_event(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    
    if request.method == 'POST':
        event.delete()
        return redirect('evento_eliminado_exitosamente')  
    
    return render(request, 'confirmar_eliminacion_evento.html', {'event': event}) 

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
        'start': evento.datetime
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