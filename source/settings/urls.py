"""Project root URL Configuration"""
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from settings.admin import admin


urlpatterns = []

#Admin endpoints
urlpatterns.append(path('admin/', admin.urls))

# API endpoints
urlpatterns.append(path('', include('apps.tos.urls')))

# Static endpoints
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
