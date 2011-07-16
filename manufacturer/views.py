from models import Manufacturer, Link
from gear.models import AddGearForm
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

@rendered_with('manufacturer/add_link.html')
def add_link(request,slug):
    manufacturer = get_object_or_404(Manufacturer,slug=slug)
    form = manufacturer.add_link_form()
    if request.method == "POST":
        f = form(request.POST)
        if f.is_valid():
            l = f.save(commit=False)
            l.content_object = manufacturer
            l.save()
            return HttpResponseRedirect(manufacturer.get_absolute_url())
    else:
        f = form()
    return dict(manufacturer=manufacturer,form=f)

def edit_links(request,slug):
    manufacturer = get_object_or_404(Manufacturer,slug=slug)
    LinksFormset = generic.generic_inlineformset_factory(Link, extra=1)
    if request.method == 'POST':
        formset = LinksFormset(request.POST, request.FILES,instance=manufacturer)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(manufacturer.get_absolute_url())

@rendered_with('manufacturer/add_gear.html')
def add_gear(request,slug):
    manufacturer = get_object_or_404(Manufacturer,slug=slug)
    form = manufacturer.add_gear_form()
    if request.method == "POST":
        f = form(request.POST,request.FILES)
        if f.is_valid():
            g = f.save(commit=False)
            g.manufacturer = manufacturer
            g.save()
            return HttpResponseRedirect(manufacturer.get_absolute_url())
    else:
        f = form()
    return dict(manufacturer=manufacturer,form=f)
