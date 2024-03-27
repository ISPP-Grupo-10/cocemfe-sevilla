from django.urls import path
from . import views

app_name = 'organizations'

urlpatterns = [
    path('', views.organization_options, name='organization_options'),
    path('list/', views.organization_list, name='organization_list'),
    path('create/', views.create_organization, name='create_organization'),
    path('<int:pk>/', views.get_organization, name='get_organization'),
    path('<int:pk>/update/', views.update_organization, name='update_organization'),
    path('<int:pk>/delete/', views.delete_organization, name='delete_organization'),
]