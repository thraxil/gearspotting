# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='description',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=256, default='', unique=True),
        ),
    ]
