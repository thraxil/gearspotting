# flake8: noqa
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20150522_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image',
        ),
    ]
