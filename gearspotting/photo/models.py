from django.db import models
from django.contrib.contenttypes.admin import GenericTabularInline
from django.forms import ModelForm
from django.conf import settings


class Photo(models.Model):
    # reticulum fields
    reticulum_key = models.CharField(max_length=256, default="")
    extension = models.CharField(max_length=256, default="jpg")

    caption = models.TextField(blank=True, default="")
    source_name = models.CharField(max_length=256, blank=True, default="")
    source_url = models.URLField(blank=True)

    added = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def label(self):
        return unicode(self.content_object)

    def get_absolute_url(self):
        return "/photos/%d/" % self.id

    def type_display(self):
        return "Photo"

    def gear(self):
        return [g.gear for g in self.gearphoto_set.all()]

    def musicians(self):
        return [g.musician for g in self.musicianphoto_set.all()]

    def musiciangear(self):
        return [g.musiciangear for g in self.musiciangearphoto_set.all()]

    def get_full_src(self):
        return ("%simage/%s/full/%d%s" % (
            settings.RETICULUM_PUBLIC_BASE,
            self.reticulum_key,
            self.id,
            self.extension))

    def get_1024_src(self):
        return ("%simage/%s/1024w1024h/%d%s" % (
            settings.RETICULUM_PUBLIC_BASE,
            self.reticulum_key,
            self.id,
            self.extension))

    def get_300_src(self):
        return ("%simage/%s/300w300h/%d%s" % (
            settings.RETICULUM_PUBLIC_BASE,
            self.reticulum_key,
            self.id,
            self.extension))

    def get_200_src(self):
        return ("%simage/%s/200w200h/%d%s" % (
            settings.RETICULUM_PUBLIC_BASE,
            self.reticulum_key,
            self.id,
            self.extension))

    def get_100h_src(self):
        return ("%simage/%s/100h/%d%s" % (
            settings.RETICULUM_PUBLIC_BASE,
            self.reticulum_key,
            self.id,
            self.extension))


class AddPhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = []


class ImportPhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ('reticulum_key', 'extension')


class PhotoInline(GenericTabularInline):
    model = Photo
