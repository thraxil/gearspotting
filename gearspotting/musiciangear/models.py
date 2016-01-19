from django.db import models
from gearspotting.link.models import Link
from gearspotting.gear.models import Gear
from gearspotting.musician.models import Musician
from gearspotting.photo.models import Photo
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.admin import generic_inlineformset_factory
from django.forms import ModelForm


class MusicianGear(models.Model):
    musician = models.ForeignKey(Musician)
    gear = models.ForeignKey(Gear)
    description = models.TextField(default="", blank=True)
    links = GenericRelation(Link)
    added = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def get_absolute_url(self):
        return "/musiciangear/%d/" % self.id

    def __unicode__(self):
        return "%s - %s" % (self.musician.name, self.gear.name)

    def links_formset(self):
        LinkFormset = generic_inlineformset_factory(Link, extra=1)
        return LinkFormset(instance=self)

    def first_photo(self):
        if self.musiciangearphoto_set.count() > 0:
            return self.musiciangearphoto_set.all()[0].photo
        else:
            return None

    def type_display(self):
        return "Musician Gear"

    def add_link_form(self):
        class LinkForm(ModelForm):
            class Meta:
                model = Link
                exclude = ('content_object', 'content_type', 'object_id')
        return LinkForm


class MusicianGearPhoto(models.Model):
    musiciangear = models.ForeignKey(MusicianGear)
    photo = models.ForeignKey(Photo)
