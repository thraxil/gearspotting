from models import Musician, Link, Photo
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib.contenttypes import generic
from django.forms.models import inlineformset_factory
from django.views.generic.base import TemplateView, View


class MusicianTagView(TemplateView):
    template_name = "musician/musician_tag_list.html"

    def get_context_data(self, tag=""):
        return dict(tag=tag,
                    musicians=Musician.objects.filter(tags__name__in=[tag]))


class TagsView(TemplateView):
    template_name = "musician/tags.html"


class AddSomethingView(View):
    def get(self, request, slug):
        musician = get_object_or_404(Musician, slug=slug)
        form = self.get_form(musician)
        f = form()
        return render(
            request, self.template_name,
            dict(musician=musician, form=f))

    def post(self, request, slug):
        musician = get_object_or_404(Musician, slug=slug)
        form = self.get_form(musician)
        f = form(request.POST, request.FILES)
        if f.is_valid():
            l = f.save(commit=False)
            l.content_object = musician
            l.save()
            return HttpResponseRedirect(musician.get_absolute_url())
        return render(
            request, self.template_name,
            dict(musician=musician, form=f))


class AddLinkView(AddSomethingView):
    template_name = 'musician/add_link.html'

    def get_form(self, musician):
        return musician.add_link_form()


class AddPhotoView(AddSomethingView):
    template_name = "musician/add_photo.html"

    def get_form(self, musician):
        return musician.add_photo_form()


class AddGearView(AddSomethingView):
    template_name = "musician/add_gear.html"

    def get_form(self, musician):
        return musician.add_gear_form()


class EditSomethingView(View):
    def get(self, request, slug):
        musician = get_object_or_404(Musician, slug=slug)
        return HttpResponseRedirect(musician.get_absolute_url())

    def post(self, request, slug):
        musician = get_object_or_404(Musician, slug=slug)
        Formset = self.get_formset()
        formset = Formset(request.POST, request.FILES, instance=musician)
        if formset.is_valid():
            formset.save()
        return HttpResponseRedirect(musician.get_absolute_url())


class EditLinksView(EditSomethingView):
    def get_formset(self):
        return generic.generic_inlineformset_factory(Link, extra=1)


class EditPhotosView(EditSomethingView):
    def get_formset(self):
        return generic.generic_inlineformset_factory(Photo, extra=1)


class EditGearView(EditSomethingView):
    def get_formset(self):
        from musiciangear.models import MusicianGear
        return inlineformset_factory(Musician, MusicianGear, extra=1)
