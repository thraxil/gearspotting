# flake8: noqa
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
        ('gear', '0001_initial'),
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicianGear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('gear', models.ForeignKey(to='gear.Gear', on_delete=models.CASCADE)),
                ('musician', models.ForeignKey(to='musician.Musician', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MusicianGearPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('musiciangear', models.ForeignKey(to='musiciangear.MusicianGear', on_delete=models.CASCADE)),
                ('photo', models.ForeignKey(to='photo.Photo', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
