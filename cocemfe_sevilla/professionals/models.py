from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_password_strength
from organizations.models import Organization
from django.apps import apps
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

class Professional(AbstractUser):
    phone_number_validator = RegexValidator(
        regex=r'^\d{9}$',  
        message='El número de teléfono debe tener exactamente 9 dígitos.',
        code='invalid_phone_number'
    )
    telephone_number = models.CharField(max_length=9, validators=[phone_number_validator])
    license_number = models.CharField(max_length=20)
    organizations = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='professionals', null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    access_documents = models.ManyToManyField('documents.Document', blank=True)
    terms_accepted = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.username


class Request(models.Model):
    class Status(models.TextChoices):
        PENDING = 'Pendiente'
        ON_REVIEW = 'En revisión'
        REVIEWED = 'Revisada'

    description = models.TextField(null=False, blank=False)
    email = models.EmailField(max_length=30, null=False, blank = False)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

    def __str__(self):
        return f"{self.id}: {self.status}"