from django.shortcuts import render
import folium
import requests
from documents.models import Document
from .models import Coordinates

def map_index(request):
    mapa = folium.Map(location=[37.3896, -5.9845], zoom_start=10, zoom_control=True, scrollWheelZoom=True)
    cities_with_documents = Document.objects.values_list('ubication', flat=True).distinct()
    
    for city in cities_with_documents:
        documents = Document.objects.filter(ubication=city)
        coordinates = Coordinates.objects.filter(location=city).first()
        if not coordinates:
            latitude, longitude = get_coordinates_openstreetmap(city)
            Coordinates.objects.create(location=city, latitude=latitude, longitude=longitude)
        else:
            latitude, longitude = coordinates.latitude, coordinates.longitude
            
        marker = folium.Marker(location=[latitude, longitude], popup=city)
        marker.add_to(mapa)
        
        # Crear un control de tipo Popup con el listado de documentos
        popup_content = "<h3>{}</h3><ul>".format(city)
        for document in documents:
            popup_content += "<li><a href='/documents/view_pdf/{0}' target='_top'>{1}</a></li>".format(document.id, document.name)
        popup_content += "</ul>"
        
        folium.Popup(popup_content).add_to(marker)

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