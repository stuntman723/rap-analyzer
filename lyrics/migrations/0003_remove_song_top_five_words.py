# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics', '0002_auto_20150919_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='top_five_words',
        ),
    ]
