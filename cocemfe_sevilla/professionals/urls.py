from django.urls import path
from .views import professional_list, professional_detail_view, professional_update_view

urlpatterns = [
    path('', professional_list, name='professional_list'),
    path('<int:pk>/', professional_detail_view, name='professional_detail'),
    path('<int:pk>/edit/', professional_update_view, name='professional_edit'),
]
