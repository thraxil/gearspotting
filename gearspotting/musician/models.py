from typing import TYPE_CHECKING, Any, Optional, Type

from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.forms import generic_inlineformset_factory
from django.db import models
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.template.defaultfilters import slugify

from gearspotting.link.models import Link
from gearspotting.photo.models import Photo
from gearspotting.tag.models import Tag

if TYPE_CHECKING:
    from django.forms.models import BaseInlineFormSet


class Musician(models.Model):
    name = models.CharField(default="", unique=True, max_length=256)
    slug = models.SlugField(max_length=256, editable=False)
    description = models.TextField(default="", blank=True)
    description_html = models.TextField(default="", blank=True)
    links = GenericRelation(Link)
    added = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = [
            "name",
        ]

    def get_absolute_url(self) -> str:
        return f"/musician/{self.slug}/"

    def __str__(self) -> str:
        return self.name

    def links_formset(self):
        LinkFormset = generic_inlineformset_factory(Link, extra=1)  # type: ignore
        return LinkFormset(instance=self)

    def add_link_form(self) -> Type[ModelForm]:
        class LinkForm(ModelForm):
            class Meta:
                model = Link
                exclude = ("content_object", "content_type", "object_id")

        return LinkForm

    def add_gear_form(self) -> Type[ModelForm]:
        from gearspotting.musiciangear.models import MusicianGear

        class GearForm(ModelForm):
            class Meta:
                model = MusicianGear
                exclude = ("musician",)

        return GearForm

    def add_photo_form(self) -> Type[ModelForm]:
        class PhotoForm(ModelForm):
            class Meta:
                model = Photo
                exclude = ("content_object", "content_type", "object_id")

        return PhotoForm

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.slug = slugify(self.name)[:256]
        super().save(*args, **kwargs)

    def gear_formset(self):
        from gearspotting.musiciangear.models import MusicianGear

        GearFormSet: Any = inlineformset_factory(
            Musician, MusicianGear, extra=1
        )
        return GearFormSet(instance=self)

    def first_photo(self) -> Optional[Photo]:
        if self.musicianphoto_set.count() > 0:
            return self.musicianphoto_set.all()[0].photo
        else:
            return None

    def type_display(self) -> str:
        return "Musician"


class MusicianPhoto(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class MusicianTag(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class MusicianForm(ModelForm):
    class Meta:
        model = Musician
        exclude: list[str] = []
