from django.conf import settings
from django.urls import path
from .views import professional_data, professional_profile
from django.conf.urls.static import static


from .views import professional_list, create_professional, delete_professional, edit_user_view, professional_details, custom_login, custom_logout, request_list, create_request, update_request, request_document_chats, delete_account, change_password, VerifyEmailView


app_name = 'professionals'

urlpatterns = [
    path('', professional_list, name='professional_list'),
    path('create_professional/', create_professional, name='create_professional'),
    path('<int:id>/delete/', delete_professional, name='delete_professional'),
    path('<int:pk>/update', edit_user_view, name='professional_detail'),
    path('<int:pk>/', professional_details, name='professional_details'),
    path('profile/<int:pk>/', professional_profile, name='professional_profile'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('requests/', request_list, name='request_list'),
    path('requests/create', create_request, name='create_request'),
    path('requests/<int:pk>/update', update_request, name='update_request'),
    path('chats/', request_document_chats, name="chats"),
    path('change_password/', change_password, name='update_password'),
    path('verify_email/<str:uidb64>/', VerifyEmailView.as_view(), name='verify_email'),
    path('delete_account/', delete_account, name='delete_account'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
