# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

import requests
from django.conf import settings
from django.db import migrations


def upload_to_reticulum(apps, schema_editor):
    Photo = apps.get_model("photo", "Photo")
    for photo in Photo.objects.all():
        fullpath = photo.image.path
        ext = os.path.splitext(fullpath)[1].lower()
        files = {
            'image': ("image%s" % ext, open(fullpath, 'rb'))
        }
        r = requests.post(settings.RETICULUM_BASE, files=files)
        photo.reticulum_key = r.json()["hash"]
        photo.extension = ext
        photo.save()
        print(fullpath)


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20150522_1658'),
    ]

    operations = [
        migrations.RunPython(upload_to_reticulum)
    ]
