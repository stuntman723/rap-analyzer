from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)

    list_display = ('name')

    def __str__(self):
        return self.name

class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class Song(models.Model):
    name = models.TextField()
    lyrics = models.TextField()
    artist = models.ForeignKey(Artist)
    number_of_words = models.IntegerField()
    number_unique_words = models.IntegerField()
    unique_word_percent = models.FloatField()
    repeated_rhymes = models.IntegerField()
    bad_words = models.IntegerField()
    thug_rating = models.FloatField()
    avg_syllables = models.FloatField()

    list_display = ("name", "artist")

    def __str__(self):
        return self.name + " by " + self.artist.name