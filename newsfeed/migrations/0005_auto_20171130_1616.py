# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0004_auto_20171130_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventregistrypost',
            name='id',
        ),
        migrations.AlterField(
            model_name='eventregistrypost',
            name='created_at',
            field=models.DateTimeField(default='2017-11-30 16:16:49', max_length=150),
        ),
        migrations.AlterField(
            model_name='eventregistrypost',
            name='news_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
