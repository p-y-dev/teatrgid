# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actors',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Имя'),
        ),
    ]
