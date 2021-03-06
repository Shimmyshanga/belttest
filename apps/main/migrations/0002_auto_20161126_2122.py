# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 21:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0002_user_date_birth'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=30)),
                ('date', models.DateField(max_length=45)),
                ('time', models.TimeField(max_length=45)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='login_reg_app.User')),
            ],
        ),
        migrations.DeleteModel(
            name='Apointment',
        ),
    ]
