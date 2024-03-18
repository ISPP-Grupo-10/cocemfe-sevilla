from django.db import models
from documents.models import Document
from professionals.models import Professional

class Suggestion(models.Model):
    RELEVANCE_CHOICES = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('poco', 'Poco importante'),
    )
    main = models.CharField(max_length=255)
    justification = models.TextField()
    relevance = models.CharField(max_length=20, choices=RELEVANCE_CHOICES)
    section = models.CharField(max_length=2000)
    page = models.IntegerField()
    date = models.DateField()
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, null=True, related_name='suggestions')
    document = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, related_name='suggestions')

    def __str__(self):
        return self.main