from django.test import TestCase
from django.urls import reverse
from documents.models import Document, valid_location
from professionals.models import Professional
from django.utils import timezone
from datetime import timedelta
from organizations.models import Organization
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.translation import gettext as _  
class DocumentTestCase(TestCase):
    def setUp(self):
        # Creamos una organización
        self.user = Professional.objects.create_superuser(username='admin', password='admin', terms_accepted=True)
        self.pdf_file = SimpleUploadedFile("test.pdf", b"file_content", content_type="application/pdf")

        self.organization = Organization.objects.create(
            name='Mi Organización',
            telephone_number='123456789',
            address='Dirección de la organización',
            email='info@miorganizacion.com',
            zip_code=12345
        )

        # Creamos un profesional asignado a la organización
        self.professional = Professional.objects.create(
            first_name='Juan',
            last_name='Pérez',
            username='juanperez',
            telephone_number='987654321',
            license_number='Licencia del profesional',
            organizations=self.organization,
            terms_accepted=True
        )
        
        # Creamos un documento asignado al profesional
        self.document = Document.objects.create(
            name='Documento de prueba',
            suggestion_start_date=timezone.now()+ timedelta(days=10),
            suggestion_end_date=timezone.now() + timedelta(days=30),
            voting_start_date=timezone.now() + timedelta(days=30),
            voting_end_date=timezone.now() + timedelta(days=60),
            ubication='Sevilla',
            status='Cerrado',
            pdf_file=self.pdf_file
        )
        self.document.professionals.add(self.professional)

        self.client.login(username='admin', password='admin')

    def test_list_pdf_view(self):
        response = self.client.get(reverse('list_pdf'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.document.name)

    def test_view_pdf_admin_as_admin(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('view_pdf_admin', kwargs={'pk': self.document.pk}))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_pdf.html')
        self.assertContains(response, self.document.name)
        self.assertContains(response, self.document.ubication)
        self.assertContains(response, self.document.status)

    def test_view_pdf_admin_invalid_pk(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('view_pdf_admin', args=[1000]))
        self.assertEqual(response.status_code, 404)

    def test_redirection_from_list_pdf_to_view_pdf_admin(self):
        list_pdf_url = reverse('list_pdf')
        response = self.client.get(list_pdf_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.document.name)

        view_pdf_admin_url = reverse('view_pdf_admin', args=[self.document.pk])

        response = self.client.get(view_pdf_admin_url)
        self.assertEqual(response.status_code, 200)

    def test_filter_documents_by_name(self):
        response = self.client.get(reverse('list_pdf'), {'name': 'prueba'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.document.name)

    def test_filter_documents_by_status(self):
        response = self.client.get(reverse('list_pdf'), {'status': 'Cerrado'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.document.name)

    def test_filter_documents_by_suggestion_start_date(self):
        suggestion_start_date = self.document.suggestion_start_date
        response = self.client.get(reverse('list_pdf'), {'suggestion_start_date': suggestion_start_date})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.document.name)
    '''
    def test_upload_pdf_valid_form(self):
        self.client.login(username='admin', password='admin')

        data = {
            'name': 'Documento de prueba',
            'ubication': 'Sevilla', 
            'status': 'Borrador',
            'suggestion_start_date': self.document.suggestion_start_date,
            'suggestion_end_date': self.document.suggestion_end_date,
            'voting_end_date':self.document.voting_end_date,
            'pdf_file': self.pdf_file, 
        }
        url = reverse('upload_pdf')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Document.objects.count(), 2)  
    '''

    def test_upload_pdf_invalid_form(self):
        self.client.login(username='admin', password='admin')
        data = {
            'suggestion_start_date': timezone.now().date(),
            'name': 'Documento de prueba',
            'ubication': 'Sevilla',  
            'status': 'Abierto',  
            'suggestion_end_date': '01/01/2021',
            'pdf_file': self.pdf_file,
            'professionals': [1],
        }
        url=reverse('upload_pdf')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(Document.objects.count(), 1) 
        self.client.logout()

    '''
    def test_upload_pdf_not_superuser(self):
        self.client.logout()
        url=reverse('upload_pdf')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '403.html')
    '''
    '''
    def test_modify_pdf_add_professional(self):
        self.client.login(username='admin', password='admin')

        new_professional = Professional.objects.create(
            first_name='Pedro',
            last_name='González',
            username='pedrogonzalez',
            telephone_number='987654321',
            license_number='Licencia del nuevo profesional',
            organizations=self.organization
        )

        self.assertIsNotNone(new_professional)

        self.assertEqual(self.document.professionals.count(), 1)

        modify_pdf_url = reverse('update_pdf', args=[self.document.pk])

        new_name = 'Documento modificado con nuevo profesional'
        new_suggestion_end_date = timezone.now().date() + timedelta(days=15)
        new_voting_end_date = timezone.now().date() + timedelta(days=65) 
        new_professional_id = new_professional.id

        response = self.client.post(modify_pdf_url, {
            'name': new_name,
            'status': 'Borrador',            
            'suggestion_end_date': new_suggestion_end_date,
            'voting_end_date':new_voting_end_date,
            'professionals': [self.professional.id, new_professional_id],
            'pdf_file': self.pdf_file,
            'ubication': 'Sevilla',  
        })
        self.assertEqual(response.status_code, 302) 


        modified_document = Document.objects.get(pk=self.document.pk)

        self.assertEqual(modified_document.name, new_name)
        self.assertEqual(modified_document.professionals.count(), 2) 
        self.assertIn(self.professional, modified_document.professionals.all()) 
        self.assertIn(new_professional, modified_document.professionals.all()) 
    '''
    def test_delete_pdf(self):
        self.client.login(username='admin', password='admin')

        delete_pdf_url = reverse('delete_pdf', args=[self.document.pk])

        initial_count = Document.objects.count()

        response = self.client.post(delete_pdf_url)

        self.assertRedirects(response, reverse('list_pdf'))

        self.assertEqual(Document.objects.count(), initial_count - 1)

        with self.assertRaises(Document.DoesNotExist):
            Document.objects.get(pk=self.document.pk)

    def test_modify_pdf_with_invalid_suggestion_end_date(self):
        self.client.login(username='admin', password='admin')

        modify_pdf_url = reverse('update_pdf', args=[self.document.pk])


        invalid_suggestion_end_date = timezone.now().date() - timedelta(days=15)  
        new_voting_end_date = timezone.now().date() + timedelta(days=65) 
        
        response = self.client.post(modify_pdf_url, {
            'name': self.document.name,
            'status': 'Borrador',            
            'suggestion_end_date': invalid_suggestion_end_date,
            'voting_end_date':new_voting_end_date,
            'professionals': [self.professional.id],
        })

        self.assertEqual(response.status_code, 200)

        modified_document = Document.objects.get(pk=self.document.pk)
        self.assertNotEqual(modified_document.suggestion_end_date, invalid_suggestion_end_date)

        self.assertFormError(response, 'form', 'suggestion_end_date', ('La fecha de fin de sugerencia no puede ser anterior a la fecha actual.'))

    '''
    def test_modify_pdf_with_valid_data(self):
        self.client.login(username='admin', password='admin')

        modify_pdf_url = reverse('update_pdf', args=[self.document.pk])

        new_name = 'Documento modificado con datos validos'
        new_suggestion_end_date = timezone.now().date() + timedelta(days=20)
        new_voting_end_date = timezone.now().date() + timedelta(days=65) 

        response = self.client.post(modify_pdf_url, {
            'name': new_name,
            'status': 'Borrador',            
            'suggestion_end_date': new_suggestion_end_date,
            'voting_end_date':new_voting_end_date,
            'professionals': [self.professional.id],
            'pdf_file': self.pdf_file,
            'ubication': 'Sevilla', 
         })


        self.assertEqual(response.status_code, 302)

        modified_document = Document.objects.get(pk=self.document.pk)
        modified_suggestion_end_date = timezone.localtime(modified_document.suggestion_end_date).date()

        self.assertEqual(modified_document.name, new_name)
        self.assertEqual(modified_suggestion_end_date, new_suggestion_end_date)
    '''
class GetCoordinatesOpenStreetMapTestCase(TestCase):
    
    def test_get_coordinates_openstreetmap(self):
        city = 'Seville'
        self.assertTrue(valid_location(city))
    
    def test_get_coordinates_openstreetmap_not_exist(self):
        city = 'ADFASDJIV'
        self.assertFalse(valid_location(city))