from django.db import models
from manufacturer.models import Manufacturer
from link.models import Link
from photo.models import Photo
from django.contrib.contenttypes import generic
from django.forms import ModelForm
import tagging
from django.template.defaultfilters import slugify

from south.modelsinspector import add_introspection_rules

add_introspection_rules(
    [],
    ["^django_extensions\.db\.fields\.CreationDateTimeField",
     "django_extensions.db.fields.ModificationDateTimeField",
     "sorl.thumbnail.fields.ImageWithThumbnailsField",
     "django_extensions.db.fields.UUIDField"])


class Gear(models.Model):
    name = models.CharField(default="", max_length=256)
    slug = models.SlugField(max_length=256, editable=False)
    manufacturer = models.ForeignKey(Manufacturer)
    description = models.TextField(default="", blank=True)
    tags = tagging.fields.TagField()
    links = generic.GenericRelation(Link)
    added = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ["manufacturer__name", "name", ]

    def get_absolute_url(self):
        return "/gear/%s/" % self.slug

    def __unicode__(self):
        return self.manufacturer.name + ": " + self.name

    def links_formset(self):
        LinkFormset = generic.generic_inlineformset_factory(Link, extra=1)
        return LinkFormset(instance=self)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.manufacturer.name + "-" + self.name)[:256]
        super(Gear, self).save(*args, **kwargs)

    def first_photo(self):
        if self.gearphoto_set.count() > 0:
            return self.gearphoto_set.all()[0].photo
        else:
            return None

    def type_display(self):
        return "Gear"

    def add_link_form(self):
        class LinkForm(ModelForm):
            class Meta:
                model = Link
                exclude = ('content_object', 'content_type', 'object_id')
        return LinkForm


class GearPhoto(models.Model):
    gear = models.ForeignKey(Gear)
    photo = models.ForeignKey(Photo)


class AddGearForm(ModelForm):
    class Meta:
        model = Gear
        exclude = ('manufacturer',)
