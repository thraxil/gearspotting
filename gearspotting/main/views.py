from django.views.generic.base import TemplateView
from gearspotting.gear.models import Gear
from gearspotting.musician.models import Musician
from gearspotting.blog.models import Post


class IndexView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self):
        return dict(
            newest_gear=Gear.objects.all().order_by("-added")[:10],
            newest_musicians=Musician.objects.all().order_by("-added")[:10],
            newest_posts=Post.objects.all()[:10],
        )


class TagsView(TemplateView):
    template_name = "main/tags.html"


class SearchView(TemplateView):
    template_name = "main/search.html"

    def get_context_data(self):
        q = self.request.GET.get('q', None)
        results = dict()
        if q is not None:
            results["gear"] = Gear.objects.filter(name__icontains=q)
            results["musicians"] = Musician.objects.filter(name__icontains=q)
        return dict(q=q, results=results)
