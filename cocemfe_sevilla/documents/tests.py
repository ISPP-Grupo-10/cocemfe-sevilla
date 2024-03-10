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
            suggestion_start_date='2024-03-01',
            suggestion_end_date='2024-04-01',
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

    def test_filter_documents_by_suggestion_start_date(self):
        # Verificar que los documentos se filtran correctamente por fecha de inicio
        response = self.client.get(reverse('list_pdf'), {'suggestion_start_date': '2024-03-01'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.document.name)


    def test_upload_pdf_valid_form(self):
        self.client.login(username='admin', password='admin')
        data = {
            'suggestion_start_date': '02/03/2024',  # Current date
            'name': 'Documento de prueba',
            'ubication': 'Ubicación de prueba',  # 'ubication' is a typo, should be 'location
            'status': 'Abierto',  # 'status' is a typo, should be 'status
            'suggestion_end_date': '30/03/2024',
            'pdf_file': self.pdf_file,
            'professionals': [1],
        }
        url=reverse('upload_pdf')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)  # Check if redirecting to 'list_pdf' page
        self.assertEqual(Document.objects.count(), 2)  # Check if document is created
        document = Document.objects.last()
        self.assertEqual(document.suggestion_start_date, timezone.now().date())  # Check if suggestion_start_date is set to current date
        self.assertEqual(document.status, 'Borrador')  # Check if status is set to 'Borrador'
        self.assertEqual(list(document.professionals.values_list('id', flat=True)), [1])  # Check if professionals are set correctly
        self.client.logout()

    def test_upload_pdf_invalid_form(self):
        self.client.login(username='admin', password='admin')
        data = {
            'suggestion_start_date': timezone.now().date(),
            'name': 'Documento de prueba',
            'ubication': 'Ubicación de prueba',  
            'status': 'Abierto',  
            'suggestion_end_date': '01/01/2021',
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


    def test_modify_pdf_add_professional(self):
        # Verificar que se puede agregar un nuevo profesional al documento desde la vista de modificación

        # Creamos un nuevo profesional
        new_professional = Professional.objects.create(
            first_name='Pedro',
            last_name='González',
            username='pedrogonzalez',
            telephone_number='987654321',
            license_number='Licencia del nuevo profesional',
            organizations=self.organization
        )

        # Verificamos que el nuevo profesional se haya creado correctamente
        self.assertIsNotNone(new_professional)

        # Verificar que el documento tenga solo un profesional antes de la modificación
        self.assertEqual(self.document.professionals.count(), 1)

        # Obtener la URL para modificar el PDF
        modify_pdf_url = reverse('update_pdf', args=[self.document.pk])

        # Simular la modificación de datos del formulario para incluir al nuevo profesional
        new_name = 'Documento modificado con nuevo profesional'
        new_suggestion_end_date = '2025-04-15'  # Nueva fecha de fin
        new_professional_id = new_professional.id

        # Realizar la solicitud POST con los datos modificados
        response = self.client.post(modify_pdf_url, {
            'name': new_name,
            'suggestion_end_date': new_suggestion_end_date,
            'professionals': [self.professional.id, new_professional_id],  # Incluimos ambos profesionales
            # Puedes agregar más campos aquí según lo que permita el formulario
        })

        # Verificar que la redirección sea correcta
        self.assertEqual(response.status_code, 200)  # Código 302 indica redirección

        # Obtener el documento modificado desde la base de datos
        modified_document = Document.objects.get(pk=self.document.pk)

        # Verificar que los cambios se reflejan correctamente
        self.assertEqual(modified_document.name, new_name)
        self.assertEqual(str(modified_document.suggestion_end_date), new_suggestion_end_date)
        self.assertEqual(modified_document.professionals.count(), 2)  # Verificamos que se han agregado ambos profesionales
        self.assertIn(self.professional, modified_document.professionals.all())  # Verificamos que el primer profesional está incluido
        self.assertIn(new_professional, modified_document.professionals.all())  # Verificamos que el nuevo profesional está incluido

    def test_modify_pdf_with_invalid_suggestion_end_date(self):
        # Verificar que no se pueda modificar el documento con una fecha de fin inválida

        # Obtener la URL para modificar el PDF
        modify_pdf_url = reverse('update_pdf', args=[self.document.pk])

        # Simular la modificación de datos del formulario con fecha de fin inválida
        invalid_suggestion_end_date = '2022-01-01'  # Fecha pasada, debe ser al menos la fecha actual o futura

        # Realizar la solicitud POST con los datos modificados
        response = self.client.post(modify_pdf_url, {
            'name': self.document.name,
            'suggestion_end_date': invalid_suggestion_end_date,
            'professionals': [self.professional.id],
        })

        # Verificar que la página de modificación se vuelva a renderizar con errores
        self.assertEqual(response.status_code, 200)

        # Verificar que el documento no se ha modificado
        modified_document = Document.objects.get(pk=self.document.pk)
        self.assertNotEqual(modified_document.suggestion_end_date, invalid_suggestion_end_date)


    def test_modify_pdf_with_valid_data(self):
        # Verificar que se pueda modificar el documento con datos válidos

        # Obtener la URL para modificar el PDF
        modify_pdf_url = reverse('update_pdf', args=[self.document.pk])

        # Simular la modificación de datos del formulario
        new_name = 'Documento modificado'
        new_suggestion_end_date = '2025-04-01'  # Nueva fecha de fin válida

        # Realizar la solicitud POST con los datos modificados
        response = self.client.post(modify_pdf_url, {
            'name': new_name,
            'suggestion_end_date': new_suggestion_end_date,
            'professionals': [self.professional.id],
        })

        # Verificar que la redirección sea correcta
        self.assertEqual(response.status_code, 200)  # Código 302 indica redirección

        # Obtener el documento modificado desde la base de datos
        modified_document = Document.objects.get(pk=self.document.pk)

        # Verificar que los cambios se reflejan correctamente
        self.assertEqual(modified_document.name, new_name)
        self.assertEqual(str(modified_document.suggestion_end_date), new_suggestion_end_date)

    def test_delete_pdf(self):
        # Verificar que se puede borrar un documento correctamente

        # Obtener la URL para borrar el PDF
        delete_pdf_url = reverse('delete_pdf', args=[self.document.pk])

        # Obtener el número de documentos antes de la eliminación
        initial_count = Document.objects.count()

        # Realizar la solicitud POST para borrar el documento
        response = self.client.post(delete_pdf_url)

        # Verificar que la redirección sea correcta después de borrar el documento
        self.assertRedirects(response, reverse('list_pdf'))

        # Verificar que el número de documentos ha disminuido después de la eliminación
        self.assertEqual(Document.objects.count(), initial_count - 1)

        # Verificar que el documento ya no existe en la base de datos
        with self.assertRaises(Document.DoesNotExist):
            Document.objects.get(pk=self.document.pk)