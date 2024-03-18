from django.test import TestCase
from django.urls import reverse
from documents.models import Document
from professionals.models import Professional
from django.utils import timezone
from organizations.models import Organization
from django.test import RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile

class PoliticaTestCase(TestCase):
    def test_terms_accepted_initialization(self):
        # Creamos una organización
        user = Professional.objects.create_superuser(username='admin', password='admin')
        self.assertFalse(user.terms_accepted)