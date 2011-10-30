# Create your views here.
from photo.models import Photo
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



@rendered_with('photo/import_photo.html')
def import_photo(request):
    if request.method == "POST":
        pass
    return dict(url=request.GET.get('url',''))
