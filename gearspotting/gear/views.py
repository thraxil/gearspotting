from models import Gear, Link, Photo
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.contenttypes import generic
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView

from gearspotting.manufacturer.models import Manufacturer, ManufacturerForm


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


class GearTagView(TemplateView):
    template_name = "gear/gear_tag_list.html"
    def get_context_data(self, tag=""):
        return dict(tag=tag,
                    gear_list=Gear.objects.filter(tags__name__in=[tag]))


@rendered_with('gear/index.html')
def index(request):
    return dict(manufacturers=Manufacturer.objects.all(),
                add_manufacturer_form=ManufacturerForm())


@rendered_with('gear/tags.html')
def tags(request):
    return dict()


@rendered_with('gear/add_link.html')
def add_link(request, slug):
    gear = get_object_or_404(Gear, slug=slug)
    form = gear.add_link_form()
    if request.method == "POST":
        f = form(request.POST)
        if f.is_valid():
            l = f.save(commit=False)
            l.content_object = gear
            l.save()
            return HttpResponseRedirect(gear.get_absolute_url())
    else:
        f = form()
    return dict(gear=gear, form=f)


@rendered_with('gear/add_photo.html')
def add_photo(request, slug):
    gear = get_object_or_404(Gear, slug=slug)
    form = gear.add_photo_form()
    if request.method == "POST":
        f = form(request.POST, request.FILES)
        if f.is_valid():
            p = f.save(commit=False)
            p.content_object = gear
            p.save()
            return HttpResponseRedirect(gear.get_absolute_url())
    else:
        f = form()
    return dict(gear=gear, form=f)


def edit_links(request, slug):
    gear = get_object_or_404(Gear, slug=slug)
    LinksFormset = generic.generic_inlineformset_factory(Link, extra=1)
    if request.method == 'POST':
        formset = LinksFormset(request.POST, request.FILES, instance=gear)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(gear.get_absolute_url())


def edit_photos(request, slug):
    gear = get_object_or_404(Gear, slug=slug)
    PhotosFormset = generic.generic_inlineformset_factory(Photo, extra=1)
    if request.method == 'POST':
        formset = PhotosFormset(request.POST, request.FILES, instance=gear)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(gear.get_absolute_url())
