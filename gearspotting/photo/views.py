from gearspotting.photo.models import ImportPhotoForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from restclient import GET
from django.conf import settings
import os
import os.path
from datetime import datetime
import gearspotting.musician.models as musician
import gearspotting.gear.models as gear
import gearspotting.manufacturer.models as manmodels
import re


def clean_filename(filename):
    filename = filename.replace("%20", "_")
    filename = filename.replace("%25", "_")
    filename = filename.replace(' ', '_')
    filename = filename.replace('%', '_')
    (base, ext) = os.path.splitext(filename)
    base = base[:75]
    filename = base + ext
    return filename.lower()


def url_to_filename(url):
    if " " in url:
        url = url.replace(" ", "%20")
    filename = url.split("/")[-1]
    if "?" in filename:
        filename = re.sub(r'(\?.*)$', '', filename)
    if "#" in filename:
        filename = re.sub(r'(\#.*)$', '', filename)
    return filename


def mdirs(path):
    try:
        os.makedirs(path)
    except:
        pass


def make_musicians_and_mphotos(text, p):
    for line in text.split('\n'):
        mline = line.strip()
        if not mline:
            continue
        m, created = musician.models.Musician.objects.get_or_create(
            name=mline)
        musician.models.MusicianPhoto.objects.create(
            musician=m, photo=p)


def process_gearline(line, p):
    gearline = line.strip()
    if not gearline:
        return
    split_char = ' '
    if ':' in gearline:
        split_char = ':'
    if split_char not in gearline:
        return
    parts = gearline.split(split_char)
    manufacturer_name = parts[0].strip()
    gear_name = ' '.join(parts[1:]).strip()

    (manufacturer,
     created) = manmodels.Manufacturer.objects.get_or_create(
         name=manufacturer_name)
    g, created = gear.models.Gear.objects.get_or_create(
        manufacturer=manufacturer, name=gear_name)
    gear.models.GearPhoto.objects.create(gear=g, photo=p)


def save_image(form, url):
    p = form.save(commit=False)
    filename = url_to_filename(url)
    imgdata = GET(url)

    filename = clean_filename(filename)
    now = datetime.now()
    rel_path = "images/%04d/%02d/%02d/" % (now.year,
                                           now.month,
                                           now.day)
    path = os.path.join(settings.MEDIA_ROOT, rel_path)
    mdirs(path)
    f = open(os.path.join(path, filename), "wb")
    f.write(imgdata)
    f.close()
    p.image = os.path.join(rel_path, filename)
    p.save()
    return p


class ImportPhotosView(View):
    template_name = 'photo/import_photo.html'

    def get(self, request):
        form = ImportPhotoForm()
        return render(
            request, self.template_name,
            dict(url=request.GET.get('url', ''),
                 form=form))

    def post(self, request):
        form = ImportPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            p = save_image(form, request.POST.get('url', ''))
            make_musicians_and_mphotos(request.POST.get('musicians', ''), p)

            for line in request.POST.get('gear', '').split('\n'):
                process_gearline(line, p)
            return HttpResponseRedirect(p.get_absolute_url())
