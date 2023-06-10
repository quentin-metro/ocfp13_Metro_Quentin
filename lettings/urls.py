from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('lettings/', views.index, name='lettings_index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
