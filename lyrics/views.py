
# Create your views here.
from django.template import RequestContext, loader
from models import Artist, Song
from django.shortcuts import render, redirect
from forms import SongForm
from django.http import HttpResponse
from justAnalyze import analyze

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
            data = analyze(form.cleaned_data['lyrics'])
            try :
                artist = Artist.objects.all().filter(name=form.cleaned_data['artist-name'])
            except:
                artist = Artist(name=form.cleaned_data['artist_name'])
                artist.save()
            song = Song(name=form.cleaned_data['song_name'], lyrics = form.cleaned_data['lyrics'], artist=artist,
                        number_of_words= data['total_words'], number_unique_words=data['unique_words'],
                        unique_word_percent=data['percentage'], repeated_rhymes=data['repeated_rhymes'],
                        bad_words=data['bad_words'], thug_rating=data['thug_rating'], avg_syllables=data['thug_rating'])
            song.save()
            return redirect("/")
    form = SongForm()
    return render(request, 'lyrics/new_song.html', { 'form': form })