from django.test import TestCase
from django.test import Client
from django.urls import reverse

class MapIndexTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_map_index_view(self):
        response = self.client.get(reverse('maps:map_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maps_index.html')

class MapSearchTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_map_search_view(self):
        latitude = '37.3896'
        longitude = '-5.9845'
        response = self.client.get(reverse('maps:map_search', kwargs={'latitude': latitude, 'longitude': longitude}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maps_index.html')

