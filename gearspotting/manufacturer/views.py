from models import Manufacturer, Link
from django.contrib.contenttypes import generic

from gearspotting.utils.views import AddSomethingView, EditSomethingView


class AddLinkView(AddSomethingView):
    template_name = "manufacturer/add_link.html"
    model = Manufacturer
    context_obj_name = "manufacturer"

    def get_form(self, manufacturer):
        return manufacturer.add_link_form()


class AddGearView(AddSomethingView):
    template_name = "manufacturer/add_gear.html"
    model = Manufacturer
    context_obj_name = "manufacturer"

    def get_form(self, manufacturer):
        return manufacturer.add_gear_form()


class EditLinksView(EditSomethingView):
    model = Manufacturer

    def get_formset(self):
        return generic.generic_inlineformset_factory(Link, extra=1)
