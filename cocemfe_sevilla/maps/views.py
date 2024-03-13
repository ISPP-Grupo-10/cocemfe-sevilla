from django.shortcuts import render

def map_index(request):
    return render(request, 'maps_index.html')