from django.urls import path

from makevideo.apps import MakevideoConfig
from makevideo.views import index

app_name = MakevideoConfig.name

urlpatterns = [
    path('makevideo/', index, name='index'),
]
