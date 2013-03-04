from gearspotting.photo.models import ImportPhotoForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from restclient import GET
from django.conf import settings
import os
import os.path
from datetime import datetime
import gearspotting.musician.models
import gearspotting.gear.models
import gearspotting.manufacturer.models as manmodels
import re


class rendered_with(object):
    def __init__(self, template_name):
        self.template_name = template_name

    def __call__(self, func):
        def rendered_func(request, *args, **kwargs):
            items = func(request, *args, **kwargs)
            if isinstance(items, dict):
                return render_to_response(
                    self.template_name,
                    items,
                    context_instance=RequestContext(request))
            else:
                return items
        return rendered_func


def clean_filename(filename):
    filename = filename.replace("%20", "_")
    filename = filename.replace("%25", "_")
    filename = filename.replace(' ', '_')
    filename = filename.replace('%', '_')
    (base, ext) = os.path.splitext(filename)
    base = base[:75]
    filename = base + ext
    return filename.lower()


@rendered_with('photo/import_photo.html')
def import_photo(request):
    form = ImportPhotoForm()
    if request.method == "POST":
        form = ImportPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            p = form.save(commit=False)
            url = request.POST.get('url', '')
            if " " in url:
                url = url.replace(" ", "%20")
            filename = url.split("/")[-1]
            if "?" in filename:
                filename = re.sub(r'(\?.*)$', '', filename)
            if "#" in filename:
                filename = re.sub(r'(\#.*)$', '', filename)

            imgdata = GET(url)

            filename = clean_filename(filename)
            now = datetime.now()
            rel_path = "images/%04d/%02d/%02d/" % (now.year,
                                                   now.month,
                                                   now.day)
            path = os.path.join(settings.MEDIA_ROOT, rel_path)
            try:
                os.makedirs(path)
            except:
                pass
            f = open(os.path.join(path, filename), "wb")
            f.write(imgdata)
            f.close()
            p.image = os.path.join(rel_path, filename)
            p.save()

            for line in request.POST.get('musicians', '').split('\n'):
                mline = line.strip()
                if not mline:
                    continue
                m, created = musician.models.Musician.objects.get_or_create(
                    name=mline)
                musician.models.MusicianPhoto.objects.create(
                    musician=m, photo=p)

            for line in request.POST.get('gear', '').split('\n'):
                gearline = line.strip()
                if not gearline:
                    continue
                split_char = ' '
                if ':' in gearline:
                    split_char = ':'
                if split_char in gearline:
                    parts = gearline.split(split_char)
                    manufacturer_name = parts[0].strip()
                    gear_name = ' '.join(parts[1:]).strip()

                    (manufacturer,
                     created) = manmodels.Manufacturer.objects.get_or_create(
                         name=manufacturer_name)
                    g, created = gear.models.Gear.objects.get_or_create(
                        manufacturer=manufacturer, name=gear_name)
                    gear.models.GearPhoto.objects.create(gear=g, photo=p)
            return HttpResponseRedirect(p.get_absolute_url())

    return dict(url=request.GET.get('url', ''),
                form=form)
