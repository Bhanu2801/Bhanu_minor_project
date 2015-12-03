# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0002_institute_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'date published'),
        ),
    ]
