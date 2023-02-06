from django.contrib.contenttypes.admin import generic_inlineformset_factory

from gearspotting.utils.views import AddSomethingView, EditSomethingView

from .models import Link, Manufacturer


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
        return generic_inlineformset_factory(Link, extra=1)
