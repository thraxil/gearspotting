from typing import Any, Dict, Type

from django.contrib.contenttypes.forms import generic_inlineformset_factory
from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View

from gearspotting.link.models import Link
from gearspotting.photo.models import Photo
from gearspotting.utils.views import EditSomethingView

from .models import MusicianGear, MusicianGearPhoto


class AddLinkView(View):
    model = MusicianGear
    template_name = "musiciangear/add_link.html"

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        musiciangear = get_object_or_404(self.model, pk=pk)
        form = musiciangear.add_link_form()()
        return render(
            request,
            self.template_name,
            {"form": form, "musiciangear": musiciangear},
        )

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
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

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        musiciangear = get_object_or_404(self.model, pk=pk)
        form = musiciangear.add_photo_form()()
        return render(
            request,
            self.template_name,
            {"form": form, "musiciangear": musiciangear},
        )

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        musiciangear = get_object_or_404(self.model, pk=pk)
        Form = musiciangear.add_photo_form()
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # custom photo saving logic would go here
            photo.save()
            MusicianGearPhoto.objects.create(
                musiciangear=musiciangear, photo=photo
            )
            return HttpResponseRedirect(musiciangear.get_absolute_url())
        return render(
            request,
            self.template_name,
            {"form": form, "musiciangear": musiciangear},
        )


class EditLinksView(EditSomethingView):
    model = MusicianGear

    def get_formset(self) -> Any:
        return generic_inlineformset_factory(Link, extra=1)


class EditPhotosView(EditSomethingView):
    model = MusicianGear

    def get_formset(self) -> Any:
        return generic_inlineformset_factory(Photo, extra=1)
