from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from .models import Events
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from .forms import EventForm
from professionals.views import is_admin
from documents.models import Document
from django.db import IntegrityError
from django.utils import timezone
from datetime import datetime
from django.utils.timezone import make_aware

@user_passes_test(is_admin)
def create_event(request, title, description, event_datetime, document, creator, type):
    try:
        
        event_datetime = make_aware(event_datetime)

        if event_datetime < timezone.now():
            raise ValueError("La fecha del evento no puede ser anterior a la fecha actual")
        
        event = Events.objects.create(
            creator=creator, 
            title=title,
            description=description,
            datetime=event_datetime,
            document=document,
            type=type
        )
        return event  
    except Exception as e:
        print(f"Error al crear el evento: {e}")
        return HttpResponseBadRequest('Error al crear el evento:', str(e))


@user_passes_test(is_admin)
def create_modal_event(request):
    try:
        document = get_object_or_404(Document, pk=request.POST.get('document_id'))
        event_datetime = request.POST.get('datetime')
        
        datetime_object = datetime.fromisoformat(event_datetime)
        datetime_object = timezone.make_aware(datetime_object, timezone.get_current_timezone())

        # Comparar con la fecha y hora actual
        if datetime_object < timezone.now():
            raise ValueError("La fecha del evento no puede ser anterior a la fecha actual")
        
        event = Events.objects.create(
            creator=request.user, 
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            datetime=request.POST.get('datetime'),
            document=document,
            type=request.POST.get('type'),
        )
        return HttpResponse('Evento creado con éxito')  
    except Exception as e:
        print(f"Error al crear el evento: {e}")
        return JsonResponse({'error': f'Error al crear el evento: {e}'}, status=400)


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
                error_message = "Error al crear el evento: {}".format(e)
                return render(request, 'create_event.html', {'form': form, 'error_message': error_message})
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})


@user_passes_test(is_admin)
def edit_event_from_document(request, document_id, type, old_datetime, new_datetime):
    try:
        document= get_object_or_404(Document, pk=document_id)
        event=Events.objects.filter(document=document, type=type, datetime=old_datetime).first()
        print("Evento: ", event)
        event.datetime = new_datetime
        event.save()
        return HttpResponse('Evento actualizado con éxito')
    except Exception as e:
        print(f"Error al actualizar el evento: {e}")
        return HttpResponseBadRequest('Error al actualizar el evento')

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

