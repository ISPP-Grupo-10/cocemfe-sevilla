# urls.py

from django.urls import path
from .views import professional_detail_view, professional_update_view

urlpatterns = [
    path('detalles-profesionales/<int:pk>/', professional_detail_view, name='professional_detail'),
    path('detalles-profesionales/<int:pk>/editar/', professional_update_view, name='professional_edit'),
    # Otras rutas según sea necesario
]
