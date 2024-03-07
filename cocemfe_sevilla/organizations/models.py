from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Organization(models.Model):

    phone_number_validator = RegexValidator(
        regex=r'^\d{9}$',
        message='El número de teléfono debe tener exactamente 9 dígitos.',
        code='invalid_phone_number'
    )

    name = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=9, validators=[phone_number_validator])
    address = models.CharField(max_length=255)
    email = models.EmailField()
    zip_code = models.IntegerField(validators=[RegexValidator(regex=r'^\d{5}$', message='El codigo postal debe tener 5 dígitos')])



    def __str__(self):
        return self.name