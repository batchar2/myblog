# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_sitepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='allow_comments',
            field=models.BooleanField(default=True, verbose_name='allow comments'),
        ),
    ]
