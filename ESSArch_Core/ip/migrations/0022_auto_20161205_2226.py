# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0021_auto_20161201_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivalinstitution',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='archivallocation',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='archivaltype',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='archivistorganization',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]