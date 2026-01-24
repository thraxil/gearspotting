from django.contrib.contenttypes.admin import generic_inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View

from gearspotting.utils.views import EditSomethingView

from .models import Link, MusicianGear, Photo


class AddLinkView(View):
    model = MusicianGear
    template_name = "musiciangear/add_link.html"

    def get(self, request, pk):
        musiciangear = get_object_or_404(self.model, pk=pk)
        form = musiciangear.add_link_form()()
        return render(
            request,
            self.template_name,
            {"form": form, "musiciangear": musiciangear},
        )

    def post(self, request, pk):
        musiciangear = get_object_or_404(self.model, pk=pk)
        Form = musiciangear.add_link_form()
        form = Form(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.content_object = musiciangear
            link.save()
            return HttpResponseRedirect(musiciangear.get_absolute_url())
        return render(
            request,
            self.template_name,
            {"form": form, "musiciangear": musiciangear},
        )


class AddPhotoView(View):
    model = MusicianGear
    template_name = "musiciangear/add_photo.html"

    def get(self, request, pk):
        musiciangear = get_object_or_404(self.model, pk=pk)
        form = musiciangear.add_photo_form()()
        return render(
            request,
            self.template_name,
            {"form": form, "musiciangear": musiciangear},
        )

    def post(self, request, pk):
        musiciangear = get_object_or_404(self.model, pk=pk)
        Form = musiciangear.add_photo_form()
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # custom photo saving logic would go here
            photo.save()
            musiciangear.photos.add(photo)
            return HttpResponseRedirect(musiciangear.get_absolute_url())
        return render(
            request,
            self.template_name,
            {"form": form, "musiciangear": musiciangear},
        )


class EditLinksView(EditSomethingView):
    model = MusicianGear

    def get_formset(self):
        return generic_inlineformset_factory(Link, extra=1)


class EditPhotosView(EditSomethingView):
    model = MusicianGear

    def get_formset(self):
        return generic_inlineformset_factory(Photo, extra=1)
