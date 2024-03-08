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

    def test_create_professional_view_POST_success(self):
        professionals_before = Professional.objects.count()
        request = RequestFactory().post('/create_professional/', data=self.valid_form_data)
        response = create_professional(request, self.valid_form_data)
        self.assertEqual(response.status_code, 200)
        professionals_after = Professional.objects.count()
        self.assertEqual(professionals_after, professionals_before + 1)

    def test_create_professional_view_POST_failure(self):
        request = RequestFactory().post('/create_professional/', data=self.invalid_form_data)
        response = create_professional(request, self.invalid_form_data)
        professionals_before = Professional.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'professional_create.html')
        self.assertIsInstance(response.context['form'], ProfessionalCreationForm)
        professionals_after = Professional.objects.count()
        self.assertEqual(professionals_after, professionals_before)

    def test_valid_professional_creation_form(self):
        form = ProfessionalCreationForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_invalid_professional_creation_form(self):
        form = ProfessionalCreationForm(data=self.invalid_form_data)
        self.assertFalse(form.is_valid())


class EditUserViewTest(TestCase):
    def setUp(self):
        # Crear un usuario de prueba con privilegios de staff para la prueba
        self.staff_user = get_user_model().objects.create_user(username='staffuser', password='password', is_staff=True)
        self.client = Client()

    def test_edit_user_view_staff(self):
        # Simular la autenticación del usuario con privilegios de staff
        self.client.login(username='staffuser', password='password')

        # Crear un profesional de prueba
        professional = Professional.objects.create(username='testuser', first_name='John', last_name='Doe', password='password', telephone_number='123456789', license_number='ABC123', organizations=None, email='test@example.com')

        # Obtener la URL de la vista de edición
        url = reverse('professional_detail', kwargs={'pk': professional.id})

        # Enviar una solicitud GET a la vista
        response = self.client.get(url)

        # Verificar que la respuesta es 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar que el formulario se renderiza correctamente
        self.assertContains(response, 'Editar Usuario')

        # Enviar una solicitud POST para editar el profesional
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

        # Verificar que la redirección fue exitosa
        self.assertRedirects(response, reverse('professional_list') + '?message=Profesional+editado&status=Success')

        # Obtener el profesional actualizado desde la base de datos
        updated_professional = Professional.objects.get(id=professional.id)

        # Verificar que los datos fueron actualizados correctamente
        self.assertEqual(updated_professional.username, 'updateduser')
        self.assertEqual(updated_professional.first_name, 'Updated')
        self.assertEqual(updated_professional.last_name, 'User')
        self.assertEqual(updated_professional.telephone_number, '987654321')
        self.assertEqual(updated_professional.license_number, 'XYZ456')
        self.assertEqual(updated_professional.email, 'updated@example.com')

    def test_edit_user_view_non_staff(self):
        # Crear un usuario de prueba sin privilegios de staff para la prueba
        non_staff_user = get_user_model().objects.create_user(username='nonstaffuser', password='password', is_staff=False)
        self.client.login(username='nonstaffuser', password='password')

        # Crear un profesional de prueba
        professional = Professional.objects.create(username='testuser', first_name='John', last_name='Doe', password='password', telephone_number='123456789', license_number='ABC123', organizations=None, email='test@example.com')

        # Obtener la URL de la vista de edición
        url = reverse('professional_detail', kwargs={'pk': professional.id})

        # Enviar una solicitud GET a la vista
        response = self.client.get(url)

        # Verificar que la respuesta es 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar que el formulario no contiene campos específicos de staff
        self.assertNotContains(response, 'username')
        self.assertNotContains(response, 'first_name')
        self.assertNotContains(response, 'last_name')
        self.assertNotContains(response, 'license_number')
        self.assertNotContains(response, 'organizations')
        self.assertNotContains(response, 'profile_picture')

        # Enviar una solicitud POST con datos de actualización
        updated_data = {
            'telephone_number': '987654321',
            'email': 'updated@example.com',
        }

        response = self.client.post(url, updated_data, follow=True)

        # Verificar que la redirección fue exitosa
        self.assertRedirects(response, reverse('professional_list') + '?message=Profesional+editado&status=Success')

        # Obtener el profesional actualizado desde la base de datos
        updated_professional = Professional.objects.get(id=professional.id)

        # Verificar que los datos fueron actualizados correctamente
        self.assertEqual(updated_professional.telephone_number, '987654321')
        self.assertEqual(updated_professional.email, 'updated@example.com')

    def test_edit_user_view_unauthenticated(self):
        # Crear un profesional de prueba
        professional = Professional.objects.create(username='testuser', first_name='John', last_name='Doe', password='password', telephone_number='123456789', license_number='ABC123', organizations=None, email='test@example.com')

        # Obtener la URL de la vista de edición
        url = reverse('professional_detail', kwargs={'pk': professional.id})

        # Enviar una solicitud GET a la vista sin autenticación
        response = self.client.get(url)

        # Verificar que la respuesta es 302 (redirección a la página de inicio de sesión)
        self.assertEqual(response.status_code, 302)
        # Verificar que el usuario es redirigido a la página de inicio de sesión
        self.assertRedirects(response, '/accounts/login/')

    def test_edit_user_view_invalid_data(self):
        # Simular la autenticación del usuario con privilegios de staff
        self.client.login(username='staffuser', password='password')

        # Crear un profesional de prueba
        professional = Professional.objects.create(username='testuser', first_name='John', last_name='Doe', password='password', telephone_number='123456789', license_number='ABC123', organizations=None, email='test@example.com')

        # Obtener la URL de la vista de edición
        url = reverse('professional_detail', kwargs={'pk': professional.id})

        # Enviar una solicitud POST con datos inválidos
        invalid_data = {
            'telephone_number': 'invalid_phone_number',
            'email': 'invalidemail',
        }

        response = self.client.post(url, invalid_data)

        # Verificar que la respuesta es 200 (OK) porque el formulario es inválido
        self.assertEqual(response.status_code, 200)
        # Verificar que el formulario contiene mensajes de error
        self.assertContains(response, 'Enter a valid phone number.')
        self.assertContains(response, 'Enter a valid email address.')

        # Verificar que los datos no se han actualizado en la base de datos
        updated_professional = Professional.objects.get(id=professional.id)
        self.assertNotEqual(updated_professional.telephone_number, 'invalid_phone_number')
        self.assertNotEqual(updated_professional.email, 'invalidemail')