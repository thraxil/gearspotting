# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', sorl.thumbnail.fields.ImageWithThumbnailsField(upload_to=b'images/%Y/%m/%d')),
                ('caption', models.TextField(default=b'', blank=True)),
                ('source_name', models.CharField(default=b'', max_length=256, blank=True)),
                ('source_url', models.URLField(blank=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
