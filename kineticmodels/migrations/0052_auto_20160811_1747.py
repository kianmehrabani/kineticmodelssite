# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-11 17:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kineticmodels', '0051_auto_20160811_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thermo',
            old_name='preferred_key',
            new_name='preferredKey',
        ),
    ]
