# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 13:16
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170606_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='SitePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('url', models.CharField(default='', max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('number_views', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('-name',),
                'verbose_name_plural': 'Страницы сайта',
                'verbose_name': 'Страница сайта',
            },
        ),
    ]