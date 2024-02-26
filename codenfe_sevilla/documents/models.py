from django.db import models
from professionals.models import Professional

class Document(models.Model):
    name = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=True)
    professionals = models.ManyToManyField(Professional, related_name='documents')

    def __str__(self):
        return self.name