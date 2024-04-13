from django.test import TestCase
from django.test import Client
from django.urls import reverse
from maps.views import get_coordinates_openstreetmap, map_index, map_search

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


class GetCoordinatesOpenStreetMapTestCase(TestCase):
    def test_get_coordinates_openstreetmap(self):
        city = 'Seville'
        latitude, longitude = get_coordinates_openstreetmap(city)
        self.assertIsNotNone(latitude)
        self.assertIsNotNone(longitude)

        self.assertTrue(37.3886 <= latitude <= 37.4192)
        self.assertTrue(-6.0524 <= longitude <= -5.9312)
