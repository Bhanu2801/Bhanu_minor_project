# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='views',
            field=models.CharField(default=datetime.datetime(2015, 10, 2, 5, 29, 4, 857000, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
