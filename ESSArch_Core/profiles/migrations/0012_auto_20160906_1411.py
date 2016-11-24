# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20160905_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_type',
            field=models.CharField(choices=[(b'transfer_project', b'Transfer Project'), (b'content_type', b'Content Type'), (b'data_selection', b'Data Selection'), (b'classification', b'Classification'), (b'import', b'Import'), (b'submit_description', b'Submit Description'), (b'sip', b'SIP'), (b'aip', b'AIP'), (b'dip', b'DIP'), (b'workflow', b'Workflow'), (b'preservation_description', b'Preservation Description'), (b'event', b'Event')], max_length=255),
        ),
    ]