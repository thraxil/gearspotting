# Create your views here.
from photo.models import Photo,AddPhotoForm,ImportPhotoForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.contenttypes import generic
from django.forms.models import inlineformset_factory
from django.template import RequestContext
from django.shortcuts import render_to_response
import urllib2
from restclient import GET
from django.conf import settings
import cStringIO
import os
from datetime import datetime
import musician.models
import gear.models
import manufacturer.models as manmodels

class rendered_with(object):
    def __init__(self, template_name):
        self.template_name = template_name

    def __call__(self, func):
        def rendered_func(request, *args, **kwargs):
            items = func(request, *args, **kwargs)
            if type(items) == type({}):
                return render_to_response(self.template_name, items, context_instance=RequestContext(request))
            else:
                return items
        return rendered_func



@rendered_with('photo/import_photo.html')
def import_photo(request):
    form = ImportPhotoForm()
    if request.method == "POST":
        form = ImportPhotoForm(request.POST,request.FILES)
        if form.is_valid():
            p = form.save(commit=False)
            url = request.POST.get('url','')
            if " " in url:
                url = url.replace(" ","%20")
            filename = url.split("/")[-1]
            if "?" in filename:
                filename = re.sub(r'(\?.*)$','',filename)
            if "#" in filename:
                filename = re.sub(r'(\#.*)$','',filename)

            imgdata = GET(url)
            ext = ".jpg"
            try:
                ext = "." + filename.split(".")[-1].lower()
            except:
                # bad filename
                pass

            now = datetime.now()
            rel_path = "images/%04d/%02d/%02d/" % (now.year,now.month,now.day)
            path = os.path.join(settings.MEDIA_ROOT,rel_path)
            try:
                os.makedirs(path)
            except:
                pass
            f = open(os.path.join(path,filename),"wb")
            f.write(imgdata)
            f.close()
            p.image = os.path.join(rel_path,filename)
            p.save()

            for line in request.POST.get('musicians','').split('\n'):
                mline = line.strip()
                if not mline:
                    continue
                m,created = musician.models.Musician.objects.get_or_create(name=mline)
                mp = musician.models.MusicianPhoto.objects.create(musician=m,photo=p)

            for line in request.POST.get('gear','').split('\n'):
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

                    manufacturer,created = manmodels.Manufacturer.objects.get_or_create(name=manufacturer_name)
                    g,created = gear.models.Gear.objects.get_or_create(manufacturer=manufacturer,name=gear_name)
                    gp = gear.models.GearPhoto.objects.create(gear=g,photo=p)
                
            return HttpResponseRedirect(p.get_absolute_url())
            
    return dict(url=request.GET.get('url',''),
                form=form)
