from django.db import models
from professionals.models import Professional
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


class Document(models.Model):
    STATUS = (
        ('Aportaciones', 'Aportaciones'),
        ('Votaciones', 'Votaciones'),
        ('En revisión', 'En revisión'),
        ('Revisado', 'Revisado'),
        )

    name = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    ubication = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='Aportaciones')
    professionals = models.ManyToManyField(Professional, related_name='document_professionals')

    def __str__(self):
        return self.name
  