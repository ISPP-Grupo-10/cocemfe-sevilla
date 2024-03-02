from django.test import TestCase
from django.urls import reverse
from documents.models import Document
from professionals.models import Professional
from django.utils import timezone
from organizations.models import Organization
from django.test import RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile

class DocumentTestCase(TestCase):
    def setUp(self):
        # Creamos una organización
        self.user = Professional.objects.create_superuser(username='admin', password='admin')
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
            organizations=self.organization
        )
        
        # Creamos un documento asignado al profesional
        self.document = Document.objects.create(
            name='Documento de prueba',
            start_date='2024-03-01',
            end_date='2024-04-01',
            ubication='Ubicación de prueba',
            status='Cerrado'
        )
        self.document.professionals.add(self.professional)

        
    def test_list_pdf_view(self):
        # Verificar que la vista list_pdf muestra correctamente el documento creado
        response = self.client.get(reverse('list_pdf'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.document.name)

    def test_view_pdf_admin(self):
        # Verificar que la vista view_pdf_admin muestra correctamente los detalles del documento
        response = self.client.get(reverse('view_pdf_admin', args=[self.document.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.document.name)
        self.assertContains(response, self.document.ubication)
        self.assertTrue(self.document.status == 'Cerrado')

    def test_view_pdf_admin_invalid_pk(self):
        # Verificar que se maneja correctamente un ID de documento no válido en la vista view_pdf_admin
        response = self.client.get(reverse('view_pdf_admin', args=[1000]))  # Assuming 1000 is an invalid pk
        self.assertEqual(response.status_code, 404)

    def test_redirection_from_list_pdf_to_view_pdf_admin(self):
        # Verificar que hacer clic en el nombre del documento en list_pdf redirige a view_pdf_admin
        list_pdf_url = reverse('list_pdf')
        response = self.client.get(list_pdf_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.document.name)

        # Obtener la URL de la vista view_pdf_admin para el documento actual
        view_pdf_admin_url = reverse('view_pdf_admin', args=[self.document.pk])

        # Simular hacer clic en el enlace del documento para redirigir a view_pdf_admin
        response = self.client.get(view_pdf_admin_url)
        self.assertEqual(response.status_code, 200)
        # Puedes agregar más aserciones aquí para verificar otros detalles del documento o la redirección

    def test_filter_documents_by_name(self):
        # Verificar que los documentos se filtran correctamente por nombre
        response = self.client.get(reverse('list_pdf'), {'name': 'prueba'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.document.name)

    def test_filter_documents_by_status(self):
        # Verificar que los documentos se filtran correctamente por estado
        response = self.client.get(reverse('list_pdf'), {'status': 'Cerrado'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.document.name)

    def test_filter_documents_by_start_date(self):
        # Verificar que los documentos se filtran correctamente por fecha de inicio
        response = self.client.get(reverse('list_pdf'), {'start_date': '2024-03-01'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.document.name)


    def test_upload_pdf_valid_form(self):
        self.client.login(username='admin', password='admin')
        data = {
            'start_date': '02/03/2024',  # Current date
            'name': 'Documento de prueba',
            'ubication': 'Ubicación de prueba',  # 'ubication' is a typo, should be 'location
            'status': 'Abierto',  # 'status' is a typo, should be 'status
            'end_date': '30/03/2024',
            'pdf_file': self.pdf_file,
            'professionals': [1],
        }
        url=reverse('upload_pdf')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Check if redirecting to 'list_pdf' page
        self.assertEqual(Document.objects.count(), 2)  # Check if document is created
        document = Document.objects.last()
        self.assertEqual(document.start_date, timezone.now().date())  # Check if start_date is set to current date
        self.assertEqual(document.status, 'Abierto')  # Check if status is set to 'Abierto'
        self.assertEqual(list(document.professionals.values_list('id', flat=True)), [1])  # Check if professionals are set correctly
        self.client.logout()

    def test_upload_pdf_invalid_form(self):
        self.client.login(username='admin', password='admin')
        data = {
            'start_date': timezone.now().date(),
            'name': 'Documento de prueba',
            'ubication': 'Ubicación de prueba',  
            'status': 'Abierto',  
            'end_date': '01/01/2021',
            'pdf_file': self.pdf_file,
            'professionals': [1],
        }
        url=reverse('upload_pdf')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)  # Check if form is not valid and returns to the same page
        self.assertEqual(Document.objects.count(), 1)  # Check if document is not created
        self.client.logout()
    
    def test_upload_pdf_not_superuser(self):
        self.client.logout()
        url=reverse('upload_pdf')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Check if non-superuser gets redirected to '403.html' page
        self.assertTemplateUsed(response, '403.html')
