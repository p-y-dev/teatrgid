# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='content',
            field=models.TextField(default='', max_length=6000),
        ),
    ]