from django.shortcuts import render, redirect
from .forms import SuggestionForm
from documents.models import Document
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.contrib import messages
from django.utils import timezone

from django.shortcuts import render, redirect
from .models import Suggestion
from datetime import date

def crear_sugerencia(request, document_id):
    if request.method == 'POST':
        # Recibe los datos del formulario
        main = request.POST.get('main')
        justification = request.POST.get('justification')
        relevance = request.POST.get('relevance')
        section = request.POST.get('section')
        page = request.POST.get('page')
        # Obtiene la fecha actual
        today = date.today()
        # Obtiene al profesional (usuario actual)
        profesional = request.user  # Asume que el usuario tiene un perfil profesional asociado
        # Obtiene el documento relacionado
        documento = Document.objects.get(pk=document_id)

        # Crea la sugerencia con los datos recibidos
        sugerencia = Suggestion.objects.create(
            main=main,
            justification=justification,
            relevance=relevance,
            section=section,
            page=page,
            date=today,  # Utiliza la fecha actual
            professional=profesional,  # Asigna al usuario como profesional
            document=documento
        )

        # Guarda la sugerencia en la base de datos
        sugerencia.save()

        # Mensaje de éxito
        messages.success(request, 'El comentario se ha creado correctamente.')

    else:

        # Mensaje de error
        messages.error(request, 'Ha ocurrido un error al procesar el formulario. Inténtalo de nuevo.')

    # Redirecciona a la misma página de detalles del documento
    return redirect('view_pdf_admin', pk=document_id)

