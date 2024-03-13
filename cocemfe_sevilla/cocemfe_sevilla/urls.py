"""
URL configuration for cocemfe_sevilla project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from documents import views as docsViews
from django.conf import settings
from django.conf.urls.static import static
from professionals import views as profViews


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('base.urls', namespace='base')),
    path('documents/', include('documents.urls')),
    path('professionals/', include('professionals.urls')),
    path('organizations/', include('organizations.urls')),
    path('maps/', include('maps.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)