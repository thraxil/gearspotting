from .models import MusicianGear, Link, Photo
from django.contrib.contenttypes.admin import generic_inlineformset_factory
from gearspotting.utils.views import AddSomethingView, EditSomethingView


class AddLinkView(AddSomethingView):
    model = MusicianGear
    context_obj_name = "musiciangear"
    template_name = "musiciangear/add_link.html"

    def get_form(self, mg):
        return mg.add_link_form()


class AddPhotoView(AddSomethingView):
    model = MusicianGear
    context_obj_name = "musiciangear"
    template_name = "musiciangear/add_photo.html"

    def get_form(self, mg):
        return mg.add_photo_form()


class EditLinksView(EditSomethingView):
    model = MusicianGear

    def get_formset(self):
        return generic_inlineformset_factory(Link, extra=1)


class EditPhotosView(EditSomethingView):
    model = MusicianGear

    def get_formset(self):
        return generic_inlineformset_factory(Photo, extra=1)
