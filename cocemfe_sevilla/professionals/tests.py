# tests.py

from django.test import TestCase
from django.urls import reverse
from professionals.models import Professional
from professionals.forms import ProfessionalForm
from organizations.models import Organization

class ProfessionalModelTest(TestCase):
    def setUp(self):
        # Creamos una organización de prueba
        self.organization = Organization.objects.create(
            name='Test Organization',
            telephone_number='123456789',
            address='Test Address',
            email='test@example.com',
            zip_code=12345,
        )

        # Creamos un profesional de prueba asociado a la organización
        self.professional = Professional.objects.create(
            username='testuser',
            first_name='John',
            last_name='Doe',
            telephone_number='123456789',
            license_number='ABC123',
            organizations=self.organization,
        )


    def test_professional_str(self):
        self.assertEqual(str(self.professional), 'testuser')


class ProfessionalFormTest(TestCase):
    def setUp(self):
        # Creamos una organización de prueba para utilizar en las pruebas
        self.organization = Organization.objects.create(
            name='Test Organization',
            telephone_number='123456789',
            address='Test Address',
            email='test@example.com',
            zip_code=12345,
        )

    def test_valid_professional_form(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'telephone_number': '123456789',
            'license_number': 'ABC123',
            'organizations': self.organization.id,
            'email': 'john.doe@example.com',
            'profile_picture': 'test.jpg',
        }
        form = ProfessionalForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_invalid_professional_form(self):
        form_data = {}
        form = ProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)


class ProfessionalViewTest(TestCase):
    def setUp(self):
        self.professional = Professional.objects.create(
            username='testuser',
            first_name='John',
            last_name='Doe',
            telephone_number='123456789',
            license_number='ABC123',
        )

    def test_professional_detail_view(self):
        url = reverse('professional_detail', kwargs={'pk': self.professional.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John')

    def test_professional_update_view(self):

        url = reverse('professional_detail', kwargs={'pk': self.professional.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        updated_data = {
            'first_name': 'UpdatedName',
            'last_name': 'UpdatedSurname',
            'telephone_number': '987654321',
            'license_number': 'XYZ789',
        }

        response = self.client.post(url, updated_data)

        self.assertEqual(response.status_code, 200)