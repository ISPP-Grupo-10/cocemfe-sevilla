# tests.py
import uuid
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase, Client
from django.urls import reverse
from django.utils import timezone

from documents.models import Document
from organizations.models import Organization
from professionals.forms import ProfessionalCreationForm, SecurePasswordChangeForm
from professionals.models import Professional
from professionals.views import create_professional


"""
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
        self.admin_user = Professional.objects.create_superuser(
            username='admin',
            email='admin@admin.com',
            password='admin1234',
            terms_accepted=True,
            is_staff=True
        )
        self.client.login(username='admin', password='admin1234')

    def test_professional_detail_view(self):
        self.assertTrue('_auth_user_id' in self.client.session)
        url = reverse('professionals:professional_detail', kwargs={'pk': self.professional.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John')
"""

'''
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

        self.admin_user = Professional.objects.create_superuser(
            username='admin',
            email='admin@admin.com',
            password='admin1234',
            terms_accepted=True,
            is_staff=True
        )
        self.client.login(username='admin', password='admin1234')

    def test_professional_list_no_filter(self):
        self.assertTrue('_auth_user_id' in self.client.session)
        url = reverse('professionals:professional_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['professionals'].order_by('id'),
            [repr(self.professional1), repr(self.professional2)],
            transform=repr
        )

    def test_professional_list_with_name_filter(self):
        self.assertTrue('_auth_user_id' in self.client.session)
        url = reverse('professionals:professional_list') + '?name=John&surname=&license_number=&organization='
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.professional1)
        self.assertQuerysetEqual(response.context['professionals'], [repr(self.professional1)], transform=repr)

    def test_professional_list_with_surname_filter(self):
        self.assertTrue('_auth_user_id' in self.client.session)
        url = reverse('professionals:professional_list') + '?surname=Doe'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.professional1)
        self.assertQuerysetEqual(response.context['professionals'], [repr(self.professional1)], transform=repr)

    def test_professional_list_with_license_number_filter(self):
        self.assertTrue('_auth_user_id' in self.client.session)
        url = reverse('professionals:professional_list') + '?license_number=12345'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.professional1)
        self.assertQuerysetEqual(response.context['professionals'], [repr(self.professional1)], transform=repr)

    def test_professional_list_with_organization_filter(self):
        self.assertTrue('_auth_user_id' in self.client.session)
        response = self.client.get(reverse('professionals:professional_list') + '?organization=Test Organization')
        self.assertIn(self.professional1, response.context['professionals'])
        self.assertIn(self.professional2, response.context['professionals'])
'''

'''
class ProfessionalChatTestCase(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(
            name='Mi Organización',
            telephone_number='123456789',
            address='Dirección de la organización',
            email='info@miorganizacion.com',
            zip_code=12345
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
            suggestion_start_date=timezone.now() + timedelta(days=10),
            suggestion_end_date=timezone.now() + timedelta(days=30),
            voting_start_date=timezone.now() + timedelta(days=30),
            voting_end_date=timezone.now() + timedelta(days=60),
            ubication='Ubicación de prueba',
            status='Cerrado'
        )

        self.document3 = Document.objects.create(
            name='Documento de prueba 3',
            suggestion_start_date=timezone.now() + timedelta(days=10),
            suggestion_end_date=timezone.now() + timedelta(days=30),
            voting_start_date=timezone.now() + timedelta(days=30),
            voting_end_date=timezone.now() + timedelta(days=60),
            ubication='Ubicación de prueba',
            status='Cerrado'
        )
        self.document1.professionals.add(self.professional1)
        self.document3.professionals.add(self.professional1)

        self.admin_user = Professional.objects.create_superuser(
            username='admin',
            email='admin@admin.com',
            password='admin1234',
            terms_accepted=True,
            is_staff=True
        )
        self.client.login(username='admin', password='admin1234')

    def test_professional_list_documents(self):
        self.client.force_login(self.professional1)
        url = "/professionals/chats/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Documento de prueba 1')
        self.assertContains(response, 'Documento de prueba 3')
        self.assertNotContains(response, 'Documento de prueba 2')
'''

'''
class ProfessionalCreationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_professional_url = reverse('professionals:create_professional')

        self.organization = Organization.objects.create(
            name='Test Organization',
            zip_code='12345'
        )

        # Create a new user for authentication
        unique_username = f'testuser_{uuid.uuid4().hex[:6]}'
        self.user = get_user_model().objects.create_superuser(
            username=unique_username,
            password='testpassword',
            email=f'{unique_username}@example.com'
        )

        # Datos válidos para el formulario
        self.valid_form_data = {
            'username': unique_username + "1",
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
            'username': '',  # Nombre de usuario vacío

            'first_name': 'Test',
            'last_name': 'User',
            'email': 'invalid_email',  # Correo electrónico inválido
            'telephone_number': '12345',  # Número de teléfono demasiado corto
            'license_number': '',  # Número de licencia vacío
            'organizations': '',  # Organización no seleccionada
            'profile_picture': '',
        }

        self.admin_user = Professional.objects.create_superuser(
            username='admin',
            email='admin@admin.com',
            password='admin1234',
            terms_accepted=True,
            is_staff=True
        )
        self.client.login(username='admin', password='admin1234')

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

    def test_create_professional_view_POST_success(self):
        request = RequestFactory().post(self.create_professional_url, data=self.valid_form_data)
        request.user = self.user
        professionals_before = Professional.objects.count()
        response = create_professional(request)
        self.assertEqual(response.status_code, 302)
        redirect_url = response.url
        response = self.client.get(redirect_url)
        self.assertEqual(response.status_code, 200)
        professionals_after = Professional.objects.count()
        self.assertEqual(professionals_after, professionals_before + 1)

    def test_create_professional_view_POST_failure(self):
        request = RequestFactory().post(self.create_professional_url, data=self.invalid_form_data)
        request.user = self.user
        response = create_professional(request)
        professionals_before = Professional.objects.count()
        self.assertEqual(response.status_code, 200)
        professionals_after = Professional.objects.count()
        self.assertEqual(professionals_after, professionals_before)
'''


class EditUserViewTestCase(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(name='Org1', telephone_number='123456789',
                                                        address='Address1', email='org1@example.com',
                                                        zip_code='12345')
        self.professional_staff = Professional.objects.create(username='staff_user', is_staff=True,
                                                              telephone_number='123456789', license_number='ABC123',
                                                              organizations=self.organization)
        self.professional_normal = Professional.objects.create(username='normal_user',
                                                               telephone_number='987654321',
                                                               license_number='XYZ789')

    def tearDown(self):
        Organization.objects.all().delete()
        Professional.objects.all().delete()

    def test_get_edit_page(self):
        self.client.force_login(self.professional_staff)
        response = self.client.get(
            reverse('professionals:professional_detail', kwargs={'pk': self.professional_staff.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'professional_detail.html')
        self.assertTrue('form' in response.context)
        self.assertTrue('professional' in response.context)

    def test_post_edit_page_as_staff(self):
        self.client.force_login(self.professional_staff)
        data = {
            'username': 'testuser_new',
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'test_updated@example.com',
            'telephone_number': '987654322',
            'license_number': 'XYZ789',
            'organizations': self.organization.pk
        }
        response = self.client.post(
            reverse('professionals:professional_detail', kwargs={'pk': self.professional_staff.pk}), data)
        
        
        self.assertEqual(response.status_code, 302)
        self.professional_staff.refresh_from_db()
        self.assertEqual(self.professional_staff.username, 'testuser_new')
        self.assertEqual(self.professional_staff.first_name, 'Updated')
        self.assertEqual(self.professional_staff.email, 'test_updated@example.com')

    def test_post_edit_page_as_normal_user(self):
        self.client.force_login(self.professional_normal)
        data = {
            'username': 'testusernormal_new',
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'test_updated@example.com',
            'telephone_number': '987654321',
            'license_number': 'XYZ789',
            'organizations': self.organization.pk
        }
        response = self.client.post(
            reverse('professionals:professional_detail', kwargs={'pk': self.professional_normal.pk}), data)
        
        self.assertEqual(response.status_code, 302)
        self.professional_normal.refresh_from_db()
        print('-----------------------', self.professional_normal.email)
        
        self.assertEqual(self.professional_normal.telephone_number, '987654321')
        self.assertEqual(self.professional_normal.email, 'test_updated@example.com')


    def test_edit_user_view_unauthenticated(self):
        self.client.logout()
        professional = Professional.objects.create(username='testuser', first_name='John', last_name='Doe',
                                                   password='password', telephone_number='123456789',
                                                   license_number='ABC123', organizations=None,
                                                   email='test@example.com')
        url = reverse('professionals:professional_detail', kwargs={'pk': professional.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class ProfessionalDataViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.organization = Organization.objects.create(name='Org1', telephone_number='123456789',
                                                        address='Address1', email='org1@example.com',
                                                        zip_code='12345')

        self.professional_staff = Professional.objects.create(username='staff_user', is_staff=True,
                                                                telephone_number='123456789', license_number='ABC123',
                                                                terms_accepted=True, organizations=self.organization)
        self.professional_normal = Professional.objects.create(username='normal_user',
                                                                telephone_number='987654321',
                                                                terms_accepted=True, license_number='XYZ789')


    def test_view_raises_403_for_unauthorized_user(self):
        unauthorized_user = Professional.objects.create(username='unauthorizeduser',
                                                        telephone_number='111111111',
                                                        license_number='DEF456',
                                                        terms_accepted=True
                                                        )
        self.client.force_login(unauthorized_user)
        response = self.client.get(reverse('professionals:professional_data',
                                        kwargs={'professional_id': self.professional_staff.pk}))
        self.assertEqual(response.status_code, 403)

    def test_view_redirects_for_non_authenticated_user(self):
        response = self.client.get(reverse('professionals:professional_data', kwargs={'professional_id': self.professional_normal.pk}))
        self.assertEqual(response.status_code, 302)


class PasswordChangeFormTests(TestCase):
    def setUp(self):
        self.user = Professional.objects.create_user(username='testuser', email='test@example.com', password='old_password', terms_accepted=True)

    def test_change_password_page_rendered_correctly(self):
        self.client.login(username='testuser', password='old_password')
        response = self.client.get(reverse('professionals:update_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_password.html')

    def test_change_password_with_correct_data(self):
        self.client.login(username='testuser', password='old_password')
        response = self.client.post(reverse('professionals:update_password'), {
            'old_password': 'old_password',
            'new_password1': 'New_Password123',
            'new_password2': 'New_Password123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Professional.objects.get(username='testuser').check_password('New_Password123'))

    def test_change_password_with_wrong_old_password(self):
        self.client.login(username='testuser', password='old_password')
        response = self.client.post(reverse('professionals:update_password'), {
            'old_password': 'wrong_password',
            'new_password1': 'New_Password123',
            'new_password2': 'New_Password123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Professional.objects.get(username='testuser').check_password('New_Password123'))

    def test_weak_password_password_not_changed(self):
        self.client.login(username='testuser', password='old_password')
        response = self.client.post(reverse('professionals:update_password'), {
            'old_password': 'old_password',
            'new_password1': 'weak',
            'new_password2': 'weak',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Professional.objects.get(username='testuser').check_password('weak'))

    def test_passwords_not_matching_password_not_changed(self):
        self.client.login(username='testuser', password='old_password')
        response = self.client.post(reverse('professionals:update_password'), {
            'old_password': 'old_password',
            'new_password1': 'New_Password123',
            'new_password2': 'Mismatched_Password123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Professional.objects.get(username='testuser').check_password('old_password'))

    def test_empty_data_password_not_changed(self):
        self.client.login(username='testuser', password='old_password')
        response = self.client.post(reverse('professionals:update_password'), {
            'old_password': '',
            'new_password1': '',
            'new_password2': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Professional.objects.get(username='testuser').check_password('old_password'))

    def test_same_old_and_new_password_password_not_changed(self):
        self.client.login(username='testuser', password='old_password')
        response = self.client.post(reverse('professionals:update_password'), {
            'old_password': 'old_password',
            'new_password1': 'old_password',
            'new_password2': 'old_password',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Professional.objects.get(username='testuser').check_password('old_password'))

    def test_new_password_not_meeting_security_policies_password_not_changed(self):
        self.client.login(username='testuser', password='old_password')
        response = self.client.post(reverse('professionals:update_password'), {
            'old_password': 'old_password',
            'new_password1': 'weakpassword',
            'new_password2': 'weakpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Professional.objects.get(username='testuser').check_password('old_password'))

    def test_invalid_data_in_password_fields_password_not_changed(self):
        self.client.login(username='testuser', password='old_password')
        response = self.client.post(reverse('professionals:update_password'), {
            'old_password': 'old_password',
            'new_password1': 'invalid*password',
            'new_password2': 'invalid*password',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Professional.objects.get(username='testuser').check_password('old_password'))

    def test_unauthenticated_user_password_not_changed(self):
        response = self.client.get(reverse('professionals:update_password'))
        self.assertEqual(response.status_code, 302)

    def test_password_strength_validation_no_uppercase(self):
        self.client.login(username='testuser', password='old_password')
        form = SecurePasswordChangeForm(user=self.user, data={
            'old_password': 'old_password',
            'new_password1': 'new_password123',
            'new_password2': 'new_password123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('new_password1', form.errors)
        self.assertEquals(form.errors['new_password1'], ['La contraseña debe contener al menos una letra mayúscula.'])

    def test_password_strength_validation_no_lowercase(self):
        self.client.login(username='testuser', password='old_password')
        form = SecurePasswordChangeForm(user=self.user, data={
            'old_password': 'old_password',
            'new_password1': 'NEW_PASSWORD123',
            'new_password2': 'NEW_PASSWORD123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('new_password1', form.errors)
        self.assertEquals(form.errors['new_password1'], ['La contraseña debe contener al menos una letra minúscula.'])

    def test_password_strength_validation_short(self):
        self.client.login(username='testuser', password='old_password')
        form = SecurePasswordChangeForm(user=self.user, data={
            'old_password': 'old_password',
            'new_password1': 'Short_123',
            'new_password2': 'Short_123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('new_password1', form.errors)
        self.assertEquals(form.errors['new_password1'], ['La contraseña debe tener al menos 12 caracteres.'])

    def test_password_strength_validation_no_digits(self):
        self.client.login(username='testuser', password='old_password')
        form = SecurePasswordChangeForm(user=self.user, data={
            'old_password': 'old_password',
            'new_password1': 'New_Password!!!',
            'new_password2': 'New_Password!!!',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('new_password1', form.errors)
        self.assertEquals(form.errors['new_password1'], ['La contraseña debe contener al menos un dígito.'])

    def test_password_strength_validation_no_special_character(self):
        self.client.login(username='testuser', password='old_password')
        form = SecurePasswordChangeForm(user=self.user, data={
            'old_password': 'old_password',
            'new_password1': 'NewPassword12345',
            'new_password2': 'NewPassword12345',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('new_password1', form.errors)
        self.assertEquals(form.errors['new_password1'], ['La contraseña debe contener al menos un carácter especial.'])

    def test_password_matching_validation(self):
        self.client.login(username='testuser', password='old_password')
        form = SecurePasswordChangeForm(user=self.user, data={
            'old_password': 'old_password',
            'new_password1': 'New_Password123',
            'new_password2': 'Mismatched_Password123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)
        self.assertEqual(form.errors['__all__'], ['Las contraseñas nuevas no coinciden.'])

    def test_blank_data_validation(self):
        self.client.login(username='testuser', password='old_password')
        form = SecurePasswordChangeForm(user=self.user, data={})
        self.assertFalse(form.is_valid())
        self.assertIn('old_password', form.errors)
        self.assertIn('new_password1', form.errors)
        self.assertIn('new_password2', form.errors)
        self.assertEqual(form.errors['old_password'], ['Este campo es obligatorio.'])
        self.assertEqual(form.errors['new_password1'], ['Este campo es obligatorio.'])
        self.assertEqual(form.errors['new_password2'], ['Este campo es obligatorio.'])

    def test_password_change_success(self):
        self.client.login(username='testuser', password='old_password')
        form = SecurePasswordChangeForm(user=self.user, data={
            'old_password': 'old_password',
            'new_password1': 'New_Password123',
            'new_password2': 'New_Password123',
        })
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertTrue(user.check_password('New_Password123'))
