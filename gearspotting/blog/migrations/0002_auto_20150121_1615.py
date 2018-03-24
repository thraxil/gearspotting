# flake8: noqa
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
        ('gear', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmusician',
            name='musician',
            field=models.ForeignKey(to='musician.Musician', on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postmusician',
            name='post',
            field=models.ForeignKey(to='blog.Post', on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postgear',
            name='gear',
            field=models.ForeignKey(to='gear.Gear', on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postgear',
            name='post',
            field=models.ForeignKey(to='blog.Post', on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
