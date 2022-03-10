from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("api/", include("shangkai_app.urls")),
    path("users/", include("users.urls")),
    path("clients/", include("clients.urls")),
    path("auth_clients/", include("auth_travel.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
