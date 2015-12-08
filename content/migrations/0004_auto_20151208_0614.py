# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20151208_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='color',
            field=colorful.fields.RGBColorField(default=b'#FDE961', null=True, blank=True),
        ),
    ]
