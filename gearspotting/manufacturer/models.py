from django.contrib.contenttypes.admin import generic_inlineformset_factory
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.forms import ModelForm
from django.template.defaultfilters import slugify

from gearspotting.link.models import Link


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

    def get_absolute_url(self):
        return "/manufacturer/%s/" % self.slug

    def __unicode__(self):
        return self.name

    def links_formset(self):
        LinkFormset = generic_inlineformset_factory(Link, extra=1)
        return LinkFormset(instance=self)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)[:256]
        super(Manufacturer, self).save(*args, **kwargs)

    def add_gear_form(self):
        from gearspotting.gear.models import AddGearForm

        return AddGearForm

    def add_link_form(self):
        class LinkForm(ModelForm):
            class Meta:
                model = Link
                exclude = ("content_object", "content_type", "object_id")

        return LinkForm

    def gear_count(self):
        return self.gear_set.all().count()

    def type_display(self):
        return "Manufacturer"


class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        exclude = []
