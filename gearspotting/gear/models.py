from typing import TYPE_CHECKING, Any, Optional, Type

from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.forms import generic_inlineformset_factory
from django.db import models
from django.forms import ModelForm
from django.template.defaultfilters import slugify

from gearspotting.link.models import Link
from gearspotting.manufacturer.models import Manufacturer
from gearspotting.photo.models import Photo
from gearspotting.tag.models import Tag

if TYPE_CHECKING:
    from django.forms.models import BaseInlineFormSet


class Gear(models.Model):
    name = models.CharField(default="", max_length=256)
    slug = models.SlugField(max_length=256, editable=False)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    description = models.TextField(default="", blank=True)
    description_html = models.TextField(default="", blank=True)
    links = GenericRelation(Link)
    added = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = [
            "manufacturer__name",
            "name",
        ]

    def get_absolute_url(self) -> str:
        return f"/gear/{self.slug}/"

    def __str__(self) -> str:
        return f"{self.manufacturer.name}: {self.name}"

    def links_formset(self):
        LinkFormset = generic_inlineformset_factory(Link, extra=1)  # type: ignore
        return LinkFormset(instance=self)

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.slug = slugify(self.manufacturer.name + "-" + self.name)[:256]
        super().save(*args, **kwargs)

    def first_photo(self) -> Optional[Photo]:
        if self.gearphoto_set.count() > 0:
            return self.gearphoto_set.all()[0].photo
        else:
            return None

    def type_display(self) -> str:
        return "Gear"

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


class GearPhoto(models.Model):
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class GearTag(models.Model):
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class AddGearForm(ModelForm):
    class Meta:
        model = Gear
        exclude: list[str] = ["manufacturer"]
