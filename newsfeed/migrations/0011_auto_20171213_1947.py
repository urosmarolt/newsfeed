# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0010_auto_20171208_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistrypost',
            name='created_at',
            field=models.DateTimeField(default='2017-12-13 19:47:32', max_length=150),
        ),
        migrations.RemoveField(
            model_name='eventregistrypost',
            name='tags',
        ),
    ]
