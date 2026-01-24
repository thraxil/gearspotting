import os
import os.path
import re
from io import BytesIO

import requests
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View

import gearspotting.gear.models as gear
import gearspotting.manufacturer.models as manmodels
import gearspotting.musician.models as musician
from gearspotting.photo.models import ImportPhotoForm


def clean_filename(filename):
    filename = filename.replace("%20", "_")
    filename = filename.replace("%25", "_")
    filename = filename.replace(" ", "_")
    filename = filename.replace("%", "_")
    (base, ext) = os.path.splitext(filename)
    base = base[:75]
    filename = base + ext
    return filename.lower()


def url_to_filename(url):
    if " " in url:
        url = url.replace(" ", "%20")
    filename = url.split("/")[-1]
    if "?" in filename:
        filename = re.sub(r"(\?.*)$", "", filename)
    if "#" in filename:
        filename = re.sub(r"(\#.*)$", "", filename)
    return filename


def mdirs(path):
    try:
        os.makedirs(path)
    except Exception:  # nosec
        pass


def make_musicians_and_mphotos(text, p):
    for line in text.split("\n"):
        mline = line.strip()
        if not mline:
            continue
        m, created = musician.Musician.objects.get_or_create(name=mline)
        musician.MusicianPhoto.objects.create(musician=m, photo=p)


def process_gearline(line, p):
    gearline = line.strip()
    if not gearline:
        return
    split_char = " "
    if ":" in gearline:
        split_char = ":"
    if split_char not in gearline:
        return
    parts = gearline.split(split_char)
    manufacturer_name = parts[0].strip()
    gear_name = " ".join(parts[1:]).strip()

    (manufacturer, created) = manmodels.Manufacturer.objects.get_or_create(
        name=manufacturer_name
    )
    g, created = gear.Gear.objects.get_or_create(
        manufacturer=manufacturer, name=gear_name
    )
    gear.GearPhoto.objects.create(gear=g, photo=p)


def save_image(form, url):
    p = form.save(commit=False)
    filename = url_to_filename(url)
    ext = os.path.splitext(filename)[1].lower()

    r = requests.get(url, timeout=10)
    imgobj = BytesIO()
    for chunk in r.iter_content(1024):
        imgobj.write(chunk)
    imgobj.seek(0)
    files = {"image": ("image" + ext, imgobj)}
    r = requests.post(settings.RETICULUM_BASE, files=files, timeout=10)
    rhash = r.json()["hash"]

    p.reticulum_key = rhash
    p.extension = ext
    p.save()
    return p


class ImportPhotoView(View):
    template_name = "photo/import_photo.html"

    def get(self, request):
        form = ImportPhotoForm()
        return render(
            request,
            self.template_name,
            dict(url=request.GET.get("url", ""), form=form),
        )

    def post(self, request):
        form = ImportPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            p = save_image(form, request.POST.get("url", ""))
            make_musicians_and_mphotos(request.POST.get("musicians", ""), p)

            for line in request.POST.get("gear", "").split("\n"):
                process_gearline(line, p)
            return HttpResponseRedirect(p.get_absolute_url())
