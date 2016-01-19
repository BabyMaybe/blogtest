# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_auto_20160119_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugreport',
            name='feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='color',
            field=colorful.fields.RGBColorField(default=b'#CA5082', null=True, blank=True),
        ),
    ]
