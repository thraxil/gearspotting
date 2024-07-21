from django.contrib.contenttypes.admin import generic_inlineformset_factory
from django.views.generic.base import TemplateView

from gearspotting.manufacturer.models import Manufacturer, ManufacturerForm
from gearspotting.utils.views import AddSomethingView, EditSomethingView

from .models import Gear, Link, Photo


class GearTagView(TemplateView):
    template_name = "gear/gear_tag_list.html"

    def get_context_data(self, tag=""):
        return dict(
            tag=tag, gear_list=Gear.objects.filter(tags__name__in=[tag])
        )


class IndexView(TemplateView):
    template_name = "gear/index.html"

    def get_context_data(self):
        manufacturers = Manufacturer.objects.all().prefetch_related("gear_set")
        return dict(
            manufacturers=manufacturers,
            add_manufacturer_form=ManufacturerForm(),
        )


class TagsView(TemplateView):
    template_name = "gear/tags.html"


class AddLinkView(AddSomethingView):
    template_name = "gear/add_link.html"
    model = Gear
    context_obj_name = "gear"

    def get_form(self, gear):
        return gear.add_link_form()


class AddPhotoView(AddSomethingView):
    template_name = "gear/add_photo.html"
    model = Gear
    context_obj_name = "gear"

    def get_form(self, gear):
        return gear.add_photo_form()


class EditLinksView(EditSomethingView):
    model = Gear

    def get_formset(self):
        return generic_inlineformset_factory(Link, extra=1)


class EditPhotosView(EditSomethingView):
    model = Gear

    def get_formset(self):
        generic_inlineformset_factory(Photo, extra=1)
