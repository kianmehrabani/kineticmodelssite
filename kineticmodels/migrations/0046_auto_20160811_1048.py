# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-11 10:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kineticmodels', '0045_auto_20160811_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transport',
            old_name='collision_diameter',
            new_name='collisionDiameter',
        ),
    ]
