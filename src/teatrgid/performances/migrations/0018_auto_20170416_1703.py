# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performances', '0017_auto_20170416_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datesevent',
            name='duration',
            field=models.TimeField(blank=True, default='00:00:00', verbose_name='Продолжительность'),
        ),
    ]
