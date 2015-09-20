from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Artist, Song

def index(request):
    song_list = Song.objects.all()
    template = loader.get_template('lyrics/index.html')
    context = RequestContext(request, {
        'song_list': song_list,
    })
    return HttpResponse(template.render(context))