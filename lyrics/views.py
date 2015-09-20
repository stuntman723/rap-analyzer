
# Create your views here.
from django.template import RequestContext, loader
from models import Artist, Song
from django.shortcuts import render
from forms import SongForm
from django.http import HttpResponse

def index(request):
    song_list = Song.objects.all()
    context = {
        'song_list': song_list,
    }
    return render(request, 'lyrics/index.html', context=context)

def new_song(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            return HttpResponse("Cheers")

    form = SongForm()
    return render(request, 'lyrics/new_song.html', { 'form': form})