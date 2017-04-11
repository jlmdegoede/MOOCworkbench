# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 08:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('experiments_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False)),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiments_manager.Experiment')),
            ],
        ),
    ]