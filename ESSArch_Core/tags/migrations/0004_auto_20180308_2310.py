# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-08 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_auto_20180209_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='current_version',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='index',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='tag',
            name='link_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='tag',
            name='type',
            field=models.CharField(default='', max_length=255, verbose_name=b'Type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='version_end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='version_start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
