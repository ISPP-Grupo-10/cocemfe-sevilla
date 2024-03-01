from django.urls import path
from .views import professional_list, ProfessionalDetailView, ProfessionalUpdateView

urlpatterns = [
    path('professionals/', professional_list, name='professional_list'),
    path('professionals/<int:pk>/', ProfessionalDetailView.as_view(), name='professional_detail'),
    path('professionals/<int:pk>/edit/', ProfessionalUpdateView.as_view(), name='professional_edit'),
]

