# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-08 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination_reminder', '0010_auto_20170708_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccination_reminder.User'),
        ),
    ]
