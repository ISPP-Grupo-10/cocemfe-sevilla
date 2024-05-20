from django.utils import timezone
from django_q.tasks import schedule
from django_q.models import Schedule

from .models import Document

def update_document_status():
    documents = Document.objects.filter(
        status='Borrador',
        suggestion_start_date__lte=timezone.now()
    )
    for document in documents:
        document.status = 'Aportaciones'
        document.save()

    documents = Document.objects.filter(
        status='Aportaciones',
        suggestion_end_date__lte=timezone.now()
    )
    for document in documents:
        document.status = 'Votaciones'
        document.save()

    documents = Document.objects.filter(
        status='Votaciones',
        voting_end_date__lte=timezone.now()
    )
    for document in documents:
        document.status = 'En revisión'
        document.save()

# Programa la tarea para que se ejecute diariamente
schedule(
    'documents.tasks.update_document_status',
    schedule_type=Schedule.DAILY
)