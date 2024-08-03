
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import *

urlpatterns = [
    # core
    path("", index, name="index"),
    path("contacts/", contacts, name="contacts"),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
