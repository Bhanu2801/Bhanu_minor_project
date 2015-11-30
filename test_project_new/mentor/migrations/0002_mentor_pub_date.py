# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 3, 14, 21, 57, 763000, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
