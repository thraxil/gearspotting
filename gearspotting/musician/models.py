from django.db import models
from gearspotting.link.models import Link
from gearspotting.photo.models import Photo
from django.forms import ModelForm
from django.contrib.contenttypes import generic
from django.template.defaultfilters import slugify
from django.forms.models import inlineformset_factory
from taggit.managers import TaggableManager


class Musician(models.Model):
    name = models.CharField(default="", unique=True, max_length=256)
    slug = models.SlugField(max_length=256, editable=False)
    description = models.TextField(default="", blank=True)
    links = generic.GenericRelation(Link)
    tags = TaggableManager()
    added = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ["name", ]

    def get_absolute_url(self):
        return "/musician/%s/" % self.slug

    def __unicode__(self):
        return self.name

    def links_formset(self):
        LinkFormset = generic.generic_inlineformset_factory(Link, extra=1)
        return LinkFormset(instance=self)

    def add_link_form(self):
        class LinkForm(ModelForm):
            class Meta:
                model = Link
                exclude = ('content_object', 'content_type', 'object_id')
        return LinkForm

    def add_gear_form(self):
        from gearspotting.musiciangear.models import MusicianGear

        class GearForm(ModelForm):
            class Meta:
                model = MusicianGear
                exclude = ('musician')
        return GearForm

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)[:256]
        super(Musician, self).save(*args, **kwargs)

    def gear_formset(self):
        from gearspotting.musiciangear.models import MusicianGear
        GearFormSet = inlineformset_factory(Musician, MusicianGear, extra=1)
        return GearFormSet(instance=self)

    def first_photo(self):
        if self.musicianphotos.count() > 0:
            return self.musicianphotos.all()[0].photo
        else:
            return None

    def type_display(self):
        return "Musician"


class MusicianPhoto(models.Model):
    musician = models.ForeignKey(Musician)
    photo = models.ForeignKey(Photo)


class MusicianForm(ModelForm):
    class Meta:
        model = Musician
        exclude = []
