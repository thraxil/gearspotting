from models import Manufacturer, ManufacturerForm
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

@rendered_with('gear/index.html')
def index(request):
    return dict(manufacturers=Manufacturer.objects.all(),
                add_manufacturer_form=ManufacturerForm())

def add_manufacturer(request):
    if request.method == "POST":
        f = ManufacturerForm(request.POST)
        if f.is_valid():
            m = f.save()
    return HttpResponseRedirect("/gear/")
