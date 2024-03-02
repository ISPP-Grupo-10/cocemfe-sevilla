from django.conf import settings
from django.urls import path
from .views import professional_list, EditUserView
from django.conf.urls.static import static

urlpatterns = [
    path('', professional_list, name='professional_list'),
    path('<int:pk>/', EditUserView.as_view(), name='professional_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)