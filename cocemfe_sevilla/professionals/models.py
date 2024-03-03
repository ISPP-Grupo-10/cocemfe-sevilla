from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_password_strength
from organizations.models import Organization
from django.apps import apps


class Professional(AbstractUser):
    telephone_number = models.CharField(max_length=15)
    license_number = models.CharField(max_length=20)
    organizations = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='professionals', null=True)
    email = models.EmailField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
#    access_documents = models.ManyToManyField(Document, related_name='professionals', blank=True)

    def __str__(self):
        return self.username

    def get_document_model(self):
        Document = apps.get_model('documents', 'Document')
        return Document

    def some_method_that_uses_document(self):
        Document = self.get_document_model()
