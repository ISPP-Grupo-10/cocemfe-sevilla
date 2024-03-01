# urls.py

from django.urls import path
from .views import ProfessionalDetailView, ProfessionalUpdateView

urlpatterns = [
    path('detalles-profesionales/<int:pk>/', ProfessionalDetailView.as_view(), name='professional_detail'),
    path('detalles-profesionales/<int:pk>/editar/', ProfessionalUpdateView.as_view(), name='professional_edit'),
    # Otras rutas según sea necesario
]
