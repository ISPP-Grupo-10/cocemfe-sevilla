from django.test import TestCase
from django.urls import reverse
from documents.models import Document
from professionals.models import Professional
from django.utils import timezone
from datetime import timedelta
from organizations.models import Organization
from django.test import RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
from pathlib import Path
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
            suggestion_start_date=timezone.now()+ timedelta(days=10),
            suggestion_end_date=timezone.now() + timedelta(days=30),
            voting_start_date=timezone.now() + timedelta(days=30),
            voting_end_date=timezone.now() + timedelta(days=60),
            ubication='Ubicación de prueba',
            status='Cerrado'
        )
        self.document.professionals.add(self.professional)

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

    def test_upload_pdf_valid_form(self):
        self.client.login(username='admin', password='admin')
        # Obtén la ruta absoluta del archivo PDF
        pdf_path = Path(__file__).resolve().parent.parent / 'media' / 'pdfs' / 'Jaime_García_García_-_Compromiso_de_Participación_en_la_asignatura_ISPP_v1.3.pdf'
        
        # Verifica si el archivo PDF existe
        if pdf_path.exists():
            # Lee el contenido del archivo PDF
            with open(pdf_path, 'rb') as f:
                pdf_file = f.read()
        else:
            raise FileNotFoundError(f"No se encontró el archivo PDF en la ruta: {pdf_path}")

        data = {
            'name': 'Documento de prueba',
            'ubication': 'Ubicación de prueba',  # Corregido el nombre del campo
            'suggestion_start_date': self.document.suggestion_start_date,
            'suggestion_end_date': self.document.suggestion_end_date,
            'voting_start_date' :self.document.voting_start_date,
            'voting_end_date':self.document.voting_end_date,
            'pdf_file': pdf_file, 
        }
        url = reverse('upload_pdf')
        response = self.client.post(url, data)
        print(response.content) 
        self.assertEqual(response.status_code, 302)  # Verifica si se redirecciona a la página 'list_pdf'
        self.assertEqual(Document.objects.count(), 2)  # Verifica si se creó el documento
        
        document = Document.objects.last()
        self.assertEqual(document.suggestion_start_date, self.document.suggestion_start_date)  # Verifica si suggestion_start_date está establecido correctamente
        self.assertEqual(document.suggestion_end_date, self.document.suggestion_end_date)  # Verifica si suggestion_end_date está establecido correctamente

        self.client.logout()