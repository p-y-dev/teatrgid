# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performances', '0013_auto_20170416_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datesevent',
            name='date_time',
            field=models.DateTimeField(verbose_name='Дата и время'),
        ),
    ]
