from django.conf import settings
from django.urls import path
from .views import *
from django.conf.urls.static import static

app_name = 'professionals'

urlpatterns = [
    path('', professional_list, name='professional_list'),
    path('create_professional/', create_professional, name='create_professional'),
    path('professional_data/<int:professional_id>/', professional_data, name='professional_data'),
    path('<int:id>/delete/', delete_professional, name='delete_professional'),
    path('<int:pk>/', edit_user_view, name='professional_detail'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('requests/', request_list, name='request_list'),
    path('requests/create/', create_request, name='create_request'),
    path('requests/<int:pk>/update', update_request, name='update_request'),
    path('chats/', request_document_chats, name="chats"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
