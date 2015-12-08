# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20151206_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='color',
            field=colorful.fields.RGBColorField(default=b'#829748', null=True, blank=True),
        ),
    ]
