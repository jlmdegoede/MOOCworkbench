# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Worker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submittedexperiments',
            name='run_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
