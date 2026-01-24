from django.contrib.contenttypes.admin import generic_inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View

from gearspotting.utils.views import AddSomethingView, EditSomethingView

from .models import Link, Manufacturer


class AddLinkView(AddSomethingView):
    template_name = "manufacturer/add_link.html"
    model = Manufacturer
    context_obj_name = "manufacturer"

    def get_form(self, manufacturer):
        return manufacturer.add_link_form()


class AddGearView(View):
    template_name = "manufacturer/add_gear.html"
    model = Manufacturer

    def get(self, request, slug):
        manufacturer = get_object_or_404(self.model, slug=slug)
        form = manufacturer.add_gear_form()()
        return render(
            request, self.template_name, {"form": form, "manufacturer": manufacturer}
        )

    def post(self, request, slug):
        manufacturer = get_object_or_404(self.model, slug=slug)
        Form = manufacturer.add_gear_form()
        form = Form(request.POST)
        if form.is_valid():
            gear = form.save(commit=False)
            gear.manufacturer = manufacturer
            gear.save()
            return HttpResponseRedirect(manufacturer.get_absolute_url())
        return render(
            request, self.template_name, {"form": form, "manufacturer": manufacturer}
        )


class EditLinksView(EditSomethingView):
    model = Manufacturer

    def get_formset(self):
        return generic_inlineformset_factory(Link, extra=1)
