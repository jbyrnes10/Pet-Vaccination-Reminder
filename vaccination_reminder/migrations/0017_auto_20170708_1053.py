# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-08 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination_reminder', '0016_auto_20170708_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccinations',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]