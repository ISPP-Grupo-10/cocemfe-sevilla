from django.urls import path
from .views import list_pdf, upload_pdf, view_pdf_admin, update_pdf, delete_pdf, check_pdf, delete_pdf_form
from suggestions.views import *



urlpatterns = [
    path("", list_pdf, name="list_pdf"),
    path('upload_pdf', upload_pdf, name='upload_pdf'),
    path('view_pdf/<int:pk>/', view_pdf_admin, name='view_pdf_admin'),
    path('update_pdf/<int:pk>/', update_pdf, name='update_pdf'),
    path('delete_pdf/<int:pk>/', delete_pdf, name='delete_pdf'),
    path('check_pdf/<int:pk>/', check_pdf, name='check_pdf'),
    path('create-suggestion/<int:document_id>/', crear_sugerencia, name='create_suggestion'),
    path('delete_pdf_form/<int:pk>/', delete_pdf_form, name='delete_pdf_form'),
]