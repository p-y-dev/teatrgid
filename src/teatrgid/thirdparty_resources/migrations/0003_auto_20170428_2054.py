# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thirdparty_resources', '0002_advertising'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertising',
            name='thumbnail',
            field=models.ImageField(blank=True, default='', upload_to='img/thumbnail/', verbose_name='Миниатюра'),
        ),
        migrations.AlterField(
            model_name='thirdpartyresources',
            name='thumbnail',
            field=models.ImageField(blank=True, default='', upload_to='img/thumbnail/', verbose_name='Миниатюра'),
        ),
    ]
