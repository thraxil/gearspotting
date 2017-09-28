from .models import Musician, Link, Photo
from django.contrib.contenttypes.admin import generic_inlineformset_factory
from django.forms.models import inlineformset_factory
from django.views.generic.base import TemplateView
from gearspotting.utils.views import AddSomethingView, EditSomethingView


class MusicianTagView(TemplateView):
    template_name = "musician/musician_tag_list.html"

    def get_context_data(self, tag=""):
        return dict(tag=tag,
                    musicians=Musician.objects.filter(tags__name__in=[tag]))


class TagsView(TemplateView):
    template_name = "musician/tags.html"


class AddLinkView(AddSomethingView):
    template_name = 'musician/add_link.html'
    model = Musician
    context_obj_name = "musician"

    def get_form(self, musician):
        return musician.add_link_form()


class AddPhotoView(AddSomethingView):
    template_name = "musician/add_photo.html"
    model = Musician
    context_obj_name = "musician"

    def get_form(self, musician):
        return musician.add_photo_form()


class AddGearView(AddSomethingView):
    template_name = "musician/add_gear.html"
    model = Musician
    context_obj_name = "musician"

    def get_form(self, musician):
        return musician.add_gear_form()


class EditLinksView(EditSomethingView):
    model = Musician

    def get_formset(self):
        return generic_inlineformset_factory(Link, extra=1)


class EditPhotosView(EditSomethingView):
    model = Musician

    def get_formset(self):
        return generic_inlineformset_factory(Photo, extra=1)


class EditGearView(EditSomethingView):
    model = Musician

    def get_formset(self):
        from musiciangear.models import MusicianGear
        return inlineformset_factory(Musician, MusicianGear, extra=1)
