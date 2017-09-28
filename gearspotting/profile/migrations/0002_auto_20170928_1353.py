# flake8: noqa
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='privacy',
            field=models.CharField(verbose_name='privacy', help_text='Designates who can view your profile.', choices=[('open', 'Open'), ('registered', 'Registered'), ('closed', 'Closed')], default='open', max_length=15),
        ),
    ]
