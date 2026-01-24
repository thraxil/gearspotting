from typing import Any, Dict, Type

from django.contrib.contenttypes.forms import generic_inlineformset_factory
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView

from gearspotting.link.models import Link
from gearspotting.photo.models import Photo
from gearspotting.tag.models import Tag
from gearspotting.utils.views import AddSomethingView, EditSomethingView

from .models import Musician


class MusicianDetailView(DetailView):
    model = Musician

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data["tags"] = self.object.musiciantag_set.all().prefetch_related(
            "tag"
        )
        data["gear"] = self.object.musiciangear_set.all().prefetch_related(
            "gear",
            "gear__manufacturer",
        )

        data["photos"] = self.object.musicianphoto_set.all().prefetch_related(
            "photo"
        )
        return data


class MusicianTagView(TemplateView):
    template_name = "musician/musician_tag_list.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        tag = kwargs.get("tag", "")
        t = get_object_or_404(Tag, slug=tag)
        musicians = t.musiciantag_set.all().prefetch_related("musician")
        return dict(tag=tag, musicians=musicians)


class TagsView(TemplateView):
    template_name = "musician/tags.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        tags = (
            Tag.objects.filter(musiciantag__isnull=False)
            .distinct()
            .order_by("name")
        )
        return dict(tags=tags)


class AddLinkView(AddSomethingView):
    template_name = "musician/add_link.html"
    model = Musician
    context_obj_name = "musician"

    def get_form(self, musician: Musician) -> Type[ModelForm]:
        return musician.add_link_form()


class AddPhotoView(AddSomethingView):
    template_name = "musician/add_photo.html"
    model = Musician
    context_obj_name = "musician"

    def get_form(self, musician: Musician) -> Type[ModelForm]:
        return musician.add_photo_form()


class AddGearView(View):
    template_name = "musician/add_gear.html"
    model = Musician

    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        musician = get_object_or_404(self.model, slug=slug)
        form = musician.add_gear_form()()
        return render(
            request, self.template_name, {"form": form, "musician": musician}
        )

    def post(self, request: HttpRequest, slug: str) -> HttpResponse:
        musician = get_object_or_404(self.model, slug=slug)
        Form = musician.add_gear_form()
        form = Form(request.POST)
        if form.is_valid():
            musiciangear = form.save(commit=False)
            musiciangear.musician = musician
            musiciangear.save()
            return HttpResponseRedirect(musician.get_absolute_url())
        return render(
            request, self.template_name, {"form": form, "musician": musician}
        )


class EditLinksView(EditSomethingView):
    model = Musician

    def get_formset(self) -> Any:
        return generic_inlineformset_factory(Link, extra=1)


class EditPhotosView(EditSomethingView):
    model = Musician

    def get_formset(self) -> Any:
        return generic_inlineformset_factory(Photo, extra=1)


class EditGearView(EditSomethingView):
    model = Musician

    def get_formset(self) -> Any:
        from gearspotting.musiciangear.models import MusicianGear

        return inlineformset_factory(Musician, MusicianGear, extra=1)
