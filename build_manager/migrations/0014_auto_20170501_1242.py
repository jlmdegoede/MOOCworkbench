# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build_manager', '0013_auto_20170501_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travisinstance',
            name='last_build_status',
            field=models.CharField(choices=[('F', 'Failed'), ('S', 'Success'), ('C', 'Cancelled')], max_length=1, null=True),
        ),
    ]
