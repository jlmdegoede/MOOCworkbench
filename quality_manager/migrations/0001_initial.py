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
        ('experiments_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperimentMeasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('high_message', models.CharField(default='High', max_length=255)),
                ('medium_message', models.CharField(default='Medium', max_length=255)),
                ('low_message', models.CharField(default='Low', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ExperimentMeasureResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('result', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], max_length=1)),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quality_manager.ExperimentMeasure')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RawMeasureResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='experimentmeasureresult',
            name='raw_values',
            field=models.ManyToManyField(to='quality_manager.RawMeasureResult'),
        ),
        migrations.AddField(
            model_name='experimentmeasureresult',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiments_manager.ChosenExperimentSteps'),
        ),
    ]
