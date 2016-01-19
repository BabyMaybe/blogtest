# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0010_auto_20151217_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('os', models.CharField(max_length=200, choices=[(b'OSX', b'Mac OSX'), (b'WINDOWS', b'Windows'), (b'LINUX', b'Linux'), (b'OTHER', b'Something Else')])),
                ('browser', models.CharField(max_length=200, choices=[(b'CHROME', b'Google Chrome'), (b'FIREFOX', b'Mozilla Firefox'), (b'SAFARI', b'Apple Safari'), (b'IE', b'Internet Explorer'), (b'EDGE', b'Microsoft Edge'), (b'OTHER', b'Something Else')])),
                ('bug', models.TextField()),
                ('steps', models.TextField(null=True, blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='xmas',
            name='animal',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='authors',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='books',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='candy',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='color1',
            field=colorful.fields.RGBColorField(default=b'#000000', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='color2',
            field=colorful.fields.RGBColorField(default=b'#000000', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='color3',
            field=colorful.fields.RGBColorField(default=b'#000000', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='color4',
            field=colorful.fields.RGBColorField(default=b'#000000', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='color5',
            field=colorful.fields.RGBColorField(default=b'#000000', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='dress',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='drink',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='games',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='hat',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='learning',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='pants',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='shirt',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='shoe',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='xmas',
            name='systems',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='color',
            field=colorful.fields.RGBColorField(default=b'#DDF271', null=True, blank=True),
        ),
        migrations.RemoveField(
            model_name='xmas',
            name='snitch_on',
        ),
        migrations.AddField(
            model_name='xmas',
            name='snitch_on',
            field=models.OneToOneField(related_name='snitch', default=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
