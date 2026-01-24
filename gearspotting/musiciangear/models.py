from typing import TYPE_CHECKING, Any, Optional, Type

from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.forms import generic_inlineformset_factory
from django.db import models
from django.forms import ModelForm

from gearspotting.gear.models import Gear
from gearspotting.link.models import Link
from gearspotting.musician.models import Musician
from gearspotting.photo.models import Photo

if TYPE_CHECKING:
    from django.forms.models import BaseInlineFormSet


from django.urls import reverse


class MusicianGear(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
    description = models.TextField(default="", blank=True)
    description_html = models.TextField(default="", blank=True)
    links = GenericRelation(Link)
    added = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def get_absolute_url(self) -> str:
        return reverse("musiciangear:musiciangear_detail", args=[self.pk])

    def __str__(self) -> str:
        return f"{self.musician.name} - {self.gear.name}"

    def links_formset(self):
        LinkFormset = generic_inlineformset_factory(Link, extra=1)  # type: ignore
        return LinkFormset(instance=self)

    def first_photo(self) -> Optional[Photo]:
        if self.musiciangearphoto_set.count() > 0:
            return self.musiciangearphoto_set.all()[0].photo
        else:
            return None

    def type_display(self) -> str:
        return "Musician Gear"

    def add_link_form(self) -> Type[ModelForm]:
        class LinkForm(ModelForm):
            class Meta:
                model = Link
                exclude = ("content_object", "content_type", "object_id")

        return LinkForm

    def add_photo_form(self) -> Type[ModelForm]:
        class PhotoForm(ModelForm):
            class Meta:
                model = Photo
                exclude = ("content_object", "content_type", "object_id")

        return PhotoForm


class MusicianGearPhoto(models.Model):
    musiciangear = models.ForeignKey(MusicianGear, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
