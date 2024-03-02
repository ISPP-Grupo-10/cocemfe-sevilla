# tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Professional
from .forms import ProfessionalForm

class ProfessionalModelTest(TestCase):
    def setUp(self):
        self.professional = Professional.objects.create(
            username='testuser',
            name='John',
            surname='Doe',
            telephone_number='123456789',
            license_number='ABC123',
        )

    def test_professional_str(self):
        self.assertEqual(str(self.professional), 'testuser')

class ProfessionalFormTest(TestCase):
    def test_valid_professional_form(self):
        form_data = {
            'username': 'testuser',
            'name': 'John',
            'surname': 'Doe',
            'telephone_number': '123456789',
            'license_number': 'ABC123',
        }
        form = ProfessionalForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_professional_form(self):
        form_data = {}  # Deja campos requeridos en blanco para probar la invalidación
        form = ProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)  # Asegúrate de que haya 5 errores, uno por cada campo requerido

class ProfessionalViewTest(TestCase):
    def setUp(self):
        self.professional = Professional.objects.create(
            username='testuser',
            name='John',
            surname='Doe',
            telephone_number='123456789',
            license_number='ABC123',
        )

    def test_professional_detail_view(self):
        url = reverse('professional_detail', kwargs={'pk': self.professional.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John')  # Ajusta esto según la información que esperas en la vista

    def test_professional_update_view(self):
        url = reverse('professional_edit', kwargs={'pk': self.professional.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        updated_data = {
            'name': 'UpdatedName',
            'surname': 'UpdatedSurname',
            'telephone_number': '987654321',
            'license_number': 'XYZ789',
        }

        response = self.client.post(url, updated_data)
        self.assertEqual(response.status_code, 302)  # 302 es el código para redirección después de una actualización
        self.professional.refresh_from_db()
        self.assertEqual(self.professional.name, 'UpdatedName')


class ProfessionalListTestCase(TestCase):
    def setUp(self):
        self.professional1 = Professional.objects.create(name='John', surname='Doe', license_number='12345', organizations__name='Org1')
        self.professional2 = Professional.objects.create(name='Jane', surname='Smith', license_number='67890', organizations__name='Org2')

    def test_professional_list_no_filter(self):
        response = self.client.get(reverse('professional_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['professionals'], [repr(self.professional1), repr(self.professional2)])

    def test_professional_list_with_name_filter(self):
        response = self.client.get(reverse('professional_list') + '?name=John')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['professionals'], [repr(self.professional1)])

    def test_professional_list_with_organization_filter(self):
        response = self.client.get(reverse('professional_list') + '?organization=Org2')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['professionals'], [repr(self.professional2)])
