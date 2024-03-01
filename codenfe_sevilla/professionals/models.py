from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_password_strength
from organizations.models import Organization

class Professional(AbstractUser):

    address = models.CharField(max_length=255)
    license = models.CharField(max_length=50)
    organizations = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='profesionals', null=True)


    def __str__(self):
        return self.username