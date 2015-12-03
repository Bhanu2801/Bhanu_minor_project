# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0004_auto_20151129_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.BigIntegerField()),
                ('views', models.CharField(max_length=200)),
                ('institute', models.ForeignKey(to='institution.Institute')),
            ],
        ),
    ]
