# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-05 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0003_auto_20170403_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback_dislike',
            field=models.TextField(null=True, verbose_name="What didn't you like about your experience?"),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback_like',
            field=models.TextField(null=True, verbose_name='What did you like about your experience?'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='like',
            field=models.BooleanField(verbose_name='Overall, was your experience positive?'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='other_comments',
            field=models.TextField(null=True, verbose_name='Do you have any other comments?'),
        ),
    ]