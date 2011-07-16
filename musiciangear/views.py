from models import MusicianGear, Link, Photo
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.contenttypes import generic
from django.template import RequestContext
from django.shortcuts import render_to_response

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

@rendered_with('musiciangear/add_link.html')
def add_link(request,id):
    musiciangear = get_object_or_404(MusicianGear,id=id)
    form = musiciangear.add_link_form()
    if request.method == "POST":
        f = form(request.POST)
        if f.is_valid():
            l = f.save(commit=False)
            l.content_object = musiciangear
            l.save()
            return HttpResponseRedirect(musiciangear.get_absolute_url())
    else:
        f = form()
    return dict(musiciangear=musiciangear,form=f)

@rendered_with('musiciangear/add_photo.html')
def add_photo(request,id):
    musiciangear = get_object_or_404(MusicianGear,id=id)
    form = musiciangear.add_photo_form()
    if request.method == "POST":
        f = form(request.POST,request.FILES)
        if f.is_valid():
            p = f.save(commit=False)
            p.content_object = musiciangear
            p.save()
            return HttpResponseRedirect(musiciangear.get_absolute_url())
    else:
        f = form()
    return dict(musiciangear=musiciangear,form=f)

def edit_links(request,id):
    musiciangear = get_object_or_404(MusicianGear,id=id)
    LinksFormset = generic.generic_inlineformset_factory(Link, extra=1)
    if request.method == 'POST':
        formset = LinksFormset(request.POST, request.FILES,instance=musiciangear)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(musiciangear.get_absolute_url())

def edit_photos(request,id):
    musiciangear = get_object_or_404(MusicianGear,id=id)
    PhotosFormset = generic.generic_inlineformset_factory(Photo, extra=1)
    if request.method == 'POST':
        formset = PhotosFormset(request.POST, request.FILES,instance=musiciangear)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(musiciangear.get_absolute_url())
