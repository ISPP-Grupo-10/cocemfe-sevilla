from django.urls import path
from .views import upload_pdf, view_pdf

urlpatterns = [
    path('upload_pdf', upload_pdf, name='upload_pdf'),
    path('view_pdf/<int:pk>/', view_pdf, name='view_pdf'),

]