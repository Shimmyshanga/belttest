# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20161126_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='Pending', max_length=30),
        ),
    ]
