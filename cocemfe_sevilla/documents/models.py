from django.db import models
from professionals.models import Professional
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime
from django.utils.translation import gettext as _


class Document(models.Model):
    STATUS = (
        ('Borrador', 'Borrador'),
        ('Aportaciones', 'Aportaciones'),
        ('Votaciones', 'Votaciones'),
        ('En revisión', 'En revisión'),
        ('Revisado', 'Revisado'),
        )

    name = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)
    ubication = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='Borrador')
    professionals = models.ManyToManyField(Professional, related_name='document_professionals')
    suggestion_start_date  = models.DateTimeField(null=True, blank=True)
    suggestion_end_date = models.DateTimeField(null=True, blank=True)
    voting_start_date = models.DateTimeField(null=True, blank=True)
    voting_end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def clean(self):
            if self.suggestion_start_date and self.suggestion_end_date:
                if self.suggestion_start_date > self.suggestion_end_date:
                    raise ValidationError({'suggestion_end_date': ('La fecha de fin de sugerencia no puede ser anterior a la fecha de inicio.')})
                elif self.suggestion_start_date == self.suggestion_end_date:
                    raise ValidationError({'suggestion_end_date': ('La fecha de fin de sugerencia no puede ser igual que la fecha de inicio.')})

            if self.voting_start_date and self.voting_end_date:
                if self.voting_start_date > self.voting_end_date:
                    raise ValidationError({'voting_end_date': ('La fecha de fin de votación no puede ser anterior a la fecha de inicio.')})
                elif self.voting_start_date == self.voting_end_date:
                    raise ValidationError({'voting_end_date': ('La fecha de fin de votación no puede ser igual que la fecha de inicio.')})
                
            if self.suggestion_end_date and self.voting_end_date:
                if self.suggestion_end_date > self.voting_end_date:
                    raise ValidationError({'voting_end_date': ('La fecha de fin de votación no puede ser anterior a la fecha de fin de sugerencia.')})
                elif self.voting_end_date == self.suggestion_end_date:
                    raise ValidationError({'voting_end_date': ('La fecha de fin de votación no puede ser igual que la fecha de fin de sugerencia.')})
            
            if self.suggestion_start_date and self.suggestion_start_date.date() < timezone.now().date():
                raise ValidationError({'suggestion_start_date': ('La fecha de inicio de sugerencia no puede ser anterior a la fecha actual.')})
            
            if self.suggestion_end_date and self.suggestion_end_date.date() < timezone.now().date():
                raise ValidationError({'suggestion_end_date': ('La fecha de fin de sugerencia no puede ser anterior a la fecha actual.')})
            
            if self.voting_end_date and self.voting_end_date.date() < timezone.now().date():
                raise ValidationError({'voting_end_date': ('La fecha de fin de votación no puede ser anterior a la fecha actual.')})

            if self.pdf_file:
                try:
                    FileExtensionValidator(allowed_extensions=['pdf'])(self.pdf_file)
                except ValidationError as e:
                    raise ValidationError({'pdf_file': ('El archivo debe ser un PDF.')}) 
            else:
                raise ValidationError({'pdf_file': ('Debe subir un archivo PDF.')})
            
            if not self.ubication:
                raise ValidationError({'ubication': ('Debe indicar la ubicación.')})
       
      