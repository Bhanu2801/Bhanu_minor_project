# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 28, 3, 40, 41, 220000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
