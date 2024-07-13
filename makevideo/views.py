
from django.shortcuts import render

from makevideo.models import Request


def index(request):
    param = request.GET.get('text')
    if param:
        Request.objects.create(query=param)
    return render(request, 'makevideo/index.html')
