from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Events
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from .forms import EventForm
from professionals.views import is_admin
from documents.models import Document
from django.db import IntegrityError


@user_passes_test(is_admin)
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
def create_modal_event(request):
    try:
        document = get_object_or_404(Document, pk= request.POST.get('document_id'))
        event = Events.objects.create(
            creator=request.user, 
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            datetime=request.POST.get('datetime'),
            document=document,
            type=request.POST.get('type'),
        )
        return HttpResponse('Evento creado con éxito')  
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
                return redirect('/')
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
        'start': evento.datetime,
        'color': 'red' if evento.type == 'aportaciones' else ('green' if evento.type ==  'votaciones' else ('blue' if evento.type ==  'reunion' else ('yellow' if evento.type ==  'revision' else 'orange'))),
    } for evento in all_events]
    return JsonResponse(eventos_data, safe=False)

