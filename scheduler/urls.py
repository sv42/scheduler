from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('main.urls'), name='home'),
    path("bases", include('bases.urls'), name='schedule'),
    path("grade", include('grade.urls'), name='grades')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
