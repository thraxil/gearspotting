# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_remove_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='extension',
            field=models.CharField(max_length=256, default='jpg'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='reticulum_key',
            field=models.CharField(max_length=256, default=''),
        ),
        migrations.AlterField(
            model_name='photo',
            name='source_name',
            field=models.CharField(max_length=256, default='', blank=True),
        ),
    ]
