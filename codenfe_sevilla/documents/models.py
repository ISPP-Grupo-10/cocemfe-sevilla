from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=True)
    professionals = models.ManyToManyField('Professional', related_name='documents')

    def __str__(self):
        return self.name