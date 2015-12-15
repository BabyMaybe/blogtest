# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_auto_20151215_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='addr_state',
            field=models.CharField(default=b'NA', max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='color',
            field=colorful.fields.RGBColorField(default=b'#4E8BF6', null=True, blank=True),
        ),
    ]
