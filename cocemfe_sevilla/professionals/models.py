from django.db import models
from django.contrib.auth.models import AbstractUser
from organizations.models import Organization
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
import re
from django.core.exceptions import ValidationError


class Professional(AbstractUser):
    phone_number_validator = RegexValidator(
        regex=r'^\d{9}$',  
        message='El número de teléfono debe tener exactamente 9 dígitos numéricos.',
        code='invalid_phone_number'
    )
    telephone_number = models.CharField(max_length=9, validators=[phone_number_validator])
    license_number = models.CharField(max_length=20)
    organizations = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='professionals', null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    access_documents = models.ManyToManyField('documents.Document', blank=True)
    terms_accepted = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    def clean(self):

        if not re.match(r'^[a-zA-Z0-9_\s]*$', self.username):
            raise ValidationError({'username': 'El nombre de usuario solo puede contener letras, números y espacios.'})

        if not re.match(r'^[a-zA-Z0-9\s\u00C0-\u00FF]*$', self.first_name):
            raise ValidationError({'first_name': 'El nombre solo puede contener letras, números y espacios.'})

        if not re.match(r'^[a-zA-Z0-9\s\u00C0-\u00FF]*$', self.last_name):
            raise ValidationError({'last_name': 'Los apellidos solo puede contener letras, números y espacios.'})

class Request(models.Model):
    class Status(models.TextChoices):
        PENDING = 'Pendiente'
        ON_REVIEW = 'En revisión'
        REVIEWED = 'Revisada'

    description = models.TextField(max_length=500, null=False, blank=False)
    email = models.EmailField(max_length=30, null=False, blank = False)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

    def __str__(self):
        return f"{self.id}: {self.status}"
