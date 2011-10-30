from django.db import models
from django.contrib import admin
from link.models import Link, LinkInline
from gear.models import Gear
from musician.models import Musician
from photo.models import Photo, PhotoInline
from django.contrib.contenttypes import generic
from django.forms import ModelForm
from south.modelsinspector import add_introspection_rules

add_introspection_rules([], 
                        ["^django_extensions\.db\.fields\.CreationDateTimeField",
                         "django_extensions.db.fields.ModificationDateTimeField",
                         "sorl.thumbnail.fields.ImageWithThumbnailsField",
                         "django_extensions.db.fields.UUIDField"])


class MusicianGear(models.Model):
    musician = models.ForeignKey(Musician)
    gear = models.ForeignKey(Gear)
    description = models.TextField(default="",blank=True)
    links = generic.GenericRelation(Link)
    photos = generic.GenericRelation(Photo)
    added = models.DateTimeField(auto_now_add=True,editable=False)
    modified = models.DateTimeField(auto_now=True,editable=False)

    def get_absolute_url(self):
        return "/musiciangear/%d/" % self.id

    def __unicode__(self):
        return "%s - %s" % (self.musician.name,self.gear.name)

    def links_formset(self):
        LinkFormset = generic.generic_inlineformset_factory(Link, extra=1)
        return LinkFormset(instance=self)

    def first_photo(self):
        if self.musiciangearphotos.count() > 0:
            return self.musiciangearphotos.all()[0].photo
        else:
            return None
    def type_display(self):
        return "Musician Gear"

    def add_link_form(self):
        class LinkForm(ModelForm):
            class Meta:
                model = Link
                exclude = ('content_object','content_type','object_id')
        return LinkForm


class MusicianGearPhoto(models.Model):
    musiciangear = models.ForeignKey(MusicianGear)
    photo = models.ForeignKey(Photo)

class MusicianGearAdmin(admin.ModelAdmin):
    inlines = [LinkInline,PhotoInline]
admin.site.register(MusicianGear, MusicianGearAdmin)
