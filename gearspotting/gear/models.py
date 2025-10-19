from django.contrib.contenttypes.admin import generic_inlineformset_factory
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.forms import ModelForm
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager

from gearspotting.link.models import Link
from gearspotting.manufacturer.models import Manufacturer
from gearspotting.photo.models import Photo
from gearspotting.tag.models import Tag


class Gear(models.Model):
    name = models.CharField(default="", max_length=256)
    slug = models.SlugField(max_length=256, editable=False)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    description = models.TextField(default="", blank=True)
    description_html = models.TextField(default="", blank=True)
    links = GenericRelation(Link)
    tags = TaggableManager()
    added = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = [
            "manufacturer__name",
            "name",
        ]

    def get_absolute_url(self):
        return "/gear/%s/" % self.slug

    def __unicode__(self):
        return self.manufacturer.name + ": " + self.name

    def links_formset(self):
        LinkFormset = generic_inlineformset_factory(Link, extra=1)
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
                exclude = ("content_object", "content_type", "object_id")

        return LinkForm


class GearPhoto(models.Model):
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class GearTag(models.Model):
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class AddGearForm(ModelForm):
    class Meta:
        model = Gear
        exclude = ("manufacturer",)
