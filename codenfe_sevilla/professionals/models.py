from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    zip_code = models.IntegerField()

    def __str__(self):
        return self.name

class Professional(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    license = models.CharField(max_length=50)
    organizations = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='profesionals', null=True, blank=True)

    def __str__(self):
        return self.username