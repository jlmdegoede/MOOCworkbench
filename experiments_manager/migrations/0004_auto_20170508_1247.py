# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments_manager', '0003_experiment_schema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
