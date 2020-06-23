import os

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from test_django import settings
from images.views import list, upload, get_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('images.urls')),
    path('upload/', upload, name='upload'),
    path('', list, name='list'),
    path('<str:hash>', get_image)
] + static('/', document_root=settings.MEDIA_ROOT)
