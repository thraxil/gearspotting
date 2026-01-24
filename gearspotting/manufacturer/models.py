from typing import TYPE_CHECKING, Any, Type

from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.forms import generic_inlineformset_factory
from django.db import models
from django.forms import ModelForm
from django.template.defaultfilters import slugify

from gearspotting.link.models import Link

if TYPE_CHECKING:
    from django.forms.models import BaseInlineFormSet


class Manufacturer(models.Model):
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
        return f"/manufacturer/{self.slug}/"

    def __str__(self) -> str:
        return self.name

    def links_formset(self):
        LinkFormset = generic_inlineformset_factory(Link, extra=1)  # type: ignore
        return LinkFormset

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.slug = slugify(self.name)[:256]
        super().save(*args, **kwargs)

    def add_gear_form(self) -> Type[ModelForm]:
        from gearspotting.gear.models import AddGearForm

        return AddGearForm

    def add_link_form(self) -> Type[ModelForm]:
        class LinkForm(ModelForm):
            class Meta:
                model = Link
                exclude: list[str] = [
                    "content_object",
                    "content_type",
                    "object_id",
                ]

        return LinkForm

    def gear_count(self) -> int:
        return self.gear_set.all().count()

    def type_display(self) -> str:
        return "Manufacturer"


class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        exclude: list[str] = []
