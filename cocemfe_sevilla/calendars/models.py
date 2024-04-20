from django.db import models
from professionals.models import Professional
from documents.models import Document
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class Events(models.Model):
    class TIPO_CHOICES(models.TextChoices):
        REUNION = 'reunion', 'Reunión'
        APORTACIONES = 'aportaciones', 'Aportaciones'
        VOTACIONES = 'votaciones', 'Votaciones'
        REVISION = 'revision', 'Revisión'

    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(Professional, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    datetime = models.DateTimeField(null=True,blank=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, null=False)
    type = models.CharField(max_length=20, choices=TIPO_CHOICES.choices, default=TIPO_CHOICES.REUNION)
    
    def clean(self):
        super().clean()

        if self.datetime and self.datetime < timezone.now():
            raise ValidationError("La fecha y hora del evento no pueden ser anteriores a la fecha y hora actuales.")