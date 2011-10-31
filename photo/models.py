from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from sorl.thumbnail.fields import ImageWithThumbnailsField
from south.modelsinspector import add_introspection_rules
from django.forms import ModelForm

add_introspection_rules([], 
                        ["^django_extensions\.db\.fields\.CreationDateTimeField",
                         "django_extensions.db.fields.ModificationDateTimeField",
                         "sorl.thumbnail.fields.ImageWithThumbnailsField",
                         "django_extensions.db.fields.UUIDField"])


class Photo(models.Model):
    image = ImageWithThumbnailsField(
        upload_to="images/%Y/%m/%d",
        thumbnail = {
            'size' : (65,65)
            },
        extra_thumbnails={
            'admin': {
                'size': (70, 50),
                'options': ('sharpen',),
                }
            }
        )
    caption = models.TextField(blank=True,default="")
    source_name = models.CharField(max_length=256,blank=True,default="")
    source_url = models.URLField(blank=True)

    added = models.DateTimeField(auto_now_add=True,editable=False)
    modified = models.DateTimeField(auto_now=True,editable=False)

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


class AddPhotoForm(ModelForm):
    class Meta:
        model = Photo

class ImportPhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ('image',)

class PhotoInline(generic.GenericTabularInline):
    model = Photo

#PhotoFormset = generic.generic_inlineformset_factory(Photo, extra=1)

