# flake8: noqa
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('url', models.URLField()),
                ('description', models.TextField(default=b'', blank=True)),
                ('object_id', models.PositiveIntegerField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
