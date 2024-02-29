from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_password_strength
from organizations.models import Organization


class Professional(AbstractUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    telephone_number = models.CharField(max_length=15)
    license_number = models.CharField(max_length=20)
    organizations = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='professionals', null=True)

    def __str__(self):
        return self.username