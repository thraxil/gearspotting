#from gear.models import Gear
#from musician.models import Musician
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
#from threadedcomments.models import ThreadedComment


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

@rendered_with("homepage.html")
def index(request):
    return dict()
 #   return dict(newest_gear=Gear.objects.all().order_by("-added")[:10],
#                newest_musicians=Musician.objects.all().order_by("-added")[:10],
#                newest_comments=ThreadedComment.objects.all().order_by("-date_submitted")[:10])
