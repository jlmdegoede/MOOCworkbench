# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 14:08
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('Marketplace', '0002_packageresource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packageresource',
            name='resource',
            field=markdownx.models.MarkdownxField(),
        ),
    ]