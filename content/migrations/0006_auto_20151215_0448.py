# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import colorful.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20151210_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 15, 4, 48, 4, 348325, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='addr_city',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='addr_state',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='addr_street',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='addr_zip',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='color',
            field=colorful.fields.RGBColorField(default=b'#E2FB58', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='prof_h',
            field=models.IntegerField(default=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='prof_w',
            field=models.IntegerField(default=200, null=True, blank=True),
        ),
    ]
