# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performances', '0006_performance_link_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='rating',
            field=models.FloatField(default=0, verbose_name='Рейтинг'),
        ),
    ]
