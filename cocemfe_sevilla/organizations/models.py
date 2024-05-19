from django.db import models
from django.core.validators import RegexValidator
import re
from django.core.exceptions import ValidationError

# Create your models here.
class Organization(models.Model):

    phone_number_validator = RegexValidator(
        regex=r'^\d{9}$',
        message='El número de teléfono debe tener exactamente 9 dígitos numéricos.',
        code='invalid_phone_number'
    )

    name = models.CharField(max_length=125)
    telephone_number = models.CharField(max_length=9, validators=[phone_number_validator])
    address = models.CharField(max_length=125)
    email = models.EmailField()
    zip_code = models.IntegerField(validators=[RegexValidator(regex=r'^\d{5}$', message='El codigo postal debe tener exactamente 5 dígitos numéricos')])

    def __str__(self):
        return self.name
    
    def clean(self):
        
        if not re.match(r'^[a-zA-Z0-9\s\u00C0-\u00FF]*$', self.name):
            raise ValidationError({'name': 'El nombre solo puede contener letras, números y espacios.'})