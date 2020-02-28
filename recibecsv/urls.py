from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import holaMundo,simple_upload

urlpatterns=[
    path("hola-mundo.php",holaMundo),
    path("simple-upload.asp",simple_upload)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)