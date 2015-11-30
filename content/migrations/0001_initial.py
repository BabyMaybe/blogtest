# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import content.models
import colorful.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_author', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now_add=True, null=True)),
                ('content', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('like_count', models.IntegerField(default=0)),
                ('author', models.ForeignKey(related_name='comment_author', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='comment_likes', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now_add=True, null=True)),
                ('comment_count', models.IntegerField(default=0)),
                ('like_count', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(related_name='post_author', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'ordering': ['-date_published'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField()),
                ('birthday', models.DateField()),
                ('addr_street', models.CharField(max_length=500)),
                ('addr_city', models.CharField(max_length=200)),
                ('addr_state', models.CharField(max_length=2, null=True)),
                ('addr_zip', models.IntegerField()),
                ('prof_pic', models.ImageField(height_field=b'prof_h', width_field=b'prof_w', null=True, upload_to=content.models.generate_image_path, blank=True)),
                ('prof_h', models.IntegerField(default=200, null=True)),
                ('prof_w', models.IntegerField(default=200, null=True)),
                ('color', colorful.fields.RGBColorField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_post',
            field=models.ForeignKey(related_name='parent_post', to='content.Post'),
        ),
    ]
