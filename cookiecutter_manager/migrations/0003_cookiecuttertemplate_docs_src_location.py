# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookiecutter_manager', '0002_auto_20170502_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookiecuttertemplate',
            name='docs_src_location',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
