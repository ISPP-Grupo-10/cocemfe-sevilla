from django.db import models
from professionals.models import Professional
from documents.models import Document
from django.core.exceptions import ValidationError
from django.utils import timezone
import re

class Events(models.Model):
    class TIPO_CHOICES(models.TextChoices):
        REUNION = 'reunion', 'Reunión'
        APORTACIONES = 'aportaciones', 'Aportaciones'
        VOTACIONES = 'votaciones', 'Votaciones'
        REVISION = 'revision', 'Revisión'

    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(Professional, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=255 ,null=False, blank=False)
    datetime = models.DateTimeField(null=True,blank=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, null=False)
    type = models.CharField(max_length=20, choices=TIPO_CHOICES.choices, default=TIPO_CHOICES.REUNION)
    
    def __str__(self):
        return self.title
    
    def clean(self):
        super().clean()

        # Validación: La fecha y hora del evento no pueden ser anteriores a la fecha y hora actuales.
        if self.datetime and self.datetime < timezone.now():
            raise ValidationError("La fecha y hora del evento no pueden ser anteriores a la fecha y hora actuales.")
        
        # Validación: Verificar que el título solo contenga letras, números y espacios.
        if not re.match(r'^[a-zA-Z0-9\s\u00C0-\u00FF]*$', self.title):
            raise ValidationError({"El título del evento solo puede contener letras, números y espacios."})
        
        # Validación: Verificar que la descripción solo contenga letras, números y espacios.
        if not re.match(r'^[a-zA-Z0-9\s\u00C0-\u00FF]*$', self.description):
            raise ValidationError({"La descripción del evento solo puede contener letras, números y espacios."})
        
        # Validación: Tipo de evento debe ser uno de los tipos permitidos.
        if self.type not in [choice[0] for choice in self.TIPO_CHOICES.choices]:
            raise ValidationError("El tipo de evento no es válido.")
        
        # Validación: Verificar que la longitud del título no exceda cierto valor.
        if len(self.title) > 50:
            raise ValidationError("El título del evento no puede exceder los 50 caracteres.")

        # Validación: Verificar que la longitud de la descripción no exceda cierto valor.
        if len(self.description) > 255:
            raise ValidationError("La descripción del evento no puede exceder los 255 caracteres.")

        if not self.document_id:
            raise ValidationError("El documento asociado al evento es requerido.")
        if not Document.objects.filter(pk=self.document_id).exists():
            raise ValidationError("El documento especificado no existe.")