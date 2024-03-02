# tests.py

from django.test import TestCase
from django.urls import reverse
from professionals.models import Professional
from professionals.forms import ProfessionalForm


class ProfessionalModelTest(TestCase):
    def setUp(self):
        self.professional = Professional.objects.create(
            username='testuser',
            first_name='John',
            last_name='Doe',
            telephone_number='123456789',
            license_number='ABC123',
        )

    def test_professional_str(self):
        self.assertEqual(str(self.professional), 'testuser')


class ProfessionalFormTest(TestCase):
    def test_valid_professional_form(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'telephone_number': '123456789',
            'license_number': 'ABC123',
            'organizations': 1,
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
        self.professional.refresh_from_db()
        self.assertEqual(self.professional.first_name, 'UpdatedName')