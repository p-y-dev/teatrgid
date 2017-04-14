# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general_information', '0002_auto_20170412_1651'),
        ('performances', '0002_auto_20170413_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='genres',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='general_information.ListGenres', verbose_name='Жанры'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='performance',
            name='city',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='general_information.ListCity', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='performance',
            name='thumbnail',
            field=models.ImageField(upload_to='img/thumbnail/', verbose_name='Миниатюра'),
        ),
    ]