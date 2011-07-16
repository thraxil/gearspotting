from models import Musician, Link, Photo
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.contenttypes import generic
from django.forms.models import inlineformset_factory
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

@rendered_with('musician/tags.html')
def tags(request):
    return dict()

@rendered_with('musician/add_link.html')
def add_link(request,slug):
    musician = get_object_or_404(Musician,slug=slug)
    form = musician.add_link_form()
    if request.method == "POST":
        f = form(request.POST)
        if f.is_valid():
            l = f.save(commit=False)
            l.content_object = musician
            l.save()
            return HttpResponseRedirect(musician.get_absolute_url())
    else:
        f = form()
    return dict(musician=musician,form=f)

@rendered_with('musician/add_photo.html')
def add_photo(request,slug):
    musician = get_object_or_404(Musician,slug=slug)
    form = musician.add_photo_form()
    if request.method == "POST":
        f = form(request.POST,request.FILES)
        if f.is_valid():
            p = f.save(commit=False)
            p.content_object = musician
            p.save()
            return HttpResponseRedirect(musician.get_absolute_url())
    else:
        f = form()
    return dict(musician=musician,form=f)

@rendered_with('musician/add_gear.html')
def add_gear(request,slug):
    musician = get_object_or_404(Musician,slug=slug)
    form = musician.add_gear_form()
    if request.method == "POST":
        f = form(request.POST,request.FILES)
        if f.is_valid():
            g = f.save(commit=False)
            g.musician = musician
            g.save()
            return HttpResponseRedirect(musician.get_absolute_url())
    else:
        f = form()
    return dict(musician=musician,form=f)


def edit_links(request,slug):
    musician = get_object_or_404(Musician,slug=slug)
    LinksFormset = generic.generic_inlineformset_factory(Link, extra=1)
    if request.method == 'POST':
        formset = LinksFormset(request.POST, request.FILES,instance=musician)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(musician.get_absolute_url())

def edit_photos(request,slug):
    musician = get_object_or_404(Musician,slug=slug)
    PhotosFormset = generic.generic_inlineformset_factory(Photo, extra=1)
    if request.method == 'POST':
        formset = PhotosFormset(request.POST, request.FILES,instance=musician)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(musician.get_absolute_url())


def edit_gear(request,slug):
    musician = get_object_or_404(Musician,slug=slug)
    from musiciangear.models import MusicianGear
    GearFormSet = inlineformset_factory(Musician, MusicianGear,extra=1)
    if request.method == 'POST':
        formset = GearFormSet(request.POST, request.FILES,instance=musician)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(musician.get_absolute_url())
