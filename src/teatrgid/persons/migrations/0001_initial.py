# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 15:58
from __future__ import unicode_literals

import autoslug.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general_information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='img/thumbnail/', verbose_name='Миниатюра')),
                ('publication_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Дата публикации')),
                ('content', models.TextField(default='', max_length=6000)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='name', unique=True, verbose_name='Slug')),
                ('my_order', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=120, verbose_name='Имя')),
                ('city', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='general_information.ListCity', verbose_name='Город')),
            ],
            options={
                'ordering': ('-my_order',),
                'verbose_name_plural': 'Актеры',
                'verbose_name': 'Актер',
            },
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='img/thumbnail/', verbose_name='Миниатюра')),
                ('publication_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Дата публикации')),
                ('content', models.TextField(default='', max_length=6000)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='name', unique=True, verbose_name='Slug')),
                ('my_order', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=120, verbose_name='Имя')),
                ('city', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='general_information.ListCity', verbose_name='Город')),
            ],
            options={
                'ordering': ('-my_order',),
                'verbose_name_plural': 'Режиссеры',
                'verbose_name': 'Режиссер',
            },
        ),
    ]
