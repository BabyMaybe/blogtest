# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0009_auto_20151215_0547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xmas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(null=True, blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('addr_street', models.CharField(default=b'None', max_length=500, null=True, blank=True)),
                ('addr_city', models.CharField(default=b'None', max_length=200, null=True, blank=True)),
                ('addr_state', models.CharField(default=b'NA', max_length=2, null=True, blank=True)),
                ('addr_zip', models.IntegerField(null=True, blank=True)),
                ('movies', models.TextField(null=True, blank=True)),
                ('giftee', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('snitch_on', models.ManyToManyField(related_name='snitch', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='color',
            field=colorful.fields.RGBColorField(default=b'#8DD918', null=True, blank=True),
        ),
    ]
