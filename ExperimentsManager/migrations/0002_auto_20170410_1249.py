# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 12:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExperimentsManager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experimentstep',
            old_name='step_name',
            new_name='name',
        ),
    ]
