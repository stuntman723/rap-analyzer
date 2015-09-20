# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics', '0003_remove_song_top_five_words'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='avg_syllables',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='thug_rating',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
