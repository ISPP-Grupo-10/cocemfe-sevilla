from django.urls import path
from .views import *

urlpatterns = [
    path("", list_pdf, name="list_pdf"),
    path('upload_pdf', upload_pdf, name='upload_pdf'),
    path('view_pdf/<int:pk>/', view_pdf_admin, name='view_pdf_admin'),
    path('update_pdf/<int:pk>/', update_pdf, name='update_pdf'),
    path('delete_pdf/<int:pk>/', delete_pdf, name='delete_pdf'),
]