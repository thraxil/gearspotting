# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiciangear', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musiciangear',
            name='description',
            field=models.TextField(default='', blank=True),
        ),
    ]
