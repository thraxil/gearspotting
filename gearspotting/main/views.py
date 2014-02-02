from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from gearspotting.gear.models import Gear
from gearspotting.musician.models import Musician
from gearspotting.blog.models import Post


class rendered_with(object):
    def __init__(self, template_name):
        self.template_name = template_name

    def __call__(self, func):
        def rendered_func(request, *args, **kwargs):
            items = func(request, *args, **kwargs)
            if isinstance(items, dict):
                return render_to_response(
                    self.template_name, items,
                    context_instance=RequestContext(request))
            else:
                return items
        return rendered_func


class IndexView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self):
        return dict(
            newest_gear=Gear.objects.all().order_by("-added")[:10],
            newest_musicians=Musician.objects.all().order_by("-added")[:10],
            newest_posts=Post.objects.all()[:10],
        )


@rendered_with('main/tags.html')
def tags(request):
    return dict()


@rendered_with("main/search.html")
def search(request):
    q = request.GET.get('q', None)
    results = dict()
    if q is not None:
        results["gear"] = Gear.objects.filter(name__icontains=q)
        results["musicians"] = Musician.objects.filter(name__icontains=q)
    return dict(q=q, results=results)
