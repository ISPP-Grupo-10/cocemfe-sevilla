# tests.py

from django.utils import timezone
from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from documents.models import Document
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
            terms_accepted=True
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
            'terms_accepted': 'True',
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
            terms_accepted=True
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

class ProfessionalListTestCase(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(
            name='Test Organization',
            telephone_number='123456789',
            address='Test Address',
            email='test@example.com',
            zip_code=12345,
        )

        self.professional1 = Professional.objects.create(
            username='testuser1',
            email='testuser1@example.com',
            first_name='John',
            last_name='Doe',
            telephone_number='123456789',
            license_number='12345',
            organizations=self.organization,
            terms_accepted=True
        )

        self.professional2 = Professional.objects.create(
            username='testuser2',
            email='testuser2@example.com',
            first_name='Jane',
            last_name='Smith',
            telephone_number='987654321',
            license_number='67890',
            organizations=self.organization,
            terms_accepted=True
        )

    def test_professional_list_no_filter(self):
        url = reverse('professional_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['professionals'].order_by('id'),  # Assuming 'id' is the primary key field
            [repr(self.professional1), repr(self.professional2)],
            transform=repr
        )

    def test_professional_list_with_name_filter(self):
        url = reverse('professional_list') + '?name=John'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['professionals'], [repr(self.professional1)], transform=repr)

    def test_professional_list_with_surname_filter(self):
        url = reverse('professional_list') + '?surname=Doe'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['professionals'], [repr(self.professional1)], transform=repr)

    def test_professional_list_with_license_number_filter(self):
        url = reverse('professional_list') + '?license_number=12345'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['professionals'], [repr(self.professional1)], transform=repr)

    def test_professional_list_with_organization_filter(self):
        response = self.client.get(reverse('professional_list') + '?organization=Test Organization')
        self.assertIn(self.professional1, response.context['professionals'])
        self.assertIn(self.professional2, response.context['professionals'])

class ProfessionalChatTestCase(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(
            name='Test Organization',
            telephone_number='123456789',
            address='Test Address',
            email='test@example.com',
            zip_code=12345,
        )

        self.professional1 = Professional.objects.create(
            username='testuser1',
            email='testuser1@example.com',
            first_name='John',
            last_name='Doe',
            telephone_number='123456789',
            license_number='12345',
            organizations=self.organization,
            terms_accepted=True
        )

        self.document1 = Document.objects.create(
            name='Documento de prueba 1',
            suggestion_start_date=timezone.now()+ timedelta(days=10),
            suggestion_end_date=timezone.now() + timedelta(days=30),
            voting_start_date=timezone.now() + timedelta(days=30),
            voting_end_date=timezone.now() + timedelta(days=60),
            ubication='Ubicación de prueba',
            status='Cerrado'
        )

        self.document2 = Document.objects.create(
            name='Documento de prueba 2',
            suggestion_start_date=timezone.now()+ timedelta(days=10),
            suggestion_end_date=timezone.now() + timedelta(days=30),
            voting_start_date=timezone.now() + timedelta(days=30),
            voting_end_date=timezone.now() + timedelta(days=60),
            ubication='Ubicación de prueba',
            status='Cerrado'
        )

        self.document3 = Document.objects.create(
            name='Documento de prueba 3',
            suggestion_start_date=timezone.now()+ timedelta(days=10),
            suggestion_end_date=timezone.now() + timedelta(days=30),
            voting_start_date=timezone.now() + timedelta(days=30),
            voting_end_date=timezone.now() + timedelta(days=60),
            ubication='Ubicación de prueba',
            status='Cerrado'
        )
        self.document1.professionals.add(self.professional1)
        self.document3.professionals.add(self.professional1)

    def test_professional_list_documents(self):
        self.client.force_login(self.professional1)
        url = "/professionals/chats/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Documento de prueba 1')
        self.assertContains(response, 'Documento de prueba 3')
        self.assertNotContains(response, 'Documento de prueba 2')
