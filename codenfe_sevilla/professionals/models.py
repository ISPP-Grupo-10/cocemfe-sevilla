from django.db import models
from organizations.models import Organization

class Professional(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    license = models.CharField(max_length=50)
    organizations = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='profesionals', null=True, blank=True)

    def __str__(self):
        return self.username