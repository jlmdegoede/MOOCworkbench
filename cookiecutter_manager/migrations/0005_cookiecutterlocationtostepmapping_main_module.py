# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookiecutter_manager', '0004_auto_20170428_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookiecutterlocationtostepmapping',
            name='main_module',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
