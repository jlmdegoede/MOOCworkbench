# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 09:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GitManager', '0002_auto_20170320_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gitrepository',
            name='subrepos',
        ),
    ]
