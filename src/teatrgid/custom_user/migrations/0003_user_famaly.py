# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0002_auto_20170403_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='famaly',
            field=models.CharField(default='', max_length=100),
        ),
    ]
