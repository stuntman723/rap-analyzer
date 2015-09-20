__author__ = 'ryanstuntz'

from django import forms


class SongForm (forms.Form):
    artist_name = forms.CharField(label="Artist's Name ", max_length=50)
    song_name = forms.CharField(label="Song's Name ", max_length=50)
    lyrics = forms.CharField(widget=forms.Textarea)
