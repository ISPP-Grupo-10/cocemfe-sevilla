from django.shortcuts import render
import folium
import requests
from documents.models import Document

def map_index(request):
    mapa = folium.Map(location=[37.3896, -5.9845], zoom_start=10, zoom_control=True, scrollWheelZoom=True)
    documents = Document.objects.all()
    for document in documents:
        latitude, longitude = get_coordinates_openstreetmap(document.ubication)
        folium.Marker(location=[latitude, longitude], popup=document.name).add_to(mapa)


    folium.Marker(location=[37.3896, -5.9845], popup='Sevilla').add_to(mapa)

    mapa_html = mapa._repr_html_()

    return render(request, 'maps_index.html', {'mapa_html': mapa_html})

def get_coordinates_openstreetmap(city):
    url = f'https://nominatim.openstreetmap.org/search?q={city}&format=json'
    response = requests.get(url)
    data = response.json()

    if data:
        latitude = float(data[0]['lat'])
        longitude = float(data[0]['lon'])
        return latitude, longitude
    else:
        return None, None


