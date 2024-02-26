from django.urls import path
from . import views

urlpatterns = [
    path('organizations/', views.organization_list, name='organization_list'),
    path('organizations/create/', views.create_organization, name='create_organization'),
    path('organizations/<int:pk>/', views.get_organization, name='get_organization'),
    path('organizations/<int:pk>/update/', views.update_organization, name='update_organization'),
    path('organizations/<int:pk>/delete/', views.delete_organization, name='delete_organization'),
]
