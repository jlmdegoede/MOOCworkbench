# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build_manager', '0002_auto_20170502_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travisinstance',
            name='last_build_status',
            field=models.CharField(choices=[('S', 'Success'), ('C', 'Cancelled'), ('F', 'Failed')], max_length=1, null=True),
        ),
    ]