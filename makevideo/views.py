import os
from pathlib import Path
import wget
from makevideo.utils.funcs import make_video
from django.shortcuts import render

from makevideo.models import Request


def index(request):
    param = request.GET.get('text')
    if param:
        obj = Request.objects.create(query=param)
        make_video(param, obj.pk)

        file_url = f'http://localhost:8000/media/{obj.pk}.mp4'
        path_to_folder = str(os.path.join(Path.home(), 'Downloads'))
        wget.download(file_url, out=path_to_folder)

    return render(request, 'makevideo/index.html')
