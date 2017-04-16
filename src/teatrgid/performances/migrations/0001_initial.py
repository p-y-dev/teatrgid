# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 15:11
from __future__ import unicode_literals

import autoslug.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('theaters', '0001_initial'),
        ('persons', '0001_initial'),
        ('general_information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='img/thumbnail/', verbose_name='Миниатюра')),
                ('name', models.CharField(max_length=120, verbose_name='Название')),
                ('publication_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Дата публикации')),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='name', unique=True, verbose_name='Slug')),
                ('actors', models.ManyToManyField(default='', to='persons.Actors', verbose_name='Актеры')),
                ('age_restrictions', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='general_information.ListAgeRestrictions', verbose_name='Возастное ограничение')),
                ('city', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='general_information.ListCity', verbose_name='Город')),
                ('directors', models.ManyToManyField(default='', to='persons.Directors', verbose_name='Режиссеры')),
                ('genres', models.ManyToManyField(to='general_information.ListGenres', verbose_name='Жанры')),
                ('theaters', models.ManyToManyField(default='', to='theaters.Theaters', verbose_name='Театры')),
            ],
            options={
                'verbose_name_plural': 'Спектакли',
                'ordering': ('-publication_date',),
                'verbose_name': 'Спектакль',
            },
        ),
    ]
