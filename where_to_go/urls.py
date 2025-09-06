from django.contrib import admin
from places import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('places', views.index),
    path('places/<int:place_id>/', views.show_place, name='show_place'),
    path('tinymce/', include('tinymce.urls'))
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
    ) + static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
        )
