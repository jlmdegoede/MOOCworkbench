# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookiecutter_manager', '0003_cookiecuttertemplate_docs_src_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookiecuttertemplate',
            name='folder_file_locations',
            field=models.ManyToManyField(blank=True, to='cookiecutter_manager.CookieCutterLocationToStepMapping'),
        ),
    ]
