from django.urls import path
from .views import *
from suggestions.views import *



urlpatterns = [
    path("", list_pdf, name="list_pdf"),
    path('upload_pdf', upload_pdf, name='upload_pdf'),
    path('view_pdf/<int:pk>/', view_pdf_admin, name='view_pdf_admin'),
    path('view_pdf/<int:pk>/chat', load_comments, name='view_pdf_chat'),
    path('view_pdf/<int:pk>/chat/post', publish_comment, name='publish_comment'),
    path('update_pdf/<int:pk>/', update_pdf, name='update_pdf'),
    path('delete_pdf/<int:pk>/', delete_pdf, name='delete_pdf'),
    path('create-suggestion/<int:document_id>/', crear_sugerencia, name='create_suggestion'),
]