# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality_manager', '0002_auto_20170426_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawmeasureresult',
            name='value',
            field=models.CharField(max_length=1000),
        ),
    ]
