from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from professionals.models import Professional
from documents.models import Document

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