from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from makevideo.apps import MakevideoConfig
from makevideo.views import index

app_name = MakevideoConfig.name

urlpatterns = [
    path('makevideo/', index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
