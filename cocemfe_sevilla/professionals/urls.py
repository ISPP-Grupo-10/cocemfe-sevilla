from django.conf import settings
from django.urls import path
from .views import create_professional, professional_list, edit_user_view, delete_professional
from django.conf.urls.static import static

urlpatterns = [
    path('', professional_list, name='professional_list'),
    path('create_professional/', create_professional, name='create_professional'),
    path('<int:id>/delete/', delete_professional, name='delete_professional'),
    path('<int:pk>/', edit_user_view, name='professional_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
