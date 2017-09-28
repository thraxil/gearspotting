# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='description',
            field=models.TextField(default='', blank=True),
        ),
    ]
