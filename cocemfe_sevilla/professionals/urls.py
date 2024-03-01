from django.urls import path
from .views import professional_list, professional_detail_view, professional_update_view

urlpatterns = [
    path('professionals/', professional_list, name='professional_list'),
    path('professionals/<int:pk>/', professional_detail_view, name='professional_detail'),
    path('professionals/<int:pk>/edit/', professional_update_view, name='professional_edit'),
]
