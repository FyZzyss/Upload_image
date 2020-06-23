from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
# admin.autodiscover()

from .views import list
app_name = "images"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
]