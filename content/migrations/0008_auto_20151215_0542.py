# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20151215_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='addr_city',
            field=models.CharField(default=b'None', max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='addr_state',
            field=models.CharField(default=b'None', max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='addr_street',
            field=models.CharField(default=b'None', max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='color',
            field=colorful.fields.RGBColorField(default=b'#4525AF', null=True, blank=True),
        ),
    ]
