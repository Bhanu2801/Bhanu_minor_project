# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0003_auto_20151128_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
