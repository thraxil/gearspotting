# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='extension',
            field=models.CharField(default=b'jpg', max_length=256),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='reticulum_key',
            field=models.CharField(default=b'', max_length=256),
            preserve_default=True,
        ),
    ]
