from django.contrib.contenttypes.admin import (GenericTabularInline,
                                               generic_inlineformset_factory)
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.forms import ModelForm


class Link(models.Model):
    title = models.CharField(max_length=256)
    url = models.URLField()
    description = models.TextField(blank=True, default="")

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    added = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)


class LinkInline(GenericTabularInline):
    model = Link


class LinkForm(ModelForm):
    class Meta:
        model = Link
        exclude = []


LinkFormset = generic_inlineformset_factory(Link, extra=1)
