# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-18 09:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0030_auto_20170328_1545'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='informationpackage',
            options={'ordering': ['id'], 'permissions': (('can_upload', 'Can upload files to IP'), ('set_uploaded', 'Can set IP as uploaded'), ('create_sip', 'Can create SIP'), ('submit_sip', 'Can submit SIP'), ('transfer_sip', 'Can transfer SIP'), ('change_sa', 'Can change SA connected to IP'), ('lock_sa', 'Can lock SA to IP'), ('unlock_profile', 'Can unlock profile connected to IP'), ('receive', 'Can receive IP'), ('preserve', 'Can preserve IP'), ('view', 'Can view extracted IP'), ('view_tar', 'Can view packaged IP'), ('edit_as_new', 'Can edit IP "as new"'), ('diff-check', 'Can diff-check IP'), ('query', 'Can query IP')), 'verbose_name': 'Information Package'},
        ),
    ]
