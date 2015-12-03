# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0003_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_name',
            field=models.CharField(default=datetime.datetime(2015, 10, 3, 14, 34, 5, 133000, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.ForeignKey(to='mentor.Mentor'),
        ),
    ]
