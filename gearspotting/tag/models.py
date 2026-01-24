from typing import Any

from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.forms import generic_inlineformset_factory
from django.db import models
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.template.defaultfilters import slugify


class Tag(models.Model):
    name = models.CharField(default="", unique=True, max_length=256)
    slug = models.SlugField(max_length=256, editable=False)

    class Meta:
        ordering = [
            "name",
        ]

    def __str__(self) -> str:
        return self.name

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.slug = slugify(self.name)[:256]
        super().save(*args, **kwargs)
