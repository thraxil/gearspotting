from models import Gear, Link, Photo
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib.contenttypes import generic
from django.views.generic.base import TemplateView, View

from gearspotting.manufacturer.models import Manufacturer, ManufacturerForm


class GearTagView(TemplateView):
    template_name = "gear/gear_tag_list.html"

    def get_context_data(self, tag=""):
        return dict(tag=tag,
                    gear_list=Gear.objects.filter(tags__name__in=[tag]))


class IndexView(TemplateView):
    template_name = 'gear/index.html'

    def get_context_data(self):
        return dict(manufacturers=Manufacturer.objects.all(),
                    add_manufacturer_form=ManufacturerForm())


class TagsView(TemplateView):
    template_name = 'gear/tags.html'


class AddSomethingView(View):
    def get(self, request, slug):
        gear = get_object_or_404(Gear, slug=slug)
        form = self.get_form(gear)
        f = form()
        return render(
            request, self.template_name,
            dict(gear=gear, form=f))

    def post(self, request, slug):
        gear = get_object_or_404(Gear, slug=slug)
        form = self.get_form(gear)
        f = form(request.POST, request.FILES)
        if f.is_valid():
            l = f.save(commit=False)
            l.content_object = gear
            l.save()
            return HttpResponseRedirect(gear.get_absolute_url())
        return render(
            request, self.template_name,
            dict(gear=gear, form=f))


class AddLinkView(AddSomethingView):
    template_name = 'gear/add_link.html'

    def get_form(self, gear):
        return gear.add_link_form()


class AddPhotoView(AddSomethingView):
    template_name = 'gear/add_photo.html'

    def get_form(self, gear):
        return gear.add_photo_form()


class EditSomethingView(View):
    def get(self, request, slug):
        gear = get_object_or_404(Gear, slug=slug)
        return HttpResponseRedirect(gear.get_absolute_url())

    def post(self, request, slug):
        gear = get_object_or_404(Gear, slug=slug)
        Formset = self.get_formset()
        formset = Formset(request.POST, request.FILES, instance=gear)
        if formset.is_valid():
            formset.save()
        return HttpResponseRedirect(gear.get_absolute_url())


class EditLinksView(EditSomethingView):
    def get_formset(self):
        return generic.generic_inlineformset_factory(Link, extra=1)


class EditPhotosView(EditSomethingView):
    def get_formset(self):
        generic.generic_inlineformset_factory(Photo, extra=1)
