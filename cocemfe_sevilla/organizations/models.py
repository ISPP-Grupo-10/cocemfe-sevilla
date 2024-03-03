from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    zip_code = models.IntegerField()

    def __str__(self):
        return self.name