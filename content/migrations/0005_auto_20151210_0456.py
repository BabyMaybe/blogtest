# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20151208_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='display_author',
            field=models.CharField(default=b'anonymous coward', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='color',
            field=colorful.fields.RGBColorField(default=b'#F4B8F9', null=True, blank=True),
        ),
    ]
