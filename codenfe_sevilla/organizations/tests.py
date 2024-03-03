from django.test import TestCase
from django.urls import reverse
from organizations.models import Organization

class OrganizationTestCase(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(
            name='Mi Organización',
            telephone_number='123456789',
            address='Dirección de la organización',
            email='info@miorganizacion.com',
            zip_code=12345
        )

    def test_create_organization_view(self):
        response = self.client.post(reverse('organizations:create_organization'), {
            'name': 'Nueva Organización',
            'telephone_number': '987654321',
            'address': 'Nueva Dirección',
            'email': 'info@nuevaorganizacion.com',
            'zip_code': 54321,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Organization.objects.filter(name='Nueva Organización').exists())

    def test_update_organization_view(self):
        updated_name = 'Organización Actualizada'
        response = self.client.post(reverse('organizations:update_organization', args=[self.organization.pk]), {
            'name': updated_name,
            'telephone_number': self.organization.telephone_number,
            'address': self.organization.address,
            'email': self.organization.email,
            'zip_code': self.organization.zip_code,
        })
        self.assertEqual(response.status_code, 302)  
        self.organization.refresh_from_db()  
        self.assertEqual(self.organization.name, updated_name)
    
    def test_list_organizations_view(self):
        response = self.client.get(reverse('organizations:organization_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.organization.name)
    
    def test_get_organization_view(self):
        response = self.client.get(reverse('organizations:get_organization', args=[self.organization.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.organization.name)
        
    def test_delete_organization_view(self):
        response = self.client.post(reverse('organizations:delete_organization', args=[self.organization.pk]))
        self.assertEqual(response.status_code, 302)  
        self.assertFalse(Organization.objects.filter(pk=self.organization.pk).exists())
        
        