# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0007_auto_20171202_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistrypost',
            name='created_at',
            field=models.DateTimeField(default='2017-12-02 13:25:05', max_length=150),
        ),
    ]
