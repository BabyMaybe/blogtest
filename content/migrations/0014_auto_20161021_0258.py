# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-21 02:58
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_auto_20160121_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='color',
            field=colorful.fields.RGBColorField(blank=True, default=b'#C041BC', null=True),
        ),
    ]