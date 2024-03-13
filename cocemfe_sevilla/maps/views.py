from django.shortcuts import render
import folium

def map_index(request):
    # Creamos un mapa centrado en una ubicación específica
    mapa = folium.Map(location=[37.3896, -5.9845], zoom_start=10, zoom_control=True, scrollWheelZoom=True)

    # Agregamos marcadores al mapa
    folium.Marker(location=[37.3896, -5.9845], popup='Sevilla').add_to(mapa)

    # Convertimos el mapa a HTML
    mapa_html = mapa._repr_html_()

    # Renderizamos la plantilla con el mapa
    return render(request, 'maps_index.html', {'mapa_html': mapa_html})