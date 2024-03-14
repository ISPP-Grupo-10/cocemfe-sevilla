# tests.py
import uuid

from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase, Client
from django.urls import reverse
from professionals.views import create_professional
from professionals.models import Professional
from professionals.forms import ProfessionalCreationForm, ProfessionalForm
from organizations.models import Organization
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser


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
            is_staff=True,
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
            is_staff = True
        )

        self.professional2 = Professional.objects.create(
            username='testuser2',
            email='testuser2@example.com',
            first_name='Jane',
            last_name='Smith',
            telephone_number='987654321',
            license_number='67890',
            is_staff=True,
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
        self.create_professional_url = reverse('professionals:create_professional')

        self.organization = Organization.objects.create(
            name='Test Organization',
            zip_code='12345'
        )

        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )

        # Log in the user before the tests
        unique_username = f'testuser_{uuid.uuid4().hex[:6]}'

        # Create a new user for authentication
        self.user = get_user_model().objects.create_user(
            username=unique_username,
            password='testpassword',
            email=f'{unique_username}@example.com'
        )

        # Datos válidos para el formulario
        self.valid_form_data = {
            'username': unique_username+"1",
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'telephone_number': '123456789',
            'license_number': 'ABC123',
            'organizations': self.organization.id,
            'profile_picture': '',
        }

        # Datos inválidos para el formulario
        self.invalid_form_data = {
            'username': '',               # Nombre de usuario vacío
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'invalid_email',     # Correo electrónico inválido
            'telephone_number': '12345',  # Número de teléfono demasiado corto
            'license_number': '',         # Número de licencia vacío
            'organizations': '',          # Organización no seleccionada
            'profile_picture':  '',
        }


    def tearDown(self):
        # Delete the user and any related data
        self.user.delete()
        Professional.objects.all().delete()

    def test_valid_professional_creation_form(self):
        form = ProfessionalCreationForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_invalid_professional_creation_form(self):
        form = ProfessionalCreationForm(data=self.invalid_form_data)
        self.assertFalse(form.is_valid())

        '''
            def test_create_professional_view_POST_success(self):
                request = RequestFactory().post('/create_professional/', data=self.valid_form_data)
                request.user = self.user
                response = create_professional(self.valid_form_data, request)
                self.assertEqual(response.status_code, 302)


            def test_create_professional_view_POST_failure(self):
                request = RequestFactory().post('/create_professional/', data=self.invalid_form_data)
                request.user = self.user
                response = create_professional(self.valid_form_data, request)
                professionals_before = Professional.objects.count()
                self.assertEqual(response.status_code, 302)
                professionals_after = Professional.objects.count()
                self.assertEqual(professionals_after, professionals_before)
        '''


class EditUserViewTest(TestCase):
    def setUp(self):
        self.staff_user = get_user_model().objects.create_user(username='staffuser', password='password', is_staff=True)
        self.client = Client()

    def test_edit_user_view_staff(self):
        self.client.login(username='staffuser', password='password')
        professional = Professional.objects.create(username='testuser', first_name='John', last_name='Doe', password='password', telephone_number='123456789', license_number='ABC123', organizations=None, email='test@example.com')
        url = reverse('professional_detail', kwargs={'pk': professional.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        updated_data = {
            'username': 'updateduser',
            'first_name': 'Updated',
            'last_name': 'User',
            'password': 'newpassword',
            'telephone_number': '987654321',
            'license_number': 'XYZ456',
            'organizations': None,
            'email': 'updated@example.com',
        }
        response = self.client.post(url, updated_data, follow=True)
        self.assertRedirects(response, reverse('professional_list') + '?message=Profesional+editado&status=Success')
        updated_professional = Professional.objects.get(id=professional.id)
        self.assertEqual(updated_professional.username, 'updateduser')
        self.assertEqual(updated_professional.first_name, 'Updated')
        self.assertEqual(updated_professional.last_name, 'User')
        self.assertEqual(updated_professional.telephone_number, '987654321')
        self.assertEqual(updated_professional.license_number, 'XYZ456')
        self.assertEqual(updated_professional.email, 'updated@example.com')

    def test_edit_user_view_non_staff(self):
        non_staff_user = get_user_model().objects.create_user(username='nonstaffuser', password='password', is_staff=False)
        self.client.login(username='nonstaffuser', password='password')
        organization = Organization.objects.create(name='Test Organization', zip_code='12345')
        non_staff_user.organizations.add(organization)
        professional = Professional.objects.create(username='testuser', first_name='John', last_name='Doe', password='password', telephone_number='123456789', license_number='ABC123', organizations=organization, email='test@example.com')
        url = reverse('professional_detail', kwargs={'pk': professional.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        updated_data = {
            'telephone_number': '987654321',
            'email': 'updated@example.com',
        }
        response = self.client.post(url, updated_data, follow=True)
        self.assertRedirects(response, reverse('professional_list') + '?message=Profesional+editado&status=Success')
        updated_professional = Professional.objects.get(id=professional.id)
        self.assertEqual(updated_professional.telephone_number, '987654321')
        self.assertEqual(updated_professional.email, 'updated@example.com')
        
    def test_edit_user_view_unauthenticated(self):
        self.client.logout()
        request = self.client.get(reverse('professional_detail', kwargs={'pk': 1}))
        request.user = AnonymousUser()
        professional = Professional.objects.create(username='testuser', first_name='John', last_name='Doe', password='password', telephone_number='123456789', license_number='ABC123', organizations=None, email='test@example.com')
        url = reverse('professional_detail', kwargs={'pk': professional.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_edit_user_view_invalid_data(self):
        self.client.login(username='staffuser', password='password')
        professional = Professional.objects.create(username='testuser', first_name='John', last_name='Doe', password='password', telephone_number='123456789', license_number='ABC123', organizations=None, email='test@example.com')
        url = reverse('professional_detail', kwargs={'pk': professional.id})
        invalid_data = {
            'telephone_number': 'invalid_phone_number',
            'email': 'invalidemail',
        }
        response = self.client.post(url, invalid_data)
        self.assertEqual(response.status_code, 200)
        updated_professional = Professional.objects.get(id=professional.id)
        self.assertNotEqual(updated_professional.telephone_number, 'invalid_phone_number')
        self.assertNotEqual(updated_professional.email, 'invalidemail')