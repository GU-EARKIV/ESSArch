# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-27 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0020_auto_20190326_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagversiontype',
            name='archive_type',
            field=models.BooleanField(default=False, verbose_name='archive type'),
        ),
    ]