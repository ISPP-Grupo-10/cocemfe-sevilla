# urls.py

from django.urls import path
from .views import professional_detail_view, professional_update_view

urlpatterns = [
    path('professionals/<int:pk>/', professional_detail_view, name='professional_detail'),
    path('professionals/<int:pk>/edit/', professional_update_view, name='professional_edit'),
    # Otras rutas según sea necesario
]
