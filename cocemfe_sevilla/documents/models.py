from django.db import models
from professionals.models import Professional
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import gettext as _
import requests
import re
from maps.models import Coordinates
import time

class Document(models.Model):
    STATUS = (
        ('Borrador', 'Borrador'),
        ('Aportaciones', 'Aportaciones'),
        ('Votaciones', 'Votaciones'),
        ('En revisión', 'En revisión'),
        ('Revisado', 'Revisado'),
        )

    name = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)
    ubication = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='Borrador')
    professionals = models.ManyToManyField(Professional, related_name='document_professionals')
    checked_professionals = models.ManyToManyField(Professional, related_name='checked_professionals', blank=True)
    suggestion_start_date  = models.DateTimeField(null=True, blank=True)
    suggestion_end_date = models.DateTimeField(null=True, blank=True)
    voting_start_date = models.DateTimeField(null=True, blank=True)
    voting_end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def clean(self):
            
        if not re.match(r'^[a-zA-Z0-9\s\u00C0-\u00FF]*$', self.name):
            raise ValidationError({'name': 'El nombre solo puede contener letras, números y espacios.'})

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
            raise ValidationError({'ubication': ('Debe indicar la localidad.')})
        
        if not valid_location(self.ubication):
            raise ValidationError({'ubication': ('La localidad introducida no es válida.')})
       
      
def valid_location(city):
    url = f'https://nominatim.openstreetmap.org/search?q={city}&format=json'
    headers = {
        "Referer": "https://cocemfe-wpl-4a7kpawtwa-no.a.run.app/",
        "User-Agent": "CocemfeWebNGO/1.0 (https://cocemfe-wpl-4a7kpawtwa-no.a.run.app/; info@cocemfesevilla.es)"
    }
    time.sleep(1)
    res = False
    try:
        response = requests.get(url, timeout=None, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        if response.status_code == 403:
            res = True
        else:
            raise e
    if response:
        data = response.json()
        if data:
            latitude = float(data[0]['lat'])
            longitude = float(data[0]['lon'])
            Coordinates.objects.create(location=city, latitude=latitude, longitude=longitude)
            res = True
 
    return res
