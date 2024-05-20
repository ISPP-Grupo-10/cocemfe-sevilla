from django.test import TestCase

from calendars.models import Events
from professionals.models import Professional
from documents.models import Document
from organizations.models import Organization

from django.utils import timezone
from datetime import timedelta
from django.urls import reverse

# Create your tests here.
class CalendarsTestCase(TestCase):
    def setUp(self):

        # Crear una organización para usar en las pruebas
        self.organization = Organization.objects.create(
            name='Mi Organización',
            telephone_number='123456789',
            address='Dirección de la organización',
            email='info@miorganizacion.com',
            zip_code=12345
        )

        # Crear un profesional para usar en las pruebas
        self.professional_staff = Professional.objects.create(
            username='staff_user', 
            is_staff=True,
            telephone_number='123456789', 
            license_number='ABC123',
            organizations=self.organization, 
            terms_accepted=True, 
            email_verified=True
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
        self.document.professionals.add(self.professional_staff)

        # Crear un evento para usar en las pruebas
        self.event = Events.objects.create(
            creator=self.professional_staff, 
            title='Nuevo evento',
            description='Descripción del evento',
            datetime=timezone.now() + timedelta(days=1),
            document=self.document,
            type=Events.TIPO_CHOICES.REUNION
        )
    
    def test_create_event(self):
        event = Events.objects.get(pk=self.event.pk)
        self.assertEqual(event.title, 'Nuevo evento')
        self.assertEqual(event.description, 'Descripción del evento')
        self.assertEqual(event.datetime, self.event.datetime)
        self.assertEqual(event.document, self.document)
        self.assertEqual(event.type, Events.TIPO_CHOICES.REUNION)

    def test_create_modal_event(self):
        self.client.login(username='staff_user', password='staff_user')
        response = self.client.post(reverse('calendars:create_modal_event'), {
            'title': 'Nuevo evento',
            'description': 'Descripción del evento',
            'datetime': timezone.now() + timedelta(days=1),
            'document_id': self.document.pk,
            'type': Events.TIPO_CHOICES.REUNION
        })
        #self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Events.objects.filter(title='Nuevo evento').exists())
    '''
    def test_list_events(self):
        response = self.client.get(reverse('calendars:calendar'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.title)
    
    def test_delete_event(self):
        self.client.login(username='admin', password='admin')
        
        response = self.client.post(reverse('calendars:delete_event', args=[self.event.pk]))
        self.assertEqual(response.status_code, 302)
        initial_count = Events.objects.count()

        self.assertEqual(Events.objects.count(), initial_count - 1)
        
        with self.assertRaises(Document.DoesNotExist):
            Document.objects.get(pk=self.document.pk)
    '''        