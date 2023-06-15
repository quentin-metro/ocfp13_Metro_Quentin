from django.conf import settings
from django.conf import urls
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urls.handler404 = views.error_404
