# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performances', '0018_auto_20170416_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datesevent',
            name='duration',
            field=models.TimeField(default='00:00:00', verbose_name='Продолжительность'),
        ),
    ]