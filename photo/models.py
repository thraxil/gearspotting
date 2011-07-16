from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from sorl.thumbnail.fields import ImageWithThumbnailsField


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

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    added = models.DateTimeField(auto_now_add=True,editable=False)
    modified = models.DateTimeField(auto_now=True,editable=False)

    def is_gear(self):
        return self.content_object.model == "gear"

    def is_musiciangear(self):
        return self.content_object.model == "musiciangear"

    def is_musician(self):
        return self.content_object.model == "musician"

    def gear(self):
        return self.content_object

    def label(self):
        return unicode(self.content_object)


    def get_absolute_url(self):
        return "/photos/%d/" % self.id

    def type_display(self):
        return "Photo"

    def name(self):
        return "Photo of " + self.content_object.name


class PhotoInline(generic.GenericTabularInline):
    model = Photo

PhotoFormset = generic.generic_inlineformset_factory(Photo, extra=1)

