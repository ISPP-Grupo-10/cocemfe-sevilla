from django.db import models
from professionals.models import Professional

class Document(models.Model):
    STATUS = (
        ('Abierto', 'Abierto'),
        ('Cerrado', 'Cerrado'),
        ('En revisión', 'En revisión'),
        ('Revisado', 'Revisado'),
        ('Aprobado', 'Aprobado'),
        ('Rechazado', 'Rechazado'),
        )

    name = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    ubication = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='Cerrado')
    professionals = models.ManyToManyField(Professional, related_name='document_professionals')

    def __str__(self):
        return self.name