# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', unique=True, max_length=256)),
                ('slug', models.SlugField(max_length=256, editable=False)),
                ('description', models.TextField(default=b'', blank=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
    ]
