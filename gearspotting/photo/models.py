from typing import TYPE_CHECKING, List

from django.conf import settings
from django.contrib.contenttypes.admin import GenericTabularInline
from django.db import models
from django.forms import ModelForm

if TYPE_CHECKING:
    from gearspotting.gear.models import Gear
    from gearspotting.musician.models import Musician
    from gearspotting.musiciangear.models import MusicianGear


class Photo(models.Model):
    # reticulum fields
    reticulum_key = models.CharField(max_length=256, default="")
    extension = models.CharField(max_length=256, default="jpg")

    caption = models.TextField(blank=True, default="")
    caption_html = models.TextField(blank=True, default="")
    source_name = models.CharField(max_length=256, blank=True, default="")
    source_url = models.URLField(blank=True)

    added = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def label(self) -> str:
        return str(self.content_object)  # type: ignore

    def get_absolute_url(self) -> str:
        return f"/photos/{self.id}/"

    def type_display(self) -> str:
        return "Photo"

    def gear(self) -> List["Gear"]:
        return [g.gear for g in self.gearphoto_set.all()]

    def musicians(self) -> List["Musician"]:
        return [g.musician for g in self.musicianphoto_set.all()]

    def musiciangear(self) -> List["MusicianGear"]:
        return [g.musiciangear for g in self.musiciangearphoto_set.all()]

    def get_full_src(self) -> str:
        return f"{settings.RETICULUM_PUBLIC_BASE}image/{self.reticulum_key}/full/{self.id}{self.extension}"

    def get_1024_src(self) -> str:
        return f"{settings.RETICULUM_PUBLIC_BASE}image/{self.reticulum_key}/1024w1024h/{self.id}{self.extension}"

    def get_300_src(self) -> str:
        return f"{settings.RETICULUM_PUBLIC_BASE}image/{self.reticulum_key}/300w300h/{self.id}{self.extension}"

    def get_200_src(self) -> str:
        return f"{settings.RETICULUM_PUBLIC_BASE}image/{self.reticulum_key}/200w200h/{self.id}{self.extension}"

    def get_100h_src(self) -> str:
        return f"{settings.RETICULUM_PUBLIC_BASE}image/{self.reticulum_key}/100h/{self.id}{self.extension}"


class AddPhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude: List[str] = []


class ImportPhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude: List[str] = ["reticulum_key", "extension"]


class PhotoInline(GenericTabularInline):
    model = Photo
