# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0003_workbenchuser_ssh_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSHKeys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssh_key', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='workbenchuser',
            name='ssh_key',
        ),
        migrations.AddField(
            model_name='sshkeys',
            name='workbench_user',
            field=models.ManyToManyField(to='UserManager.WorkbenchUser'),
        ),
    ]
