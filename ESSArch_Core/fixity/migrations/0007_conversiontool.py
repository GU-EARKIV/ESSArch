# Generated by Django 3.0.3 on 2020-03-06 10:05

import ESSArch_Core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixity', '0006_validation_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversionTool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('APP', 'Application'), ('DOCKER_IMG', 'Docker Image')], max_length=20, verbose_name='type')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('path', models.TextField(verbose_name='path')),
                ('cmd', models.TextField(verbose_name='command')),
                ('enabled', models.BooleanField(verbose_name='enabled')),
                ('form', ESSArch_Core.fields.JSONField(blank=True, null=True, verbose_name='form')),
            ],
            options={
                'verbose_name': 'conversion tool',
                'verbose_name_plural': 'conversion tools',
            },
        ),
    ]