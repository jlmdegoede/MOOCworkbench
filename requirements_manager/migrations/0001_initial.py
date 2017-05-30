# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 09:52
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('package_name', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=255, null=True)),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marketplace.InternalPackage')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
