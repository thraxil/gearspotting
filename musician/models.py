from django.db import models
from django.contrib import admin
from link.models import Link, LinkInline
from photo.models import Photo, PhotoInline
from django.forms import ModelForm
from django.contrib.contenttypes import generic
from django.template.defaultfilters import slugify
import tagging
from tagging import fields
from django.forms.models import inlineformset_factory

class Musician(models.Model):
    name = models.CharField(default="",unique=True, max_length=256)
    slug = models.SlugField(max_length=256,editable=False)
    description = models.TextField(default="",blank=True)
    tags = tagging.fields.TagField()
    links = generic.GenericRelation(Link)
    photos = generic.GenericRelation(Photo)

    added = models.DateTimeField(auto_now_add=True,editable=False)
    modified = models.DateTimeField(auto_now=True,editable=False)

    class Meta:
        ordering = ["name",]

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
                exclude = ('content_object','content_type','object_id')
        return LinkForm

    def add_photo_form(self):
        class PhotoForm(ModelForm):
            class Meta:
                model = Photo
                exclude = ('content_object','content_type','object_id')
        return PhotoForm

    def add_gear_form(self):
        from musiciangear.models import MusicianGear
        class GearForm(ModelForm):
            class Meta:
                model = MusicianGear
                exclude = ('musician')
        return GearForm

    def save(self):
        self.slug = slugify(self.name)[:256]
        super(Musician, self).save()

    def photos_formset(self):
        PhotoFormset = generic.generic_inlineformset_factory(Photo, extra=1)
        return PhotoFormset(instance=self)

    def gear_formset(self):
        from musiciangear.models import MusicianGear
        GearFormSet = inlineformset_factory(Musician, MusicianGear,extra=1)
        return GearFormSet(instance=self)

    def first_photo(self):
        if self.photos.count() > 0:
            return self.photos.all()[0]
        else:
            return None

    def type_display(self):
        return "Musician"

class MusicianForm(ModelForm):
    class Meta:
        model = Musician

class MusicianAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [LinkInline,PhotoInline]
admin.site.register(Musician, MusicianAdmin)
