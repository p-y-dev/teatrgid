# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general_information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThirdpartyResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название')),
                ('thumbnail', models.ImageField(upload_to='img/thumbnail/', verbose_name='Миниатюра')),
                ('link', models.CharField(max_length=120, verbose_name='Ссылка на ресурс')),
                ('city', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='general_information.ListCity', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Сторонние ресуры',
                'verbose_name_plural': 'Сторонние ресуры',
            },
        ),
    ]
