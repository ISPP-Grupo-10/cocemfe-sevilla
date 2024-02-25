from django.db import models
from professionals.models import Professional

class Document(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=True)
    professionals = models.ManyToManyField('professionals.Professional', related_name='document_professionals')


    def __str__(self):
        return self.name