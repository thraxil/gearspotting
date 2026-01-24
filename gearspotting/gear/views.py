from typing import Any, Dict, Type

from django.contrib.contenttypes.forms import generic_inlineformset_factory
from django.forms import ModelForm
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from gearspotting.link.models import Link
from gearspotting.manufacturer.models import Manufacturer, ManufacturerForm
from gearspotting.photo.models import Photo
from gearspotting.tag.models import Tag
from gearspotting.utils.views import AddSomethingView, EditSomethingView

from .models import Gear


class GearTagView(TemplateView):
    template_name = "gear/gear_tag_list.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        tag = kwargs.get("tag", "")
        t = get_object_or_404(Tag, slug=tag)
        geartags = t.geartag_set.all().prefetch_related(
            "gear", "gear__manufacturer"
        )
        return dict(tag=tag, gear_list=geartags)


class IndexView(TemplateView):
    template_name = "gear/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        manufacturers = Manufacturer.objects.all().prefetch_related("gear_set")
        return dict(
            manufacturers=manufacturers,
            add_manufacturer_form=ManufacturerForm(),
        )


class GearDetailView(DetailView):
    slug_field = "slug"
    model = Gear

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        photos = self.object.gearphoto_set.all().prefetch_related("photo")
        context.update(
            dict(
                photos=photos,
                object=self.object,
            )
        )
        return context


class TagsView(TemplateView):
    template_name = "gear/tags.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        tags = (
            Tag.objects.filter(geartag__isnull=False)
            .distinct()
            .order_by("name")
        )
        return dict(tags=tags)


class AddLinkView(AddSomethingView):
    template_name = "gear/add_link.html"
    model = Gear
    context_obj_name = "gear"

    def get_form(self, gear: Gear) -> Type[ModelForm]:
        return gear.add_link_form()


class AddPhotoView(AddSomethingView):
    template_name = "gear/add_photo.html"
    model = Gear
    context_obj_name = "gear"

    def get_form(self, gear: Gear) -> Type[ModelForm]:
        return gear.add_photo_form()


class EditLinksView(EditSomethingView):
    model = Gear

    def get_formset(self) -> Any:
        return generic_inlineformset_factory(Link, extra=1)


class EditPhotosView(EditSomethingView):
    model = Gear

    def get_formset(self) -> Any:
        return generic_inlineformset_factory(Photo, extra=1)
