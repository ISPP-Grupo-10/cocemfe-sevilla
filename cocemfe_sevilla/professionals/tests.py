# tests.py

from django.test import TestCase, Client
from django.urls import reverse
from professionals.models import Professional
from professionals.forms import ProfessionalCreationForm, ProfessionalForm
from organizations.models import Organization
from django.core.files.uploadedfile import SimpleUploadedFile

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
            'username': 'testuser',
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
        self.assertEqual(len(form.errors), 4)


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
            organizations=self.organization
        )

        self.professional2 = Professional.objects.create(
            username='testuser2',
            email='testuser2@example.com',
            first_name='Jane',
            last_name='Smith',
            telephone_number='987654321',
            license_number='67890',
            organizations=self.organization
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

class ProfessionalCreationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_professional_url = reverse('create_professional')
        
        # Crear una organización con zip_code
        self.organization = Organization.objects.create(
            name='Test Organization',
            zip_code='12345'  # Proporciona un valor para el campo zip_code
        )
        
        # Datos válidos para el formulario
        self.valid_form_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'telephone_number': '123456789',
            'license_number': 'ABC123',
            'organizations': self.organization.id,
            'profile_picture': SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
        }

        # Datos inválidos para el formulario
        self.invalid_form_data = {
            'username': '',  # Nombre de usuario vacío
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'invalid_email',  # Correo electrónico inválido
            'telephone_number': '12345',  # Número de teléfono demasiado corto
            'license_number': '',  # Número de licencia vacío
            'organizations': '',  # Organización no seleccionada
            'profile_picture': SimpleUploadedFile("test_image.txt", b"file_content", content_type="text/plain"),  # Tipo de archivo incorrecto
        }

    def test_create_professional_view_POST_success(self):
        response = self.client.post(self.create_professional_url, self.valid_form_data)

        self.assertRedirects(response, reverse('create_professional'))
        self.assertContains(response, 'Profesional creado exitosamente.')

    def test_create_professional_view_POST_failure(self):
        response = self.client.post(self.create_professional_url, self.invalid_form_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'professional_create.html')
        self.assertIsInstance(response.context['form'], ProfessionalCreationForm)
        self.assertContains(response, 'Error al crear el profesional. Por favor, corrija los errores en el formulario.')

    def test_valid_professional_creation_form(self):
        form = ProfessionalCreationForm(data=self.valid_form_data, files={'profile_picture': self.valid_form_data['profile_picture']})

        self.assertTrue(form.is_valid())

    def test_invalid_professional_creation_form(self):
        form = ProfessionalCreationForm(data=self.invalid_form_data)
        self.assertFalse(form.is_valid())