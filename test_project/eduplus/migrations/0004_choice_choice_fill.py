# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eduplus', '0003_auto_20151005_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_fill',
            field=models.FileField(null=True, upload_to=b'profile/%Y/%m/%d', blank=True),
        ),
    ]
