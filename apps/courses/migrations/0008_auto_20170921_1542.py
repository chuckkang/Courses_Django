# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 22:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='course',
            new_name='coursecomment',
        ),
    ]
