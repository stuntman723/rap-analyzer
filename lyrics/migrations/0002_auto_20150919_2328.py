# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lyrics.models


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('lyrics', models.TextField()),
                ('number_of_words', models.IntegerField()),
                ('number_unique_words', models.IntegerField()),
                ('unique_word_percent', models.FloatField()),
                ('repeated_rhymes', models.IntegerField()),
                ('bad_words', models.IntegerField()),
                ('top_five_words', lyrics.models.ListField()),
                ('artist', models.ForeignKey(to='lyrics.Artist')),
            ],
        ),
        migrations.RemoveField(
            model_name='verse',
            name='artist',
        ),
        migrations.DeleteModel(
            name='Verse',
        ),
    ]
