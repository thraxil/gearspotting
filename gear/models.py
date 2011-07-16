from django.db import models
from django.contrib import admin
from manufacturer.models import Manufacturer
from link.models import Link, LinkInline
from photo.models import Photo, PhotoInline
from django.contrib.contenttypes import generic
from django.forms import ModelForm
import tagging
from tagging import fields
from django.template.defaultfilters import slugify

class Gear(models.Model):
    name = models.CharField(default="",max_length=256)
    slug = models.SlugField(max_length=256,editable=False)
    manufacturer = models.ForeignKey(Manufacturer)
    description = models.TextField(default="",blank=True)
    tags = tagging.fields.TagField()
    links = generic.GenericRelation(Link)
    photos = generic.GenericRelation(Photo)
    added = models.DateTimeField(auto_now_add=True,editable=False)
    modified = models.DateTimeField(auto_now=True,editable=False)

    class Meta:
        ordering = ["manufacturer__name","name",]

    def get_absolute_url(self):
        return "/gear/%s/" % self.slug

    def __unicode__(self):
        return self.manufacturer.name + ": " + self.name

    def links_formset(self):
        LinkFormset = generic.generic_inlineformset_factory(Link, extra=1)
        return LinkFormset(instance=self)

    def photos_formset(self):
        PhotoFormset = generic.generic_inlineformset_factory(Photo, extra=1)
        return PhotoFormset(instance=self)

    def save(self):
        self.slug = slugify(self.manufacturer.name + "-" + self.name)[:256]
        super(Gear, self).save()

    def first_photo(self):
        if self.photos.count() > 0:
            return self.photos.all()[0]
        else:
            return None

    def type_display(self):
        return "Gear"

    def add_link_form(self):
        class LinkForm(ModelForm):
            class Meta:
                model = Link
                exclude = ('content_object','content_type','object_id')
        return LinkForm

    def add_photo_form(self):
        class PhotoForm(ModelForm):
            class Meta:
                model = Photo
                exclude = ('content_object','content_type','object_id')
        return PhotoForm

class AddGearForm(ModelForm):
    class Meta:
        model = Gear
        exclude = ('manufacturer',)


