# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 16:51
from __future__ import unicode_literals

import autoslug.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general_information', '0002_auto_20170412_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='img/performances/', verbose_name='Миниатюра')),
                ('name', models.CharField(max_length=120, verbose_name='Название')),
                ('publication_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Дата публикации')),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='name', unique=True, verbose_name='Slug спектакля')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general_information.ListCity')),
            ],
            options={
                'verbose_name': 'Спектакль',
                'verbose_name_plural': 'Спектакли',
                'ordering': ('-publication_date',),
            },
        ),
    ]
