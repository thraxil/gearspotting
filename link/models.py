from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.forms import ModelForm

class Link(models.Model):
    title = models.CharField(max_length=256)
    url = models.URLField()
    description = models.TextField(blank=True,default="")

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    added = models.DateTimeField(auto_now_add=True,editable=False)
    modified = models.DateTimeField(auto_now=True,editable=False)


class LinkInline(generic.GenericTabularInline):
    model = Link

class LinkForm(ModelForm):
    class Meta:
        model = Link

LinkFormset = generic.generic_inlineformset_factory(Link, extra=1)

