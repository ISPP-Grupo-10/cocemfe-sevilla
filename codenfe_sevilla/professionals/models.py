from django.db import models

class Professional(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    license = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Organization(models.Model):
    name = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    zip_code = models.IntegerField()

    def str(self):
        return self.name
