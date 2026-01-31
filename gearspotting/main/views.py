from typing import Any, Dict

from django.views.generic.base import TemplateView

from gearspotting.blog.models import Post
from gearspotting.gear.models import Gear
from gearspotting.musician.models import Musician


class IndexView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return dict(
            newest_gear=Gear.objects.select_related("manufacturer").order_by(
                "-added"
            )[:10],
            newest_musicians=Musician.objects.all().order_by("-added")[:10],
            newest_posts=Post.objects.all()[:10],
        )


class TagsView(TemplateView):
    template_name = "main/tags.html"


class SearchView(TemplateView):
    template_name = "main/search.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        q = self.request.GET.get("q", None)
        results: Dict[str, Any] = {}
        if q is not None:
            results["gear"] = Gear.objects.filter(name__icontains=q)
            results["musicians"] = Musician.objects.filter(name__icontains=q)
        return dict(q=q, results=results)
