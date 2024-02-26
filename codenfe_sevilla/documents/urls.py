from django.urls import path
from .views import upload_pdf, view_pdf, update_pdf, delete_pdf

urlpatterns = [
    path('upload_pdf', upload_pdf, name='upload_pdf'),
    path('view_pdf/<int:pk>/', view_pdf, name='view_pdf'),
    path('update_pdf/<int:pk>/', update_pdf, name='update_pdf'),
    path('delete_pdf/<int:pk>/', delete_pdf, name='delete_pdf'),
]